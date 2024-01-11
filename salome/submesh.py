#!/usr/bin/env python

###
### This file is generated automatically by SALOME v9.10.0 with dump python functionality
###

import sys
import salome

salome.salome_init()
import salome_notebook
notebook = salome_notebook.NoteBook()
sys.path.insert(0, r'C:/Users/DELL/Desktop/energy_container_platform/salome')

###
### GEOM component
###

import GEOM
from salome.geom import geomBuilder
import math
import SALOMEDS


geompy = geomBuilder.New()

O = geompy.MakeVertex(0, 0, 0)
OX = geompy.MakeVectorDXDYDZ(1, 0, 0)
OY = geompy.MakeVectorDXDYDZ(0, 1, 0)
OZ = geompy.MakeVectorDXDYDZ(0, 0, 1)
pack_simple5 = geompy.ImportSTEP("E:/project_simulation/energy_container/container_V1/pack_simple_V1/pack_simple5.stp", True, True)
[yelengban,fluid,duanban,guoliuyuanjian,cell] = geompy.ExtractShapes(pack_simple5, geompy.ShapeType["COMPOUND"], False)
[yelengban1] = geompy.ExtractShapes(yelengban, geompy.ShapeType["SOLID"], False)
[fluid1] = geompy.ExtractShapes(fluid, geompy.ShapeType["SOLID"], False)
[duanban1] = geompy.ExtractShapes(duanban, geompy.ShapeType["SOLID"], False)
[guoliuyuanjian1] = geompy.ExtractShapes(guoliuyuanjian, geompy.ShapeType["SOLID"], False)
[cell1,cell2] = geompy.ExtractShapes(cell, geompy.ShapeType["SOLID"], False)
[geomObj_1,geomObj_2,geomObj_3,geomObj_4,geomObj_5,geomObj_6,geomObj_7,geomObj_8,geomObj_9,geomObj_10,geomObj_11,geomObj_12,geomObj_13,geomObj_14,geomObj_15,geomObj_16,geomObj_17,geomObj_18,geomObj_19,geomObj_20,geomObj_21,geomObj_22,geomObj_23,geomObj_24,geomObj_25,geomObj_26,geomObj_27,geomObj_28,geomObj_29,geomObj_30,geomObj_31,geomObj_32,geomObj_33,geomObj_34,geomObj_35,geomObj_36,geomObj_37,geomObj_38,geomObj_39,geomObj_40,geomObj_41,geomObj_42,geomObj_43,geomObj_44,geomObj_45,geomObj_46,geomObj_47,geomObj_48,geomObj_49,geomObj_50,geomObj_51,geomObj_52,geomObj_53,geomObj_54,geomObj_55,geomObj_56,geomObj_57,geomObj_58,geomObj_59,geomObj_60,geomObj_61,geomObj_62,geomObj_63,geomObj_64,geomObj_65,geomObj_66,geomObj_67,geomObj_68,geomObj_69] = geompy.SubShapes(yelengban1, [79, 89, 99, 767, 109, 119, 129, 141, 151, 161, 171, 181, 188, 198, 797, 205, 800, 839, 212, 870, 219, 875, 226, 934, 231, 939, 236, 952, 246, 957, 252, 988, 259, 993, 264, 1028, 270, 275, 1033, 278, 1054, 283, 1106, 1111, 290, 1114, 297, 1119, 302, 309, 1122, 1127, 312, 315, 1132, 1135, 320, 1138, 1143, 1146, 1151, 1156, 1161, 1164, 1167, 1170, 1173, 1175, 1178])
[geomObj_70,geomObj_71] = geompy.SubShapes(yelengban1, [767, 320])
[geomObj_72,geomObj_73,geomObj_74,geomObj_75,geomObj_76] = geompy.SubShapes(yelengban1, [767, 415, 425, 467, 474])
[geomObj_77,geomObj_78,geomObj_79,geomObj_80,geomObj_81,geomObj_82,geomObj_83,geomObj_84,geomObj_85,geomObj_86,geomObj_87,geomObj_88,geomObj_89,geomObj_90,geomObj_91,geomObj_92,geomObj_93,geomObj_94,geomObj_95,geomObj_96,geomObj_97,geomObj_98,geomObj_99,geomObj_100,geomObj_101,geomObj_102,geomObj_103,geomObj_104,geomObj_105,geomObj_106,geomObj_107,geomObj_108,geomObj_109,geomObj_110,geomObj_111,geomObj_112,geomObj_113,geomObj_114,geomObj_115,geomObj_116,geomObj_117,geomObj_118,geomObj_119,geomObj_120,geomObj_121,geomObj_122,geomObj_123,geomObj_124,geomObj_125,geomObj_126,geomObj_127,geomObj_128,geomObj_129,geomObj_130,geomObj_131,geomObj_132,geomObj_133,geomObj_134,geomObj_135,geomObj_136,geomObj_137,geomObj_138,geomObj_139,geomObj_140,geomObj_141,geomObj_142,geomObj_143,geomObj_144,geomObj_145,geomObj_146] = geompy.SubShapes(fluid1, [3, 13, 22, 32, 42, 54, 64, 74, 84, 94, 104, 114, 124, 141, 151, 161, 168, 175, 180, 183, 188, 193, 202, 209, 216, 220, 224, 227, 230, 237, 244, 247, 251, 255, 257, 260, 267, 274, 282, 287, 293, 298, 303, 310, 317, 328, 331, 338, 345, 355, 357, 364, 371, 375, 382, 385, 390, 395, 399, 401, 406, 411, 414, 417, 420, 422, 425, 430, 433, 438])
[geomObj_147,geomObj_148,geomObj_149,geomObj_150,geomObj_151,geomObj_152,geomObj_153,geomObj_154,geomObj_155,geomObj_156,geomObj_157,geomObj_158,geomObj_159,geomObj_160,geomObj_161,geomObj_162,geomObj_163,geomObj_164,geomObj_165,geomObj_166,geomObj_167,geomObj_168,geomObj_169,geomObj_170,geomObj_171] = geompy.SubShapes(duanban1, [1203, 1871, 1878, 1921, 1955, 1963, 2066, 2081, 2094, 2111, 2115, 2118, 2135, 2151, 2158, 2169, 2173, 2180, 2186, 2189, 2194, 2201, 2207, 2210, 2218])
[geomObj_172,geomObj_173,geomObj_174] = geompy.SubShapes(guoliuyuanjian1, [20, 27, 33])
[geomObj_175,geomObj_176,geomObj_177] = geompy.SubShapes(guoliuyuanjian1, [20, 27, 31])
[geomObj_178,geomObj_179,geomObj_180,geomObj_181,geomObj_182] = geompy.SubShapes(cell1, [3, 38, 45, 49, 51])
[geomObj_183,geomObj_184,geomObj_185] = geompy.SubShapes(cell1, [65, 70, 73])
[geomObj_186,geomObj_187,geomObj_188,geomObj_189,geomObj_190] = geompy.SubShapes(cell1, [3, 13, 38, 45, 49])
[geomObj_191,geomObj_192,geomObj_193,geomObj_194,geomObj_195] = geompy.SubShapes(cell2, [3, 38, 45, 49, 95])
[geomObj_196,geomObj_197,geomObj_198] = geompy.SubShapes(cell2, [3, 38, 95])
[geomObj_199,geomObj_200,geomObj_201] = geompy.SubShapes(cell2, [80, 85, 93])
[geomObj_202,geomObj_203,geomObj_204,geomObj_205,geomObj_206] = geompy.SubShapes(cell2, [3, 13, 38, 45, 49])
inlet = geompy.CreateGroup(pack_simple5, geompy.ShapeType["FACE"])
geompy.UnionIDs(inlet, [1534])
outlet = geompy.CreateGroup(pack_simple5, geompy.ShapeType["FACE"])
geompy.UnionIDs(outlet, [1429])

