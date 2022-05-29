from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt

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


class LargePushButton(QtWidgets.QPushButton):
	def __init__(self, text, parent=None):
		super().__init__(text, parent=parent)
		sizePolicy = self.sizePolicy()
		sizePolicy.setVerticalPolicy(QtWidgets.QSizePolicy.Expanding)
		self.setSizePolicy(sizePolicy)
