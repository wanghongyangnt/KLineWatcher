import sys
from forms.klinegraphicsview import KLineGraphicsView
from datatype.kline import KLineData
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = KLineGraphicsView()

    kData = KLineData(100, 200, 225, 75)
    window.drawKLineBox(kData)
    window.show()
    sys.exit(app.exec())