import sys
from PyQt5 import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Rename')

        # Create a QTabWidget
        tab_widget = QTabWidget()
        self.setCentralWidget(tab_widget)

        # Add some tabs
        tab_widget.addTab(QLabel('Tab 1'), 'Tab 1')
        tab_widget.addTab(QLabel('Tab 2'), 'Tab 2')

        # Set the contextMenuPolicy to CustomContextMenu
        tab_widget.setContextMenuPolicy(Qt.CustomContextMenu)

        # Connect the customContextMenuRequested signal to a slot
        tab_widget.customContextMenuRequested.connect(self.showContextMenu)

    def showContextMenu(self, position):
        # Get the index of the tab at the given position
        tab_widget = self.centralWidget()
        tab_index = tab_widget.tabBar().tabAt(position)

        #restricted for only to click on tabs
        if tab_index != -1:
            # Create a context menu
            context_menu = QMenu(self)

            # Add a rename action to the context menu
            rename_action = QAction('Rename Tab', tab_widget)
            rename_action.triggered.connect(lambda: self.renameTab(tab_index))
            context_menu.addAction(rename_action)

            #For screenshot option
            Screeshot_action = QAction('ScreenShot', tab_widget)
            Screeshot_action.triggered.connect(lambda: self.ScreenShot(tab_index))
            context_menu.addAction(Screeshot_action)

            # Show the context menu at the given position
            context_menu.exec_(self.mapToGlobal(position))

    def renameTab(self, tab_index):
        tab_widget = self.centralWidget()
        old_text = tab_widget.tabText(tab_index)

        new_text, ok = QInputDialog.getText(self, 'Rename Tab', 'Enter new tab name:', text=old_text)

        if ok:
            tab_widget.setTabText(tab_index, new_text)

    def ScreenShot():
        True
if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())