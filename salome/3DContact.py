# -*- coding: utf-8 -*-
# Detect and create 3D contact script
# License: LGPL v 2.1
# Autor: Lucio Gomez (psicofil@gmail.com)
# Version: 17/06/2017

## Import necesary Libreries
import sys
import salome
from platform import system
import subprocess
import tempfile

try:
    from PyQt4 import QtGui, QtCore
    from PyQt4.QtGui import *
    from PyQt4.QtCore import *
except:
    from PyQt5.QtWidgets import QWidget, QMessageBox
    from PyQt5 import QtCore, QtGui
    import PyQt5.QtCore as QtCore
    from PyQt5.QtWidgets import *
    from PyQt5.QtCore import Qt

import GEOM
from salome.geom import geomBuilder
import math

# Detect current study
theStudy = salome.myStudy
geompy = geomBuilder.New(theStudy)
salome.salome_init()


### START OF MACRO

class Conact3D(QWidget):
    def __init__(self):
        super(Conact3D, self).__init__()
        self.initUI()
        self.selectParts()

    def __del__(self):
        return

    def initUI(self):
        # 3D parts selected 
        self.l_parts = QLabel("3D Parts for contact analysis: ", self)
        self.tb_parts = QTextBrowser()
        self.pb_loadpart = QPushButton()
        self.pb_loadpart.setText("Load selected")
        # Adjust Gap
        self.l_gap = QLabel("Gap: ")
        self.sb_gap = QDoubleSpinBox()
        self.sb_gap.setDecimals(3)
        self.sb_gap.setValue(0.000)
        self.sb_gap.setSingleStep(0.001)
        # Common open_gmsh_options        
        self.cb_common = QCheckBox("  Compound Results", self)
        self.cb_common.setChecked(Qt.Checked)
        # Ok buttons:
        self.okbox = QDialogButtonBox(self)
        self.okbox.setOrientation(Qt.Horizontal)
        self.okbox.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
        # Layout:
        layout = QGridLayout()
        layout.addWidget(self.l_parts, 1, 0)
        layout.addWidget(self.tb_parts, 2, 0)
        layout.addWidget(self.pb_loadpart, 3, 0)
        layout.addWidget(self.l_gap, 4, 0)
        layout.addWidget(self.sb_gap, 5, 0)
        layout.addWidget(self.cb_common, 6, 0)
        layout.addWidget(self.okbox, 8, 0)
        self.setLayout(layout)
        # Connectors:
        self.okbox.accepted.connect(self.proceed)
        self.okbox.rejected.connect(self.cancel)
        self.pb_loadpart.clicked.connect(self.selectParts)

    def selectParts(self):
        try:
            selCount = salome.sg.SelectedCount()
            selobj = list()
            self.tb_parts.clear()
            for i in range(0, selCount):
                sel_i = salome.sg.getSelected(i)
                selobj_i = salome.myStudy.FindObjectID(sel_i).GetObject()
                selobj.append(selobj_i)
                self.tb_parts.append(selobj[i].GetName())   # push name to text browser
            self.parts = selobj                             # record obj list to property
        except:
            QMessageBox.critical(None, 'Error', "error in selected parts", QMessageBox.Abort)

    def proceed(self):
        gap = eval(str(self.sb_gap.text()))     # get gap
        interface_list = list()
        if self.cb_common.isChecked():
            Common = True
        else:
            Common = False
        # selobj = self.selectParts()
        try:
            selobj = self.parts
            selobj_i = selobj[0]
            selobj_j = selobj[1]
            selCount = len(selobj)
        except:
            QMessageBox.critical(None, 'Error', "Select 2 or more parts 3D first", QMessageBox.Abort)
        num_cont = 0
        for i in range(0, selCount):
            for j in range(1, selCount):
                if i != j and i < j:
                    try:
                        isOk, res1, res2 = geompy.FastIntersect(selobj[i], selobj[j], gap)
                    except:
                        QMessageBox.critical(None, 'Error 1', "Unexpected error", QMessageBox.Abort)
                    if isOk > 0:
                        N_C = len(res1)
                        N_C2 = len(res2)
                        # QMessageBox.information(None, "Informacion", str(res1), QMessageBox.Ok)
                        CONT = geompy.SubShapes(selobj[i], res1)
                        CONT2 = geompy.SubShapes(selobj[j], res2)
                        cont_sf_i = list()
                        cont_sf_j = list()
                        for h in range(0, N_C):
                            for k in range(0, N_C2):
                                common1 = geompy.MakeCommon(CONT[h], CONT2[k])
                                props = geompy.BasicProperties(common1)
                                area_com = props[1]
                                if Common == False:
                                    if area_com > 0.0:
                                        name_group_i = 'CZ_' + str(i) + str(j) + '_' + str(k)
                                        geompy.addToStudyInFather(selobj[i], CONT[h], name_group_i)
                                        name_group_j = 'CZ_' + str(j) + str(i) + '_' + str(h)
                                        geompy.addToStudyInFather(selobj[j], CONT2[k], name_group_j)
                                        num_cont += 1
                                if Common == True:
                                    if area_com > 0.0:
                                        cont_sf_i.append(CONT[h])
                                        cont_sf_j.append(CONT2[k])
                        if cont_sf_i not in interface_list:
                            comp_sf_i = geompy.MakeCompound(cont_sf_i)
                            name_group_i = 'CZ_' + str(i) + str(j)
                            geompy.addToStudyInFather(selobj[i], comp_sf_i, name_group_i)
                            interface_list.append(cont_sf_i)
                            num_cont += 1
                        if cont_sf_j not in interface_list:
                            comp_sf_j = geompy.MakeCompound(cont_sf_j)
                            name_group_j = 'CZ_' + str(j) + str(i)
                            geompy.addToStudyInFather(selobj[j], comp_sf_j, name_group_j)
                            interface_list.append(cont_sf_j)
                            num_cont += 1
        print(interface_list)
        # msg_cont = "Cantidad de pares de contactos detectados: " + str(num_cont)
        QMessageBox.information(None, "Informacion", str(interface_list), QMessageBox.Ok)
        if salome.sg.hasDesktop():
            salome.sg.updateObjBrowser()

    # cancel function
    def cancel(self):
        self.close()
        d.close()


d = QDockWidget()
d.setWidget(Conact3D())
d.setAttribute(Qt.WA_DeleteOnClose)
d.setWindowFlags(d.windowFlags() | QtCore.Qt.WindowStaysOnTopHint)
d.setWindowTitle(" 3D Contacts ")
d.setGeometry(600, 300, 400, 400)
d.show()

# END OF MACRO
