from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor
from utils.widgets_ec import ValueIndicator


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
	def __init__(self, tc, radioEquipment, parachute, backup):
		text = "Turn on"
		self.shortcut = "Ctrl+P"
		tooltip = "{} ({})".format("Turn the power on and synchronise the clock", self.shortcut)

		super(PowerMode, self).__init__(text)
		self.setShortcut(self.shortcut) # Shortcut key
		self.clicked.connect(self._power)
		self.setToolTip(tooltip) # Tool tip

		self.radioEquipment = radioEquipment
		self.parachute = parachute
		self.backup = backup

		self.tc = tc

		self.state = False # Power is off


	def _power(self):
		if self.state:
			self._powerOff()
		else:
			self._powerOn()

	def _powerOn(self):
		self.setEnabled(False)
		self.tc.set_flight_power_mode(None).then(self._timeSync) # TBD

	def _powerOff(self):
		self.setEnabled(False)
		self.radioEquipment.setEnabled(False)
		self.parachute.setEnabled(False)
		self.backup.setEnabled(False)
		self.tc.set_flight_power_mode(None).then(self._powerIsOff) # TBD

	def _timeSync(self, result):
		# if not result:
		#     print("Flight power: Got no response")
		#     return

		# PUT HERE SOME VERIFICATION OF THE POWER STATUS (WAIT FOR THE DATA PROTOCOL TO BE UPDATED)

		print("Power on")
		self.tc.time_sync().then(self._powerIsOn)

	def _powerIsOn(self, result):
		# if not result:
		#     print("Time Sync: Got no response")
		#     return

		# PUT HERE SOME VERIFICATION OF THE POWER STATUS (WAIT FOR THE DATA PROTOCOL TO BE UPDATED)

		self.radioEquipment.setEnabled(True)
		self.parachute.setEnabled(True)
		self.backup.setEnabled(True)
		print("Time synchronised")
		self.setText("Power off")
		self.setShortcut(self.shortcut) # Refresh the shortcut
		self.state = True
		self.setEnabled(True)


	def _powerIsOff(self, result):
		# if not result:
		#     print("Time Sync: Got no response")
		#     return

		# PUT HERE SOME VERIFICATION OF THE POWER STATUS (WAIT FOR THE DATA PROTOCOL TO BE UPDATED)

		print("Power off")
		self.setText("Power on")
		self.setShortcut(self.shortcut) # Refresh the shortcut
		self.state = False
		self.setEnabled(True)


class RadioEquipment(QtWidgets.QWidget):
	def __init__(self, tc, parent=None): 
		super(RadioEquipment, self).__init__(parent=parent)
		self.tc = tc

		tooltipFVP = "Enable FVP"
		tooltipTM =  "Enable TM"

		self.state = [False, False]
		# [is_fpv_en, is_tm_en]

		layout = QtWidgets.QGridLayout()
		layout.setContentsMargins(0,0,0,0)

		self.title = QtWidgets.QLabel("Radio Equipment")
		# Alignment / Font size of the title
		self.title.setAlignment(Qt.AlignHCenter | Qt.AlignBottom)
		font = self.title.font()
		font.setPointSize(12)
		self.title.setFont(font)
		layout.addWidget(self.title, 0, 0, 1, 2)

		self.fpv = QtWidgets.QPushButton("Enable fvp")
		self.fpv.clicked.connect(self._functionFVP)
		self.fpv.setToolTip(tooltipFVP) # Tool tip
		self.fpv.setEnabled(False)
		layout.addWidget(self.fpv, 1, 0, 1, 1)

		self.tm = QtWidgets.QPushButton("Enable tm")
		self.tm.clicked.connect(self._functionTM)
		self.tm.setToolTip(tooltipFVP) # Tool tip
		self.tm.setEnabled(False)
		layout.addWidget(self.tm, 1, 1, 1, 1)

		self.setLayout(layout)

	def _functionFVP(self):
		self.fpv.setEnabled(False)
		self.tc.set_radio_emitters(True, self.state[1]).then(self._updateFVP)

	def _updateFVP(self, result):
		# if not result:
		#     print("FVP: Got no response")
		#     return

		# PUT HERE SOME VERIFICATION OF THE FVP STATUS (WAIT FOR THE DATA PROTOCOL TO BE UPDATED)
		# DON'T FORGET TO ENABLE THE BUTTON

		self.state[0] = True
		print("FVP enabled")


	def _functionTM(self):
		self.tm.setEnabled(False)
		self.tc.set_radio_emitters(self.state[0], True).then(self._updateTM)

	def _updateTM(self, result):
		# if not result:
		#     print("TM: Got no response")
		#     return

		# PUT HERE SOME VERIFICATION OF THE TM STATUS (WAIT FOR THE DATA PROTOCOL TO BE UPDATED)
		# DON'T FORGET TO ENABLE THE BUTTON

		self.state[1] = True
		print("TM enabled")

	def setEnabled(self, b):
		self.fpv.setEnabled(b)
		self.tm.setEnabled(b)


