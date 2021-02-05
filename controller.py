# controller.py
import sys  # We need sys so that we can pass argv to QApplication

from utils.telecommand import Telecommand
from utils.widgets_ec import EngineController
from utils.widgets_fc import FlightController
from PyQt5 import QtWidgets, QtCore, QtGui


class QHSeperationLine(QtWidgets.QFrame):
  """A horizontal seperation line"""

  def __init__(self):
    super().__init__()
    self.setMinimumWidth(1)
    self.setFixedHeight(20)
    self.setFrameShape(QtWidgets.QFrame.HLine)
    self.setFrameShadow(QtWidgets.QFrame.Sunken)
    self.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)


class QVSeperationLine(QtWidgets.QFrame):
  """A vertical seperation line"""
  def __init__(self):
    super().__init__()
    self.setFixedWidth(20)
    self.setMinimumHeight(1)
    self.setFrameShape(QtWidgets.QFrame.VLine)
    self.setFrameShadow(QtWidgets.QFrame.Sunken)
    self.setSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)


# Main window
class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, tc, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle("Æsir - Control Dashboard")

        window = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout()
        layout.setContentsMargins(0,0,0,0)
        layout.addWidget(EngineController(tc))
        layout.addWidget(QHSeperationLine())
        layout.addWidget(FlightController(tc))
        window.setLayout(layout)

        QtCore.QCoreApplication.setQuitLockEnabled(True)
        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(window)


def main():

    # Telecommand
    tc = Telecommand()

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