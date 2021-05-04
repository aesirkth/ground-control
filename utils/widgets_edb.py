from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import Qt
import pyqtgraph as pg
from PyQt5.QtGui import QPalette, QColor
from time import time
from random import randint
import utils.fc as fc


INTERVAL = 30 # delay in ms - increase it if the dashboard is freezing, decrease to speed up the update rate

COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 0, 255), (0, 255, 255)]

X_AXIS_LENGTH = 120

AUTO_MODE = True

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
        

def random_update_plot_data(x, y, mini=0, maxi=200):
    if len(x) == 100:
        x.pop(0) # Remove the first y element.
        x.append(x[-1] + 1)  # Add a new value 1 higher than the last.

        y.pop(0) # Remove the first y element.
        y.append( randint(mini,maxi))  # Add a new random value.
    else:
        x = list(range(100))
        y = [randint(mini, maxi) for _ in range(100)]

    return x, y


def getDataBetween(time_list, data_list, t_min, t_max):
    k = len(time_list)
    while k > 0 and time_list[k-1] >= t_max:
        k -= 1
    k_max = k
    while k > 0 and time_list[k-1] >= t_min:
        k -= 1
    # These two loops can be optimized using a dichotomy
    # It select all the data that are in the time window, and the first one
    # which is not in the time window
    return time_list[k:k_max], time_list[k:k_max]


def updateData(tm, device, datatype, field):

    t_max = tm.get_current_time()
    t_min = t_max - X_AXIS_LENGTH
    x, y = tm.data[device][datatype][field].pack()
    k = len(x)-1
    while k > 0 and x[k] >= t_min:
        k -= 1
    # This whole loop can be optimized using a dichotomy
    # It select all the data that are in the time window, and the first one
    # which is not in the time window
    return x[k:], y[k:], t_min, t_max


class Line(object):
    def __init__(self, graph, num, tm, updateField, timer, name=""):
        self.graph = graph
        self.k = num
        self.tm = tm
        self.device = updateField[0]
        self.datatype = updateField[1]
        self.field = updateField[2]
        self.updateFunction = tm.data[self.device][self.datatype][self.field].pack
        self.name = name
        self.x = []
        self.y = []
        pen = pg.mkPen(color=COLORS[self.k])
        self.line = graph.plot(self.x, self.y, name=self.name, pen=pen)
        self.t_min = 0
        self.t_max = 0

        timer.timeout.connect(self.update)

    def update(self):
        x, y = self.updateFunction()
        
        if AUTO_MODE:
            t_max = self.tm.get_current_time()
            t_min = t_max - X_AXIS_LENGTH
            self.graph.setXRange(t_min, t_max)

        else:
            state = self.graph.getPlotItem().getViewBox().getState()
            t_min, t_max = state['targetRange'][0]

        # self.x, self.y = x, y
        # self.line.setData(self.x, self.y)

        # self.x, self.y = getDataBetween(x, y, t_min, t_max)
        # self.line.setData(self.x, self.y)
        # # This method is less efficient than the one above

        if t_max != self.t_max or t_min != self.t_min:
            self.t_max, self.t_min = t_max, t_min
            self.x, self.y = x, y
            self.line.setData(self.x, self.y)
            

class GraphWidget(pg.PlotWidget):

    def __init__(self, timer, tm, updateFields=[], dataNames=None, displayXLabel=True, parent=None):
        """
            updateFields is a list of [device, datatype, field]
        """
        super().__init__(parent)
        self.setAttribute(Qt.WA_DeleteOnClose, True)
        self.setMinimumWidth(260)

        self.setBackground('w')
        self.setMouseEnabled(x=not AUTO_MODE, y=False)
        # self.getPlotItem().getViewBox().setBorder(width=4.5, color='r')
        self.getAxis("left").setWidth(25)
        self.getPlotItem().hideButtons()

        # Labels
        if displayXLabel:
            self.setLabel('bottom', 'Time (s)')
            self.addLegend(offset=(1, 1))

        self.nbPlots = len(updateFields)
        self.updateFields = updateFields

        # Init lines
        self.data_lines = [None]*self.nbPlots
        for k in range(self.nbPlots):
            if dataNames is None:
                name = None
            else:
                name = dataNames[k]
            self.data_lines[k] = Line(self, k, tm, self.updateFields[k], timer, name=name)


