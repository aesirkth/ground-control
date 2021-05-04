from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor
from utils.widgets_edb import DataWidget


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


class OpenSerial(QtWidgets.QPushButton):
	def __init__(self, parent):
		self.parent = parent
		text = "Open serial"
		self.shortcut = "Ctrl+O"
		tooltip = "{} ({})".format("Open the serial communication", self.shortcut)

		super(OpenSerial, self).__init__(text)
		self.setShortcut(self.shortcut) # Shortcut key
		self.clicked.connect(self.parent.parent()._open_serial)
		self.setToolTip(tooltip) # Tool tip


class PowerMode(QtWidgets.QPushButton):
	def __init__(self, tc, engineState):
		text = "Turn on"
		shortcut = "Ctrl+M"
		tooltip = "{} ({})".format(text, shortcut)

		super(PowerMode, self).__init__(text)
		self.setShortcut(shortcut)  # Shortcut key
		self.clicked.connect(self._powerOn)
		self.setToolTip(tooltip) # Tool tip

		self.engineState = engineState
		self.engineState.power = self

		self.tc = tc
		self.state = False # Power is off
		self.setEnabled(False)

	def _powerOn(self):
		self.tc.set_engine_power_mode(None).then(self._update) # TBD

	def _update(self, result):
		# if not result:
		#     print("Engine power: Got no response")
		#     return

		# PUT HERE SOME VERIFICATION OF THE POWER STATUS (WAIT FOR THE DATA PROTOCOL TO BE UPDATED)

		self.engineState.setEnabled(True)
		self.setEnabled(False)
		self.state = True
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
		self.setEnabled(False)
		error = self.tc.set_engine_state(True, False, False).wait()
		print(error)
		# if error == -1:
		#     print("Serial closed")
		#     return
		print("Abort the mission !")
		self.power.setEnabled(True)
		self.power.state = False

	def _functionArming(self):
		self.arming.setEnabled(False)
		self.tc.set_engine_state(False, True, False).then(self._updateArming)

	def _updateArming(self, result):
		# if not result:
		#     print("Engine power: Got no response")
		#     return

		# PUT HERE SOME VERIFICATION OF THE ARMING STATUS (WAIT FOR THE DATA PROTOCOL TO BE UPDATED)
		# DON'T FORGET TO ENABLE THE BUTTON

		print("Arming the engine...")
		self.enable.setEnabled(True)
		self.status.setText("Engine armed")


	def _functionEnable(self):
		self.enable.setEnabled(False)
		self.tc.set_engine_state(False, True, True).then(self._updateEnable)


	def _updateEnable(self, result):
		# if not result:
		#     print("Engine power: Got no response")
		#     return

		# PUT HERE SOME VERIFICATION OF THE ARMING STATUS (WAIT FOR THE DATA PROTOCOL TO BE UPDATED)
		# DON'T FORGET TO ENABLE THE BUTTON

		print("This is the greatest plan!")
		self.fire.setEnabled(True)
		self.status.setText("Engine enabled")


	def setEnabled(self, b):
		self.abort.setEnabled(b)
		self.arming.setEnabled(b)
		self.enable.setEnabled(False)
		self.fire.setEnabled(False)
		if b:
			self.status.setText("Engine on")
		else:
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
		self.serial = OpenSerial(self)
		fire = FireRocket(tc)
		engineState = EngineState(tc, fire)
		self.power = PowerMode(tc, engineState)


		title.setMinimumSize(250, 0)
		

		layout = QtWidgets.QVBoxLayout()
		layout.setContentsMargins(5,5,5,5)
		layout.setSpacing(10)
		widgets = [title, self.serial, self.power, engineState, fire]
		
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
		self.diameter = 15
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


class ValueIndicator(QtWidgets.QWidget):
	"""ValueIndicator"""
	def __init__(self, text, timer, updateFunction, sizeTitle=10, sizeData=11, formatting="{}", parent=None):
		super(ValueIndicator, self).__init__(parent)

		# Background color
		# self.setAutoFillBackground(True)
		# palette = self.palette()
		# palette.setColor(QPalette.Window, QColor("white"))
		# self.setPalette(palette)

		# Layout
		layout = QtWidgets.QHBoxLayout()
		layout.setAlignment(Qt.AlignVCenter)
		# Title
		self.title = QtWidgets.QLabel(text)
		self.title.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
		font = self.title.font()
		font.setPointSize(sizeTitle)
		self.title.setFont(font)

		# Indicator
		self.indic = DataWidget("-", timer, updateFunction, sizeData, formatting=formatting)
		self.indic.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
		# self.indic.setContentsMargins(0,0,0,0)
		self.indic.setFixedHeight(14)

		layout.addWidget(self.title)
		layout.addWidget(self.indic)
		layout.setContentsMargins(0,0,0,0)

		self.setLayout(layout)


