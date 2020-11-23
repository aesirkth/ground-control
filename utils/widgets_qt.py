from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import Qt
import pyqtgraph as pg
from PyQt5.QtGui import QPalette, QColor
from time import time
from random import randint
import threading


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
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor("white"))
        self.setPalette(palette)

        self.setFixedHeight(35)
        

class GraphWidget(pg.PlotWidget):

    def __init__(self, parent, timer):
        super(GraphWidget, self).__init__(parent)
        self.setAttribute(Qt.WA_DeleteOnClose, True)
        self.setMinimumWidth(260)

        self.x = list(range(100))  # 100 time points
        self.y = [randint(0,100) for _ in range(100)]  # 100 data points

        self.setBackground('w')
        self.setMouseEnabled(x=False, y=False)

        pen = pg.mkPen(color=(255, 0, 0))
        self.data_line =  self.plot(self.x, self.y, pen=pen)
        
        timer.timeout.connect(self.update_plot_data)

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


# Electrical
class HorizontalTextWidget(QtWidgets.QLabel):
    """docstring for TextWidget"""
    def __init__(self, parent, text):
        super(HorizontalTextWidget, self).__init__(text, parent)
        self.setAlignment(Qt.AlignCenter)
        font = self.font()
        font.setPointSize(10)
        self.setFont(font)

        # Background color
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor("white"))
        self.setPalette(palette)

        # self.setContentsMargins(left, up, right, down)
        self.setContentsMargins(10, 0, 2, 0)
        self.setFixedHeight(18)


class VerticalTextWidget(QtWidgets.QLabel):
    """docstring for TextWidget"""
    def __init__(self, parent, text):
        super(VerticalTextWidget, self).__init__(text, parent)
        self.setAlignment(Qt.AlignCenter)
        font = self.font()
        font.setPointSize(10)
        self.setFont(font)

        # Background color
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor("white"))
        self.setPalette(palette)

        size = self.minimumSizeHint()
        self.setMinimumHeight(size.width()+10)
        self.setFixedWidth(size.height()+4)

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.translate(0, self.height()-5)
        painter.rotate(-90)
        painter.drawText(0, self.width()/2+2, self.text())
        painter.end()


    # def paintEvent(self, event):
    #     QtWidgets.QLabel.paintEvent(self, event)
    #     painter = QtGui.QPainter (self)
    #     painter.translate(0, self.height()-1)
    #     painter.rotate(-90)
    #     self.setGeometry(self.x(), self.y(), self.height(), self.width())
    #     QtWidgets.QLabel.render(self, painter)

    # def minimumSizeHint(self):
    #     size = QtWidgets.QLabel.minimumSizeHint(self)
    #     return QtCore.QSize(size.height(), size.width())

    # def sizeHint(self):
    #     size = QtWidgets.QLabel.sizeHint(self)
    #     return QtCore.QSize(size.height(), size.width())

    # def minimumSizeHint(self):
    #     size = QtWidgets.QLabel.minimumSizeHint(self)
    #     return QtCore.QSize(size.height(), size.width())

    # def sizeHint(self):
    #     size = QtWidgets.QLabel.sizeHint(self)
    #     return QtCore.QSize(size.height(), size.width())


class DataWidget(QtWidgets.QLabel):
    """docstring for DataWidget"""
    def __init__(self, text, timer, updateFunction, fontSize, parent=None):
        super(DataWidget, self).__init__(text, parent)
        self.setAlignment(Qt.AlignCenter)
        font = self.font()
        font.setPointSize(fontSize)
        self.setFont(font)

        self.updateFunction = updateFunction
        timer.timeout.connect(self.update_value)
    
    def update_value(self):
        self.setText(str(self.updateFunction()))


def random_value():
    return randint(0,200)

