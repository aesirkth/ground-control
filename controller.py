# controller.py
import sys  # We need sys so that we can pass argv to QApplication

from utils.telecommand import Telecommand
from utils.widgets_ec import EngineController, EngineStatus
from utils.widgets_fc import FlightController, FlightStatus, FlightStatus2, DebugStatus
from utils.widgets_edb import InfoDialog
from PyQt5 import QtWidgets, QtCore, QtGui

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


class MenuBar(QtWidgets.QMenuBar):
    def __init__(self, parent=None):
        super().__init__(parent=parent)

        # File
        self.fileMenu = QtWidgets.QMenu("&File", self)

        self.openSerial = QtWidgets.QAction("Open &serial")
        self.openSerial.triggered.connect(self.parent()._open_serial)

        self.exit = QtWidgets.QAction("&Exit")
        self.exit.triggered.connect(self.parent().close)

        self.fileMenu.addAction(self.openSerial)
        self.fileMenu.addAction(self.exit)
        self.addMenu(self.fileMenu)

        # Help
        self.helpMenu = QtWidgets.QMenu("&Help", self)

        self.aboutFEC = QtWidgets.QAction("About Flight/Engine &Controller")
        self.aboutFEC.triggered.connect(self._aboutFEC)

        self.aboutAesir = QtWidgets.QAction("&About Æsir")
        self.aboutAesir.triggered.connect(self._aboutAesir)

        self.helpMenu.addAction(self.aboutFEC)
        self.helpMenu.addAction(self.aboutAesir)
        self.addMenu(self.helpMenu)

    def _aboutFEC(self):
        title = "Controller"
        text = """Here some text"""
        InfoDialog(title, text).exec_()

    def _aboutAesir(self):
        title = "Æsir"
        text = """ÆSIR is a student rocketry association founded in 2016 at KTH Royal Institute of Technology in Stockholm. It has around 40 members every year, which are all students at KTH. Roughly half of the members are international students and they cover many disciplines and levels of study, although most of ÆSIR's members study Aerospace Engineering, Computer Science, Vehicle Engineering, Electrical Engineering, Engineering Physics and Mechanical Engineering.<br /><br /><a href=\"http://aesir.se\">ÆSIR website</a>"""
        image = 'gui/logo/256x256.png'
        InfoDialog(title, text, image).exec_()


# Main window
class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, tc, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle("Æsir - Control Dashboard")

        self.timer = QtCore.QTimer(self)
        self.timer.setInterval(INTERVAL)
        self.tc = tc

        window = QtWidgets.QWidget()
        layout = QtWidgets.QGridLayout()

        layout.setContentsMargins(0,0,0,0)
        self.flightController = FlightController(tc, parent=self)
        layout.addWidget(self.flightController, 0, 0)
        layout.addWidget(QVSeperationLine(), 0, 1)
        layout.addWidget(FlightStatus(tc, self.timer), 0, 2)
        hline1 = QHSeperationLine()
        hline1.setContentsMargins(5, 0, 0, 0)
        layout.addWidget(hline1, 1, 0, 1, 3)
        self.engineController = EngineController(tc, parent=self)
        layout.addWidget(self.engineController, 2, 0)
        layout.addWidget(QVSeperationLine(), 2, 1)
        layout.addWidget(EngineStatus(tc, self.timer), 2, 2)
        layout.addWidget(QVSeperationLine(), 0, 3, 3, 1)
        layout.addWidget(FlightStatus2(tc, self.timer), 0, 4)
        hline2 = QHSeperationLine()
        hline2.setContentsMargins(0, 0, 5, 0)
        layout.addWidget(hline2, 1, 4)
        layout.addWidget(DebugStatus(tc, self.timer, self.flightController), 2, 4)
        window.setLayout(layout)

        # Menu bar
        self.menuBar = MenuBar(parent=self)
        self.setMenuBar(self.menuBar)

        self.timer.start()
        QtCore.QCoreApplication.setQuitLockEnabled(True)
        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(window)
        def closeEvent(event):
            tc.stop()
            event.accept()
        self.closeEvent = closeEvent

    def _open_serial(self):
        self.flightController.serial.setEnabled(False)
        self.engineController.serial.setEnabled(False)
        if self.tc.open_serial():
            if not self.flightController.power.state:
                self.flightController.power.setEnabled(True)
            if not self.engineController.power.state:
                self.flightController.power.setEnabled(True)
        else:
            self.flightController.serial.setEnabled(True)
            self.engineController.serial.setEnabled(True)
            print("Error while opening serial")


def main():

    # Telecommand
    tc = Telecommand()
    # tc.open_serial()
    
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