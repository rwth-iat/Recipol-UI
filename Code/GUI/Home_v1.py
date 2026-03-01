# Code/GUI/Home.py
import os
import shutil
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QColor
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout,
    QFileDialog, QTableWidgetItem, QProgressBar
)
from qfluentwidgets import (
    CardWidget,
    PushButton,
    SubtitleLabel,
    BodyLabel,
    TableWidget,
    PrimaryPushButton,
    InfoBar,
    InfoBarPosition
)

from Code.GUI.Workers import Worker


class HomePage(QWidget):
    def __init__(self, log_callback, parent=None):
        super().__init__(parent)
        self.setObjectName("home_page")

        self.log_callback = log_callback
        self.selected_file = ""

        # --------------------------------------------------
        # Artifact directory (project-root based)
        # --------------------------------------------------
        project_root = os.path.abspath(os.getcwd())
        self.artifact_dir = os.path.join(
            project_root, "Code", "Recipol", "Artifact"
        )
        os.makedirs(self.artifact_dir, exist_ok=True)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(30, 30, 30, 30)
        layout.setSpacing(16)

        # ---------- Title ----------
        layout.addWidget(SubtitleLabel("Recipol Artifact Manager", self))
        layout.addWidget(
            BodyLabel("Recipes (.xml) and MTP files (.aml) are grouped below.", self)
        )

        # ---------- Import ----------
        card = CardWidget(self)
        card_layout = QHBoxLayout(card)

        btn_import = PushButton("Import File", self)
        btn_import.clicked.connect(self.import_file)

        card_layout.addWidget(btn_import)
        card_layout.addStretch(1)

        layout.addWidget(card)

        # ---------- Table ----------
        self.table = TableWidget(self)
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(["Type", "File"])
        self.table.verticalHeader().setVisible(False)
        self.table.setSelectionBehavior(TableWidget.SelectionBehavior.SelectRows)
        self.table.setSelectionMode(TableWidget.SelectionMode.MultiSelection)
        self.table.itemSelectionChanged.connect(self.on_selection_changed)
        self.table.horizontalHeader().setStretchLastSection(True)

        layout.addWidget(self.table, 1)

        # ---------- Selected ----------
        self.lbl_selected = BodyLabel("Selected: None", self)
        self.lbl_selected.setStyleSheet("font-weight: bold;")
        layout.addWidget(self.lbl_selected)

        # ---------- Run ----------
        self.btn_run = PrimaryPushButton("Run Worker", self)
        self.btn_run.setEnabled(False)
        self.btn_run.clicked.connect(self.run_worker)
        layout.addWidget(self.btn_run)

        self.pbar = QProgressBar(self)
        layout.addWidget(self.pbar)

        # Initial scan
        self.scan_artifact_dir()

    # ------------------------------------------------------------------
    # Scan & Group
    # ------------------------------------------------------------------
    def scan_artifact_dir(self):
        self.table.setRowCount(0)

        recipes = []
        mtps = []

        for name in sorted(os.listdir(self.artifact_dir)):
            full = os.path.join(self.artifact_dir, name)
            if not os.path.isfile(full):
                continue

            if name.lower().endswith(".xml"):
                recipes.append(full)
            elif name.lower().endswith(".aml"):
                mtps.append(full)

        if recipes:
            self.add_group_header("Recipe Files")
            for f in recipes:
                self.add_file_row("Recipe", f)

            # Add spacing after group
            self.add_empty_row()

        if mtps:
            self.add_group_header("MTP Files")
            for f in mtps:
                self.add_file_row("MTP", f)

            # Add spacing after group
            self.add_empty_row()

        self.log_callback(
            f"Scanned Artifact: {len(recipes)} recipes, {len(mtps)} MTP files"
        )

    # ------------------------------------------------------------------
    # Table Helpers
    # ------------------------------------------------------------------
    def add_group_header(self, title):
        row = self.table.rowCount()
        self.table.insertRow(row)

        item = QTableWidgetItem(title)
        item.setFlags(Qt.ItemFlag.NoItemFlags)

        font = QFont()
        font.setBold(True)
        font.setPointSize(10)
        item.setFont(font)
        item.setBackground(QColor("#2d2d2d"))
        item.setForeground(QColor("#ffffff"))

        self.table.setItem(row, 0, item)
        self.table.setSpan(row, 0, 1, 2)
        self.table.setRowHeight(row, 28)

    def add_file_row(self, ftype, path):
        row = self.table.rowCount()
        self.table.insertRow(row)

        type_item = QTableWidgetItem(ftype)
        type_item.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled)
        self.table.setItem(row, 0, type_item)

        file_item = QTableWidgetItem(os.path.basename(path))
        file_item.setToolTip(path)  # Full path tooltip
        file_item.setFlags(Qt.ItemFlag.ItemIsSelectable | Qt.ItemFlag.ItemIsEnabled)
        self.table.setItem(row, 1, file_item)

        self.table.setRowHeight(row, 24)

    def add_empty_row(self):
        """Add a small spacer row for visual separation."""
        row = self.table.rowCount()
        self.table.insertRow(row)
        self.table.setRowHeight(row, 8)

    # ------------------------------------------------------------------
    # Import
    # ------------------------------------------------------------------
    def import_file(self):
        src, _ = QFileDialog.getOpenFileName(
            self, "Import File", "", "All Supported Files (*.xml *.aml);;XML Files (*.xml);;AML Files (*.aml);;All Files (*)"
        )
        if not src:
            return

        dst = os.path.join(self.artifact_dir, os.path.basename(src))

        try:
            shutil.copy2(src, dst)
            self.scan_artifact_dir()
            self.log_callback(f"Imported: {dst}")

            InfoBar.success(
                title="Imported",
                content=os.path.basename(dst),
                parent=self.window(),
                position=InfoBarPosition.TOP_RIGHT
            )
        except Exception as e:
            InfoBar.error(
                title="Import Failed",
                content=str(e),
                parent=self.window(),
                position=InfoBarPosition.TOP_RIGHT
            )

    # ------------------------------------------------------------------
    # Selection
    # ------------------------------------------------------------------
    def on_selection_changed(self):
        items = self.table.selectedItems()
        if not items:
            self.selected_file = ""
            self.lbl_selected.setText("Selected: None")
            self.btn_run.setEnabled(False)
            return

        # Ignore group headers or empty rows
        if not items[0].flags() & Qt.ItemFlag.ItemIsSelectable:
            return

        self.selected_file = items[1].text()
        self.lbl_selected.setText(f"Selected: {self.selected_file}")
        self.btn_run.setEnabled(True)

    # ------------------------------------------------------------------
    # Worker
    # ------------------------------------------------------------------
    def run_worker(self):
        self.btn_run.setEnabled(False)
        self.pbar.setValue(0)

        self.worker = Worker(self.selected_file)
        self.worker.log_signal.connect(self.log_callback)
        self.worker.progress_signal.connect(self.pbar.setValue)
        self.worker.finished_signal.connect(self.on_finished)
        self.worker.start()

    def on_finished(self):
        self.btn_run.setEnabled(True)
        InfoBar.success(
            title="Done",
            content="Worker finished successfully.",
            parent=self.window(),
            position=InfoBarPosition.TOP_RIGHT
        )