class Electrical(QtWidgets.QWidget):

    def __init__(self, timer, parent=None):
        super().__init__(parent)
        layout = QtWidgets.QVBoxLayout(self)
        layout.setContentsMargins(0,0,0,0)

        title = TitleWidget("Electrical")

        tab = QtWidgets.QGridLayout()
        tab.setSpacing(2)

        tab.addWidget(VerticalTextWidget(self, "Voltage"), 1, 0)
        tab.addWidget(VerticalTextWidget(self, "Current"), 2, 0)
        tab.addWidget(VerticalTextWidget(self, "Resistance"), 3, 0)

        tab.addWidget(HorizontalTextWidget(self, "Main valve solenoid"), 0, 1)
        tab.addWidget(HorizontalTextWidget(self, "Vent line solenoid"), 0, 2)
        tab.addWidget(HorizontalTextWidget(self, "Ignition system"), 0, 3)

        tab.addWidget(DataWidget(str(randint(0,100)), timer, random_value, 25), 1, 1)
        tab.addWidget(DataWidget(str(randint(0,100)), timer, random_value, 25), 1, 2)
        tab.addWidget(DataWidget(str(randint(0,100)), timer, random_value, 25), 1, 3)
        tab.addWidget(DataWidget(str(randint(0,100)), timer, random_value, 25), 2, 1)
        tab.addWidget(DataWidget(str(randint(0,100)), timer, random_value, 25), 2, 2)
        tab.addWidget(DataWidget(str(randint(0,100)), timer, random_value, 25), 2, 3)
        tab.addWidget(DataWidget(str(randint(0,100)), timer, random_value, 25), 3, 1)
        tab.addWidget(DataWidget(str(randint(0,100)), timer, random_value, 25), 3, 2)
        tab.addWidget(DataWidget(str(randint(0,100)), timer, random_value, 25), 3, 3)

        layout.addWidget(title)
        layout.addLayout(tab)
        self.setLayout(layout)


# Status signals
class ColoredCircle(QtWidgets.QWidget):
    """docstring for ColoredCircle"""
    def __init__(self, timer, parent=None):
        super(ColoredCircle, self).__init__(parent)
        self.status = False
        self.diameter = 30
        self.color = Qt.red

        self.setFixedSize(self.diameter, self.diameter)

        self.variable_for_demo = 0
        timer.timeout.connect(self.update_color)

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.setRenderHint(painter.Antialiasing)
        painter.setBrush(QtGui.QBrush(self.color, Qt.SolidPattern))
        painter.setPen(Qt.NoPen)
        painter.drawEllipse(0, 0, self.diameter, self.diameter)

    def update_color(self):
        self.variable_for_demo = (self.variable_for_demo + 1) % 100
        if self.variable_for_demo == 0:
            self.status = not self.status
            if self.status:
                self.color = Qt.green
            else:
                self.color = Qt.red
            self.update()


class BoolIndicator(QtWidgets.QWidget):
    """docstring for BoolIndicator"""
    def __init__(self, text, timer, parent=None):
        super(BoolIndicator, self).__init__(parent)

        # Background color
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor("white"))
        self.setPalette(palette)

        # Layout
        layout = QtWidgets.QHBoxLayout()
        layout.setAlignment(Qt.AlignVCenter)
        # Title
        title = QtWidgets.QLabel(text)
        title.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        font = title.font()
        font.setPointSize(15)
        title.setFont(font)

        # Indicator
        indic = ColoredCircle(timer)

        layout.addWidget(title)
        layout.addWidget(indic)

        self.setLayout(layout)
        

class ValueIndicator(QtWidgets.QWidget):
    """docstring for ValueIndicator"""
    def __init__(self, text, timer, updateFunction, sizeTitle=15, sizeData=17, parent=None):
        super(ValueIndicator, self).__init__(parent)

        # Background color
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor("white"))
        self.setPalette(palette)

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
        self.indic = DataWidget("-", timer, updateFunction, sizeData)
        self.indic.setAlignment(Qt.AlignRight | Qt.AlignVCenter)

        layout.addWidget(self.title)
        layout.addWidget(self.indic)

        self.setLayout(layout)


