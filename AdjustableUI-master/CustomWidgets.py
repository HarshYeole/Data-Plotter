from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import *


_translate = QtCore.QCoreApplication.translate


# GUI functions
def custom_font(family: str = "Century", size: int = 10):
    font = QtGui.QFont()
    font.setFamily(family)
    font.setPointSize(size)
    return font


def custom_size_policy(x: object = "QSizePolicy", y: object = "QSizePolicy", h: int = None, v: int = None):
    sizePolicy = QSizePolicy(x, y)
    if h and v is not None:
        sizePolicy.setHorizontalStretch(h)
        sizePolicy.setVerticalStretch(v)
    return sizePolicy


def CheckBox(text: str, objectName: str, _list: list = None, parent: object = None, size: int = 10):
    check_box = QCheckBox()
    if parent is not None:
        check_box = QCheckBox(parent)
    if _list is not None:
        check_box.setGeometry(QtCore.QRect(_list[0], _list[1], _list[2], _list[3]))
    check_box.setText(text)
    check_box.setObjectName(objectName)
    check_box.setFont(custom_font(size=size))
    return check_box


def PushButton(parent: object, objectName: str, location: list = None, size: int = 9):
    button = QPushButton(parent)
    if location is not None:
        button.setGeometry(QtCore.QRect(location[0], location[1], location[2], location[3]))
    button.setFont(custom_font(size=size))
    button.setObjectName(objectName)
    return button


def Box(parent: object, objectName: str, size: int = 10, location: list = None):
    box = QGroupBox(parent)
    if location is not None:
        box.setGeometry(QtCore.QRect(location[0], location[1], location[2], location[3]))
    box.setFont(custom_font(size=size))
    box.setObjectName(objectName)
    return box


def ScrollBox(parent: object, location: list, objectName: str):
    Scroll = QScrollArea(parent)
    Scroll.setGeometry(QtCore.QRect(location[0], location[1], location[2], location[3]))
    Scroll.setFrameShape(QFrame.NoFrame)
    Scroll.setWidgetResizable(True)
    Scroll.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
    Scroll.setObjectName(objectName)
    return Scroll


def TabWidget(parent: object, objectName: str, location: list = None,  closeable: bool = True, updated: bool = True, family: str = "Segeo UI",
              size: int = 10):
    tab = QTabWidget(parent)
    if location is not None:
        tab.setGeometry(QtCore.QRect(location[0], location[1], location[2], location[3]))
    tab.setTabShape(QTabWidget.Triangular)
    tab.setTabsClosable(closeable)
    if updated:
        tab.setUpdatesEnabled(True)
        tab.currentChanged.connect(lambda: NewTab(parent=tab))
    tab.setObjectName(objectName)
    tab.setFont(custom_font(family=family, size=size))
    return tab


# ----Tab functions
def remove_tab(parent, index):
    if parent.count() != 2 and index != 0 and index != parent.count() - 1:
        if parent.currentIndex() == parent.count() - 2:
            parent.setCurrentIndex(parent.currentIndex() - 1)
        parent.removeTab(index)


def NewTab(parent):
    tab = QWidget()
    count = parent.count()
    if count - 1 == parent.currentIndex():
        parent.addTab(tab, '')
        parent.setTabText(parent.indexOf(tab), _translate("MainWindow", ' + '))
        parent.widget(parent.indexOf(tab)).setObjectName('AddTab')
    if parent.count() == 2:
        return
    parent.setTabText(parent.indexOf(tab) - 1, _translate("MainWindow", "Tab"))
