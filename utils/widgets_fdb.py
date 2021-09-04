import os, random
from math import ceil, pi, cos, sin, sqrt
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5 import QtPositioning, QtQuickWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette, QColor
from utils.widgets_edb import MenuButton, InfoDialog, DataWidget, GraphWidget, TitleWidget
from .save import save_data_to_file_json, load_json, save_data_to_file_csv, load_csv
from utils.simulation import Simulator
import pyqtgraph as pg


INTERVAL = 60 # delay in ms - increase it if the dashboard is freezing, decrease to speed up the update rate

AUTO_MODE = True # Will be use in the futur (maybe)

# + Altitude
# + Air Speed
# + Acceleration
# ~ Bousole
# + GNSS position (map)
# ~ GNSS position (coordinates)
# + Inside (static) Temperature
# + External pressure
# + Inside (static) Pressure
# Onboard Battery Voltage


class ValueIndicator(QtWidgets.QWidget):
	"""ValueIndicator for the flight dashboard"""
	def __init__(self, text, timer, updateFunction, sizeTitle=10, sizeData=17, formatting="{}", parent=None):
		super(ValueIndicator, self).__init__(parent)

		# Background color
		# self.setAutoFillBackground(True)
		# palette = self.palette()
		# palette.setColor(QPalette.Window, QColor("white"))
		# self.setPalette(palette)

		# Size policy
		sizePolicy = self.sizePolicy()
		sizePolicy.setVerticalPolicy(QtWidgets.QSizePolicy.Fixed)
		self.setSizePolicy(sizePolicy)

		# Layout
		layout = QtWidgets.QVBoxLayout()
		layout.setAlignment(Qt.AlignHCenter)
		layout.setContentsMargins(0, 0, 0, 0)
		layout.setSpacing(0)
		# Title
		self.title = QtWidgets.QLabel(text)
		self.title.setAlignment(Qt.AlignCenter)
		font = self.title.font()
		font.setPointSize(sizeTitle)
		self.title.setFont(font)

		# Indicator
		self.indic = DataWidget("-", timer, updateFunction, sizeData, formatting=formatting)
		self.indic.setAlignment(Qt.AlignCenter)

		layout.addWidget(self.title)
		layout.addWidget(self.indic)

		self.setLayout(layout)


class PathManager(QtCore.QObject):
	pathChanged = QtCore.pyqtSignal(list)

	def __init__(self, parent=None):
		super(PathManager, self).__init__(parent)
		self._width = 100
		self._height = 100
		self._path = [QtPositioning.QGeoCoordinate(67.85, 20.24), QtPositioning.QGeoCoordinate(68, 20)]

	@QtCore.pyqtProperty(list, notify=pathChanged)
	def path(self):
		return self._path

	@path.setter
	def path(self, p):
		if self._path != p:
			self._path = p
			self.pathChanged.emit(self._path)

	def addCoordinate(self, lat, lon):
		self._path.append(QtPositioning.QGeoCoordinate(lat, lon))
		self.pathChanged.emit(self._path)


class MapWidget(QtQuickWidgets.QQuickWidget):
	def __init__(self, timer, parent=None):
		super(MapWidget, self).__init__(parent,
			resizeMode=QtQuickWidgets.QQuickWidget.SizeRootObjectToView)

		# Antialiasing
		form = QtGui.QSurfaceFormat()
		form.setSamples(8)
		self.setFormat(form)


		self.manager = PathManager()
		self.rootContext().setContextProperty("p_manager", self.manager)

		# Load QML
		current_path = os.path.abspath(os.path.dirname(__file__))
		qml_file = os.path.join(current_path, "Map.qml")
		self.setSource(QtCore.QUrl.fromLocalFile(qml_file))

		# Errors
		if self.status() == QtQuickWidgets.QQuickWidget.Error:
			for err in self.errors():
				print(err.toString())
			sys.exit(-1)

		timer.timeout.connect(self.update)
		# self.timer = QtCore.QTimer(interval=500, parent=self)
		# self.timer.timeout.connect(self.update)
		# self.timer.start()

		QtCore.QCoreApplication.setQuitLockEnabled(True)

	# def closeEvent(self, event):
	# 	self.timer.stop()
	# 	self.timer.deleteLater()
	# 	event.accept()

	def update(self):
		if self.isVisible():

			x = 67.85 + random.randint(-20, 20)/100
			y = 20.24 + random.randint(-40, 40)/100

			# Two different method to plot a path

			# self.manager.addCoordinate(x, y)

			path = [QtPositioning.QGeoCoordinate(67.85 , 20.24), QtPositioning.QGeoCoordinate(x, y)]
			self.manager.path = path

			# path = self.manager.path.copy()
			# path.append(QtPositioning.QGeoCoordinate(x, y))
			# self.manager.path = path