class GraphPlusWidget(QtWidgets.QWidget):
    def __init__(self, timer, tm, Graph, updateFields=[], formatting="{:>5.1f}", parent=None):
        super().__init__(parent=parent)
        self.graph = Graph(timer, tm, parent=self)
        
        labLayout = QtWidgets.QVBoxLayout()
        for device, datatype, field in updateFields:
            func = tm.data[device][datatype][field].get_last
            lab = DataWidget("-", timer, func, 10, formatting=formatting)
            lab.setFixedWidth(30)
            labLayout.addWidget(lab)

        layout = QtWidgets.QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(3)
        layout.addWidget(self.graph)
        layout.addLayout(labLayout)
        self.setLayout(layout)


class AutoModeSwitch(QtWidgets.QWidget):
    def __init__(self, graphs_list, parent=None):
        super().__init__(parent=parent)
        self.graphs_list = graphs_list
        self.checkBox = QtWidgets.QCheckBox('Enable auto mode')
        self.checkBox.setChecked(AUTO_MODE)
        self.checkBox.stateChanged.connect(self.change_mode)
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.checkBox)
        self.setLayout(layout)


    def change_mode(self):
        global AUTO_MODE
        AUTO_MODE = self.checkBox.isChecked()
        for graph in self.graphs_list:
            graph.setMouseEnabled(x=not AUTO_MODE, y=False)


# Temperature
# Graphs
class TempOxidizerGraph(GraphWidget):
    def __init__(self, timer, tm, parent=None):
        updateField = ["test", "gyro", "x"]
        updateFields = [updateField]*5
        dataNames = None
        super().__init__(timer, tm, updateFields=updateFields, dataNames=dataNames, parent=parent)
        self.setYRange(-30, 30, padding=0)
        self.setTitle("Oxidizer tank + Passive vent line", color=(0, 0, 0))

        # timer.timeout.connect(lambda : print(self.getPlotItem().getViewBox().getState()))


class TempPipeworkGraph(GraphWidget):
    def __init__(self, timer, tm, parent=None):
        updateField = ["test", "gyro", "x"]
        updateFields = [updateField]*4
        dataNames = None
        super().__init__(timer, tm, updateFields=updateFields, dataNames=dataNames, parent=parent)
        self.setYRange(-30, 30, padding=0)
        self.setTitle("Pipework", color=(0, 0, 0))


class TempInjectorGraph(GraphWidget):
    def __init__(self, timer, tm, parent=None):
        updateField = ["test", "gyro", "x"]
        updateFields = [updateField]
        dataNames = None
        super().__init__(timer, tm, updateFields=updateFields, dataNames=dataNames, parent=parent)
        self.setYRange(-30, 500, padding=0)
        self.setTitle("Injector", color=(0, 0, 0))


class TempCombustionGraph(GraphWidget):
    def __init__(self, timer, tm, parent=None):
        updateField = ["test", "gyro", "x"]
        updateFields = [updateField]*3
        dataNames = ["Wall 1", "Wall 2", "Wall 3"]
        super().__init__(timer, tm, updateFields=updateFields, dataNames=dataNames, parent=parent)
        self.setYRange(0, 200, padding=0)
        self.setTitle("Combustion chamber", color=(0, 0, 0))


class TempNozzleGraph(GraphWidget):
    def __init__(self, timer, tm, parent=None):
        updateField = ["test", "gyro", "x"]
        updateFields = [updateField]
        dataNames = None
        super().__init__(timer, tm, updateFields=updateFields, dataNames=dataNames, parent=parent)
        self.setTitle("Nozzle", color=(0, 0, 0))

