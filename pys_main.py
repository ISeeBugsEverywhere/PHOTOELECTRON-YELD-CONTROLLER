from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os

from UI.pys_main_window import Ui_PYSWindow


class mainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_PYSWindow()
        self.ui.setupUi(self)
        self.__signals__()
        pass

    def __signals__(self):
        # close action
        self.ui.actionClose.triggered.connect(self.close_app)
        pass

    def close_app(self):
        self.close()
        sys.exit(0)
        pass


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = mainWindow()
    win.show()
    sys.exit(app.exec())
