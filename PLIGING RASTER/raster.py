import os 
import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from qgis.core import *
from qgis.gui import *
from qgis.utils import *

from .interfaz import Ui_MainWindow

class interfaz (QMainWindow):
    def __init__ (self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn4.clicked.connect(self.cerrar)

    def cerrar(self):
        self.close()
    
    def nombreCmb(self):
        layers = QgsProject.instance().mapLayers().values()
        for layer in layers:
            if layer.type() == QgsMapLayer.VectorLayer and layer.geometryType() == QgsWkbTypes.PolygonGeometry:
                nomVLayer = layer.name()
                self.ui.lbl1.addItem(nomVLayer)
            if layer.type()==QgsRasterLayer.RasterLayer:
                nomRLayer = layer.name()
                self.ui.lbl1.addItem(nomRLayer)
         