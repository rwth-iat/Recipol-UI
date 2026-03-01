# Code/GUI/Home.py
import os
import shutil
from PyQt6.QtCore import Qt, pyqtSignal
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
    # 定义自定义信号：用于向 MainWindow 发送解析出来的 list[Pea]
    data_ready_signal = pyqtSignal(list)

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
        layout.addWidget(SubtitleLabel("Recipol File Manager", self))
        layout.addWidget(
            BodyLabel("Recipes (.xml) and MTP files (.aml) are grouped below.", self)
        )

        # ---------- Import ----------
        card = CardWidget(self)
        card_layout = QHBoxLayout(card)

        btn_import = PushButton("Import File", self)
        btn_import.clicked.connect(self.import_file)
        # card_layout.addWidget(btn_import)
        # card_layout.addStretch(1)

        self.btn_delete = PushButton("Delete Selected", self)
        self.btn_delete.setEnabled(False)
        self.btn_delete.clicked.connect(self.delete_selected_file)

        card_layout.addWidget(btn_import)
        card_layout.addWidget(self.btn_delete)
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
        self.table.horizontalHeader().setDefaultAlignment(
            Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter
        )

        layout.addWidget(self.table, 1)

        # ---------- Selected ----------
        self.lbl_selected = BodyLabel("Selected: None", self)
        self.lbl_selected.setStyleSheet("font-weight: bold; color: #ffffff;")
        # self.lbl_selected.setStyleSheet("font-weight: bold;")
        layout.addWidget(self.lbl_selected)

        # ---------- Run ----------
        self.btn_run = PrimaryPushButton("Inspect", self)
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
        file_item.setTextAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)
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
        files, _ = QFileDialog.getOpenFileNames(
            self,
            "Import Files",
            "",
            "All Supported Files (*.xml *.aml);;XML Files (*.xml);;AML Files (*.aml);;All Files (*)"
        )

        if not files:
            return

        success_count = 0
        fail_count = 0

        for src in files:
            dst = os.path.join(self.artifact_dir, os.path.basename(src))

            try:
                shutil.copy2(src, dst)
                self.log_callback(f"Imported: {dst}")
                success_count += 1
            except Exception as e:
                self.log_callback(f"Failed to import {src}: {e}")
                fail_count += 1

        # 刷新表格
        self.scan_artifact_dir()

        # 统一提示
        if success_count > 0:
            InfoBar.success(
                title="Import Completed",
                content=f"{success_count} file(s) imported successfully.",
                parent=self.window(),
                position=InfoBarPosition.TOP_RIGHT
            )

        if fail_count > 0:
            InfoBar.error(
                title="Import Issues",
                content=f"{fail_count} file(s) failed to import. See log for details.",
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
            self.btn_delete.setEnabled(False)
            return

        # 收集所有选中的真实文件（忽略组标题和空行）
        selected_files = []
        for i in range(0, len(items), self.table.columnCount()):
            if items[i].flags() & Qt.ItemFlag.ItemIsSelectable:
                selected_files.append(items[i+1].text())

        if not selected_files:
            self.selected_file = ""
            self.lbl_selected.setText("Selected: None")
            self.btn_run.setEnabled(False)
            self.btn_delete.setEnabled(False)
            return

        self.selected_files = selected_files  # 保存所有选中文件
        self.lbl_selected.setText(f"Selected: {len(selected_files)} file(s)")
        # self.btn_run.setEnabled(len(selected_files) == 1)  # 运行Worker只允许单选
        self.btn_run.setEnabled(True)    # 多选时也可运行 Worker
        self.btn_delete.setEnabled(True)


    # ------------------------------------------------------------------
    # Delete
    # ------------------------------------------------------------------
    def delete_selected_file(self):
        if not hasattr(self, "selected_files") or not self.selected_files:
            return

        failed = []
        for fname in self.selected_files:
            full_path = os.path.join(self.artifact_dir, fname)
            try:
                if os.path.exists(full_path):
                    os.remove(full_path)
                else:
                    failed.append(fname)
            except Exception:
                failed.append(fname)

        # 更新表格
        self.scan_artifact_dir()
        self.lbl_selected.setText("Selected: None")
        self.btn_run.setEnabled(False)
        self.btn_delete.setEnabled(False)

        if failed:
            InfoBar.error(
                title="Delete Failed",
                content=f"Failed to delete: {', '.join(failed)}",
                parent=self.window(),
                position=InfoBarPosition.TOP_RIGHT
            )
        else:
            InfoBar.success(
                title="Deleted",
                content=f"Deleted {len(self.selected_files)} file(s)",
                parent=self.window(),
                position=InfoBarPosition.TOP_RIGHT
            )


    # ------------------------------------------------------------------
    # Worker
    # ------------------------------------------------------------------
    # def run_worker(self):
    #     if not self.selected_files:
    #         return

    #     self.btn_run.setEnabled(False)
    #     self.pbar.setValue(0)

    #     # 将 Worker 修改为接收文件列表
    #     full_paths = [os.path.join(self.artifact_dir, f) for f in self.selected_files]
    #     # self.worker = Worker(self.selected_files)  
    #     self.worker = Worker(full_paths)
    #     self.worker.log_signal.connect(self.log_callback)
    #     self.worker.progress_signal.connect(self.pbar.setValue)
    #     self.worker.finished_signal.connect(self.on_finished)
    #     self.worker.start()     #执行Worker.py里的run()

    # Code/GUI/Home.py

    def run_worker(self):
        if not self.selected_files:
            return

        self.btn_run.setEnabled(False)
        self.pbar.setValue(0)

        # 【核心改动】：在这里进行过滤，只提取以 .aml 结尾的文件
        # 这样只有 MTP 文件会被送入后端 getMtps 函数
        aml_files = [
            os.path.join(self.artifact_dir, f) 
            for f in self.selected_files 
            if f.lower().endswith('.aml')
        ]
        
        # 获取非 aml 文件（如 .xml），用于日志记录
        other_files = [f for f in self.selected_files if not f.lower().endswith('.aml')]

        # 如果有非 MTP 文件，在日志里打个招呼
        if other_files:
            self.log_callback(f"Skipping non-MTP files: {', '.join(other_files)}")

        # 如果连一个 .aml 都没有选，直接结束
        if not aml_files:
            self.log_callback("No .aml files selected. Task aborted.")
            self.btn_run.setEnabled(True)
            return

        # 将过滤后的 aml_files 传给 Worker
        self.worker = Worker(aml_files)         # 把 worker 对象挂在当前 HomePage 实例上，实例属性可以在任何时候创建，都会动态添加到对象，不需要提前声明。
        self.worker.log_signal.connect(self.log_callback)
        self.worker.progress_signal.connect(self.pbar.setValue)
        self.worker.finished_signal.connect(self.on_finished)       # 一旦 finished_signal 被发射（emit），请立刻自动执行 on_finished 这个函数。
        self.worker.start()

    def on_finished(self):
        self.btn_run.setEnabled(True)

        parsed_mtps = getattr(self.worker, 'mtp_results', [])       # getattr(object, "属性名", 默认值)，取object.属性名
        # print(parsed_mtps)

        if parsed_mtps:
            self.data_ready_signal.emit(parsed_mtps)
            self.log_callback(f"Successfully sent {len(parsed_mtps)} MTPs to Viewer.")

            InfoBar.success(
            title="Done",
            content="Files imported successfully.",
            isClosable=True,
            duration = 3000,
            parent=self.window(),
            position=InfoBarPosition.TOP_RIGHT
        )
        else:
            self.data_ready_signal.emit(parsed_mtps)
            self.log_callback("Error: At least one MTP file has no data parsed to display.")

            InfoBar.error(
            title="Error",
            content="At least one MTP file has no data parsed to display.",
            isClosable=True,
            duration = 5000,
            parent=self.window(),
            position=InfoBarPosition.TOP_RIGHT
        )
            
        