class Parachute(QtWidgets.QWidget):
	def __init__(self, tc, parent=None): 
		super(Parachute, self).__init__(parent=parent)
		self.tc = tc

		tooltipArming = "Arming the parachutes"
		tooltipEn1 = "Enable parachute 1"
		tooltipEn2 = "Enable parachute 2"

		self.state = [False, False, False]
		# [is_parachute_armed, is_parachute1_en, is_parachute2_en]

		layout = QtWidgets.QGridLayout()
		layout.setContentsMargins(0,0,0,0)

		self.title = QtWidgets.QLabel("Parachute")
		# Alignment / Font size of the title
		self.title.setAlignment(Qt.AlignHCenter | Qt.AlignBottom)
		font = self.title.font()
		font.setPointSize(12)
		self.title.setFont(font)
		layout.addWidget(self.title, 0, 0, 1, 2)

		self.arming = QtWidgets.QPushButton("Arming")
		self.arming.clicked.connect(self._functionArming)
		self.arming.setToolTip(tooltipArming) # Tool tip
		self.arming.setEnabled(False)
		layout.addWidget(self.arming, 1, 0, 1, 2)

		self.en1 = QtWidgets.QPushButton("Enable 1")
		self.en1.clicked.connect(self._functionEn1)
		self.en1.setToolTip(tooltipEn1) # Tool tip
		self.en1.setEnabled(False)
		layout.addWidget(self.en1, 2, 0, 1, 1)

		self.en2 = QtWidgets.QPushButton("Enable 2")
		self.en2.clicked.connect(self._functionEn2)
		self.en2.setToolTip(tooltipEn2) # Tool tip
		self.en2.setEnabled(False)
		layout.addWidget(self.en2, 2, 1, 1, 1)

		self.setLayout(layout)

	def _functionArming(self):
		self.arming.setEnabled(False)
		self.tc.set_parachute(True, False, False).then(self._updateArming)

	def _updateArming(self, result):
		# if not result:
		#     print("Parachute arming: Got no response")
		#     return

		# PUT HERE SOME VERIFICATION OF THE PARACHUTE STATUS (WAIT FOR THE DATA PROTOCOL TO BE UPDATED)
		# DON'T FORGET TO ENABLE THE BUTTON

		self.state[0] = True
		print("Parachute armed")
		self.en1.setEnabled(True)
		self.en2.setEnabled(True)

	def _functionEn1(self):
		self.en1.setEnabled(False)
		self.tc.set_parachute(True, True, self.state[2]).then(self._updateEn1)

	def _updateEn1(self, result):
		# if not result:
		#     print("Parachute arming: Got no response")
		#     return

		# PUT HERE SOME VERIFICATION OF THE PARACHUTE STATUS (WAIT FOR THE DATA PROTOCOL TO BE UPDATED)
		# DON'T FORGET TO ENABLE THE BUTTON

		self.state[1] = True
		print("Parachute 1 enable")

	def _functionEn2(self):
		self.en2.setEnabled(False)
		self.tc.set_parachute(True, self.state[1], True).then(self._updateEn2)

	def _updateEn2(self, result):
		# if not result:
		#     print("Parachute arming: Got no response")
		#     return

		# PUT HERE SOME VERIFICATION OF THE PARACHUTE STATUS (WAIT FOR THE DATA PROTOCOL TO BE UPDATED)
		# DON'T FORGET TO ENABLE THE BUTTON

		self.state[2] = True
		print("Parachute 2 enable")

	def setEnabled(self, b):
		self.arming.setEnabled(b)
		self.en1.setEnabled(False)
		self.en2.setEnabled(False)


