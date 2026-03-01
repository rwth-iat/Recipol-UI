# Code/GUI/Workers.py
from PyQt6.QtCore import QThread, pyqtSignal

from Code.Recipol.mtpparser import getMtps


class Worker(QThread):
    log_signal = pyqtSignal(str)
    progress_signal = pyqtSignal(int)
    finished_signal = pyqtSignal()

    def __init__(self, files):
        super().__init__()
        self.files = files  # Absolute file path list selected in UI
        self.mtp_results = []
        self.failed_files = []

    def run(self):
        self.mtp_results = []
        self.failed_files = []
        total_files = len(self.files)
        success_files = 0

        if total_files == 0:
            self.progress_signal.emit(0)
            self.log_signal.emit("No MTP files to process.")
            self.finished_signal.emit()
            return

        self.log_signal.emit("Starting batch processing of MTP tasks...")

        for idx, file in enumerate(self.files, start=1):
            try:
                self.log_signal.emit(f"Processing ({idx}/{total_files}): {file}")
                parsed = getMtps(input_files=[file], logger=self.log_signal.emit)

                if parsed:
                    # Count one file as success when at least one module is parsed.
                    self.mtp_results.extend(parsed)
                    success_files += 1
                    self.log_signal.emit(f"Success: {file}")
                else:
                    self.failed_files.append(file)
                    self.log_signal.emit(f"No valid MTP data parsed from: {file}")
            except Exception as e:
                self.failed_files.append(file)
                self.log_signal.emit(f"Failed to process {file}: {str(e)}")

            # Progress is based on successful files only.
            self.progress_signal.emit(int(success_files / total_files * 100))

        if self.failed_files:
            self.log_signal.emit(
                f"Completed with issues: {success_files}/{total_files} files succeeded, "
                f"{len(self.failed_files)} failed."
            )
        else:
            self.log_signal.emit(f"Completed: all {total_files} files succeeded.")

        self.log_signal.emit(f"Task completed. Parsed {len(self.mtp_results)} modules in total.")
        self.finished_signal.emit()
