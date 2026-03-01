# gui_main.py
# -*- coding: utf-8 -*-

import sys
from PyQt6.QtWidgets import QApplication
from qfluentwidgets import (
    FluentWindow,
    FluentIcon,
    NavigationItemPosition,
    setTheme,
    Theme
)

from Code.GUI.Home import HomePage
from Code.GUI.Logs import LogPage
from Code.GUI.MTPViewer import MTPViewer


class MainWindow(FluentWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Recipol UI")
        self.resize(1150, 700)
        setTheme(Theme.DARK)

        # Pages
        self.log_page = LogPage(self)
        self.mtpviewer_page = MTPViewer(self)
        self.home_page = HomePage(self.log_page.append_log, self)
        self.home_page.data_ready_signal.connect(self.mtpviewer_page.update_data)      # data_ready_signal emit后，先通过信号自动通知 viewer_page 更新界面，（由于self.data_ready_signal.emit(parsed_mtps)传递来了parsed_mtps，即执行update_data(parsed_mtps)）
        self.home_page.data_ready_signal.connect(self.switch_to_viewer)             # 后跳转

        # Navigation 导航栏
        self.addSubInterface(
            self.home_page,
            FluentIcon.HOME,
            "Home",
            NavigationItemPosition.TOP
        )

        self.addSubInterface(
            self.mtpviewer_page,
            FluentIcon.VIEW,    
            "MTP Viewer",     
            NavigationItemPosition.TOP
        )

        self.addSubInterface(
            self.log_page,
            FluentIcon.DOCUMENT,
            "Logs",
            NavigationItemPosition.TOP
        )

        self.switchTo(self.home_page)
    
    def switch_to_viewer(self, mtps: list):
        """当收到数据准备好的信号时，切换到 MTP Viewer 页面"""
        if len(mtps) > 0:
            self.switchTo(self.mtpviewer_page)
        else:
            pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec())
