import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QFrame, QColorDialog,
                             QApplication, QSpinBox, QLabel, QHBoxLayout,
                             QVBoxLayout)
from PyQt5.QtGui import QColor, QIcon
from PyQt5.QtCore import Qt
from colour import Colour


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.colour = Colour('#000000')
        self.btn = Button('Задать цвет', self)
        self.lighter = Button('Осветлить', self)
        self.darker = Button('Затемнить', self)
        self.frm = QFrame(self)
        self.spin_box = QSpinBox(self)
        self.lbl = QLabel(self)
        self.lbl.setText('Процент изменения')
        self.lbl.setFixedSize(200, 15)
        self.setStyleSheet("background-color: #1f0521; color: #fdffef;")
        self.lbl.setStyleSheet("font-family: Helvetica, Verdana, sans-serif; "
                               "font-size: 150%;"
                               "color: white; "
                               "font-weight: bold;")
        self.initUI()

    def initUI(self):
        col = QColor(0, 0, 0)
        self.lighter.clicked.connect(self.make_l)
        self.darker.clicked.connect(self.make_d)
        self.btn.clicked.connect(self.showDialog)
        self.frm.setStyleSheet("QWidget { background-color: %s }" % col.name())
        self.frm.setMinimumSize(200, 200)
        self.setWindowIcon(QIcon("icon.png"))
        self.setGeometry(300, 300, 500, 400)
        self.setWindowTitle('Палитра цветов')
        self.add_spinner()
        self.init_layout()
        self.show()

    def showDialog(self):
        dialog = QColorDialog()
        dialog.setStyleSheet("background-color: #1f0521; color: #fdffef;")
        col = dialog.getColor()
        if col.isValid():
            self.frm.setStyleSheet(
                "QWidget { background-color: %s }" % col.name())
            code = col.name().upper()
            print(code)
            self.colour = Colour(code)
            print(str(self.colour))

    def make_l(self):
        percent = self.spin_box.value()
        self.colour.lighten(percent)
        print(self.colour)
        self.frm.setStyleSheet(
            "QWidget { background-color: %s }" % str(self.colour))

    def make_d(self):
        percent = self.spin_box.value()
        self.colour.darken(percent)
        self.frm.setStyleSheet(
            "QWidget { background-color: %s }" % str(self.colour))

    def add_spinner(self):
        self.spin_box.setFocusPolicy(Qt.NoFocus)
        self.spin_box.setValue(10)
        self.spin_box.setSuffix('%')

    def init_layout(self):
        bbox = QHBoxLayout()  # по ширине
        bbox.addWidget(self.btn)
        bbox.addWidget(self.lighter)
        bbox.addWidget(self.darker)
        vbox = QVBoxLayout()
        vbox.setSpacing(5)
        vbox.addWidget(self.lbl)
        vbox.addWidget(self.spin_box)
        vbox.addWidget(self.frm)
        vbox.addLayout(bbox)
        self.setLayout(vbox)


class Button(QPushButton):
    def __init__(self, title, parent):
        super().__init__(title, parent)
        self.setStyleSheet("background-color: #4c4d62; border: none; "
                           "color: white; padding: 15px 32px; "
                           "text-align: center; text-decoration: none; "
                           "display: inline-block; font-size: 16px;")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
