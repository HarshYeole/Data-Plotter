from PyQt5.QtCore import QThreadPool, QRunnable, pyqtSlot
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from main import DEVICE_LIST
from FindDevices import *
import time


class Signals(QObject):
    new = pyqtSignal(str)
    removed = pyqtSignal(str)


class UpdatePorts(QRunnable):

    def __init__(self, list_layout):
        super().__init__()
        self.list = list_layout
        self.signal = Signals()

    def run(self):
        global DEVICE_LIST
        children = set()
        while True:
            DEVICE_LIST = getPorts()
            for i in range(self.list.count()):
                item = self.list.itemAt(i).widget()
                children.add(item.objectName())
                if item.objectName() not in DEVICE_LIST:
                    children.remove(item.objectName())
                    self.signal.removed.emit(item.objectName())
            for device in DEVICE_LIST:
                if device not in children:
                    self.signal.new.emit(device)
            time.sleep(1)


class PortParameters(QRunnable):

    def __init__(self, list_layout):
        super().__init__()
        self.list = list_layout
        self.signal = Signals()

    def run(self):
        pass