###
### SMESH component
###

import  SMESH, SALOMEDS
from salome.smesh import smeshBuilder

smesh = smeshBuilder.New()
#smesh.SetEnablePublish( False ) # Set to False to avoid publish in study if not needed or in some particular situations:
                                 # multiples meshes built in parallel, complex and numerous mesh edition (performance)

Mesh_All = smesh.Mesh(pack_simple5,'Mesh_All')
yelengban1_1 = Mesh_All.GroupOnGeom(yelengban1,'yelengban1',SMESH.VOLUME)
fluid1_1 = Mesh_All.GroupOnGeom(fluid1,'fluid1',SMESH.VOLUME)
duanban1_1 = Mesh_All.GroupOnGeom(duanban1,'duanban1',SMESH.VOLUME)
guoliuyuanjian1_1 = Mesh_All.GroupOnGeom(guoliuyuanjian1,'guoliuyuanjian1',SMESH.VOLUME)
cell1_1 = Mesh_All.GroupOnGeom(cell1,'cell1',SMESH.VOLUME)
cell2_1 = Mesh_All.GroupOnGeom(cell2,'cell2',SMESH.VOLUME)
inlet_1 = Mesh_All.GroupOnGeom(inlet,'inlet',SMESH.FACE)
outlet_1 = Mesh_All.GroupOnGeom(outlet,'outlet',SMESH.FACE)
interface_yelengban1_fluid1_1 = Mesh_All.GroupOnGeom(interface_yelengban1_fluid1,'interface_yelengban1_fluid1',SMESH.FACE)
interface_fluid1_yelengban1_1 = Mesh_All.GroupOnGeom(interface_fluid1_yelengban1,'interface_fluid1_yelengban1',SMESH.FACE)
interface_yelengban1_cell1_1 = Mesh_All.GroupOnGeom(interface_yelengban1_cell1,'interface_yelengban1_cell1',SMESH.FACE)
interface_cell1_yelengban1_1 = Mesh_All.GroupOnGeom(interface_cell1_yelengban1,'interface_cell1_yelengban1',SMESH.FACE)
interface_cell2_yelengban1_1 = Mesh_All.GroupOnGeom(interface_cell2_yelengban1,'interface_cell2_yelengban1',SMESH.FACE)
interface_duanban1_cell2_1 = Mesh_All.GroupOnGeom(interface_duanban1_cell2,'interface_duanban1_cell2',SMESH.FACE)
interface_cell2_duanban1_1 = Mesh_All.GroupOnGeom(interface_cell2_duanban1,'interface_cell2_duanban1',SMESH.FACE)
interface_guoliuyuanjian1_cell1_1 = Mesh_All.GroupOnGeom(interface_guoliuyuanjian1_cell1,'interface_guoliuyuanjian1_cell1',SMESH.FACE)
interface_cell1_guoliuyuanjian1_1 = Mesh_All.GroupOnGeom(interface_cell1_guoliuyuanjian1,'interface_cell1_guoliuyuanjian1',SMESH.FACE)
interface_cell2_guoliuyuanjian1_1 = Mesh_All.GroupOnGeom(interface_cell2_guoliuyuanjian1,'interface_cell2_guoliuyuanjian1',SMESH.FACE)
interface_cell1_cell2_1 = Mesh_All.GroupOnGeom(interface_cell1_cell2,'interface_cell1_cell2',SMESH.FACE)
interface_cell2_cell1_1 = Mesh_All.GroupOnGeom(interface_cell2_cell1,'interface_cell2_cell1',SMESH.FACE)


