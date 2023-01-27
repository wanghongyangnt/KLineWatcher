import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QPointF, QLineF
from PyQt5.QtGui import QPen, QColor, QBrush, QFont, QPixmap, QPolygonF, QPainterPath, QTransform
from PyQt5.QtWidgets import (QDialog, QLabel, QSlider, QMenuBar, QMenu, QAction,
                             QFormLayout, QGraphicsScene, QGraphicsView, QGraphicsLineItem)
from PyQt5.QtWidgets import (QApplication, QMainWindow, QGraphicsScene, QGraphicsView, QGraphicsSimpleTextItem,
                             QGraphicsTextItem, QGraphicsEllipseItem, QGraphicsRectItem,
                             QGraphicsPixmapItem, QGraphicsPolygonItem, QGraphicsPathItem)

class KLineGraphicsView(QMainWindow):
    def __init__(self, parent=None):
        super(KLineGraphicsView, self).__init__(parent)
        # 设置窗口标题
        self.setWindowTitle('KLine Graphic')
        # 设置窗口大小
        self.resize(1000, 650)
        self.initUi()

    def initUi(self):
        # 菜单条
        menuBar = self.menuBar()
        menuFile = menuBar.addMenu('操作画板')

        aTrans = QAction('变换操作', self)
        aTrans.triggered.connect(self.onTransDialog)
        aReset = QAction('复位', self)
        aReset.triggered.connect(self.onReset)
        aExit = QAction('退出', self)
        aExit.triggered.connect(self.close)

        menuFile.addAction(aTrans)
        menuFile.addAction(aReset)
        menuFile.addSeparator()
        menuFile.addAction(aExit)

        # 场景部分
        self.scene = QGraphicsScene()
        self.scene.setBackgroundBrush(QBrush(QColor(30, 30, 30)))

        # 绘制坐标轴
        linePen = QPen()
        linePen.setColor(QColor(255, 255, 255))
        linePen.setWidth(2)
        xLine = QGraphicsLineItem(20, 1020, 1020, 1020)
        xLine.setPen(linePen)
        yLine = QGraphicsLineItem(20, 20, 20, 1020)
        yLine.setPen(linePen)
        self.scene.addItem(xLine)
        self.scene.addItem(yLine)

        # 绘制文本
        textItem = QGraphicsSimpleTextItem('0')
        textFont = QFont()
        textFont.setPixelSize(15)
        textItem.setFont(textFont)
        textItem.setPen(linePen)
        textItem.setPos(5, 1005)
        self.scene.addItem(textItem)

        self.view = QGraphicsView()
        self.view.setScene(self.scene)

        self.setCentralWidget(self.view)

    def onTransDialog(self):
        dlg = TransDialog(self.view, self)
        dlg.exec()

    def drawKLineBox(self, kData):
        if (kData.closePrice - kData.openPrice) > 0:
            width = kData.closePrice - kData.openPrice
            # 这里宽度固定为30
            redColor = QColor(230, 64, 50)
            rect = QGraphicsRectItem(100, 1000 - kData.closePrice, 30, width)
            brush = QBrush(redColor)
            rect.setBrush(brush)
            self.scene.addItem(rect)
            # 绘制最高和最低
            maxLine = QGraphicsLineItem(115, 1000 - kData.maxPrice, 115, 1000 - kData.closePrice)
            minLine = QGraphicsLineItem(115, 1000 - kData.minPrice, 115, 1000 - kData.openPrice)
            pen = QPen()
            pen.setColor(redColor)
            pen.setWidth(2)
            maxLine.setPen(pen)
            minLine.setPen(pen)
            self.scene.addItem(maxLine)
            self.scene.addItem(minLine)

    def onReset(self):
        self.view.setTransform(QTransform())