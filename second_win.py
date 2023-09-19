from PyQt5.QtCore import Qt, QTimer, QTime
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit
from final_win import *
from instr import *
class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width, win_height)
        self.move(win_x, win_y)
    def initUI(self):
        self.h_line = QHBoxLayout()
        self.r_line = QVBoxLayout()
        self.l_line = QVBoxLayout()
        self.TXTfio = QLabel(txt_hintname)
        self.EDITfio = QLineEdit('ФИО')
        self.TXTage = QLabel(txt_hintage)
        self.EDITage = QLineEdit('15')
        self.HINTtest1 = QLabel(txt_hinttest1)
        self.BTNtest1 = QPushButton(txt_starttest1)
        self.EDITtest1 = QLineEdit('15')
        self.HINTtest2 = QLabel(txt_hinttest2)
        self.BTNtest2 = QPushButton(txt_starttest2)
        self.HINTtest3 = QLabel(txt_hinttest3)
        self.BTNtest3 = QPushButton(txt_starttest3)
        self.EDITtest2 = QLineEdit('45')
        self.EDITtest3 = QLineEdit('30')
        self.BTNsend = QPushButton(txt_sendresults)
        self.timers = QLabel('00:00:00')
        self.r_line.addWidget(self.timers, alignment = Qt.AlignCenter)
        self.l_line.addWidget(self.TXTfio, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.EDITfio, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.TXTage, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.EDITage, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.HINTtest1, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.BTNtest1, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.EDITtest1, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.HINTtest2, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.BTNtest2, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.HINTtest3, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.BTNtest3, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.EDITtest2, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.EDITtest3, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.BTNsend, alignment = Qt.AlignCenter)

        self.h_line.addLayout(self.l_line)
        self.h_line.addLayout(self.r_line)

        self.setLayout(self.h_line)
    def connects(self):
        self.BTNsend.clicked.connect(self.next_click)
        self.BTNtest1.clicked.connect(self.timer1)
        self.BTNtest2.clicked.connect(self.timer2)
        self.BTNtest3.clicked.connect(self.timer3)
    def result(self):
        global i
        global res
        age =  int(self.EDITage.text())
        res1 = int(self.EDITtest1.text())
        res2 = int(self.EDITtest2.text())
        res3 = int(self.EDITtest3.text())
        i = (4*(res1 + res2 + res3)-200)/10
        res = '-'
        if age in [7, 8]:
            if i >=21:
                res = 'Низкая'
            elif i >=17:
                res = 'Удовлетворительная'
            elif i >=12:
                res = 'Средная'
            elif i >=6.5:
                res = 'Выше среднего'
            else:
                res = 'Высокая'

        if age in [9, 10]:
            if i >=19.5:
                res = 'Низкая'
            elif i >=15.5:
                res = 'Удовлетворительная'
            elif i >=10.5:
                res = 'Средная'
            elif i >=5:
                res = 'Выше среднего'
            else:
                res = 'Высокая'

        if age in [11, 12]:
            if i >=18:
                res = 'Низкая'
            elif i >=14:
                res = 'Удовлетворительная'
            elif i >=9:
                res = 'Средная'
            elif i >=3.5:
                res = 'Выше среднего'
            else:
                res = 'Высокая'

        if age in [13, 14]:
            if i >=16.5:
                res = 'Низкая'
            elif i >=12.5:
                res = 'Удовлетворительная'
            elif i >=7.5:
                res = 'Средная'
            elif i >=2:
                res = 'Выше среднего'
            else:
                res = 'Высокая'

        if age >= 15:
            if i >=15:
                res = 'Низкая'
            elif i >=11:
                res = 'Удовлетворительная'
            elif i >=6:
                res = 'Средная'
            elif i >=0.5:
                res = 'Выше среднего'
            else:
                res = 'Высокая'
        
    def timer1(self):
        global time
        time = QTime(0, 0, 15)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer1Event)
        self.timer.start(1000)
    def timer1Event(self):
        global time
        time = time.addSecs(-1)
        self.timers.setText(time.toString('hh:mm:ss'))
        self.timers.setStyleSheet('color: rgb(255, 0, 0)')
        if time.toString('hh:mm:ss') == '00:00:00':
            self.timers.setStyleSheet('color: rgb(0, 0, 0)')
            self.timer.stop()
    def timer2(self):
        global time
        time = QTime(0, 0, 30)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer2Event)
        self.timer.start(1500)
    def timer2Event(self):
        global time
        time = time.addSecs(-1)
        self.timers.setText(time.toString('hh:mm:ss'))
        self.timers.setStyleSheet('color: rgb(0, 0, 255)')
        if time.toString('hh:mm:ss') == '00:00:00':
            self.timers.setStyleSheet('color: rgb(0, 0, 0)')
            self.timer.stop()
    def timer3(self):
        global time
        time = QTime(0, 1, 0)
        self.timer = QTimer()
        self.timer.timeout.connect(self.timer3Event)
        self.timer.start(1000)
    def timer3Event(self):
        global time
        time = time.addSecs(-1)
        self.timers.setText(time.toString('hh:mm:ss'))
        if time.toString('hh:mm:ss') == '00:00:59' or time.toString('hh:mm:ss') == '00:00:15':
            self.timers.setStyleSheet('color: rgb(255, 0, 0)')
        if time.toString('hh:mm:ss') == '00:00:45':
            self.timers.setStyleSheet('color: rgb(0, 0, 0)')
        if time.toString('hh:mm:ss') == '00:00:00':
            self.timers.setStyleSheet('color: rgb(0, 0, 0)')
            self.timer.stop()
    def next_click(self):
        self.result()
        self.hide()
        self.fw = FinalWin(i, res)