class Status(QtWidgets.QWidget):

    def __init__(self, timer, parent=None):
        super().__init__(parent)
        layout = QtWidgets.QVBoxLayout(self)
        layout.setContentsMargins(0,0,0,0)

        title = TitleWidget("Status signals")
        relief = BoolIndicator("Relief valve trigger", timer)
        valve = BoolIndicator("Abort valve trigger", timer)
        actuation = ValueIndicator("Main valve actuation", timer, random_value)

        layout.addWidget(title)
        layout.addWidget(relief)
        layout.addWidget(valve)
        layout.addWidget(actuation)

        self.setLayout(layout)


# Diagnostic readings
class BoardVoltageIndicator(QtWidgets.QWidget):
    """docstring for BoardVoltageIndicator"""
    def __init__(self, text, timer, parent=None):
        super(BoardVoltageIndicator, self).__init__(parent)

        # Background color
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor("white"))
        self.setPalette(palette)

        # Layout
        layout = QtWidgets.QHBoxLayout()
        layout.setAlignment(Qt.AlignVCenter)
        # Title
        title = QtWidgets.QLabel(text)
        title.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        font = title.font()
        font.setPointSize(15)
        title.setFont(font)

        # Indicators
        indicLayout = QtWidgets.QGridLayout()

        indicLayout.addWidget(DataWidget("0", timer, random_value, 14), 0, 0)
        indicLayout.addWidget(DataWidget("0", timer, random_value, 14), 1, 0)
        indicLayout.addWidget(DataWidget("0", timer, random_value, 14), 0, 1)
        indicLayout.addWidget(DataWidget("0", timer, random_value, 14), 1, 1)
        

        layout.addWidget(title)
        layout.addLayout(indicLayout)

        self.setMinimumWidth(265) # Évite le redimensionnement du widget

        self.setLayout(layout)


class RMCTemperatureIndicator(QtWidgets.QWidget):
    """docstring for RMCTemperatureIndicator"""
    def __init__(self, text, timer, parent=None):
        super(RMCTemperatureIndicator, self).__init__(parent)

        # Background color
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor("white"))
        self.setPalette(palette)

        # Layout
        layout = QtWidgets.QVBoxLayout()
        layout.setAlignment(Qt.AlignVCenter)
        # Title
        title = QtWidgets.QLabel(text)
        title.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        font = title.font()
        font.setPointSize(15)
        title.setFont(font)

        # Indicators
        indicLayout = QtWidgets.QGridLayout()

        indicLayout.addWidget(DataWidget("0", timer, random_value, 14), 0, 0)
        indicLayout.addWidget(DataWidget("0", timer, random_value, 14), 1, 0)
        indicLayout.addWidget(DataWidget("0", timer, random_value, 14), 0, 1)
        indicLayout.addWidget(DataWidget("0", timer, random_value, 14), 1, 1)
        indicLayout.addWidget(DataWidget("0", timer, random_value, 14), 0, 2)
        indicLayout.addWidget(DataWidget("0", timer, random_value, 14), 1, 2)
        indicLayout.addWidget(DataWidget("0", timer, random_value, 14), 0, 3)
        indicLayout.addWidget(DataWidget("0", timer, random_value, 14), 1, 3)
        

        layout.addWidget(title)
        layout.addLayout(indicLayout)

        self.setLayout(layout)


class ErrorGraph(GraphWidget):

    def __init__(self, timer, parent=None):
        super().__init__(parent, timer)
        self.setTitle("Error")
        # self.setMaximumWidth(300)


class FPSIndicator(ValueIndicator):
    """docstring for FPSIndicator"""
    def __init__(self, timer, parent=None):
        super(FPSIndicator, self).__init__("FPS :", timer, self.updateFPS,
            sizeTitle=10, sizeData=10,  parent=parent)
        self.count_frame = 0
        self.interval = 30
        self.time = time()
        self.fps = "-"
        self.setFixedHeight(28)

    def updateFPS(self):
        self.count_frame += 1
        self.count_frame %= self.interval

        if self.count_frame == 0:
            t = time()
            self.fps = int(self.interval / (t - self.time))
            self.time = t
        
        return self.fps 