class Compass(QtWidgets.QWidget):
	def __init__(self, timer, parent=None):
		super().__init__(parent)
		self.diameter = 200
		thickness = 7

		self.thickness = ceil(thickness/2)
		self.center = self.thickness + self.diameter/2
		self.setFixedSize(self.diameter + 2*self.thickness, self.diameter + 2*self.thickness)

		self.theta = 0
		self.ratio = 0
		timer.timeout.connect(self.update_direction)

	def paintEvent(self, event):
		theta = self.theta * pi / 180

		painter = QtGui.QPainter(self)
		painter.setRenderHint(painter.Antialiasing)
		# painter.setBrush(QtGui.QBrush(Qt.black, Qt.SolidPattern))
		painter.setPen(QtGui.QPen(Qt.black, self.thickness))
		painter.drawEllipse(self.thickness, self.thickness, self.diameter, self.diameter)
		lenght = self.diameter * (0.2 + 0.8 * self.ratio)
		x = self.center + lenght * cos(theta) / 2
		y = self.center - lenght * sin(theta) / 2
		painter.setPen(QtGui.QPen(Qt.red, self.thickness))
		painter.drawLine(self.center, self.center, x, y)

		x -= self.thickness * cos(theta)
		y += self.thickness * sin(theta)
		painter.setPen(QtGui.QPen(Qt.black, self.thickness))
		painter.drawLine(self.center, self.center, x, y)

	def update_direction(self):
		self.theta += 1
		self.ratio = (self.ratio + 0.01) % 1
		self.update()


class GNSSIndicator(QtWidgets.QWidget):
	def __init__(self, timer):
		sizeTitle=10
		sizeData=17

		super().__init__()

		# Size policy
		sizePolicy = self.sizePolicy()
		sizePolicy.setVerticalPolicy(QtWidgets.QSizePolicy.Fixed)
		self.setSizePolicy(sizePolicy)

		# Title
		self.title = QtWidgets.QLabel("GNSS")
		self.title.setAlignment(Qt.AlignCenter)
		font = self.title.font()
		font.setPointSize(sizeTitle)
		self.title.setFont(font)
		# Data
		self.lat = DataWidget("-", timer, self.update_lat, sizeData, formatting="{}")
		self.lon = DataWidget("-", timer, self.update_lon, sizeData, formatting="{}")
		# Layout
		layout = QtWidgets.QGridLayout()
		layout.setContentsMargins(0, 0, 0, 0)
		layout.setSpacing(0)
		layout.addWidget(self.title, 0, 0, 1, 2)
		layout.addWidget(self.lon, 1, 0)
		layout.addWidget(self.lat, 1, 1)

		self.setLayout(layout)


	def update_lat(self):
		return "-"

	def update_lon(self):
		return "-"


class ExpandionMargin(QtWidgets.QWidget):
	"""A simple class to create an expanding marge"""
	def __init__(self):
		super().__init__()
		# Size policy
		sizePolicy = self.sizePolicy()
		sizePolicy.setVerticalPolicy(QtWidgets.QSizePolicy.Expanding)
		# sizePolicy.setHorizontalPolicy(QtWidgets.QSizePolicy.Expanding)
		self.setSizePolicy(sizePolicy)


class GraphWidgetFDB(pg.PlotWidget):
	"""A GraphWidget used for the Flight Dashboard"""
	def __init__(self, timer, updateFunction, ylabel):
		super().__init__()
		self.setAttribute(Qt.WA_DeleteOnClose, True)
		self.setMinimumWidth(260)

		self.setBackground('w')
		self.setMouseEnabled(x=not AUTO_MODE, y=False)
		# self.getPlotItem().getViewBox().setBorder(width=4.5, color='r')
		# self.getAxis("left").setWidth(52)
		self.getPlotItem().hideButtons()

		self.setLabel("bottom", "Time (s)")
		self.setLabel("left", ylabel)


		self.updateFunction = updateFunction
		self.lenx, self.leny = 0, 0
		self.line = self.plot([], [])
		timer.timeout.connect(self.updatePlot)

	def updatePlot(self):
		x, y = self.updateFunction()
		if self.lenx != len(x) or self.leny != len(y):
			self.lenx, self.leny = len(x), len(y)
			# y = y.copy()
			# for k in range(len(y)):
			# 	y[k] *= 1000
			self.line.setData(x, y)