# Widgets
class TempOxidizer(GraphPlusWidget):
    def __init__(self, timer, tm, parent=None):
        graph = TempOxidizerGraph
        updateFields = [
            ["test", "gyro", "x"],
            ["test", "gyro", "x"],
            ["test", "gyro", "x"],
            ["test", "gyro", "x"],
            ["test", "gyro", "x"]]
        super().__init__(timer, tm, graph, updateFields, parent=parent)


class TempPipework(GraphPlusWidget):
    def __init__(self, timer, tm, parent=None):
        graph = TempPipeworkGraph
        updateFields = [
            ["test", "gyro", "x"],
            ["test", "gyro", "x"],
            ["test", "gyro", "x"],
            ["test", "gyro", "x"]]
        super().__init__(timer, tm, graph, updateFields, parent=parent)


class TempInjector(GraphPlusWidget):
    def __init__(self, timer, tm, parent=None):
        graph = TempInjectorGraph
        updateFields = [["test", "gyro", "x"]]
        super().__init__(timer, tm, graph, updateFields, parent=parent)


class TempCombustion(GraphPlusWidget):
    def __init__(self, timer, tm, parent=None):
        graph = TempCombustionGraph
        updateFields = [
            ["test", "gyro", "x"],
            ["test", "gyro", "x"],
            ["test", "gyro", "x"]]
        super().__init__(timer, tm, graph, updateFields, parent=parent)


class TempNozzle(GraphPlusWidget):
    def __init__(self, timer, tm, parent=None):
        graph = TempNozzleGraph
        updateFields = [["test", "gyro", "x"]]
        super().__init__(timer, tm, graph, updateFields, parent=parent)


# Pression
# Graphs
class PreOxidizerGraph(GraphWidget):
    def __init__(self, timer, tm, parent=None):
        updateField = ["test", "gyro", "x"]
        updateFields = [updateField]*2
        dataNames = ["Top", "Bottom"]
        super().__init__(timer, tm, updateFields=updateFields, dataNames=dataNames, parent=parent)
        self.setYRange(0, 60, padding=0)
        self.setTitle("Oxidizer tank readings", color=(0, 0, 0))


class PreInjectorGraph(GraphWidget):
    def __init__(self, timer, tm, parent=None):
        updateField = ["test", "gyro", "x"]
        updateFields = [updateField]
        dataNames = None
        super().__init__(timer, tm, updateFields=updateFields, dataNames=dataNames, parent=parent)
        self.setYRange(0, 60, padding=0)
        self.setTitle("Injector", color=(0, 0, 0))


class PreCombustionGraph(GraphWidget):
    def __init__(self, timer, tm, parent=None):
        updateField = ["test", "gyro", "x"]
        updateFields = [updateField]
        dataNames = None
        super().__init__(timer, tm, updateFields=updateFields, dataNames=dataNames, parent=parent)
        self.setYRange(0, 40, padding=0)
        self.setTitle("Combustion chamber", color=(0, 0, 0))


class PreAmbientGraph(GraphWidget):
    def __init__(self, timer, tm, parent=None):
        updateField = ["test", "gyro", "x"]
        updateFields = [updateField]*2
        dataNames = None
        super().__init__(timer, tm, updateFields=updateFields, dataNames=dataNames, parent=parent)
        self.setYRange(0, 1.5, padding=0)
        self.setTitle("Ambient pressure", color=(0, 0, 0))


# Widgets
class PreOxidizer(GraphPlusWidget):
    def __init__(self, timer, tm, parent=None):
        graph = PreOxidizerGraph
        updateFields = [
            ["test", "gyro", "x"],
            ["test", "gyro", "x"]]
        super().__init__(timer, tm, graph, updateFields, parent=parent)


