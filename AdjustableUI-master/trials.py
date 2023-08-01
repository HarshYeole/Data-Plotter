import sys
import time
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class Signals(QObject):
    started = pyqtSignal(int)
    completed = pyqtSignal(int)


class Worker(QRunnable):
    def __init__(self, n):
        super().__init__()
        self.n = n
        self.signals = Signals()

    def run(self):
        self.signals.started.emit(self.n)
        time.sleep(self.n*1.1)
        self.signals.completed.emit(self.n)


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle('QThreadPool Demo')
        self.job_count = 100
        self.completed_jobs = []

        widget = QWidget()
        widget.setLayout(QGridLayout())
        self.setCentralWidget(widget)

        self.btn_start = QPushButton('Start', clicked=self.start_jobs)
        self.progress_bar = QProgressBar(minimum=0, maximum=self.job_count)
        self.list = QListWidget()
        widget.layout().addWidget(self.list, 0, 0, 1, 2)
        widget.layout().addWidget(self.progress_bar, 1, 0)
        widget.layout().addWidget(self.btn_start, 1, 1)

        self.show()

    def start_jobs(self):
        self.restart()
        pool = QThreadPool.globalInstance()
        pool.setMaxThreadCount(100)
        for i in range(1, self.job_count+1):
            worker = Worker(i)
            worker.signals.started.connect(self.start)
            worker.signals.completed.connect(self.complete)
            pool.start(worker)

    def restart(self):
        self.progress_bar.setValue(0)
        self.completed_jobs = []

    def start(self, n):
        self.list.addItem(f'Job #{n} started...')

    def complete(self, n):
        self.list.addItem(f'Job #{n} completed.')
        self.completed_jobs.append(n)
        self.progress_bar.setValue(len(self.completed_jobs))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
