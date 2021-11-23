import sys
from random import randint
from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.setWindowTitle('Рисование')
        self.do_paint = False
        self.pushButton.clicked.connect(self.draw)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            for _ in range(randint(2, 5)):
                self.draw_flag(qp)
            qp.end()

    def draw_flag(self, qp):
        side = randint(20, 100)
        qp.setBrush(QColor("yellow"))
        qp.drawEllipse(QPoint(randint(200, 600), randint(200, 600)), side, side)

    def draw(self):
        self.do_paint = True
        self.repaint()
        self.do_paint = False


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
