from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from utils.widgets_common import TitleWidget, LargePushButton


class Servo(QtWidgets.QWidget):
	def __init__(self, name, tc, parent=None):
		super().__init__(parent=parent)
		self.name = QtWidgets.QLabel(name)

		self.slider = QtWidgets.QSlider(Qt.Horizontal)
		self.slider.setMinimum(0)
		self.slider.setMaximum(100)
		self.slider.setTickPosition(QtWidgets.QSlider.TicksBelow)
		self.slider.setTickInterval(25)
		self.slider.valueChanged.connect(self.valuechange)

		self.display = QtWidgets.QLabel("0")
		self.display.setAlignment(Qt.AlignRight)

		sublayout = QtWidgets.QHBoxLayout()
		sublayout.addWidget(self.name)
		sublayout.addWidget(self.display)
		sublayout.setContentsMargins(0, 0, 0, 0)


		layout = QtWidgets.QVBoxLayout()
		layout.addLayout(sublayout)
		layout.addWidget(self.slider)
		layout.setContentsMargins(0, 0, 0, 0)

		self.setLayout(layout)

	def valuechange(self):
		self.display.setText(str(self.slider.value()))


class LaunchPadController(QtWidgets.QWidget):

	def __init__(self, tc, parent=None):
		super().__init__(parent=parent)

		title = TitleWidget("Launch Pad Controller")
		self.servo1 = Servo("Servo 1", tc, self)
		self.servo2 = Servo("Servo 2", tc, self)
		self.servo3 = Servo("Servo 3", tc, self)

		title.setMinimumSize(250, 0)

		self.button1 = LargePushButton("Output 1")
		self.button2 = LargePushButton("Output 2")
		self.button3 = LargePushButton("Output 3")
		self.button4 = LargePushButton("Output 4")

		outputsLayout = QtWidgets.QGridLayout()
		outputsLayout.addWidget(title, 0, 0, 1, 2)
		outputsLayout.addWidget(self.button1, 1, 0)
		outputsLayout.addWidget(self.button2, 2, 0)
		outputsLayout.addWidget(self.button3, 1, 1)
		outputsLayout.addWidget(self.button4, 2, 1)

		servosLayout = QtWidgets.QVBoxLayout()
		servos = [self.servo1, self.servo2, self.servo3]
		for w in servos:
			servosLayout.addWidget(w)
		
		layout = QtWidgets.QHBoxLayout()
		layout.setContentsMargins(5,5,5,5)
		layout.setSpacing(10)
		layout.addLayout(outputsLayout)
		layout.addLayout(servosLayout)

		self.setLayout(layout)