class Backup(QtWidgets.QWidget):
	def __init__(self, tc, parent=None): 
		super(Backup, self).__init__(parent=parent)
		self.tc = tc

		tooltipEnable = "Enable backup"
		tooltipDisable = "Disable backup"
		tooltipSave = "Save backup to ???"

		layout = QtWidgets.QVBoxLayout()
		layout.setContentsMargins(0,0,0,0)

		self.title = QtWidgets.QLabel("Backup")
		# Alignment / Font size of the title
		self.title.setAlignment(Qt.AlignHCenter | Qt.AlignBottom)
		font = self.title.font()
		font.setPointSize(12)
		self.title.setFont(font)
		layout.addWidget(self.title)

		layout1 = QtWidgets.QVBoxLayout()
		self.enable = QtWidgets.QPushButton("Enable")
		self.enable.clicked.connect(self._functionEnable)
		self.enable.setToolTip(tooltipEnable) # Tool tip
		self.enable.setEnabled(False)
		layout1.addWidget(self.enable)

		self.disable = QtWidgets.QPushButton("Disable")
		self.disable.clicked.connect(self._functionDisable)
		self.disable.setToolTip(tooltipDisable) # Tool tip
		self.disable.setEnabled(False)
		layout1.addWidget(self.disable)

		layout2 = QtWidgets.QHBoxLayout()
		layout2.addLayout(layout1)
		self.save = QtWidgets.QPushButton("Save")
		self.save.clicked.connect(self._functionSave)
		self.save.setToolTip(tooltipSave) # Tool tip
		self.save.setEnabled(False)
		layout2.addWidget(self.save)

		layout.addLayout(layout2)
		self.setLayout(layout)

	def _functionEnable(self):
		self.enable.setEnabled(False)
		self.disable.setEnabled(False)
		# something.then(
		self._updateEnable(None)

	def _updateEnable(self, result):
		# if not result:
		#     print("Enable backup: Got no response")
		#     return

		# PUT HERE SOME VERIFICATION OF THE STATUS (WAIT FOR THE DATA PROTOCOL TO BE UPDATED)

		print("Backup enable")
		self.enable.setEnabled(True)
		self.disable.setEnabled(True)

	def _functionDisable(self):
		self.enable.setEnabled(False)
		self.disable.setEnabled(False)
		# something.then(
		self._updateDisable(None)

	def _updateDisable(self, result):
		# if not result:
		#     print("Disable backup: Got no response")
		#     return

		# PUT HERE SOME VERIFICATION OF THE STATUS (WAIT FOR THE DATA PROTOCOL TO BE UPDATED)

		print("Backup disable")
		self.enable.setEnabled(True)
		self.disable.setEnabled(True)

	def _functionSave(self):
		self.save.setEnabled(False)
		# something.then(
		self._updateSave(None)


	def _updateSave(self, result):
		# if not result:
		#     print("Saving backup: Got no response")
		#     return

		# PUT HERE SOME VERIFICATION OF THE STATUS (WAIT FOR THE DATA PROTOCOL TO BE UPDATED)

		print("Backup saved")
		self.save.setEnabled(True)


	def setEnabled(self, b):
		self.enable.setEnabled(b)
		self.disable.setEnabled(b)
		self.save.setEnabled(b)


class FlightController(QtWidgets.QWidget):

	def __init__(self, tc, parent=None):
		super(FlightController, self).__init__(parent=parent)

		title = TitleWidget("Flight Controller")
		radioEquipment = RadioEquipment(tc)
		parachute = Parachute(tc)
		self.backup = Backup(tc)
		power = PowerMode(tc, radioEquipment, parachute, self.backup)


		title.setMinimumSize(250, 0)
		
		layout = QtWidgets.QVBoxLayout()
		layout.setContentsMargins(5,5,5,5)
		layout.setSpacing(10)
		widgets = [title, power, radioEquipment, parachute]
		
		for w in widgets:
			layout.addWidget(w)

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