class PreInjector(GraphPlusWidget):
    def __init__(self, timer, tm, parent=None):
        graph = PreInjectorGraph
        updateFields = [["test", "gyro", "x"]]
        super().__init__(timer, tm, graph, updateFields, parent=parent)


class PreCombustion(GraphPlusWidget):
    def __init__(self, timer, tm, parent=None):
        graph = PreCombustionGraph
        updateFields = [["test", "gyro", "x"]]
        super().__init__(timer, tm, graph, updateFields, parent=parent)


class PreAmbient(GraphPlusWidget):
    def __init__(self, timer, tm, parent=None):
        graph = PreAmbientGraph
        updateFields = [
            ["test", "gyro", "x"],
            ["test", "gyro", "x"]]
        super().__init__(timer, tm, graph, updateFields, formatting="{:>5.2f}", parent=parent)


# Electrical
class HorizontalTextWidget(QtWidgets.QLabel):
    """TextWidget"""
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
    """TextWidget"""
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
        self.heightOffset = size.width()/2
        self.setMinimumHeight(size.width()+10)
        self.setFixedWidth(size.height()+4)

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.translate(0, self.height()/2+self.heightOffset)
        painter.rotate(-90)
        painter.drawText(0, self.width()/2+4, self.text())
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
    """DataWidget"""
    def __init__(self, text, timer, updateFunction, fontSize, formatting="{:>5.2f}", parent=None):
        super(DataWidget, self).__init__(text, parent)
        self.setAlignment(Qt.AlignCenter)
        font = self.font()
        font.setPointSize(fontSize)
        self.setFont(font)

        self.formatting = formatting
        self.updateFunction = updateFunction
        timer.timeout.connect(self.update_value)

    def update_value(self):
        value = self.updateFunction()
        if isinstance(value, str):
            self.setText(value)
            return
        self.setText(self.formatting.format(self.updateFunction()))


def random_value(mini=0, maxi=1000):
    return randint(mini,maxi)/100

class Electrical(QtWidgets.QWidget):

    def __init__(self, timer, tm, parent=None):
        super().__init__(parent)
        layout = QtWidgets.QVBoxLayout(self)
        layout.setContentsMargins(0,0,0,0)

        title = TitleWidget("Electrical")

        tab = QtWidgets.QGridLayout()
        tab.setSpacing(2)

        tab.addWidget(VerticalTextWidget(self, "Voltage (V)"), 1, 0, 2, 1)
        tab.addWidget(VerticalTextWidget(self, "Current (A)"), 3, 0, 2, 1)
        tab.addWidget(VerticalTextWidget(self, "Resistance (Ω)"), 5, 0, 2, 1)

        tab.addWidget(HorizontalTextWidget(self, "Main valve solenoid"), 0, 1)
        tab.addWidget(HorizontalTextWidget(self, "Vent line solenoid"), 0, 2)
        tab.addWidget(HorizontalTextWidget(self, "Ignition system"), 0, 3)

        # Data
        tab.addWidget(DataWidget("-", timer, tm.data["test"]["gyro"]["x"].get_last, 25), 1, 1)
        tab.addWidget(DataWidget("-", timer, tm.data["test"]["gyro"]["x"].get_last, 25), 1, 2)
        tab.addWidget(DataWidget("-", timer, tm.data["test"]["gyro"]["x"].get_last, 25), 1, 3)
        tab.addWidget(DataWidget("-", timer, tm.data["test"]["gyro"]["x"].get_last, 25), 3, 1)
        tab.addWidget(DataWidget("-", timer, tm.data["test"]["gyro"]["x"].get_last, 25), 3, 2)
        tab.addWidget(DataWidget("-", timer, tm.data["test"]["gyro"]["x"].get_last, 25), 3, 3)
        tab.addWidget(DataWidget("-", timer, tm.data["test"]["gyro"]["x"].get_last, 25), 5, 1)
        tab.addWidget(DataWidget("-", timer, tm.data["test"]["gyro"]["x"].get_last, 25), 5, 2)
        tab.addWidget(DataWidget("-", timer, tm.data["test"]["gyro"]["x"].get_last, 25), 5, 3)

        # Graphs
        listGraphs = [
            GraphWidget(timer, tm, [["test", "gyro", "x"]], displayXLabel=False),
            GraphWidget(timer, tm, [["test", "gyro", "x"]], displayXLabel=False),
            GraphWidget(timer, tm, [["test", "gyro", "x"]], displayXLabel=False),
            GraphWidget(timer, tm, [["test", "gyro", "x"]], displayXLabel=False),
            GraphWidget(timer, tm, [["test", "gyro", "x"]], displayXLabel=False),
            GraphWidget(timer, tm, [["test", "gyro", "x"]], displayXLabel=False),
            GraphWidget(timer, tm, [["test", "gyro", "x"]], displayXLabel=False),
            GraphWidget(timer, tm, [["test", "gyro", "x"]], displayXLabel=False),
            GraphWidget(timer, tm, [["test", "gyro", "x"]], displayXLabel=False)
        ]

        # Changing the background color
        palette = self.palette()
        for graph in listGraphs:
            graph.setBackground(palette.color(QPalette.Window))
            graph.setMinimumWidth(100) # It seems that the minimum is 144

        tab.addWidget(listGraphs[0], 2, 1)
        tab.addWidget(listGraphs[1], 2, 2)
        tab.addWidget(listGraphs[2], 2, 3)
        tab.addWidget(listGraphs[3], 4, 1)
        tab.addWidget(listGraphs[4], 4, 2)
        tab.addWidget(listGraphs[5], 4, 3)
        tab.addWidget(listGraphs[6], 6, 1)
        tab.addWidget(listGraphs[7], 6, 2)
        tab.addWidget(listGraphs[8], 6, 3)

        self.listGraphs = listGraphs

        layout.addWidget(title)
        layout.addLayout(tab)
        self.setLayout(layout)