class WareStatus(QtWidgets.QWidget):
	"""Software and hardware status"""
	def __init__(self, tc, timer, parent=None):
		super(WareStatus, self).__init__(parent=parent)
		self.tc = tc

		# ValueIndicator(text, timer, updateFunction, sizeTitle=15, sizeData=17, formatting="{}", parent=None)
		soft = ValueIndicator("Software state:", timer, self._updateSoft)
		hard = ValueIndicator("Hardware state:", timer, self._updateHard)

		# soft.title.setFixedHeight(12)
		# soft.indic.setFixedHeight(12)
		# hard.title.setFixedHeight(12)
		# hard.indic.setFixedHeight(12)
		# print(soft.sizeHint())
		# print(soft.title.sizeHint())
		# print(soft.indic.sizeHint())

		# soft.setAutoFillBackground(False)
		# hard.setAutoFillBackground(False)

		layout = QtWidgets.QVBoxLayout()
		layout.setContentsMargins(0,0,0,0)
		layout.setSpacing(0)
		layout.addWidget(soft)
		layout.addWidget(hard)
		self.setLayout(layout)

	def _updateSoft(self):
		return "TBD"

	def _updateHard(self):
		return "TBD"


class PowerModeStatus(ValueIndicator):
	def __init__(self, tc, timer, parent=None):
		super(PowerModeStatus, self).__init__("Power", timer, self._updateFunction, sizeTitle=10, sizeData=11)
		self.tc = tc

	def _updateFunction(self):
		return "Off"


class EngineStateStatus(QtWidgets.QWidget):
	def __init__(self, tc, timer, parent=None):
		super(EngineStateStatus, self).__init__(parent=parent)
		self.tc = tc

		abort = ValueIndicator("Abort:", timer, self._updateAbort)
		armed = ValueIndicator("Engine armed:", timer, self._updateArmed)
		enable = ValueIndicator("Engine enabled:", timer, self._updateEnable)

		# abort.title.setFixedHeight(12)
		# abort.indic.setFixedHeight(12)
		# armed.title.setFixedHeight(12)
		# armed.indic.setFixedHeight(12)
		# enable.title.setFixedHeight(12)
		# enable.indic.setFixedHeight(12)

		# soft.setAutoFillBackground(False)
		# hard.setAutoFillBackground(False)

		layout = QtWidgets.QVBoxLayout()
		layout.setContentsMargins(0,0,0,0)
		layout.setSpacing(0)
		layout.addWidget(abort)
		layout.addWidget(armed)
		layout.addWidget(enable)
		self.setLayout(layout)

	def _updateAbort(self):
		return "No"


	def _updateArmed(self):
		return "No"


	def _updateEnable(self):
		return "No"


class FireConfirmation(QtWidgets.QWidget):
	"""FireConfirmation"""
	def __init__(self, tc, timer, parent=None):
		super(FireConfirmation, self).__init__(parent)
		self.tc = tc

		# Layout
		layout = QtWidgets.QHBoxLayout()
		layout.setAlignment(Qt.AlignVCenter)
		layout.setContentsMargins(0,0,0,0)
		# Title
		title = QtWidgets.QLabel("Fire confirmation")
		title.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
		font = title.font()
		font.setPointSize(10)
		title.setFont(font)

		# Indicator
		self.indic = ColoredSquare(timer)

		layout.addWidget(title)
		layout.addWidget(self.indic)

		self.setLayout(layout)

		# timer.timeout.connect(self._updateFunction)

	def _updateFunction(self):
		self.indic.status = False
		

class EngineStatus(QtWidgets.QWidget):
	def __init__(self, tc, timer, parent=None):
		super(EngineStatus, self).__init__(parent=parent)

		self.setMinimumSize(230, 0)

		# title = TitleWidget("Engine Status")
		wareStatus = WareStatus(tc, timer)
		powerModeStatus = PowerModeStatus(tc, timer)
		engineStateStatus = EngineStateStatus(tc, timer)
		fireConfirmation = FireConfirmation(tc, timer)

		# title.setMinimumSize(250, 0)

		layout = QtWidgets.QVBoxLayout()
		layout.setContentsMargins(0,0,10,5)
		layout.setSpacing(10)
		widgets = [wareStatus, powerModeStatus, engineStateStatus, fireConfirmation]
		
		for w in widgets:
			layout.addWidget(w)

		self.setLayout(layout)


# Main window
class MainWindow(QtWidgets.QMainWindow):

	def __init__(self, tc, *args, **kwargs):
		super(MainWindow, self).__init__(*args, **kwargs)
		self.setWindowTitle("Æsir - Engine Control Dashboard")

		QtCore.QCoreApplication.setQuitLockEnabled(True)
		# Set the central widget of the Window. Widget will expand
		# to take up all the space in the window by default.
		self.setCentralWidget(EngineController(tc, self))