NETGEN_1D_2D = Mesh_All.Triangle(algo=smeshBuilder.NETGEN_1D2D, geom=cell1)
NETGEN_3D = Mesh_All.Tetrahedron(geom=cell1)
Sub_mesh_1 = NETGEN_1D_2D.GetSubMesh()


## Set names of Mesh objects
smesh.SetName(NETGEN_1D_2D.GetAlgorithm(), 'NETGEN 1D-2D')
smesh.SetName(interface_duanban1_cell2_1, 'interface_duanban1_cell2')
smesh.SetName(interface_cell2_duanban1_1, 'interface_cell2_duanban1')
smesh.SetName(NETGEN_3D.GetAlgorithm(), 'NETGEN 3D')
smesh.SetName(inlet_1, 'inlet')
smesh.SetName(outlet_1, 'outlet')
smesh.SetName(interface_yelengban1_fluid1_1, 'interface_yelengban1_fluid1')
smesh.SetName(interface_fluid1_yelengban1_1, 'interface_fluid1_yelengban1')
smesh.SetName(interface_yelengban1_cell1_1, 'interface_yelengban1_cell1')
smesh.SetName(interface_cell1_yelengban1_1, 'interface_cell1_yelengban1')
smesh.SetName(interface_cell2_yelengban1_1, 'interface_cell2_yelengban1')
smesh.SetName(Mesh_All.GetMesh(), 'Mesh_All')
smesh.SetName(interface_cell1_guoliuyuanjian1_1, 'interface_cell1_guoliuyuanjian1')
smesh.SetName(interface_guoliuyuanjian1_cell1_1, 'interface_guoliuyuanjian1_cell1')
smesh.SetName(cell2_1, 'cell2')
smesh.SetName(interface_cell1_cell2_1, 'interface_cell1_cell2')
smesh.SetName(cell1_1, 'cell1')
smesh.SetName(interface_cell2_guoliuyuanjian1_1, 'interface_cell2_guoliuyuanjian1')
smesh.SetName(guoliuyuanjian1_1, 'guoliuyuanjian1')
smesh.SetName(duanban1_1, 'duanban1')
smesh.SetName(interface_cell2_cell1_1, 'interface_cell2_cell1')
smesh.SetName(fluid1_1, 'fluid1')
smesh.SetName(yelengban1_1, 'yelengban1')
smesh.SetName(Sub_mesh_1, 'Sub-mesh_1')


if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser()
