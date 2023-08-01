from PyQt5 import QtCore, QtGui, QtWidgets
from CustomWidgets import *
from PyQt5.QtWidgets import *
from FindDevices import *
from PyQt5.QtCore import QThreadPool, QRunnable
from backend import *
import threading

WINDOW_SIZE = (1000, 600)
DEVICE_LIST = []


class MainWindow(object):

    def __init__(self, main_window):
        # Central widget for main_window
        self.centralwidget = QtWidgets.QWidget(main_window)
        self.centralwidget.setObjectName("centralwidget")
        # Initialising everything
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.add_osci = PushButton(parent=self.centralwidget, objectName="add_oscilloscope")
        self.button_plot_all = PushButton(parent=self.centralwidget, objectName="button_plot_all")
        self.device_list = Box(parent=self.centralwidget, objectName="device_list")
        self.parameter_list = Box(parent=self.centralwidget, objectName="parameter_list")
        self.tabWidget = TabWidget(parent=self.centralwidget, objectName="graphs_holder", closeable=True, updated=True)
        self.axes_selector = Box(parent=self.centralwidget, objectName="axes_selector")
        self.SetupUI(main_window)

        # Starts threads for backend
        self.port_updater = QThreadPool()
        changed_ports = UpdatePorts(list_layout=self.device_listLayout)
        changed_ports.signal.new.connect(lambda name: self.device_listLayout.addWidget(CheckBox(text=name, objectName=name)))
        changed_ports.signal.removed.connect(lambda name: self.device_listLayout.removeWidget(self.remove_removed_devices(name)))
        self.port_updater.start(changed_ports)

        # Lists the parameters of Ports added
        # self.port_params = QThreadPool()

    def SetupUI(self, main_window):
        # Stores the received main window in main_window
        main_window.setObjectName("MainWindow")
        main_window.setWindowTitle("MainWindow")
        main_window.resize(WINDOW_SIZE[0], WINDOW_SIZE[1])
        main_window.setMinimumSize(QtCore.QSize(WINDOW_SIZE[0], WINDOW_SIZE[1]))
        # Grid Layout for our Central Widget
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.gridLayout.setObjectName("gridLayout")
        # Buttons Section
        # ---------- Add CRO
        self.add_osci.setText("Add CRO/DSO")
        self.add_osci.setFont(custom_font(size=9))
        self.add_osci.setSizePolicy(custom_size_policy(QSizePolicy.Expanding, QSizePolicy.Ignored, 1, 0))
        self.add_osci.clicked.connect(lambda: getOscilloscope())
        self.gridLayout.addWidget(self.add_osci, 1, 0)
        # ---------- Plot all button
        self.button_plot_all.setText("Plot All")
        self.button_plot_all.setFont(custom_font(size=9))
        self.button_plot_all.setSizePolicy(custom_size_policy(QSizePolicy.Expanding, QSizePolicy.Expanding, 1, 1))
        self.gridLayout.addWidget(self.button_plot_all, 3, 0)
        # Group Boxes for Listing
        # ---------- Parameter List
        self.parameter_list.setTitle("Parameter List")
        self.parameter_list.setSizePolicy(custom_size_policy(QSizePolicy.Expanding, QSizePolicy.Expanding, 1, 0))
        self.parameter_list.setFont(custom_font(size=12))
        self.parameter_list.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.gridLayout.addWidget(self.parameter_list, 0, 2, 4, 1)
        # ---------- Device List
        self.device_list.setTitle("Device List")
        self.device_list.setSizePolicy(custom_size_policy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding, 1, 5))
        self.device_list.setFont(custom_font(size=12))
        self.device_list.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.device_listLayout = QVBoxLayout(self.device_list)
        self.device_listLayout.setAlignment(QtCore.Qt.AlignTop)
        self.gridLayout.addWidget(self.device_list, 0, 0)
        # ---------- Axes Selector
        self.axes_selector.setTitle("Axes Selector")
        self.axes_selector.setSizePolicy(custom_size_policy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding, 1, 5))
        self.axes_selector.setFont(custom_font(size=12))
        self.axes_selector.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.gridLayout.addWidget(self.axes_selector, 2, 0)
        # Tab Widget
        self.tabWidget.setWindowTitle("Graph Holder")
        self.tabWidget.setSizePolicy(custom_size_policy(QSizePolicy.Expanding, QSizePolicy.Expanding, 4, 1))
        self.tabWidget.setFont(custom_font(size=11))
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget.tabCloseRequested.connect(lambda index: remove_tab(index=index, parent=self.tabWidget))
        # ---------- Adding Start Tabs
        self.tabWidget.insertTab(0, QWidget(), "Main Tab")
        NewTab(parent=self.tabWidget)
        self.gridLayout.addWidget(self.tabWidget, 0, 1, 4, 1)
        # Sets Central Widget
        main_window.setCentralWidget(self.centralwidget)

    def remove_removed_devices(self, name):
        for i in range(self.device_listLayout.count()):
            widget = self.device_listLayout.itemAt(i).widget()
            if widget.objectName() == name:
                widget.setParent(None)
                return widget
            return


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QMainWindow()
    ui = MainWindow(window)
    window.show()
    sys.exit(app.exec_())