class GraphWithTitle(QtWidgets.QWidget):
	def __init__(self, title, timer, tm, updateField=[], dataNames=None, displayXLabel=True, parent=None):
		super().__init__()

		device = updateField[0]
		datatype = updateField[1]
		field = updateField[2]
		updateFunction = tm.data[device][datatype][field].pack

		layout = QtWidgets.QVBoxLayout()
		layout.setContentsMargins(0, 0, 0, 0)
		layout.setSpacing(0)
		title = TitleWidget(title)
		# graph = GraphWidget(timer, tm, updateFields=updateFields, dataNames=dataNames, displayXLabel=displayXLabel)
		graph = GraphWidgetFDB(timer, updateFunction, "Altitude (m)")
		layout.addWidget(title)
		layout.addWidget(graph)
		self.setLayout(layout)


class GraphAirSpeed(QtWidgets.QWidget):

	max_iter = 100
	min_super_mach = 1 # Minimum mach number of supersonic speed
	max_super_mach = 5 # Maximum mach number of supersonic speed
	epsilon = 1e-6 # Table precision
	gamma = 1.4 # Heat capacity ratio

	def __init__(self, timer, tm, parent=None):
		super().__init__()
		self.airSpeedList = []
		self.tm = tm

		layout = QtWidgets.QVBoxLayout()
		layout.setContentsMargins(0, 0, 0, 0)
		layout.setSpacing(0)
		title = TitleWidget("Mach number")
		# graph = GraphWidget(timer, tm, updateFields=updateFields, dataNames=dataNames, displayXLabel=displayXLabel)
		graph = GraphWidgetFDB(timer, lambda:self.updateAirSpeed(), "Air Speed (m/s)")
		layout.addWidget(title)
		layout.addWidget(graph)
		self.setLayout(layout)

	def updateAirSpeed(self):
		x, pressure = self.tm.data["test"]["gyro"]["x"].pack()

		#
		# TODO: Compute the pressure ratio
		#

		if len(self.airSpeedList) != len(pressure):
			for k in range(len(self.airSpeedList), len(pressure)):
				self.airSpeedList.append(self.ratio_to_M(pressure[k]+1))
		return x, self.airSpeedList

	def ratio_to_M(self, ratio):
		"""Pressure ration to Mach number"""
		M = self.subsonic(ratio)
		if M > 1:
			M = self.dicho(self.rayleigh, ratio, self.min_super_mach, self.max_super_mach, self.epsilon)
		return M


	def dicho(self, f, target, xmin, xmax, epsilon):
		x = (xmin + xmax) / 2
		y = f(x)
		nb_iter = 0
		while abs(y - target) > epsilon:
			if y < target:
				xmin = x
			else:
				xmax = x
			x = (xmin + xmax) / 2
			y = f(x)
			nb_iter += 1
			if nb_iter >= self.max_iter:
				print("Air Speed calculation: Maximum iteration reached (pressure ratio = {})".format(target))
				break
		return x

	def subsonic(self, ratio):
		M = sqrt(2/(self.gamma-1) * (ratio ** ((self.gamma-1)/self.gamma) - 1))
		return M

	def rayleigh(self, M):
		gamma = self.gamma
		ratio = (gamma + 1)**2 * M**2 / (4*gamma*M**2 - 2 * (gamma - 1))
		ratio **= gamma/(gamma-1)
		ratio *= (1-gamma + 2*gamma*M**2) / (gamma+1)
		return ratio


class MainMenu(QtWidgets.QWidget):
	def __init__(self, parent=None):
		super().__init__(parent)
		self.setAcceptDrops(True) # So one can drop a file to open it

		# Background color
		self.setAutoFillBackground(True)
		palette = self.palette()
		palette.setColor(QPalette.Window, QColor(0, 0, 0, 128))
		self.setPalette(palette)

		self.serial_button = MenuButton("Open Serial", self.parent()._open_serial)

		self.file_button = MenuButton("Open File", self.parent()._open_file)

		self.simu_button = MenuButton("Launch Simulation", self.parent()._open_simu)

		layout = QtWidgets.QVBoxLayout()
		layout.addWidget(self.serial_button)
		layout.addWidget(self.file_button)
		layout.addWidget(self.simu_button)

		layout.setSpacing(20)

		wid = QtWidgets.QWidget()
		wid.setLayout(layout)
		wid.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)

		layout = QtWidgets.QVBoxLayout()
		layout.addWidget(wid)
		layout.setAlignment(Qt.AlignCenter)

		self.setLayout(layout)

	def dragEnterEvent(self, event):
		# No file verification here
		# I assume the user know what he's doing...
		if event.mimeData().hasUrls():
			event.acceptProposedAction()

	def dropEvent(self, event):
		# print(event.mimeData().urls())
		fname = event.mimeData().urls()[0].toLocalFile()
		self.parent()._load_file(fname)