# Status signals
class ColoredCircle(QtWidgets.QWidget):
    """A circle of color!!"""
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
    """BoolIndicator"""
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
    """ValueIndicator"""
    def __init__(self, text, timer, updateFunction, sizeTitle=15, sizeData=17, formatting="{}", parent=None):
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
        self.indic = DataWidget("-", timer, updateFunction, sizeData, formatting=formatting)
        self.indic.setAlignment(Qt.AlignRight | Qt.AlignVCenter)

        layout.addWidget(self.title)
        layout.addWidget(self.indic)

        self.setLayout(layout)


class Status(QtWidgets.QWidget):

    def __init__(self, timer, tm, parent=None):
        super().__init__(parent)
        layout = QtWidgets.QVBoxLayout(self)
        layout.setContentsMargins(0,0,0,0)

        title = TitleWidget("Status signals")
        # relief = BoolIndicator("Relief valve trigger", timer)
        # valve = BoolIndicator("Abort valve trigger", timer)
        actuation = ValueIndicator("Main valve actuation", timer, tm.data["test"]["gyro"]["x"].get_last, formatting="{:.0f} mm")

        layout.addWidget(title)
        # layout.addWidget(relief)
        # layout.addWidget(valve)
        layout.addWidget(actuation)

        self.setLayout(layout)


# Diagnostic readings
class BoardVoltageIndicator(QtWidgets.QWidget):
    """BoardVoltageIndicator"""
    def __init__(self, text, timer, tm, parent=None):
        super(BoardVoltageIndicator, self).__init__(parent)

        # Background color
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor("white"))
        self.setPalette(palette)

        # Layout
        layout = QtWidgets.QVBoxLayout()

        # Title
        title = QtWidgets.QLabel(text)
        title.setAlignment(Qt.AlignCenter)
        font = title.font()
        font.setPointSize(15)
        title.setFont(font)

        title.setMaximumHeight(30)

        # Indicators
        indicLayout = QtWidgets.QGridLayout()

        indicLayout.addWidget(DataWidget("-", timer, tm.data["test"]["gyro"]["x"].get_last, 14), 0, 0)
        indicLayout.addWidget(DataWidget("-", timer, tm.data["test"]["gyro"]["x"].get_last, 14), 0, 1)
        indicLayout.addWidget(DataWidget("-", timer, tm.data["test"]["gyro"]["x"].get_last, 14), 1, 0)
        indicLayout.addWidget(DataWidget("-", timer, tm.data["test"]["gyro"]["x"].get_last, 14), 1, 1)
        

        layout.addWidget(title)
        layout.addLayout(indicLayout)

        # self.setMinimumWidth(265) # Évite le redimensionnement du widget

        self.setLayout(layout)


