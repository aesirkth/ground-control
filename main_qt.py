# main.py
import sys  # We need sys so that we can pass argv to QApplication

from utils.widgets_qt import MainWindow
from utils.telemetry import Telemetry
from PyQt5 import QtWidgets, QtCore, QtGui


def main():
    #init threads
    tm = Telemetry()

    # Init Qt
    app = QtWidgets.QApplication(sys.argv)

    # set app icon    
    app_icon = QtGui.QIcon()
    app_icon.addFile('gui/logo/16x16.png', QtCore.QSize(16,16))
    app_icon.addFile('gui/logo/24x24.png', QtCore.QSize(24,24))
    app_icon.addFile('gui/logo/32x32.png', QtCore.QSize(32,32))
    app_icon.addFile('gui/logo/48x48.png', QtCore.QSize(48,48))
    app_icon.addFile('gui/logo/256x256.png', QtCore.QSize(256,256))
    app.setWindowIcon(app_icon)

    w = MainWindow()
    w.show()
    sys.exit(app.exec_())
    
main()
