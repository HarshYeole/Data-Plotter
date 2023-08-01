import sys
from PyQt5 import *
from PyQt5.QtWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Tab Rename Example')

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

    def showContextMenu(self, pos):
        # Get the index of the tab at the given position
        tab_widget = self.centralWidget()
        tab_index = tab_widget.tabBar().tabAt(pos)

        # Create a context menu
        context_menu = QMenu(self)

        # Add a rename action to the context menu
        rename_action = QAction('Rename Tab', self)
        rename_action.triggered.connect(lambda: self.renameTab(tab_index))
        context_menu.addAction(rename_action)

        # Show the context menu at the given position
        context_menu.exec_(self.mapToGlobal(pos))

    def renameTab(self, tab_index):
        # Get the current text of the tab
        tab_widget = self.centralWidget()
        old_text = tab_widget.tabText(tab_index)

        # Ask the user for the new text of the tab
        new_text, ok = QInputDialog.getText(self, 'Rename Tab', 'Enter new tab name:', text=old_text)

        # If the user clicked OK, set the new text of the tab
        if ok:
            tab_widget.setTabText(tab_index, new_text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())