class RMCTemperatureIndicator(QtWidgets.QWidget):
    """RMCTemperatureIndicator"""
    def __init__(self, text, timer, tm, parent=None):
        super(RMCTemperatureIndicator, self).__init__(parent)

        # Background color
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.Window, QColor("white"))
        self.setPalette(palette)

        # Layout
        layout = QtWidgets.QVBoxLayout()
        # layout.setAlignment(Qt.AlignVCenter)
        # Title
        title = QtWidgets.QLabel(text)
        title.setAlignment(Qt.AlignCenter)
        font = title.font()
        font.setPointSize(15)
        title.setFont(font)

        title.setMaximumHeight(30)

        # Indicators
        indicLayout = QtWidgets.QGridLayout()

        indicLayout.addWidget(DataWidget("-", timer, tm.data["test"]["gyro"]["x"].get_last, 14), 0, 0)
        indicLayout.addWidget(DataWidget("-", timer, tm.data["test"]["gyro"]["x"].get_last, 14), 0, 1)
        indicLayout.addWidget(DataWidget("-", timer, tm.data["test"]["gyro"]["x"].get_last, 14), 1, 0)
        indicLayout.addWidget(DataWidget("-", timer, tm.data["test"]["gyro"]["x"].get_last, 14), 1, 1)
        indicLayout.addWidget(DataWidget("-", timer, tm.data["test"]["gyro"]["x"].get_last, 14), 2, 0)
        indicLayout.addWidget(DataWidget("-", timer, tm.data["test"]["gyro"]["x"].get_last, 14), 2, 1)
        indicLayout.addWidget(DataWidget("-", timer, tm.data["test"]["gyro"]["x"].get_last, 14), 3, 0)
        indicLayout.addWidget(DataWidget("-", timer, tm.data["test"]["gyro"]["x"].get_last, 14), 3, 1)
        

        layout.addWidget(title)
        layout.addLayout(indicLayout)

        self.setLayout(layout)


class ErrorGraph(GraphWidget):

    def __init__(self, timer, tm, parent=None):
        updateFields = []
        dataNames = None
        super().__init__(timer, tm, updateFields=updateFields, dataNames=dataNames, parent=parent)
        self.setTitle("Errors", color=(0, 0, 0))
        self.setMaximumHeight(200)
        self.setMinimumHeight(100)

    def sizeHint(self):
        size = GraphWidget.sizeHint(self)
        return QtCore.QSize(size.width(), 130)


class FPSIndicator(ValueIndicator):
    """FPSIndicator"""
    def __init__(self, timer, parent=None):
        super(FPSIndicator, self).__init__("FPS :", timer, self.updateFPS,
            sizeTitle=10, sizeData=10,  formatting="{}", parent=parent)
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

    def __init__(self, timer, tm, graphs_list, parent=None):
        super().__init__(parent)
        self.setMaximumWidth(570)
        layout = QtWidgets.QVBoxLayout(self)
        layout.setContentsMargins(0,0,0,0)

        horiLayout = QtWidgets.QHBoxLayout()
        vertLayout = QtWidgets.QVBoxLayout()

        title = TitleWidget("Diagnostic readings")
        boardVoltage = BoardVoltageIndicator("Board input voltage", timer, tm)
        error = ErrorGraph(timer, tm)
        # rmc = RMCTemperatureIndicator("R&MC Temperature", timer, tm)
        fps = FPSIndicator(timer)

        layout.addWidget(title)
        horiLayout.addWidget(boardVoltage)
        vertLayout.addWidget(error)
        vertLayout.addWidget(fps)
        vertLayout.addWidget(AutoModeSwitch(graphs_list + [error], self))
        horiLayout.addLayout(vertLayout)
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

        # self.aafficher = error
        # timer.timeout.connect(self.print_size)

        self.setLayout(layout)

    # def print_size(self):
    #     print(self.aafficher.frameGeometry().height())


