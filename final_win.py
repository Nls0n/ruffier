from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout
from instr import *
from second_win import *
class FinalWin(QWidget):
    def __init__(self, i, res):
        super().__init__()
        self.set_appear()
        self.initUI(i, res)
        self.show()
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def initUI(self, i, res):
        self.txt_index = QLabel(txt_index + ' '+str(i))
        self.workheart = QLabel(txt_workheart + ' ' + res)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.txt_index, alignment = Qt.AlignCenter)
        self.layout.addWidget(self.workheart, alignment = Qt.AlignCenter)
        self.setLayout(self.layout)