class TimeSyncStatus(QtWidgets.QLabel):
	"""TimeSyncStatus"""
	def __init__(self, tc, timer, parent=None):
		super(TimeSyncStatus, self).__init__("Unsynchronized time", parent)

		# Alignment / Font size
		font = self.font()
		font.setPointSize(10)
		self.setFont(font)

		self.tc = tc
		self.timer = timer
		timer.timeout.connect(self._update)


	def _update(self):
		pass


class PowerModeStatus(ValueIndicator):
	def __init__(self, tc, timer, parent=None):
		super(PowerModeStatus, self).__init__("Power", timer, self._updateFunction, sizeTitle=10, sizeData=11)
		self.tc = tc

	def _updateFunction(self):
		return "Off"


class RadioEquipmentStatus(QtWidgets.QWidget):
	def __init__(self, tc, timer, parent=None):
		super(RadioEquipmentStatus, self).__init__(parent=parent)
		self.tc = tc

		fpv = ValueIndicator("FPV enable:", timer, self._updateFPV)
		tm = ValueIndicator("TM enable:", timer, self._updateTM)

		# fpv.title.setFixedHeight(12)
		# fpv.indic.setFixedHeight(12)
		# tm.title.setFixedHeight(12)
		# tm.indic.setFixedHeight(12)

		# soft.setAutoFillBackground(False)
		# hard.setAutoFillBackground(False)

		layout = QtWidgets.QVBoxLayout()
		layout.setContentsMargins(0,0,0,0)
		layout.setSpacing(0)
		layout.addWidget(fpv)
		layout.addWidget(tm)
		self.setLayout(layout)

	def _updateFPV(self):
		return "No"


	def _updateTM(self):
		return "No"


class ParachuteStatus(QtWidgets.QWidget):
	def __init__(self, tc, timer, parent=None):
		super(ParachuteStatus, self).__init__(parent=parent)
		self.tc = tc

		armed = ValueIndicator("Parachute armed:", timer, self._updateArmed)
		en1 = ValueIndicator("Parachute 1", timer, self._updateEn1)
		en2 = ValueIndicator("Parachute 2", timer, self._updateEn2)

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
		layout.addWidget(armed)
		layout.addWidget(en1)
		layout.addWidget(en2)
		self.setLayout(layout)

	def _updateArmed(self):
		return "No"


	def _updateEn1(self):
		return "Disable"


	def _updateEn2(self):
		return "Disable"


class FlightStatus(QtWidgets.QWidget):
	def __init__(self, tc, timer, parent=None):
		super(FlightStatus, self).__init__(parent=parent)

		self.setMinimumSize(230, 0)

		# title = TitleWidget("Flight Status")
		wareStatus = WareStatus(tc, timer)
		timeSyncStatus = TimeSyncStatus(tc, timer)
		powerModeStatus = PowerModeStatus(tc, timer)
		radioEquipmentStatus = RadioEquipmentStatus(tc, timer)
		parachuteStatus = ParachuteStatus(tc, timer)

		layout = QtWidgets.QVBoxLayout()
		layout.setContentsMargins(0,5,10,0)
		layout.setSpacing(10)
		widgets = [wareStatus, timeSyncStatus, powerModeStatus, radioEquipmentStatus, parachuteStatus]
		
		for w in widgets:
			layout.addWidget(w)

		self.setLayout(layout)


class BatteryStatus(QtWidgets.QWidget):
	def __init__(self, tc, timer, parent=None):
		super(BatteryStatus, self).__init__(parent=parent)
		self.tc = tc

		bat1 = ValueIndicator("Battery 1:", timer, self._updateBat1)
		bat2 = ValueIndicator("Battery 2:", timer, self._updateBat2)

		# fpv.title.setFixedHeight(12)
		# fpv.indic.setFixedHeight(12)
		# tm.title.setFixedHeight(12)
		# tm.indic.setFixedHeight(12)

		# soft.setAutoFillBackground(False)
		# hard.setAutoFillBackground(False)

		layout = QtWidgets.QVBoxLayout()
		layout.setContentsMargins(0,0,0,0)
		layout.setSpacing(0)
		layout.addWidget(bat1)
		layout.addWidget(bat2)
		self.setLayout(layout)


	def _updateBat1(self):
		return "{:>5.2f} V".format(3.141592653589793)


	def _updateBat2(self):
		return "{:>5.2f} V".format(2.718281828459045)