class MenuBar(QtWidgets.QMenuBar):
	def __init__(self, parent=None):
		super().__init__(parent=parent)

		# File
		self.fileMenu = QtWidgets.QMenu("&File", self)

		self.openSerial = QtWidgets.QAction("Open &serial")
		self.openSerial.triggered.connect(self.parent()._open_serial)

		self.openFile = QtWidgets.QAction("Open &file")
		self.openFile.triggered.connect(self.parent()._open_file)

		self.lauchSimulation = QtWidgets.QAction("&Launch simulation")
		self.lauchSimulation.triggered.connect(self.parent()._open_simu)

		self.showMap = QtWidgets.QAction("Show/hide &map")
		self.showMap.triggered.connect(self.parent()._show_map)

		self.exit = QtWidgets.QAction("&Exit")
		self.exit.triggered.connect(self.parent().close)

		self.fileMenu.addAction(self.openSerial)
		self.fileMenu.addAction(self.openFile)
		self.fileMenu.addAction(self.lauchSimulation)
		self.fileMenu.addAction(self.showMap)
		self.fileMenu.addAction(self.exit)
		self.addMenu(self.fileMenu)

		# Help
		self.helpMenu = QtWidgets.QMenu("&Help", self)

		self.aboutFDB = QtWidgets.QAction("About &Flight Dashboard")
		self.aboutFDB.triggered.connect(self._aboutFDB)

		self.aboutAesir = QtWidgets.QAction("&About Æsir")
		self.aboutAesir.triggered.connect(self._aboutAesir)

		self.helpMenu.addAction(self.aboutFDB)
		self.helpMenu.addAction(self.aboutAesir)
		self.addMenu(self.helpMenu)

	def _aboutFDB(self):
		title = "Engine Dashboard"
		text = """This dashboard was developed in 2021 in the context of Project Mjollnir. The purpose is to monitor the state of the rocket during the flight.<br /><br />Project Mjollnir is the third project of the Æsir association. The objective is to reach an altitude of 10 km with a sounding rocket made by students."""
		InfoDialog(title, text).exec_()

	def _aboutAesir(self):
		title = "Æsir"
		text = """ÆSIR is a student rocketry association founded in 2016 at KTH Royal Institute of Technology in Stockholm. It has around 40 members every year, which are all students at KTH. Roughly half of the members are international students and they cover many disciplines and levels of study, although most of ÆSIR's members study Aerospace Engineering, Computer Science, Vehicle Engineering, Electrical Engineering, Engineering Physics and Mechanical Engineering.<br /><br /><a href=\"http://aesir.se\">ÆSIR website</a>"""
		image = 'gui/logo/256x256.png'
		InfoDialog(title, text, image).exec_()


