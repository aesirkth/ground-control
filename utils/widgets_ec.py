from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor


class TitleWidget(QtWidgets.QLabel):
    """Widget use to write columns' title"""
    def __init__(self, text, parent=None):
        super(TitleWidget, self).__init__(text, parent)

        # Alignment / Font size
        self.setAlignment(Qt.AlignCenter)
        font = self.font()
        font.setPointSize(20)
        self.setFont(font)

        self.setMinimumSize(160, 0)

        # Background color
        # self.setAutoFillBackground(True)
        # palette = self.palette()
        # palette.setColor(QPalette.Window, QColor("white"))
        # self.setPalette(palette)

        self.setFixedHeight(35)



class PowerMode(QtWidgets.QPushButton):
    def __init__(self, tc, engineState):
        text = "Turn on"
        shortcut = "Ctrl+P"
        tooltip = "{} ({})".format(text, shortcut)

        super(PowerMode, self).__init__(text)
        self.setShortcut(shortcut)  # Shortcut key
        self.clicked.connect(self._powerOn)
        self.setToolTip(tooltip) # Tool tip

        self.engineState = engineState
        self.engineState.power = self

        self.tc = tc


    def _powerOn(self):
        self.tc.set_engine_power_mode(None).then(self._update) # TBD


    def _update(self, result):
        # if not result:
        #     print("Engine power: Got no response")
        #     return

        # PUT HERE SOME VERIFICATION OF THE POWER STATUS (WAIT FOR THE DATA PROTOCOL TO BE UPDATED)

        self.engineState.activate()
        self.setEnabled(False)
        print("Engine on")



class EngineState(QtWidgets.QWidget):
    def __init__(self, tc, fire, parent=None): 
        super(EngineState, self).__init__(parent=parent)
        self.tc = tc
        self.fire = fire

        shortcutAbort = "Ctrl+C"
        tooltipAbort = "Abort the mission (Ctrl+C)"
        tooltipArming = "Arming the engine"
        tooltipEnable = "Enable/Disable the engine"


        layout = QtWidgets.QGridLayout()
        layout.setContentsMargins(0,0,0,0)

        self.abort = QtWidgets.QPushButton("Abort")
        self.abort.setShortcut(shortcutAbort)  # Shortcut key
        self.abort.clicked.connect(self._functionAbort)
        self.abort.setToolTip(tooltipAbort) # Tool tip
        self.abort.setEnabled(False)

        sizePolicy = self.abort.sizePolicy()
        sizePolicy.setVerticalPolicy(QtWidgets.QSizePolicy.Minimum)
        self.abort.setSizePolicy(sizePolicy)
        layout.addWidget(self.abort, 0, 0, 3, 1)

        self.arming = QtWidgets.QPushButton("Arming")
        self.arming.clicked.connect(self._functionArming)
        self.arming.setToolTip(tooltipArming) # Tool tip
        self.arming.setEnabled(False)
        layout.addWidget(self.arming, 1, 1, 1, 2)

        self.enable = QtWidgets.QPushButton("Enable")
        self.enable.clicked.connect(self._functionEnable)
        self.enable.setToolTip(tooltipEnable) # Tool tip
        self.enable.setEnabled(False)
        layout.addWidget(self.enable, 2, 1, 1, 2)

        self.status = QtWidgets.QLabel("Engine off")
        self.status.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.status, 0, 1, 1, 2)

        self.setLayout(layout)


    def _functionAbort(self):
        error = self.tc.set_engine_state(True, False, False).wait()
        # if error == -1:
        #     print("Serial closed")
        #     return
        print("Abort the mission !")
        self.disableAll()


    def _functionArming(self):
        error = self.tc.set_engine_state(False, True, False)
        # if error == -1:
        #     print("Serial closed")
        #     return
        print("Arming the engine...")
        self.enable.setEnabled(True)
        self.arming.setEnabled(False)
        self.status.setText("Engine armed")


    def _functionEnable(self):
        error = self.tc.set_engine_state(False, True, True)
        # if error == -1:
        #     print("Serial closed")
        #     return
        print("This is the greatest plan !")
        self.fire.setEnabled(True)
        self.enable.setEnabled(False)
        self.status.setText("Engine enabled")


    def activate(self):
        self.abort.setEnabled(True)
        self.arming.setEnabled(True)
        self.status.setText("Engine on")


    def disableAll(self):
        self.abort.setEnabled(False)
        self.arming.setEnabled(False)
        self.enable.setEnabled(False)
        self.fire.setEnabled(False)
        self.power.setEnabled(True)
        self.status.setText("Engine off")
        