class GNSSStatus(QtWidgets.QWidget):
	def __init__(self, tc, timer, parent=None):
		super(GNSSStatus, self).__init__(parent=parent)
		self.tc = tc

		time = ValueIndicator("GNSS time:", timer, self._updateTime)
		lat = ValueIndicator("Latitude:", timer, self._updateLat)
		lon = ValueIndicator("Longitude:", timer, self._updateLon)
		hdop = ValueIndicator("Horizontal dilution\nof precision:", timer, self._updateHDOP)

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
		layout.addWidget(time)
		layout.addWidget(lat)
		layout.addWidget(lon)
		layout.addWidget(hdop)
		self.setLayout(layout)

	def _updateTime(self):
		return "-"

	def _updateLat(self):
		return "-"

	def _updateLon(self):
		return "-"

	def _updateHDOP(self):
		return "-"


class FlightStatus2(QtWidgets.QWidget):
	def __init__(self, tc, timer, parent=None):
		super(FlightStatus2, self).__init__(parent=parent)

		self.setMinimumSize(230, 0)

		# title = TitleWidget("Flight Status")
		batteryStatus = BatteryStatus(tc, timer)
		gnssStatus = GNSSStatus(tc, timer)

		layout = QtWidgets.QVBoxLayout()
		layout.setContentsMargins(0,0,10,0)
		layout.setSpacing(10)
		widgets = [batteryStatus, gnssStatus]
		
		for w in widgets:
			layout.addWidget(w)

		self.setLayout(layout)


class SerialStatus(QtWidgets.QLabel):
	"""SerialStatus"""
	def __init__(self, tc, timer, parent=None):
		super(SerialStatus, self).__init__("Serial close", parent)

		# Alignment / Font size
		font = self.font()
		font.setPointSize(10)
		self.setFont(font)

		self.tc = tc
		self.timer = timer
		timer.timeout.connect(self._update)


	def _update(self):
		pass


class BackupStatus(ValueIndicator):
	def __init__(self, tc, timer, parent=None):
		super(BackupStatus, self).__init__("Backup enabled:", timer, self._updateFunction, sizeTitle=10, sizeData=11)
		self.tc = tc

	def _updateFunction(self):
		return "No"


class DebugStatus(QtWidgets.QWidget):
	def __init__(self, tc, timer, flightController, parent=None):
		super(DebugStatus, self).__init__(parent=parent)

		self.setMinimumSize(230, 0)

		backupStatus = BackupStatus(tc, timer)
		serialStatus = SerialStatus(tc, timer)
		time = ValueIndicator("Time since\nlast message:", timer, self._updateTime, sizeData=10)
		
		layout = QtWidgets.QVBoxLayout()
		layout.setContentsMargins(0,0,10,5)

		layout1 = QtWidgets.QVBoxLayout()
		layout1.setAlignment(Qt.AlignBottom)
		widgets = [backupStatus, serialStatus, time]
		
		for w in widgets:
			layout1.addWidget(w)

		layout.addWidget(flightController.backup)
		layout.addLayout(layout1)

		self.setLayout(layout)

	def _updateTime(self):
		return "{:>5.3f} s".format(1.23456)


# Main window
class MainWindow(QtWidgets.QMainWindow):

	def __init__(self, tc, *args, **kwargs):
		super(MainWindow, self).__init__(*args, **kwargs)
		self.setWindowTitle("Æsir - Flight Control Dashboard")

		QtCore.QCoreApplication.setQuitLockEnabled(True)
		# Set the central widget of the Window. Widget will expand
		# to take up all the space in the window by default.
		self.setCentralWidget(FlightController(tc, self))