# Main window
class MainWindow(QtWidgets.QMainWindow):
	def __init__(self, tm, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.setAttribute(Qt.WA_DeleteOnClose, True)

		self.setWindowTitle("Æsir - Flight dashboard")

		self.tm = tm
		self.timer = QtCore.QTimer(self)
		self.timer.setInterval(INTERVAL)

		# Background color
		self.setAutoFillBackground(True)
		palette = self.palette()
		palette.setColor(QPalette.Window, QColor("white"))
		self.setPalette(palette)

		# Altitude
		self.altitude = ValueIndicator("Altitude", self.timer, lambda:"-")

		# Air speed
		self.speed = ValueIndicator("Air speed", self.timer, lambda:"-")

		# Acceleration
		self.acceleration = ValueIndicator("Acceleration", self.timer, lambda:"-")

		# GNSS
		self.position = GNSSIndicator(self.timer) # TODO : Change the function's input

		# Inside/Static Temperature
		self.temperature = ValueIndicator("Static Temperature", self.timer, lambda:"-")

		# External pressure
		self.ex_pressure = ValueIndicator("External Pressure", self.timer, lambda:"-")

		# Inside/Static pressure
		self.in_pressure = ValueIndicator("Static Pressure", self.timer, lambda:"-")


		# Compass
		# self.compass = Compass(self.timer)

		centralWidget = QtWidgets.QWidget()
		layoutC = QtWidgets.QVBoxLayout()
		layoutC.addWidget(GraphWithTitle("Altitude", self.timer, self.tm, ["test", "gyro", "x"]))
		# layoutC.addWidget(GraphWithTitle("Air speed", self.timer, self.tm, ["test", "gyro", "x"]))
		layoutC.addWidget(GraphAirSpeed(self.timer, self.tm))
		layoutC.setContentsMargins(0, 0, 0, 0)
		centralWidget.setLayout(layoutC)

		layout = QtWidgets.QGridLayout()
		layout.addWidget(centralWidget, 1, 0, 9, 3)
		layout.addWidget(self.altitude, 0, 0)
		layout.addWidget(self.speed, 0, 1)
		layout.addWidget(self.acceleration, 0, 2)

		layout.addWidget(self.temperature, 1, 3)
		layout.addWidget(self.ex_pressure, 3, 3)
		layout.addWidget(self.in_pressure, 5, 3)

		layout.addWidget(self.position, 7, 3)
		layout.addWidget(Compass(self.timer), 9, 3)

		layout.addWidget(ExpandionMargin(), 2, 3)
		layout.addWidget(ExpandionMargin(), 4, 3)
		layout.addWidget(ExpandionMargin(), 6, 3)
		layout.addWidget(ExpandionMargin(), 8, 3)

		layout.setContentsMargins(0, 0, 0, 0)
		layout.setSpacing(0)

		# Set the central widget of the Window. Widget will expand
		# to take up all the space in the window by default.
		self.widget = QtWidgets.QWidget(self)
		self.widget.setLayout(layout)
		self.setCentralWidget(self.widget)

		# Main menu
		self.menu = MainMenu(parent=self)
		# self.timer.start()

		# Menu bar
		self.menuBar = MenuBar(parent=self)
		self.setMenuBar(self.menuBar)

		# Map window
		self.mappy = None
		self._show_map()

		# Simulator
		self.simulator = None

		# Allow the application to end when the window is closed
		QtCore.QCoreApplication.setQuitLockEnabled(True)

	def closeEvent(self, event):
		# properly stop all threads
		self.mappy.close()
		self.tm.stop()
		if self.simulator is not None:
			self.simulator.stop()
		event.accept()

	def resizeEvent(self, event):
		self.menu.setFixedSize(self.size())

	def _open_serial(self):
		if self.tm.open_serial():
			self.menu.hide()
			self.timer.start()
		else:
			print("Error while opening serial")

	def _open_file(self):
		fname = QtWidgets.QFileDialog.getOpenFileName(self, "Open file")[0]
		if fname == "":
			return
		self._load_file(fname)

	def _load_file(self, fname):
		print("Loading:", fname)
		_, ext = os.path.splitext(fname)
		if ext == "":
			self.tm.open_flash_file(fname)
			# self.tm.open_flash_file("data/test")
			self.menu.hide()
			self.timer.start()
		elif ext == ".json":
			load_json(self.tm, fname)
			self.menu.hide()
			self.timer.start()
		elif ext == ".csv":
			#Load csv
			print("Cannot load csv files yet")
		else:
			print("Cannot load this file")

	def _save_to_json(self):
		now = datetime.now()
		date = now.strftime("%Y-%m-%d-%H-%M-%S")
		fname = self.tm.device + "-" + date + ".json"
		path = save_data_to_file_json(self.tm.data, fname)
		print('Save as "{}"'.format(path))

	def _save_to_csv(self):
		now = datetime.now()
		date = now.strftime("%Y-%m-%d-%H-%M-%S")
		fname = self.tm.device + "-" + date + ".csv"
		path = save_data_to_file_csv(self.tm.data, fname)
		print('Save as "{}"'.format(path))

	def _open_simu(self):
		self.simulator = Simulator(self.tm)
		self.simulator.launch()
		self.menu.hide()
		self.timer.start()


	def _show_map(self):
		if self.mappy is None or not self.mappy.isVisible():
			self.mappy = MapWidget(self.timer)
			self.mappy.setWindowTitle("Æsir - Flight dashboard - Map")
			self.mappy.show()
		else:
			self.mappy.close()
			self.mappy = None
