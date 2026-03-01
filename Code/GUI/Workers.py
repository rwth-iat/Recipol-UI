# Code/GUI/Workers.py
import time

from PyQt6.QtCore import QThread, pyqtSignal

# 引入后端函数
from Code.Recipol.mtpparser import getMtps

class Worker(QThread):
    log_signal = pyqtSignal(str)
    progress_signal = pyqtSignal(int)
    finished_signal = pyqtSignal()

    def __init__(self, files):
        super().__init__()
        self.files = files  # 文件绝对路径列表
        self.mtp_results = []

    def run(self):
        self.mtp_results = [] # 每次运行前清空结果
        # total = len(self.files)
        # for i, file in enumerate(self.files):
        #     # 模拟处理文件
        #     self.log_signal.emit(f"Processing: {file}")
        #     # getMtps()
        #     time.sleep(1)  # 这里换成真实处理逻辑

        #     # 更新进度条
        #     self.progress_signal.emit(int((i+1)/total*100))
        try:
            self.log_signal.emit("Starting batch processing of MTP tasks...")
            self.progress_signal.emit(20)

            # 调用后端，传入 UI 选中的文件
            # 这里的 self.files 就是你在 Home.py 里勾选的那些 .aml 文件
            self.mtp_results = getMtps(input_files=self.files, logger=self.log_signal.emit)     # 获取list[Pea]

            self.progress_signal.emit(100)
            self.log_signal.emit(f"Task completed. Processed {len(self.mtp_results)} modules in total.")
            
        except Exception as e:
            self.progress_signal.emit(100)
            self.log_signal.emit(f"Worker crashed during execution: {str(e)}")

        self.finished_signal.emit()