# Menu Widgets
class MenuButton(QtWidgets.QPushButton):
    def __init__(self, text, function, parent=None):
        super().__init__(text, parent)
        self.clicked.connect(function)

        font = self.font()
        font.setPointSize(12)
        self.setFont(font)

        self.setContentsMargins(500, 500, 500, 500)


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

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.serial_button)
        layout.addWidget(self.file_button)

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


class InfoDialog(QtWidgets.QDialog):
    def __init__(self, title, text, image=None, parent=None):
        super().__init__(parent=parent)

        self.setFixedWidth(400)
        self.setWindowTitle(title)

        layout = QtWidgets.QVBoxLayout()

        if image is not None:
            label = QtWidgets.QLabel()
            label.setPixmap(QtGui.QPixmap(image))
            label.setAlignment(Qt.AlignCenter)
            layout.addWidget(label)

        label = QtWidgets.QLabel(text)
        label.setWordWrap(True)
        label.setTextFormat(Qt.RichText)
        label.setTextInteractionFlags(Qt.TextBrowserInteraction)
        label.setOpenExternalLinks(True)

        # Alignment / Font size
        label.setAlignment(Qt.AlignJustify)
        font = label.font()
        font.setPointSize(10)
        label.setFont(font)

        layout.addWidget(label)
        self.setLayout(layout)


class MenuBar(QtWidgets.QMenuBar):
    def __init__(self, parent=None):
        super().__init__(parent=parent)

        # File
        self.fileMenu = QtWidgets.QMenu("&File", self)

        self.openSerial = QtWidgets.QAction("Open &serial")
        self.openSerial.triggered.connect(self.parent()._open_serial)

        self.openFile = QtWidgets.QAction("Open &file")
        self.openFile.triggered.connect(self.parent()._open_file)

        self.exit = QtWidgets.QAction("&Exit")
        self.exit.triggered.connect(self.parent().close)

        self.fileMenu.addAction(self.openSerial)
        self.fileMenu.addAction(self.openFile)
        self.fileMenu.addAction(self.exit)
        self.addMenu(self.fileMenu)

        # Help
        self.helpMenu = QtWidgets.QMenu("&Help", self)

        self.aboutEDB = QtWidgets.QAction("About &Engine Dashboard")
        self.aboutEDB.triggered.connect(self._aboutEDB)

        self.aboutAesir = QtWidgets.QAction("&About Æsir")
        self.aboutAesir.triggered.connect(self._aboutAesir)

        self.helpMenu.addAction(self.aboutEDB)
        self.helpMenu.addAction(self.aboutAesir)
        self.addMenu(self.helpMenu)

    def _aboutEDB(self):
        title = "Engine Dashboard"
        text = """This dashboard was developed in 2021 in the context of Project Mjollnir. The purpose is to monitor the state of the rocket's engine.<br /><br />Project Mjollnir is the third project of the Æsir association. The objective is to reach an altitude of 10 km with a sounding rocket made by students."""
        InfoDialog(title, text).exec_()

    def _aboutAesir(self):
        title = "Æsir"
        text = """ÆSIR is a student rocketry association founded in 2016 at KTH Royal Institute of Technology in Stockholm. It has around 40 members every year, which are all students at KTH. Roughly half of the members are international students and they cover many disciplines and levels of study, although most of ÆSIR's members study Aerospace Engineering, Computer Science, Vehicle Engineering, Electrical Engineering, Engineering Physics and Mechanical Engineering.<br /><br /><a href=\"http://aesir.se\">ÆSIR website</a>"""
        image = 'gui/logo/256x256.png'
        InfoDialog(title, text, image).exec_()


