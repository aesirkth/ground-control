from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import Qt


class ToolButton(QtWidgets.QWidget):

    def __init__(self):
        super(ToolButton,self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("ToolButton")
        self.setGeometry(400,400,300,260)

        self.toolbar = self.addToolBar("toolBar")
        self.statusBar()

        self._detailsbutton = QToolButton()                                     
        self._detailsbutton.setCheckable(True)                                  
        self._detailsbutton.setChecked(False)                                   
        self._detailsbutton.setArrowType(Qt.RightArrow)
        self._detailsbutton.setAutoRaise(True)
        #self._detailsbutton.setIcon(QIcon("test.jpg"))
        self._detailsbutton.setToolButtonStyle(Qt.ToolButtonIconOnly)
        self._detailsbutton.clicked.connect(self.showDetail)
        self.toolbar.addWidget(self._detailsbutton)

    def showDetail(self):
        if self._detailsbutton.isChecked():
            self.statusBar().showMessage("Show Detail....")
        else:
            self.statusBar().showMessage("Close Detail....")



# Main window
class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setWindowTitle("Æsir - Mission Control Dashboard")

        button = QtWidgets.QPushButton('Open link')
        button.setShortcut('Ctrl+L')  #shortcut key
        button.clicked.connect(lambda : print("Open link..."))
        # button.setToolTip("Open link") #Tool tip

        layout = QtWidgets.QHBoxLayout()
        layout.addWidget(button)
        
        widget = QtWidgets.QWidget(self)
        widget.setLayout(layout)

        QtCore.QCoreApplication.setQuitLockEnabled(True)
        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(widget)