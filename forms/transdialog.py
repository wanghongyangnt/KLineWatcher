import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QPointF, QLineF
from PyQt5.QtGui import QPen, QColor, QBrush, QFont, QPixmap, QPolygonF, QPainterPath, QTransform
from PyQt5.QtWidgets import (QDialog, QLabel, QSlider, QMenuBar, QMenu, QAction,
                             QFormLayout, QGraphicsScene, QGraphicsView, QGraphicsLineItem)
from PyQt5.QtWidgets import (QApplication, QMainWindow, QGraphicsScene, QGraphicsView, QGraphicsSimpleTextItem,
                             QGraphicsTextItem, QGraphicsEllipseItem, QGraphicsRectItem,
                             QGraphicsPixmapItem, QGraphicsPolygonItem, QGraphicsPathItem)
class TransDialog(QDialog):
    def __init__(self, view, parent=None):
        super(TransDialog, self).__init__(parent)

        self.view = view

        # 操作窗口标题
        self.setWindowTitle('视口变换操作')

        self.initUi()

    def initUi(self):
        fLayout = QFormLayout()

        # 旋转
        sdrRotate = QSlider(Qt.Horizontal)
        sdrRotate.setRange(-360, 360)
        sdrRotate.setPageStep(5)
        sdrRotate.setValue(0)
        sdrRotate.valueChanged.connect(self.onRotateValueChanged)

        fLayout.addRow('旋转', sdrRotate)

        # 缩放
        sdrScale = QSlider(Qt.Horizontal)
        sdrScale.setRange(0, 100)
        sdrScale.setPageStep(5)
        sdrScale.setValue(50)
        sdrScale.valueChanged.connect(self.onScaleValueChanged)
        fLayout.addRow('缩放', sdrScale)

        self.setLayout(fLayout)

    def onRotateValueChanged(self, value):
        # 是个累积效应，先对变化矩阵进行复位操作
        self.view.setTransform(QTransform())
        self.view.rotate(value)

    def onScaleValueChanged(self, value):
        s = 0.5 + value / 100.0
        # 是个累积效应，先对变化矩阵进行复位操作
        self.view.setTransform(QTransform())
        self.view.scale(s, s)