# Main window
class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, tm, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setAttribute(Qt.WA_DeleteOnClose, True)

        self.setWindowTitle("Æsir - Engine dashboard")

        self.tm = tm
        self.timer = QtCore.QTimer(self)
        self.timer.setInterval(INTERVAL)

        # Temperature
        # Left Column
        temperatureTitle = TitleWidget("Temperature (°C)")
        tempOxidizer = TempOxidizer(self.timer, tm, parent=self)
        tempPipework = TempPipework(self.timer, tm, parent=self)
        tempInjector = TempInjector(self.timer, tm, parent=self)
        tempCombustion = TempCombustion(self.timer, tm, parent=self)
        tempNozzle = TempNozzle(self.timer, tm, parent=self)


        temperature = QtWidgets.QVBoxLayout()
        widgets = [temperatureTitle, tempOxidizer, tempPipework, tempInjector, tempCombustion, tempNozzle]
        
        for w in widgets:
            temperature.addWidget(w)

        # Pressure
        # Middle Column
        pressureTitle = TitleWidget("Pressure (bar)")
        preOxidizer = PreOxidizer(self.timer, tm, parent=self)
        preInjector = PreInjector(self.timer, tm, parent=self)
        preCombustion = PreCombustion(self.timer, tm, parent=self)
        preAmbient = PreAmbient(self.timer, tm, parent=self)

        pressure = QtWidgets.QVBoxLayout()
        widgets = [pressureTitle, preOxidizer, preInjector, preCombustion, preAmbient]
        
        for w in widgets:
            pressure.addWidget(w)

        # Graphs list
        graphs_list = [tempOxidizer.graph, tempPipework.graph, tempInjector.graph, tempCombustion.graph, tempNozzle.graph, preOxidizer.graph, preInjector.graph, preCombustion.graph, preAmbient.graph]

        
        # Others
        # Right Column
        others = QtWidgets.QVBoxLayout()

        electrical = Electrical(self.timer, tm)
        status = Status(self.timer, tm)
        diagnostic = Diagnostic(self.timer, tm, graphs_list + electrical.listGraphs)

        sizePolicy = electrical.sizePolicy()
        sizePolicy.setVerticalPolicy(QtWidgets.QSizePolicy.Expanding)
        electrical.setSizePolicy(sizePolicy)

        # maxWidth = diagnostic.minimumSizeHint().width()
        maxWidth = 500

        electrical.setMaximumWidth(maxWidth)
        status.setMaximumWidth(maxWidth)
        diagnostic.setMaximumWidth(maxWidth)

        others.addWidget(electrical)
        others.addWidget(status)
        others.addWidget(diagnostic)

        # Global layout
        layout = QtWidgets.QHBoxLayout()
        layout.addLayout(temperature)
        layout.addLayout(pressure)
        layout.addLayout(others)

        self.widget = QtWidgets.QWidget(self)
        self.widget.setLayout(layout)
        
        # Timer for update
        # self.timer.start() # Now in the MainMenu class

        QtCore.QCoreApplication.setQuitLockEnabled(True)
        # Allow the application to end when the window is closed

        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(self.widget)

        # Main menu
        self.menu = MainMenu(parent=self)
        electrical.setSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)

        # Menu bar
        self.menuBar = MenuBar(parent=self)
        self.setMenuBar(self.menuBar)

    def closeEvent(self, event):
        # properly stop all threads
        self.tm.stop()
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
        self.tm.open_flash_file(fname)
        # self.tm.open_flash_file("data/test")
        self.menu.hide()
        self.timer.start()
