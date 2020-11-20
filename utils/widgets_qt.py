from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import Qt
import pyqtgraph as pg
from PyQt5.QtGui import QPalette, QColor
from time import time
from random import randint
import threading


class TitleWidget(QtWidgets.QLabel):
    """Widget use to write columns' title"""
    def __init__(self, parent, text):
        super(TitleWidget, self).__init__(text, parent)

        # Alignment / Font size
        self.setAlignment(Qt.AlignCenter)
        font = self.font()
        font.setPointSize(20)
        self.setFont(font)

        self.setMinimumSize(160, 0)

        # Background color
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor("white"))
        self.setPalette(palette)
        

class GraphWidget(pg.PlotWidget):

    def __init__(self, parent, timer):
        super(GraphWidget, self).__init__(parent)
        self.setAttribute(Qt.WA_DeleteOnClose, True)

        self.x = list(range(100))  # 100 time points
        self.y = [randint(0,100) for _ in range(100)]  # 100 data points

        self.setBackground('w')
        self.setMouseEnabled(x=False, y=False)

        pen = pg.mkPen(color=(255, 0, 0))
        self.data_line =  self.plot(self.x, self.y, pen=pen)
        

        self.timer = timer
        self.timer.timeout.connect(self.update_plot_data)

    def update_plot_data(self):

        self.x = self.x[1:]  # Remove the first y element.
        self.x.append(self.x[-1] + 1)  # Add a new value 1 higher than the last.

        self.y = self.y[1:]  # Remove the first 
        self.y.append( randint(0,100))  # Add a new random value.

        self.data_line.setData(self.x, self.y)  # Update the data.


# Temperature
class TempOxidizerGraph(GraphWidget):

    def __init__(self, parent, timer):
        super().__init__(parent, timer)
        self.setYRange(-30, 30, padding=0)
        self.setTitle("Oxidizer tank + Passive vent line")


class TempPipeworkGraph(GraphWidget):

    def __init__(self, parent, timer):
        super().__init__(parent, timer)
        self.setYRange(-30, 30, padding=0)
        self.setTitle("Pipework")


class TempInjectorGraph(GraphWidget):

    def __init__(self, parent, timer):
        super().__init__(parent, timer)
        self.setYRange(-30, 500, padding=0)
        self.setTitle("Injector")


class TempCombustionGraph(GraphWidget):

    def __init__(self, parent, timer):
        super().__init__(parent, timer)
        self.setYRange(0, 200, padding=0)
        self.setTitle("Combustion chamber")


class TempNozzleGraph(GraphWidget):

    def __init__(self, parent, timer):
        super().__init__(parent, timer)
        self.setTitle("Nozzle")


# Pression
class PreOxidizerGraph(GraphWidget):

    def __init__(self, parent, timer):
        super().__init__(parent, timer)
        self.setYRange(0, 60, padding=0)
        self.setTitle("Oxidizer tank readings")


class PreInjectorGraph(GraphWidget):

    def __init__(self, parent, timer):
        super().__init__(parent, timer)
        self.setYRange(0, 60, padding=0)
        self.setTitle("Injector")


class PreCombustionGraph(GraphWidget):

    def __init__(self, parent, timer):
        super().__init__(parent, timer)
        self.setYRange(0, 40, padding=0)
        self.setTitle("Combustion chamber")


class PreAmbientGraph(GraphWidget):

    def __init__(self, parent, timer):
        super().__init__(parent, timer)
        self.setYRange(0, 1.5, padding=0)
        self.setTitle("Ambient pressure")


# Main window
class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setAttribute(Qt.WA_DeleteOnClose, True)

        self.setWindowTitle("Æsir - Engine dashboard")

        self.widgets = []
        self.timer = QtCore.QTimer(self)
        self.timer.setInterval(30)

        # Temperature
        # Left Column
        temperatureTitle = TitleWidget(self, "Temperature")
        tempOxidizer = TempOxidizerGraph(self, self.timer)
        tempPipework = TempPipeworkGraph(self, self.timer)
        tempInjector = TempInjectorGraph(self, self.timer)
        tempCombustion = TempCombustionGraph(self, self.timer)
        tempNozzle = TempNozzleGraph(self, self.timer)

        temperature = QtWidgets.QVBoxLayout()
        widgets = [temperatureTitle, tempOxidizer, tempPipework, tempInjector, tempCombustion, tempNozzle]
        
        for w in widgets:
            temperature.addWidget(w)
            self.widgets.append(w)

        # Pressure
        # Middle Column
        pressureTitle = TitleWidget(self, "Pressure")
        preOxidizer = PreOxidizerGraph(self, self.timer)
        preInjector = PreInjectorGraph(self, self.timer)
        preCombustion = PreCombustionGraph(self, self.timer)
        preAmbient = PreAmbientGraph(self, self.timer)

        pressure = QtWidgets.QVBoxLayout()
        widgets = [pressureTitle, preOxidizer, preInjector, preCombustion, preAmbient]
        
        for w in widgets:
            pressure.addWidget(w)
            self.widgets.append(w)

        # Layout 3
        # Right Column
        layout3 = QtWidgets.QVBoxLayout()

        wid1 = QtWidgets.QLabel("Electrical")
        wid1.setAlignment(Qt.AlignCenter)
        font = wid1.font()
        font.setPointSize(30)
        wid1.setFont(font)
        wid1.setMinimumSize(160, 0)
        wid1.setAutoFillBackground(True)
        palette = wid1.palette()
        palette.setColor(QPalette.Window, QColor("white"))
        wid1.setPalette(palette)


        wid2 = QtWidgets.QLabel("Status\nsignals")
        wid2.setAlignment(Qt.AlignCenter)
        font = wid2.font()
        font.setPointSize(30)
        wid2.setFont(font)
        wid2.setMinimumSize(160, 0)
        wid2.setAutoFillBackground(True)
        palette = wid2.palette()
        palette.setColor(QPalette.Window, QColor("white"))
        wid2.setPalette(palette)

        layout3.addWidget(wid1)
        layout3.addWidget(wid2)
        self.widgets.append(wid1)
        self.widgets.append(wid2)
        
            
        layout = QtWidgets.QHBoxLayout()
        layout.addLayout(temperature)
        layout.addLayout(pressure)
        layout.addLayout(layout3)

        widget = QtWidgets.QWidget(self)
        widget.setLayout(layout)
        
        self.timer.timeout.connect(lambda: self.print_fps(100))
        self.time = time()
        self.count_frame = 0
        self.timer.start()

        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(widget)

    def print_fps(self, interval):

        self.count_frame += 1

        if self.count_frame % interval == 0:
            t = time()
            print("FPS :", interval / (t - self.time))
            self.time = t
