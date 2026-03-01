# Code/GUI/SFCMonitor.py
# -*- coding: utf-8 -*-

import math

from PyQt6.QtCore import QPointF, QRectF, Qt, QTimer
from PyQt6.QtGui import QBrush, QColor, QFont, QPainter, QPen, QPolygonF, QTextOption
from PyQt6.QtWidgets import (
    QGraphicsTextItem,
    QGraphicsScene,
    QGraphicsView,
    QHBoxLayout,
    QPushButton,
    QVBoxLayout,
    QWidget,
)
from qfluentwidgets import SubtitleLabel, TitleLabel


class SFCGraphicsView(QGraphicsView):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setDragMode(QGraphicsView.DragMode.ScrollHandDrag)
        self.setTransformationAnchor(QGraphicsView.ViewportAnchor.AnchorUnderMouse)
        self.setResizeAnchor(QGraphicsView.ViewportAnchor.AnchorViewCenter)

    def wheelEvent(self, event):
        if event.angleDelta().y() > 0:
            self.scale(1.12, 1.12)
        else:
            self.scale(1 / 1.12, 1 / 1.12)
        event.accept()


class SFCMonitor(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setObjectName("SFCMonitor")
        self.sfc_rows = []

        layout = QVBoxLayout(self)
        layout.setContentsMargins(30, 30, 30, 30)
        layout.setSpacing(16)

        self.title = TitleLabel("SFC Monitor", self)
        self.subtitle = SubtitleLabel("Sequential Function Chart", self)
        layout.addWidget(self.title)
        layout.addWidget(self.subtitle)

        self.scene = QGraphicsScene(self)
        self.view = SFCGraphicsView(self)
        self.view.setScene(self.scene)
        self.view.setRenderHint(QPainter.RenderHint.Antialiasing, True)
        self.view.setRenderHint(QPainter.RenderHint.TextAntialiasing, True)
        self.view.setStyleSheet("QGraphicsView { border: 1px solid #303030; background: #151515; }")
        layout.addWidget(self.view, 1)
        self._build_zoom_controls()

        self._pen_line = QPen(QColor("#c7c7c7"), 1.5)
        self._pen_step = QPen(QColor("#71b7ff"), 2)
        self._pen_trans = QPen(QColor("#f6c05a"), 2)
        self._brush_step = QBrush(QColor("#1f3f63"))
        self._brush_trans = QBrush(QColor("#4f3a16"))
        self._font_main = QFont("Segoe UI", 9)
        self._font_sub = QFont("Segoe UI", 8)
        # Step font increased by ~30%.
        self._font_step = QFont("Segoe UI", 16)

    def update_data(self, sfc_rows: list):
        self.sfc_rows = sorted((sfc_rows or []), key=lambda x: x.get("seq", 0))
        self.scene.clear()

        if not self.sfc_rows:
            txt = self.scene.addText("No SFC data to display", self._font_main)
            txt.setDefaultTextColor(QColor("#ffffff"))
            txt.setPos(24, 20)
            return

        levels = self._build_levels(self.sfc_rows)
        self._draw_levels(levels)
        # Make initial view identical to pressing Reset once after render.
        QTimer.singleShot(0, self._fit_to_width_80)
        QTimer.singleShot(80, self._fit_to_width_80)

    def _build_levels(self, rows: list) -> list[list[dict]]:
        levels = []
        i = 0
        while i < len(rows):
            row = rows[i]
            if row.get("parallel"):
                group = [row]
                i += 1
                while i < len(rows) and rows[i].get("parallel"):
                    group.append(rows[i])
                    i += 1
                levels.append(group)
            else:
                levels.append([row])
                i += 1
        return levels

    def _draw_levels(self, levels: list[list[dict]]):
        top_y = 30.0
        y = top_y
        col_idx = 0
        col_step = 620.0
        # Roughly 3 Steps + 3 Transitions per column.
        max_col_height = 760.0
        x_gap = 60.0
        y_gap = 80.0
        prev_anchors = []

        for level in levels:
            center_x = 380.0 + col_idx * col_step
            size_list = [self._node_size(r) for r in level]
            total_w = sum(w for w, _ in size_list) + x_gap * (len(level) - 1)
            x = center_x - total_w / 2

            level_anchors = []
            max_h = 0.0
            for row, (w, h) in zip(level, size_list):
                rect = QRectF(x, y, w, h)
                self._draw_node(row, rect)
                top = QPointF(rect.center().x(), rect.top())
                bottom = QPointF(rect.center().x(), rect.bottom())
                level_anchors.append({"top": top, "bottom": bottom, "rect": rect})
                max_h = max(max_h, h)
                x += w + x_gap

            if prev_anchors:
                for prev in prev_anchors:
                    for curr in level_anchors:
                        self._draw_arrow_orthogonal(
                            prev["bottom"],
                            curr["top"],
                            prev["rect"],
                            curr["rect"],
                        )

            prev_anchors = level_anchors
            y += max_h + y_gap
            if y + max_h > max_col_height:
                # Start a new column and continue the flow with connecting arrows.
                y = top_y
                col_idx += 1

        self.scene.setSceneRect(self.scene.itemsBoundingRect().adjusted(-30, -20, 120, 40))

    def _build_zoom_controls(self):
        self.zoom_container = QWidget(self.view.viewport())
        self.zoom_container.setStyleSheet(
            "QWidget { background: rgba(22, 22, 22, 200); border: 1px solid #404040; border-radius: 10px; }"
        )
        row = QHBoxLayout(self.zoom_container)
        row.setContentsMargins(8, 6, 8, 6)
        row.setSpacing(6)

        self.btn_zoom_out = QPushButton("-", self.zoom_container)
        self.btn_zoom_in = QPushButton("+", self.zoom_container)
        self.btn_zoom_reset = QPushButton("Reset", self.zoom_container)
        for btn in (self.btn_zoom_out, self.btn_zoom_in, self.btn_zoom_reset):
            btn.setCursor(Qt.CursorShape.PointingHandCursor)
            btn.setStyleSheet(
                "QPushButton { color: white; background: #2a2a2a; border: 1px solid #4a4a4a; border-radius: 6px; padding: 4px 8px; }"
                "QPushButton:hover { background: #3a3a3a; }"
                "QPushButton:pressed { background: #202020; }"
            )
        self.btn_zoom_out.setFixedWidth(28)
        self.btn_zoom_in.setFixedWidth(28)

        self.btn_zoom_out.clicked.connect(lambda: self.view.scale(1 / 1.15, 1 / 1.15))
        self.btn_zoom_in.clicked.connect(lambda: self.view.scale(1.15, 1.15))
        self.btn_zoom_reset.clicked.connect(self._fit_to_width_80)

        row.addWidget(self.btn_zoom_out)
        row.addWidget(self.btn_zoom_in)
        row.addWidget(self.btn_zoom_reset)
        self.zoom_container.adjustSize()
        QTimer.singleShot(0, self._position_zoom_controls)

    def _position_zoom_controls(self):
        if not hasattr(self, "zoom_container"):
            return
        pad = 14
        size = self.zoom_container.sizeHint()
        self.zoom_container.move(
            self.view.viewport().width() - size.width() - pad,
            pad,
        )
        self.zoom_container.raise_()

    def _fit_to_width_80(self):
        rect = self.scene.sceneRect()
        if rect.isEmpty():
            return
        self.view.resetTransform()
        viewport_w = max(1, self.view.viewport().width())
        scale_x = (viewport_w * 0.80) / rect.width()
        self.view.scale(scale_x, scale_x)
        self.view.centerOn(rect.center())
        self._position_zoom_controls()

    def _node_size(self, row: dict) -> tuple[float, float]:
        if str(row.get("kind", "")).lower() == "transition":
            return 180.0, 28.0
        # Step box enlarged to ~1.3x.
        return 312.0, 112.0

    def _draw_node(self, row: dict, rect: QRectF):
        kind = str(row.get("kind", ""))
        if kind.lower() == "transition":
            self.scene.addRect(rect, self._pen_trans, self._brush_trans)
            cond = str(row.get("condition", "")).strip()
            if cond:
                txt = QGraphicsTextItem(cond)
                txt.setFont(self._font_sub)
                txt.setTextWidth(260)
                txt.setDefaultTextColor(QColor("#f9f9f9"))
                self.scene.addItem(txt)
                txt.setPos(rect.right() + 12, rect.center().y() - 10)
        else:
            self.scene.addRect(rect, self._pen_step, self._brush_step)
            name = str(row.get("name", "")).strip()
            proc = str(row.get("procedure", "")).strip()
            label = name if not proc else f"{name}\nProc: {proc}"
            txt = QGraphicsTextItem(label)
            txt.setFont(self._font_step)
            txt.setTextWidth(rect.width() - 16)
            opt = txt.document().defaultTextOption()
            opt.setAlignment(Qt.AlignmentFlag.AlignCenter)
            opt.setWrapMode(QTextOption.WrapMode.WrapAtWordBoundaryOrAnywhere)
            txt.document().setDefaultTextOption(opt)
            txt.setDefaultTextColor(QColor("#ffffff"))
            self.scene.addItem(txt)
            br = txt.boundingRect()
            txt.setPos(
                rect.center().x() - br.width() / 2,
                rect.center().y() - br.height() / 2,
            )

    def _draw_arrow_orthogonal(self, start: QPointF, end: QPointF, start_rect: QRectF, end_rect: QRectF):
        clear = 18.0
        if end.y() >= start.y():
            mid_y = start.y() + clear
            points = [
                start,
                QPointF(start.x(), mid_y),
                QPointF(end.x(), mid_y),
                end,
            ]
        else:
            # Wrapped to next column: route at the middle x between the two columns.
            side_x = (start_rect.center().x() + end_rect.center().x()) / 2.0
            y1 = start.y() + clear
            y2 = end.y() - clear
            points = [
                start,
                QPointF(start.x(), y1),
                QPointF(side_x, y1),
                QPointF(side_x, y2),
                QPointF(end.x(), y2),
                end,
            ]

        for p1, p2 in zip(points, points[1:]):
            self.scene.addLine(p1.x(), p1.y(), p2.x(), p2.y(), self._pen_line)

        p_last = points[-2]
        p_end = points[-1]
        dx = p_end.x() - p_last.x()
        dy = p_end.y() - p_last.y()
        length = math.hypot(dx, dy)
        if length < 1e-6:
            return
        ux, uy = dx / length, dy / length
        head_len = 10.0
        head_w = 6.0
        tip = p_end
        base = QPointF(p_end.x() - ux * head_len, p_end.y() - uy * head_len)
        left = QPointF(base.x() - uy * head_w, base.y() + ux * head_w)
        right = QPointF(base.x() + uy * head_w, base.y() - ux * head_w)
        tri = QPolygonF([tip, left, right])
        self.scene.addPolygon(tri, self._pen_line, QBrush(self._pen_line.color()))

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self._position_zoom_controls()
        # Keep initial view scale consistent with viewport size.
        self._fit_to_width_80()