class Diagnostic(QtWidgets.QWidget):

    def __init__(self, timer, parent=None):
        super().__init__(parent)
        self.setMaximumWidth(570)
        layout = QtWidgets.QVBoxLayout(self)
        layout.setContentsMargins(0,0,0,0)

        horiLayout = QtWidgets.QHBoxLayout(self)
        vertLayoutLeft = QtWidgets.QVBoxLayout(self)
        vertLayoutRight = QtWidgets.QVBoxLayout(self)

        title = TitleWidget("Diagnostic readings")
        boardVoltage = BoardVoltageIndicator("Board input voltage", timer)
        error = ErrorGraph(timer)
        rmc = RMCTemperatureIndicator("R&MC Temperature", timer)
        fps = FPSIndicator(timer)

        layout.addWidget(title)
        vertLayoutLeft.addWidget(boardVoltage)
        vertLayoutLeft.addWidget(error)
        vertLayoutRight.addWidget(rmc)
        vertLayoutRight.addWidget(fps)
        horiLayout.addLayout(vertLayoutLeft)
        horiLayout.addLayout(vertLayoutRight)
        layout.addLayout(horiLayout)

        
        # print("Board Voltage :", boardVoltage.sizePolicy().horizontalPolicy())
        # # print("Error :", error.sizePolicy().horizontalPolicy())

        # print("Fixed :", QtWidgets.QSizePolicy.Fixed)
        # print("Minimum :", QtWidgets.QSizePolicy.Minimum)
        # print("Maximum :", QtWidgets.QSizePolicy.Maximum)
        # print("Preferred :", QtWidgets.QSizePolicy.Preferred)
        # print("Expanding :", QtWidgets.QSizePolicy.Expanding)
        # print("MinimumExpanding :", QtWidgets.QSizePolicy.MinimumExpanding)
        # print("Ignored :", QtWidgets.QSizePolicy.Ignored)

        # self.aafficher = self
        # timer.timeout.connect(self.print_size)

        self.setLayout(layout)

    def print_size(self):
        print(self.aafficher.frameGeometry().width())


# Main window
class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setAttribute(Qt.WA_DeleteOnClose, True)

        self.setWindowTitle("Æsir - Engine dashboard")

        self.timer = QtCore.QTimer(self)
        self.timer.setInterval(30)
        # self.timer.setInterval(1000)

        # Temperature
        # Left Column
        temperatureTitle = TitleWidget("Temperature")
        tempOxidizer = TempOxidizerGraph(self, self.timer)
        tempPipework = TempPipeworkGraph(self, self.timer)
        tempInjector = TempInjectorGraph(self, self.timer)
        tempCombustion = TempCombustionGraph(self, self.timer)
        tempNozzle = TempNozzleGraph(self, self.timer)


        temperature = QtWidgets.QVBoxLayout()
        widgets = [temperatureTitle, tempOxidizer, tempPipework, tempInjector, tempCombustion, tempNozzle]
        
        for w in widgets:
            temperature.addWidget(w)

        # Pressure
        # Middle Column
        pressureTitle = TitleWidget("Pressure")
        preOxidizer = PreOxidizerGraph(self, self.timer)
        preInjector = PreInjectorGraph(self, self.timer)
        preCombustion = PreCombustionGraph(self, self.timer)
        preAmbient = PreAmbientGraph(self, self.timer)

        pressure = QtWidgets.QVBoxLayout()
        widgets = [pressureTitle, preOxidizer, preInjector, preCombustion, preAmbient]
        
        for w in widgets:
            pressure.addWidget(w)

        # Others
        # Right Column
        others = QtWidgets.QVBoxLayout()

        electrical = Electrical(self.timer)
        status = Status(self.timer)
        diagnostic = Diagnostic(self.timer)

        others.addWidget(electrical)
        others.addWidget(status)
        others.addWidget(diagnostic)
       
        # Global layout
        layout = QtWidgets.QHBoxLayout()
        layout.addLayout(temperature)
        layout.addLayout(pressure)
        layout.addLayout(others)

        widget = QtWidgets.QWidget(self)
        widget.setLayout(layout)
        
        # Timer for update
        self.timer.start()

        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(widget)
