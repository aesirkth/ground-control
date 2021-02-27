# controller.py
import sys  # We need sys so that we can pass argv to QApplication

from utils.telecommand import Telecommand
from utils.widgets_ec import EngineController, EngineStatus
from utils.widgets_fc import FlightController, FlightStatus, FlightStatus2, DebugStatus
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import QPalette, QColor

INTERVAL = 30

class QHSeperationLine(QtWidgets.QFrame):
    """A horizontal seperation line"""

    def __init__(self):
        super().__init__()
        self.setMinimumWidth(1)
        self.setFixedHeight(5)
        # self.setContentsMargins(5, 0, 0, 0)
        self.setFrameShape(QtWidgets.QFrame.HLine)
        self.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)


class QVSeperationLine(QtWidgets.QFrame):
    """A vertical seperation line"""
    def __init__(self):
        super().__init__()
        self.setFixedWidth(20)
        self.setMinimumHeight(1)
        self.setContentsMargins(0, 5, 0, 5)
        self.setFrameShape(QtWidgets.QFrame.VLine)
        self.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.setSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)


# Main window
class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, tc, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle("Æsir - Control Dashboard")

        self.timer = QtCore.QTimer(self)
        self.timer.setInterval(INTERVAL)

        window = QtWidgets.QWidget()
        layout = QtWidgets.QGridLayout()

        layout.setContentsMargins(0,0,0,0)
        flightController = FlightController(tc)
        layout.addWidget(flightController, 0, 0)
        layout.addWidget(QVSeperationLine(), 0, 1)
        layout.addWidget(FlightStatus(tc, self.timer), 0, 2)
        hline1 = QHSeperationLine()
        hline1.setContentsMargins(5, 0, 0, 0)
        layout.addWidget(hline1, 1, 0, 1, 3)
        layout.addWidget(EngineController(tc), 2, 0)
        layout.addWidget(QVSeperationLine(), 2, 1)
        layout.addWidget(EngineStatus(tc, self.timer), 2, 2)
        layout.addWidget(QVSeperationLine(), 0, 3, 3, 1)
        layout.addWidget(FlightStatus2(tc, self.timer), 0, 4)
        hline2 = QHSeperationLine()
        hline2.setContentsMargins(0, 0, 5, 0)
        layout.addWidget(hline2, 1, 4)
        layout.addWidget(DebugStatus(tc, self.timer, flightController), 2, 4)
        window.setLayout(layout)

        self.timer.start()
        QtCore.QCoreApplication.setQuitLockEnabled(True)
        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(window)
        def closeEvent(event):
            tc.stop()
            event.accept()
        self.closeEvent = closeEvent

def main():

    # Telecommand
    tc = Telecommand()
    tc.open_serial()
    # Init Qt
    app = QtWidgets.QApplication(sys.argv)
    # print(QtWidgets.QStyleFactory.keys()) # Available styles
    app.setStyle('Fusion') # Selection of the style

    # set app icon
    app_icon = QtGui.QIcon()
    app_icon.addFile('gui/logo/16x16.png', QtCore.QSize(16,16))
    app_icon.addFile('gui/logo/24x24.png', QtCore.QSize(24,24))
    app_icon.addFile('gui/logo/32x32.png', QtCore.QSize(32,32))
    app_icon.addFile('gui/logo/48x48.png', QtCore.QSize(48,48))
    app_icon.addFile('gui/logo/256x256.png', QtCore.QSize(256,256))
    app.setWindowIcon(app_icon)

    w = MainWindow(tc)
    w.show()
    sys.exit(app.exec_())
    
main()