class FireRocket(QtWidgets.QPushButton):
    def __init__(self, tc):
        text = "Fire the rocket"
        fonction = tc.fire_rocket
        shortcut = "Ctrl+F"
        tooltip = "{} ({})".format(text, shortcut)
        debug = "Fire Rocket"

        super(FireRocket, self).__init__(text)
        self.setShortcut(shortcut)  #shortcut key
        self.clicked.connect(fonction)
        self.setToolTip(tooltip) #Tool tip
        self.setEnabled(False)


class EngineController(QtWidgets.QWidget):

   def __init__(self, tc, parent=None):
        super(EngineController, self).__init__(parent=parent)

        title = TitleWidget("Engine Controller")
        fire = FireRocket(tc)
        engineState = EngineState(tc, fire)
        power = PowerMode(tc, engineState)


        title.setMinimumSize(250, 0)
        

        layout = QtWidgets.QVBoxLayout()
        layout.setContentsMargins(5,5,5,5)
        layout.setSpacing(10)
        widgets = [title, power, engineState, fire]
        
        for w in widgets:
            layout.addWidget(w)

        # self.timer = QtCore.QTimer(self)
        # self.timer.setInterval(30)
        # layout.addWidget(ColoredSquare(self.timer))

        self.setLayout(layout)
        # self.timer.start()


class ColoredSquare(QtWidgets.QWidget):
    """A square of color!!"""
    def __init__(self, timer, parent=None):
        super().__init__(parent)
        self.status = False
        self.diameter = 25
        self.color = Qt.red

        self.setFixedSize(self.diameter, self.diameter)

        self.variable_for_demo = 0
        timer.timeout.connect(self.update_color)

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.setRenderHint(painter.Antialiasing)
        painter.setBrush(QtGui.QBrush(self.color, Qt.SolidPattern))
        # painter.setPen(Qt.NoPen)
        painter.setPen(QtGui.QPen(Qt.black,  2, Qt.SolidLine))
        painter.drawRect(0, 0, self.diameter, self.diameter)

    def update_color(self):
        self.variable_for_demo = (self.variable_for_demo + 1) % 100
        if self.variable_for_demo == 0:
            self.status = not self.status
            if self.status:
                self.color = Qt.green
            else:
                self.color = Qt.red
            self.update()


# class ToolButton(QtWidgets.QWidget):

#     def __init__(self):
#         super(ToolButton,self).__init__()
#         self.initUI()

#     def initUI(self):
#         self.setWindowTitle("ToolButton")
#         self.setGeometry(400,400,300,260)

#         self.toolbar = self.addToolBar("toolBar")
#         self.statusBar()

#         self._detailsbutton = QToolButton()                                     
#         self._detailsbutton.setCheckable(True)                                  
#         self._detailsbutton.setChecked(False)                                   
#         self._detailsbutton.setArrowType(Qt.RightArrow)
#         self._detailsbutton.setAutoRaise(True)
#         #self._detailsbutton.setIcon(QIcon("test.jpg"))
#         self._detailsbutton.setToolButtonStyle(Qt.ToolButtonIconOnly)
#         self._detailsbutton.clicked.connect(self.showDetail)
#         self.toolbar.addWidget(self._detailsbutton)

#     def showDetail(self):
#         if self._detailsbutton.isChecked():
#             self.statusBar().showMessage("Show Detail....")
#         else:
#             self.statusBar().showMessage("Close Detail....")



# Main window
class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, tc, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle("Æsir - Engine Control Dashboard")

        QtCore.QCoreApplication.setQuitLockEnabled(True)
        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(EngineController(tc, self))