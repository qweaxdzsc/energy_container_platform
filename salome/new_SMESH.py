#!/usr/bin/env python

###
### This file is generated automatically by SALOME v9.10.0 with dump python functionality (SMESH component)
###

import salome, SMESH, SALOMEDS
from salome.smesh import smeshBuilder

## import GEOM dump file ## 
import string, os, sys, re, inspect

thisFile = inspect.getfile(inspect.currentframe())
thisModule = os.path.splitext(os.path.basename(thisFile))[0]
sys.path.insert(0, os.path.dirname(thisFile))
exec("from " + re.sub("SMESH$", "GEOM", thisModule) + " import *")


def RebuildData():
    smesh = smeshBuilder.New()
    # smesh.SetEnablePublish( False ) # Set to False to avoid publish in study if not needed or in some particular situations:
    # multiples meshes built in parallel, complex and numerous mesh edition (performance)

    aFilterManager = smesh.CreateFilterManager()
    Mesh_1 = smesh.Mesh(pack_simple5, 'Mesh_1')
    duanban_1 = Mesh_1.GroupOnGeom(duanban, 'duanban', SMESH.VOLUME)
    yelengban_1 = Mesh_1.GroupOnGeom(yelengban, 'yelengban', SMESH.VOLUME)
    fluid_1 = Mesh_1.GroupOnGeom(fluid, 'fluid', SMESH.VOLUME)
    guoliuyuanjian_1 = Mesh_1.GroupOnGeom(guoliuyuanjian, 'guoliuyuanjian', SMESH.VOLUME)
    inlet_1 = Mesh_1.GroupOnGeom(inlet, 'inlet', SMESH.FACE)
    outlet_1 = Mesh_1.GroupOnGeom(outlet, 'outlet', SMESH.FACE)
    interface_cell_duanban_1 = Mesh_1.GroupOnGeom(interface_cell_duanban, 'interface_cell_duanban', SMESH.FACE)
    interface_cell1_cell2_1 = Mesh_1.GroupOnGeom(interface_cell1_cell2, 'interface_cell1_cell2', SMESH.FACE)
    interface_bar1_cell_1 = Mesh_1.GroupOnGeom(interface_bar1_cell, 'interface_bar1_cell', SMESH.FACE)
    interface_cell1_bar1_1 = Mesh_1.GroupOnGeom(interface_cell1_bar1, 'interface_cell1_bar1', SMESH.FACE)
    interface_cell2_bar1_1 = Mesh_1.GroupOnGeom(interface_cell2_bar1, 'interface_cell2_bar1', SMESH.FACE)
    interface_plate_cell_1 = Mesh_1.GroupOnGeom(interface_plate_cell, 'interface_plate_cell', SMESH.FACE)
    interface_cell1_plate_1 = Mesh_1.GroupOnGeom(interface_cell1_plate, 'interface_cell1_plate', SMESH.FACE)
    interface_cell2_plate_1 = Mesh_1.GroupOnGeom(interface_cell2_plate, 'interface_cell2_plate', SMESH.FACE)
    Cartesian_3D = Mesh_1.BodyFitted(geom=cell)
    Body_Fitting_Parameters_1 = Cartesian_3D.SetGrid([['10'], [0, 1]], [['10'], [0, 1]], [['10'], [0, 1]], 4, 1)
    [duanban_1, yelengban_1, smeshObj_1, fluid_1, guoliuyuanjian_1, smeshObj_2, smeshObj_3, smeshObj_4, smeshObj_5,
     inlet_1, outlet_1, interface_cell_duanban_1, interface_cell1_cell2_1, smeshObj_6, interface_bar1_cell_1,
     interface_cell1_bar1_1, interface_cell2_bar1_1, interface_plate_cell_1, interface_cell1_plate_1,
     interface_cell2_plate_1] = Mesh_1.GetGroups()
    Body_Fitting_Parameters_1.SetSizeThreshold(2)
    Body_Fitting_Parameters_1.SetToAddEdges(1)
    Body_Fitting_Parameters_1.SetGridSpacing(['10'], [0, 1], 0)
    Body_Fitting_Parameters_1.SetGridSpacing(['10'], [0, 1], 1)
    Body_Fitting_Parameters_1.SetGridSpacing(['10'], [0, 1], 2)
    [duanban_1, yelengban_1, smeshObj_1, fluid_1, guoliuyuanjian_1, smeshObj_2, smeshObj_3, smeshObj_4, smeshObj_5,
     inlet_1, outlet_1, interface_cell_duanban_1, interface_cell1_cell2_1, smeshObj_6, interface_bar1_cell_1,
     interface_cell1_bar1_1, interface_cell2_bar1_1, interface_plate_cell_1, interface_cell1_plate_1,
     interface_cell2_plate_1] = Mesh_1.GetGroups()
    Body_Fitting_Parameters_1.SetSizeThreshold(1.01)
    Body_Fitting_Parameters_1.SetToAddEdges(1)
    Body_Fitting_Parameters_1.SetGridSpacing(['1'], [0, 1], 0)
    Body_Fitting_Parameters_1.SetGridSpacing(['1'], [0, 1], 1)
    Body_Fitting_Parameters_1.SetGridSpacing(['1'], [0, 1], 2)
    [duanban_1, yelengban_1, smeshObj_1, fluid_1, guoliuyuanjian_1, smeshObj_2, smeshObj_3, smeshObj_4, smeshObj_5,
     inlet_1, outlet_1, interface_cell_duanban_1, interface_cell1_cell2_1, smeshObj_6, interface_bar1_cell_1,
     interface_cell1_bar1_1, interface_cell2_bar1_1, interface_plate_cell_1, interface_cell1_plate_1,
     interface_cell2_plate_1] = Mesh_1.GetGroups()
    Body_Fitting_Parameters_1.SetSizeThreshold(1.01)
    Body_Fitting_Parameters_1.SetToAddEdges(1)
    Body_Fitting_Parameters_1.SetGrid([0, 1, 2, 3, 5], 0)
    Body_Fitting_Parameters_1.SetGrid([0, 1, 2, 3, 4, 5], 1)
    Body_Fitting_Parameters_1.SetGrid([0, 1, 11], 2)
    [duanban_1, yelengban_1, smeshObj_1, fluid_1, guoliuyuanjian_1, smeshObj_2, smeshObj_3, smeshObj_4, smeshObj_5,
     inlet_1, outlet_1, interface_cell_duanban_1, interface_cell1_cell2_1, smeshObj_6, interface_bar1_cell_1,
     interface_cell1_bar1_1, interface_cell2_bar1_1, interface_plate_cell_1, interface_cell1_plate_1,
     interface_cell2_plate_1] = Mesh_1.GetGroups()
    Body_Fitting_Parameters_1.SetSizeThreshold(1.01)
    Body_Fitting_Parameters_1.SetToAddEdges(1)
    Body_Fitting_Parameters_1.SetGridSpacing(['10'], [0, 1], 0)
    Body_Fitting_Parameters_1.SetGridSpacing(['10'], [0, 1], 1)
    Body_Fitting_Parameters_1.SetGridSpacing(['10'], [0, 1], 2)
    [duanban_1, yelengban_1, smeshObj_1, fluid_1, guoliuyuanjian_1, smeshObj_2, smeshObj_3, smeshObj_4, smeshObj_5,
     inlet_1, outlet_1, interface_cell_duanban_1, interface_cell1_cell2_1, smeshObj_6, interface_bar1_cell_1,
     interface_cell1_bar1_1, interface_cell2_bar1_1, interface_plate_cell_1, interface_cell1_plate_1,
     interface_cell2_plate_1] = Mesh_1.GetGroups()
    Body_Fitting_Parameters_1.SetSizeThreshold(1.01)
    Body_Fitting_Parameters_1.SetToAddEdges(0)
    Body_Fitting_Parameters_1.SetGridSpacing(['10'], [0, 1], 0)
    Body_Fitting_Parameters_1.SetGridSpacing(['10'], [0, 1], 1)
    Body_Fitting_Parameters_1.SetGridSpacing(['10'], [0, 1], 2)
    [duanban_1, yelengban_1, smeshObj_1, fluid_1, guoliuyuanjian_1, smeshObj_2, smeshObj_3, smeshObj_4, smeshObj_5,
     inlet_1, outlet_1, interface_cell_duanban_1, interface_cell1_cell2_1, smeshObj_6, interface_bar1_cell_1,
     interface_cell1_bar1_1, interface_cell2_bar1_1, interface_plate_cell_1, interface_cell1_plate_1,
     interface_cell2_plate_1] = Mesh_1.GetGroups()
    Body_Fitting_Parameters_1.SetSizeThreshold(1.01)
    Body_Fitting_Parameters_1.SetToAddEdges(1)
    Body_Fitting_Parameters_1.SetToUseThresholdForInternalFaces(1)
    Body_Fitting_Parameters_1.SetGridSpacing(['10'], [0, 1], 0)
    Body_Fitting_Parameters_1.SetGridSpacing(['10'], [0, 1], 1)
    Body_Fitting_Parameters_1.SetGridSpacing(['10'], [0, 1], 2)
    [duanban_1, yelengban_1, smeshObj_1, fluid_1, guoliuyuanjian_1, smeshObj_2, smeshObj_3, smeshObj_4, smeshObj_5,
     inlet_1, outlet_1, interface_cell_duanban_1, interface_cell1_cell2_1, smeshObj_6, interface_bar1_cell_1,
     interface_cell1_bar1_1, interface_cell2_bar1_1, interface_plate_cell_1, interface_cell1_plate_1,
     interface_cell2_plate_1] = Mesh_1.GetGroups()
    Body_Fitting_Parameters_1.SetSizeThreshold(1.01)
    Body_Fitting_Parameters_1.SetToAddEdges(1)
    Body_Fitting_Parameters_1.SetGridSpacing(['5'], [0, 1], 0)
    Body_Fitting_Parameters_1.SetGridSpacing(['5'], [0, 1], 1)
    Body_Fitting_Parameters_1.SetGridSpacing(['5'], [0, 1], 2)
    [duanban_1, yelengban_1, smeshObj_1, fluid_1, guoliuyuanjian_1, smeshObj_2, smeshObj_3, smeshObj_4, smeshObj_5,
     inlet_1, outlet_1, interface_cell_duanban_1, interface_cell1_cell2_1, smeshObj_6, interface_bar1_cell_1,
     interface_cell1_bar1_1, interface_cell2_bar1_1, interface_plate_cell_1, interface_cell1_plate_1,
     interface_cell2_plate_1] = Mesh_1.GetGroups()
    Body_Fitting_Parameters_1.SetSizeThreshold(4)
    Body_Fitting_Parameters_1.SetToAddEdges(1)
    Body_Fitting_Parameters_1.SetGridSpacing(['5'], [0, 1], 0)
    Body_Fitting_Parameters_1.SetGridSpacing(['5'], [0, 1], 1)
    Body_Fitting_Parameters_1.SetGridSpacing(['5'], [0, 1], 2)
    [duanban_1, yelengban_1, smeshObj_1, fluid_1, guoliuyuanjian_1, smeshObj_2, smeshObj_3, smeshObj_4, smeshObj_5,
     inlet_1, outlet_1, interface_cell_duanban_1, interface_cell1_cell2_1, smeshObj_6, interface_bar1_cell_1,
     interface_cell1_bar1_1, interface_cell2_bar1_1, interface_plate_cell_1, interface_cell1_plate_1,
     interface_cell2_plate_1] = Mesh_1.GetGroups()
    Body_Fitting_Parameters_1.SetSizeThreshold(8)
    Body_Fitting_Parameters_1.SetToAddEdges(1)
    Body_Fitting_Parameters_1.SetGridSpacing(['5'], [0, 1], 0)
    Body_Fitting_Parameters_1.SetGridSpacing(['5'], [0, 1], 1)
    Body_Fitting_Parameters_1.SetGridSpacing(['5'], [0, 1], 2)
    [duanban_1, yelengban_1, smeshObj_1, fluid_1, guoliuyuanjian_1, smeshObj_2, smeshObj_3, smeshObj_4, smeshObj_5,
     inlet_1, outlet_1, interface_cell_duanban_1, interface_cell1_cell2_1, smeshObj_6, interface_bar1_cell_1,
     interface_cell1_bar1_1, interface_cell2_bar1_1, interface_plate_cell_1, interface_cell1_plate_1,
     interface_cell2_plate_1] = Mesh_1.GetGroups()
    Body_Fitting_Parameters_1.SetSizeThreshold(8)
    Body_Fitting_Parameters_1.SetToAddEdges(1)
    Body_Fitting_Parameters_1.SetToCreateFaces(1)
    Body_Fitting_Parameters_1.SetToConsiderInternalFaces(1)
    Body_Fitting_Parameters_1.SetGridSpacing(['5'], [0, 1], 0)
    Body_Fitting_Parameters_1.SetGridSpacing(['5'], [0, 1], 1)
    Body_Fitting_Parameters_1.SetGridSpacing(['5'], [0, 1], 2)
    [duanban_1, yelengban_1, smeshObj_1, fluid_1, guoliuyuanjian_1, smeshObj_2, smeshObj_3, smeshObj_4, smeshObj_5,
     inlet_1, outlet_1, interface_cell_duanban_1, interface_cell1_cell2_1, smeshObj_6, interface_bar1_cell_1,
     interface_cell1_bar1_1, interface_cell2_bar1_1, interface_plate_cell_1, interface_cell1_plate_1,
     interface_cell2_plate_1] = Mesh_1.GetGroups()
    Body_Fitting_Parameters_1.SetSizeThreshold(8)
    Body_Fitting_Parameters_1.SetToAddEdges(1)
    Body_Fitting_Parameters_1.SetGridSpacing(['10'], [0, 1], 0)
    Body_Fitting_Parameters_1.SetGridSpacing(['10'], [0, 1], 1)
    Body_Fitting_Parameters_1.SetGridSpacing(['20'], [0, 1], 2)
    [duanban_1, yelengban_1, smeshObj_1, fluid_1, guoliuyuanjian_1, smeshObj_2, smeshObj_3, smeshObj_4, smeshObj_5,
     inlet_1, outlet_1, interface_cell_duanban_1, interface_cell1_cell2_1, smeshObj_6, interface_bar1_cell_1,
     interface_cell1_bar1_1, interface_cell2_bar1_1, interface_plate_cell_1, interface_cell1_plate_1,
     interface_cell2_plate_1] = Mesh_1.GetGroups()
    Body_Fitting_Parameters_1.SetSizeThreshold(8)
    Body_Fitting_Parameters_1.SetToAddEdges(1)
    Body_Fitting_Parameters_1.SetGridSpacing(['15'], [0, 1], 0)
    Body_Fitting_Parameters_1.SetGridSpacing(['15'], [0, 1], 1)
    Body_Fitting_Parameters_1.SetGridSpacing(['25'], [0, 1], 2)
    [duanban_1, yelengban_1, smeshObj_1, fluid_1, guoliuyuanjian_1, smeshObj_2, smeshObj_3, smeshObj_4, smeshObj_5,
     inlet_1, outlet_1, interface_cell_duanban_1, interface_cell1_cell2_1, smeshObj_6, interface_bar1_cell_1,
     interface_cell1_bar1_1, interface_cell2_bar1_1, interface_plate_cell_1, interface_cell1_plate_1,
     interface_cell2_plate_1] = Mesh_1.GetGroups()
    Body_Fitting_Parameters_1.SetSizeThreshold(6)
    Body_Fitting_Parameters_1.SetToAddEdges(1)
    Body_Fitting_Parameters_1.SetGridSpacing(['10'], [0, 1], 0)
    Body_Fitting_Parameters_1.SetGridSpacing(['15'], [0, 1], 1)
    Body_Fitting_Parameters_1.SetGridSpacing(['25'], [0, 1], 2)
    [duanban_1, yelengban_1, smeshObj_1, fluid_1, guoliuyuanjian_1, smeshObj_2, smeshObj_3, smeshObj_4, smeshObj_5,
     inlet_1, outlet_1, interface_cell_duanban_1, interface_cell1_cell2_1, smeshObj_6, interface_bar1_cell_1,
     interface_cell1_bar1_1, interface_cell2_bar1_1, interface_plate_cell_1, interface_cell1_plate_1,
     interface_cell2_plate_1] = Mesh_1.GetGroups()
    Body_Fitting_Parameters_1.SetSizeThreshold(4)
    Body_Fitting_Parameters_1.SetToAddEdges(1)
    Body_Fitting_Parameters_1.SetGridSpacing(['15'], [0, 1], 0)
    Body_Fitting_Parameters_1.SetGridSpacing(['10'], [0, 1], 1)
    Body_Fitting_Parameters_1.SetGridSpacing(['25'], [0, 1], 2)
    [duanban_1, yelengban_1, smeshObj_1, fluid_1, guoliuyuanjian_1, smeshObj_2, smeshObj_3, smeshObj_4, smeshObj_5,
     inlet_1, outlet_1, interface_cell_duanban_1, interface_cell1_cell2_1, smeshObj_6, interface_bar1_cell_1,
     interface_cell1_bar1_1, interface_cell2_bar1_1, interface_plate_cell_1, interface_cell1_plate_1,
     interface_cell2_plate_1] = Mesh_1.GetGroups()
    Cartesian_3D_1 = Mesh_1.BodyFitted(geom=guoliuyuanjian)
    yuanjian_para = Cartesian_3D_1.SetGrid([['20'], [0, 1]], [['20'], [0, 1]], [['25'], [0, 1]], 4, 1)
    # Mesh_1.GetMesh().RemoveSubMesh( smeshObj_7 ) ### smeshObj_7 has not been yet created
    mesh_yuanjian = Cartesian_3D_1.GetSubMesh()
    Cartesian_3D_2 = Mesh_1.BodyFitted(geom=guoliuyuanjian)
    status = Mesh_1.AddHypothesis(yuanjian_para, guoliuyuanjian)
    [duanban_1, yelengban_1, smeshObj_1, fluid_1, guoliuyuanjian_1, smeshObj_2, smeshObj_3, smeshObj_4, smeshObj_5,
     inlet_1, outlet_1, interface_cell_duanban_1, interface_cell1_cell2_1, smeshObj_6, interface_bar1_cell_1,
     interface_cell1_bar1_1, interface_cell2_bar1_1, interface_plate_cell_1, interface_cell1_plate_1,
     interface_cell2_plate_1] = Mesh_1.GetGroups()
    yuanjian_para.SetSizeThreshold(4)
    yuanjian_para.SetToAddEdges(1)
    yuanjian_para.SetGridSpacing(['15'], [0, 1], 0)
    yuanjian_para.SetGridSpacing(['15'], [0, 1], 1)
    yuanjian_para.SetGridSpacing(['10'], [0, 1], 2)
    [duanban_1, yelengban_1, smeshObj_1, fluid_1, guoliuyuanjian_1, smeshObj_2, smeshObj_3, smeshObj_4, smeshObj_5,
     inlet_1, outlet_1, interface_cell_duanban_1, interface_cell1_cell2_1, smeshObj_6, interface_bar1_cell_1,
     interface_cell1_bar1_1, interface_cell2_bar1_1, interface_plate_cell_1, interface_cell1_plate_1,
     interface_cell2_plate_1] = Mesh_1.GetGroups()
    yuanjian_para.SetSizeThreshold(4)
    yuanjian_para.SetToAddEdges(1)
    yuanjian_para.SetGridSpacing(['10'], [0, 1], 0)
    yuanjian_para.SetGridSpacing(['10'], [0, 1], 1)
    yuanjian_para.SetGridSpacing(['5'], [0, 1], 2)
    [duanban_1, yelengban_1, smeshObj_1, fluid_1, guoliuyuanjian_1, smeshObj_2, smeshObj_3, smeshObj_4, smeshObj_5,
     inlet_1, outlet_1, interface_cell_duanban_1, interface_cell1_cell2_1, smeshObj_6, interface_bar1_cell_1,
     interface_cell1_bar1_1, interface_cell2_bar1_1, interface_plate_cell_1, interface_cell1_plate_1,
     interface_cell2_plate_1] = Mesh_1.GetGroups()
    yuanjian_para.SetSizeThreshold(4)
    yuanjian_para.SetToAddEdges(1)
    yuanjian_para.SetGridSpacing(['15'], [0, 1], 0)
    yuanjian_para.SetGridSpacing(['15'], [0, 1], 1)
    yuanjian_para.SetGridSpacing(['5'], [0, 1], 2)
    [duanban_1, yelengban_1, smeshObj_1, fluid_1, guoliuyuanjian_1, smeshObj_2, smeshObj_3, smeshObj_4, smeshObj_5,
     inlet_1, outlet_1, interface_cell_duanban_1, interface_cell1_cell2_1, smeshObj_6, interface_bar1_cell_1,
     interface_cell1_bar1_1, interface_cell2_bar1_1, interface_plate_cell_1, interface_cell1_plate_1,
     interface_cell2_plate_1] = Mesh_1.GetGroups()
    NETGEN_1D_2D_3D = Mesh_1.Tetrahedron(algo=smeshBuilder.NETGEN_1D2D3D, geom=duanban)
    NETGEN_3D_Parameters_1 = NETGEN_1D_2D_3D.Parameters()
    NETGEN_3D_Parameters_1.SetSecondOrder(0)
    NETGEN_3D_Parameters_1.SetOptimize(1)
    NETGEN_3D_Parameters_1.SetFineness(5)
    NETGEN_3D_Parameters_1.SetNbSegPerEdge(1)
    NETGEN_3D_Parameters_1.SetNbSegPerRadius(4)
    NETGEN_3D_Parameters_1.SetChordalError(-1)
    NETGEN_3D_Parameters_1.SetChordalErrorEnabled(0)
    NETGEN_3D_Parameters_1.SetUseSurfaceCurvature(1)
    NETGEN_3D_Parameters_1.SetFuseEdges(1)
    NETGEN_3D_Parameters_1.SetQuadAllowed(0)
    [duanban_1, yelengban_1, smeshObj_1, fluid_1, guoliuyuanjian_1, smeshObj_2, smeshObj_3, smeshObj_4, smeshObj_5,
     inlet_1, outlet_1, interface_cell_duanban_1, interface_cell1_cell2_1, smeshObj_6, interface_bar1_cell_1,
     interface_cell1_bar1_1, interface_cell2_bar1_1, interface_plate_cell_1, interface_cell1_plate_1,
     interface_cell2_plate_1] = Mesh_1.GetGroups()
    NETGEN_3D_Parameters_1.SetGrowthRate(0.25)
    [duanban_1, yelengban_1, smeshObj_1, fluid_1, guoliuyuanjian_1, smeshObj_2, smeshObj_3, smeshObj_4, smeshObj_5,
     inlet_1, outlet_1, interface_cell_duanban_1, interface_cell1_cell2_1, smeshObj_6, interface_bar1_cell_1,
     interface_cell1_bar1_1, interface_cell2_bar1_1, interface_plate_cell_1, interface_cell1_plate_1,
     interface_cell2_plate_1] = Mesh_1.GetGroups()
    NETGEN_3D_Parameters_1.SetMaxSize(10)
    NETGEN_3D_Parameters_1.SetMinSize(5)
    NETGEN_3D_Parameters_1.SetCheckChartBoundary(96)
    isDone = Mesh_1.Compute()
    [duanban_1, yelengban_1, smeshObj_1, fluid_1, guoliuyuanjian_1, smeshObj_2, smeshObj_3, smeshObj_4, smeshObj_5,
     inlet_1, outlet_1, interface_cell_duanban_1, interface_cell1_cell2_1, smeshObj_6, interface_bar1_cell_1,
     interface_cell1_bar1_1, interface_cell2_bar1_1, interface_plate_cell_1, interface_cell1_plate_1,
     interface_cell2_plate_1] = Mesh_1.GetGroups()
    mesh_editor_0 = Mesh_1.GetMeshEditor()
    [duanban_1, yelengban_1, smeshObj_1, fluid_1, guoliuyuanjian_1, smeshObj_2, smeshObj_3, smeshObj_4, smeshObj_5,
     inlet_1, outlet_1, interface_cell_duanban_1, interface_cell1_cell2_1, smeshObj_6, interface_bar1_cell_1,
     interface_cell1_bar1_1, interface_cell2_bar1_1, interface_plate_cell_1, interface_cell1_plate_1,
     interface_cell2_plate_1] = Mesh_1.GetGroups()
    NETGEN_3D_Parameters_1.SetGrowthRate(0.15)
    NETGEN_3D_Parameters_1.SetCheckChartBoundary(96)
    [duanban_1, yelengban_1, smeshObj_1, fluid_1, guoliuyuanjian_1, smeshObj_2, smeshObj_3, smeshObj_4, smeshObj_5,
     inlet_1, outlet_1, interface_cell_duanban_1, interface_cell1_cell2_1, smeshObj_6, interface_bar1_cell_1,
     interface_cell1_bar1_1, interface_cell2_bar1_1, interface_plate_cell_1, interface_cell1_plate_1,
     interface_cell2_plate_1] = Mesh_1.GetGroups()
    status = Mesh_1.RemoveHypothesis(NETGEN_1D_2D_3D, duanban)
    NETGEN_1D_2D = Mesh_1.Triangle(algo=smeshBuilder.NETGEN_1D2D, geom=duanban)
    NETGEN_2D_Parameters_1 = NETGEN_1D_2D.Parameters()
    NETGEN_2D_Parameters_1.SetMaxSize(8)
    NETGEN_2D_Parameters_1.SetMinSize(4)
    NETGEN_2D_Parameters_1.SetSecondOrder(0)
    NETGEN_2D_Parameters_1.SetOptimize(1)
    NETGEN_2D_Parameters_1.SetFineness(5)
    NETGEN_2D_Parameters_1.SetGrowthRate(0.1)
    NETGEN_2D_Parameters_1.SetNbSegPerEdge(1)
    NETGEN_2D_Parameters_1.SetNbSegPerRadius(4)
    NETGEN_2D_Parameters_1.SetChordalError(-1)
    NETGEN_2D_Parameters_1.SetChordalErrorEnabled(0)
    NETGEN_2D_Parameters_1.SetUseSurfaceCurvature(1)
    NETGEN_2D_Parameters_1.SetFuseEdges(1)
    NETGEN_2D_Parameters_1.SetUseDelauney(0)
    NETGEN_2D_Parameters_1.SetQuadAllowed(0)
    NETGEN_2D_Parameters_1.SetWorstElemMeasure(159)
    NETGEN_2D_Parameters_1.SetCheckChartBoundary(96)
    status = Mesh_1.RemoveHypothesis(NETGEN_3D_Parameters_1, duanban)
    isDone = Mesh_1.Compute()
    [duanban_1, yelengban_1, smeshObj_1, fluid_1, guoliuyuanjian_1, smeshObj_2, smeshObj_3, smeshObj_4, smeshObj_5,
     inlet_1, outlet_1, interface_cell_duanban_1, interface_cell1_cell2_1, smeshObj_6, interface_bar1_cell_1,
     interface_cell1_bar1_1, interface_cell2_bar1_1, interface_plate_cell_1, interface_cell1_plate_1,
     interface_cell2_plate_1] = Mesh_1.GetGroups()
    NETGEN_2D_Parameters_1.SetMaxSize(10)
    [duanban_1, yelengban_1, smeshObj_1, fluid_1, guoliuyuanjian_1, smeshObj_2, smeshObj_3, smeshObj_4, smeshObj_5,
     inlet_1, outlet_1, interface_cell_duanban_1, interface_cell1_cell2_1, smeshObj_6, interface_bar1_cell_1,
     interface_cell1_bar1_1, interface_cell2_bar1_1, interface_plate_cell_1, interface_cell1_plate_1,
     interface_cell2_plate_1] = Mesh_1.GetGroups()
    NETGEN_2D_Parameters_1.SetMinSize(4)
    [duanban_1, yelengban_1, smeshObj_1, fluid_1, guoliuyuanjian_1, smeshObj_2, smeshObj_3, smeshObj_4, smeshObj_5,
     inlet_1, outlet_1, interface_cell_duanban_1, interface_cell1_cell2_1, smeshObj_6, interface_bar1_cell_1,
     interface_cell1_bar1_1, interface_cell2_bar1_1, interface_plate_cell_1, interface_cell1_plate_1,
     interface_cell2_plate_1] = Mesh_1.GetGroups()
    NETGEN_2D_Parameters_1.SetGrowthRate(0.15)
    NETGEN_2D_Parameters_1.SetNbSegPerRadius(10)
    NETGEN_2D_Parameters_1.SetWorstElemMeasure(159)
    NETGEN_2D_Parameters_1.SetCheckChartBoundary(96)
    isDone = Mesh_1.Compute()
    [duanban_1, yelengban_1, smeshObj_1, fluid_1, guoliuyuanjian_1, smeshObj_2, smeshObj_3, smeshObj_4, smeshObj_5,
     inlet_1, outlet_1, interface_cell_duanban_1, interface_cell1_cell2_1, smeshObj_6, interface_bar1_cell_1,
     interface_cell1_bar1_1, interface_cell2_bar1_1, interface_plate_cell_1, interface_cell1_plate_1,
     interface_cell2_plate_1] = Mesh_1.GetGroups()
    NETGEN_2D_Parameters_1.SetMaxSize(8)
    NETGEN_2D_Parameters_1.SetWorstElemMeasure(159)
    NETGEN_2D_Parameters_1.SetCheckChartBoundary(96)
    [duanban_1, yelengban_1, smeshObj_1, fluid_1, guoliuyuanjian_1, smeshObj_2, smeshObj_3, smeshObj_4, smeshObj_5,
     inlet_1, outlet_1, interface_cell_duanban_1, interface_cell1_cell2_1, smeshObj_6, interface_bar1_cell_1,
     interface_cell1_bar1_1, interface_cell2_bar1_1, interface_plate_cell_1, interface_cell1_plate_1,
     interface_cell2_plate_1] = Mesh_1.GetGroups()
    NETGEN_3D = Mesh_1.Tetrahedron(geom=duanban)
    NETGEN_3D_Parameters_1_1 = NETGEN_3D.Parameters()
    NETGEN_3D_Parameters_1_1.SetMaxSize(6)
    NETGEN_3D_Parameters_1_1.SetMinSize(1)
    NETGEN_3D_Parameters_1_1.SetOptimize(1)
    NETGEN_3D_Parameters_1_1.SetFineness(3)
    NETGEN_3D_Parameters_1_1.SetCheckOverlapping(0)
    NETGEN_3D_Parameters_1_1.SetElemSizeWeight(1.36807e-311)
    NETGEN_3D_Parameters_1_1.SetCheckChartBoundary(96)
    [duanban_1, yelengban_1, smeshObj_1, fluid_1, guoliuyuanjian_1, smeshObj_2, smeshObj_3, smeshObj_4, smeshObj_5,
     inlet_1, outlet_1, interface_cell_duanban_1, interface_cell1_cell2_1, smeshObj_6, interface_bar1_cell_1,
     interface_cell1_bar1_1, interface_cell2_bar1_1, interface_plate_cell_1, interface_cell1_plate_1,
     interface_cell2_plate_1] = Mesh_1.GetGroups()
    # Mesh_1.GetMesh().RemoveSubMesh( smeshObj_8 ) ### smeshObj_8 has not been yet created
    NETGEN_3D_Parameters_1.SetCheckChartBoundary(96)
    NETGEN_1D_2D_3D_1 = Mesh_1.Tetrahedron(algo=smeshBuilder.NETGEN_1D2D3D, geom=duanban)
    mesh_duanban = NETGEN_1D_2D_3D_1.GetSubMesh()
    status = Mesh_1.AddHypothesis(NETGEN_3D_Parameters_1, duanban)
    isDone = Mesh_1.Compute()
    [duanban_1, yelengban_1, smeshObj_1, fluid_1, guoliuyuanjian_1, smeshObj_2, smeshObj_3, smeshObj_4, smeshObj_5,
     inlet_1, outlet_1, interface_cell_duanban_1, interface_cell1_cell2_1, smeshObj_6, interface_bar1_cell_1,
     interface_cell1_bar1_1, interface_cell2_bar1_1, interface_plate_cell_1, interface_cell1_plate_1,
     interface_cell2_plate_1] = Mesh_1.GetGroups()
    NETGEN_1D_2D_1 = Mesh_1.Triangle(algo=smeshBuilder.NETGEN_1D2D, geom=yelengban)
    yelengban2d = NETGEN_1D_2D_1.Parameters()
    yelengban2d.SetSecondOrder(0)
    yelengban2d.SetOptimize(1)
    yelengban2d.SetFineness(5)
    yelengban2d.SetGrowthRate(0.2)
    yelengban2d.SetNbSegPerEdge(1)
    yelengban2d.SetChordalError(-1)
    yelengban2d.SetChordalErrorEnabled(0)
    yelengban2d.SetUseSurfaceCurvature(1)
    yelengban2d.SetFuseEdges(1)
    yelengban2d.SetUseDelauney(0)
    yelengban2d.SetQuadAllowed(0)
    yelengban2d.SetElemSizeWeight(0.3)
    yelengban2d.SetNbSurfOptSteps(5)
    [duanban_1, yelengban_1, smeshObj_1, fluid_1, guoliuyuanjian_1, smeshObj_2, smeshObj_3, smeshObj_4, smeshObj_5,
     inlet_1, outlet_1, interface_cell_duanban_1, interface_cell1_cell2_1, smeshObj_6, interface_bar1_cell_1,
     interface_cell1_bar1_1, interface_cell2_bar1_1, interface_plate_cell_1, interface_cell1_plate_1,
     interface_cell2_plate_1] = Mesh_1.GetGroups()
    yelengban2d.SetMaxSize(14)
    yelengban2d.SetNbSegPerRadius(18)
    [duanban_1, yelengban_1, smeshObj_1, fluid_1, guoliuyuanjian_1, smeshObj_2, smeshObj_3, smeshObj_4, smeshObj_5,
     inlet_1, outlet_1, interface_cell_duanban_1, interface_cell1_cell2_1, smeshObj_6, interface_bar1_cell_1,
     interface_cell1_bar1_1, interface_cell2_bar1_1, interface_plate_cell_1, interface_cell1_plate_1,
     interface_cell2_plate_1] = Mesh_1.GetGroups()
    yelengban2d.SetMinSize(2)
    yelengban2d.SetWorstElemMeasure(154)
    yelengban2d.SetCheckChartBoundary(208)
    [duanban_1, yelengban_1, smeshObj_1, fluid_1, guoliuyuanjian_1, smeshObj_2, smeshObj_3, smeshObj_4, smeshObj_5,
     inlet_1, outlet_1, interface_cell_duanban_1, interface_cell1_cell2_1, smeshObj_6, interface_bar1_cell_1,
     interface_cell1_bar1_1, interface_cell2_bar1_1, interface_plate_cell_1, interface_cell1_plate_1,
     interface_cell2_plate_1] = Mesh_1.GetGroups()
    NETGEN_3D_1 = Mesh_1.Tetrahedron(geom=yelengban)
    yelengban3d = NETGEN_3D_1.Parameters()
    yelengban3d.SetMaxSize(4)
    yelengban3d.SetMinSize(0.75)
    yelengban3d.SetOptimize(1)
    yelengban3d.SetFineness(3)
    yelengban3d.SetNbVolOptSteps(4)
    yelengban3d.SetCheckOverlapping(0)
    yelengban3d.SetElemSizeWeight(1.02905e-311)
    yelengban3d.SetCheckChartBoundary(208)
    [duanban_1, yelengban_1, smeshObj_1, fluid_1, guoliuyuanjian_1, smeshObj_2, smeshObj_3, smeshObj_4, smeshObj_5,
     inlet_1, outlet_1, interface_cell_duanban_1, interface_cell1_cell2_1, smeshObj_6, interface_bar1_cell_1,
     interface_cell1_bar1_1, interface_cell2_bar1_1, interface_plate_cell_1, interface_cell1_plate_1,
     interface_cell2_plate_1] = Mesh_1.GetGroups()
    NETGEN_1D_2D_2 = Mesh_1.Triangle(algo=smeshBuilder.NETGEN_1D2D, geom=fluid)
    fluid2D = NETGEN_1D_2D_2.Parameters()
    fluid2D.SetMaxSize(14)
    fluid2D.SetMinSize(2)
    fluid2D.SetSecondOrder(0)
    fluid2D.SetOptimize(1)
    fluid2D.SetFineness(5)
    fluid2D.SetGrowthRate(0.2)
    fluid2D.SetNbSegPerEdge(1)
    fluid2D.SetNbSegPerRadius(18)
    fluid2D.SetChordalError(-1)
    fluid2D.SetChordalErrorEnabled(0)
    fluid2D.SetUseSurfaceCurvature(1)
    fluid2D.SetElemSizeWeight(0.3)
    fluid2D.SetNbSurfOptSteps(5)
    fluid2D.SetFuseEdges(1)
    fluid2D.SetUseDelauney(0)
    fluid2D.SetQuadAllowed(0)
    fluid2D.SetWorstElemMeasure(154)
    fluid2D.SetCheckChartBoundary(208)
    NETGEN_3D_2 = Mesh_1.Tetrahedron(geom=fluid)
    fluid3d = NETGEN_3D_2.Parameters()
    fluid3d.SetMaxSize(4)
    fluid3d.SetMinSize(0.75)
    fluid3d.SetOptimize(1)
    fluid3d.SetFineness(3)
    fluid3d.SetNbVolOptSteps(4)
    fluid3d.SetCheckOverlapping(0)
    fluid3d.SetElemSizeWeight(1.02905e-311)
    fluid3d.SetCheckChartBoundary(208)
    [duanban_1, yelengban_1, smeshObj_1, fluid_1, guoliuyuanjian_1, smeshObj_2, smeshObj_3, smeshObj_4, smeshObj_5,
     inlet_1, outlet_1, interface_cell_duanban_1, interface_cell1_cell2_1, smeshObj_6, interface_bar1_cell_1,
     interface_cell1_bar1_1, interface_cell2_bar1_1, interface_plate_cell_1, interface_cell1_plate_1,
     interface_cell2_plate_1] = Mesh_1.GetGroups()
    interface_duanban_cell_1 = Mesh_1.GroupOnGeom(interface_duanban_cell, 'interface_duanban_cell', SMESH.FACE)
    interface_plate_fluid_1 = Mesh_1.GroupOnGeom(interface_plate_fluid, 'interface_plate_fluid', SMESH.FACE)
    interface_fluid_platete_1 = Mesh_1.GroupOnGeom(interface_fluid_platete, 'interface_fluid_platete', SMESH.FACE)
    aNodeConnectivityNumber000001E49B6472C0 = aFilterManager.CreateNodeConnectivityNumber()
    aAspectRatio3D000001E49B6440D0 = aFilterManager.CreateAspectRatio3D()
    aCriteria = []
    aCriterion = smesh.GetCriterion(SMESH.EDGE, SMESH.FT_FreeFaces, '=', 0)
    aCriteria.append(aCriterion)
    aCriteria = []
    aCriterion = smesh.GetCriterion(SMESH.VOLUME, SMESH.FT_EntityType, SMESH.FT_Undefined, SMESH.Entity_Polyhedra)
    aCriteria.append(aCriterion)
    Body_Fitting_Parameters_1.SetSizeThreshold(4)
    Body_Fitting_Parameters_1.SetToAddEdges(1)
    Body_Fitting_Parameters_1.SetGridSpacing(['15'], [0, 1], 0)
    Body_Fitting_Parameters_1.SetGridSpacing(['10'], [0, 1], 1)
    Body_Fitting_Parameters_1.SetGridSpacing(['25'], [0, 1], 2)
    Body_Fitting_Parameters_1.SetSizeThreshold(6)
    Body_Fitting_Parameters_1.SetToAddEdges(1)
    Body_Fitting_Parameters_1.SetToCreateFaces(1)
    Body_Fitting_Parameters_1.SetToConsiderInternalFaces(1)
    Body_Fitting_Parameters_1.SetGridSpacing(['15'], [0, 1], 0)
    Body_Fitting_Parameters_1.SetGridSpacing(['10'], [0, 1], 1)
    Body_Fitting_Parameters_1.SetGridSpacing(['25'], [0, 1], 2)
    isDone = Mesh_1.Compute()
    aFilterLibrary000001E49D6E2820 = aFilterManager.LoadLibrary('C:/Users/DELL/FilterLib.xml')
    aCriteria = []
    aCriterion = smesh.GetCriterion(SMESH.FACE, SMESH.FT_EntityType, SMESH.FT_Undefined, SMESH.Entity_Polygon,
                                    SMESH.FT_Undefined, SMESH.FT_Undefined, 5.92879e-323);
    aCriterion.Precision = 32762
    aCriteria.append(aCriterion)
    aFilterLibrary000001E49D6E2820.Add('FaceFilter_3', aFilter000001E49D698C40)
    aCriteria = []
    aCriterion = smesh.GetCriterion(SMESH.FACE, SMESH.FT_EntityType, SMESH.FT_Undefined, SMESH.Entity_Polygon)
    aCriteria.append(aCriterion)
    aFilterLibrary000001E49D6E2820.Copy('FaceFilter_3')
    aCriteria = []
    aCriterion = smesh.GetCriterion(SMESH.FACE, SMESH.FT_EntityType, SMESH.FT_Undefined, SMESH.Entity_Polygon)
    aCriteria.append(aCriterion)
    aCriteria = []
    aCriterion = smesh.GetCriterion(SMESH.VOLUME, SMESH.FT_EntityType, SMESH.FT_Undefined, SMESH.Entity_Polyhedra)
    aCriteria.append(aCriterion)
    aFilter000001E49D64A5C0 = aFilterManager.CreateFilter()
    aCriteria = []
    aCriterion = smesh.GetCriterion(SMESH.VOLUME, SMESH.FT_EntityType, SMESH.FT_Undefined, SMESH.Entity_Polyhedra,
                                    SMESH.FT_Undefined, SMESH.FT_Undefined, 1.0285e-311)
    aCriteria.append(aCriterion)
    aFilter000001E49D64A5C0 = aFilterManager.CreateFilter()
    aCriteria = []
    aCriterion = smesh.GetCriterion(SMESH.VOLUME, SMESH.FT_EntityType, SMESH.FT_Undefined, SMESH.Entity_Polyhedra,
                                    SMESH.FT_Undefined, SMESH.FT_Undefined, 1.0285e-311)
    aCriteria.append(aCriterion)
    aCriteria = []
    aCriterion = smesh.GetCriterion(SMESH.VOLUME, SMESH.FT_EntityType, SMESH.FT_Undefined, SMESH.Entity_Polyhedra)
    aCriteria.append(aCriterion)
    aCriteria = []
    aCriterion = smesh.GetCriterion(SMESH.VOLUME, SMESH.FT_EntityType, SMESH.FT_Undefined, SMESH.Entity_Polyhedra)
    aCriteria.append(aCriterion)
    aCriteria = []
    aCriterion = smesh.GetCriterion(SMESH.VOLUME, SMESH.FT_EntityType, SMESH.FT_Undefined, SMESH.Entity_Polyhedra,
                                    SMESH.FT_Undefined, SMESH.FT_Undefined, 1.02829e-311)
    aCriteria.append(aCriterion)
    try:
        Mesh_1.ExportUNV(r'E:/project_simulation/energy_container/container_V1/cell_simple_V1/Mesh_1.unv', 0)
        pass
    except:
        print('ExportUNV() failed. Invalid file name?')
    aCriteria = []
    aCriterion = smesh.GetCriterion(SMESH.EDGE, SMESH.FT_FreeFaces, '=', 0)
    aCriteria.append(aCriterion)
    aEqualVolumes000001E4B3B9AEB0 = aFilterManager.CreateEqualVolumes()
    try:
        Mesh_1.ExportUNV(r'E:/project_simulation/energy_container/container_V1/cell_simple_V1/Mesh_1.unv', 0)
        pass
    except:
        print('ExportUNV() failed. Invalid file name?')
    aCriteria = []
    aCriterion = smesh.GetCriterion(SMESH.EDGE, SMESH.FT_FreeFaces, '=', 0)
    aCriteria.append(aCriterion)
    theNbElems = Mesh_1.Evaluate(pack_simple5)
    cell1_1 = Mesh_1.GroupOnGeom(cell1, 'Solid', SMESH.VOLUME)
    cell1_1.SetName('cell1')
    cell2_1 = Mesh_1.GroupOnGeom(cell2, 'Solid', SMESH.VOLUME)
    cell2_1.SetName('cell2')
    [duanban_1, yelengban_1, fluid_1, guoliuyuanjian_1, inlet_1, outlet_1, interface_cell_duanban_1,
     interface_cell1_cell2_1, interface_bar1_cell_1, interface_cell1_bar1_1, interface_cell2_bar1_1,
     interface_plate_cell_1, interface_cell1_plate_1, interface_cell2_plate_1, interface_duanban_cell_1,
     interface_plate_fluid_1, interface_fluid_platete_1, cell1_1, cell2_1] = Mesh_1.GetGroups()
    # Mesh_1.GetMesh().RemoveSubMesh( smeshObj_9 ) ### smeshObj_9 has not been yet created
    Body_Fitting_Parameters_2 = smesh.CreateHypothesis('CartesianParameters3D')
    Body_Fitting_Parameters_2.SetSizeThreshold(4)
    Body_Fitting_Parameters_2.SetToAddEdges(0)
    Body_Fitting_Parameters_2.SetGridSpacing(['39.0863'], [0, 1], 0)
    Body_Fitting_Parameters_2.SetGridSpacing(['39.0863'], [0, 1], 1)
    Body_Fitting_Parameters_2.SetGridSpacing(['39.0863'], [0, 1], 2)
    Cartesian_3D_3 = Mesh_1.BodyFitted(geom=cell1)
    mesh_cell1 = Cartesian_3D_3.GetSubMesh()
    [duanban_1, yelengban_1, fluid_1, guoliuyuanjian_1, inlet_1, outlet_1, interface_cell_duanban_1,
     interface_cell1_cell2_1, interface_bar1_cell_1, interface_cell1_bar1_1, interface_cell2_bar1_1,
     interface_plate_cell_1, interface_cell1_plate_1, interface_cell2_plate_1, interface_duanban_cell_1,
     interface_plate_fluid_1, interface_fluid_platete_1, cell1_1, cell2_1] = Mesh_1.GetGroups()
    Cartesian_3D_4 = Mesh_1.BodyFitted(geom=cell2)
    isDone = Mesh_1.Compute()
    [duanban_1, yelengban_1, fluid_1, guoliuyuanjian_1, inlet_1, outlet_1, interface_cell_duanban_1,
     interface_cell1_cell2_1, interface_bar1_cell_1, interface_cell1_bar1_1, interface_cell2_bar1_1,
     interface_plate_cell_1, interface_cell1_plate_1, interface_cell2_plate_1, interface_duanban_cell_1,
     interface_plate_fluid_1, interface_fluid_platete_1, cell1_1, cell2_1] = Mesh_1.GetGroups()
    aCriteria = []
    aCriterion = smesh.GetCriterion(SMESH.VOLUME, SMESH.FT_EntityType, SMESH.FT_Undefined, SMESH.Entity_Polyhedra)
    aCriteria.append(aCriterion)
    [duanban_1, yelengban_1, fluid_1, guoliuyuanjian_1, inlet_1, outlet_1, interface_cell_duanban_1,
     interface_cell1_cell2_1, interface_bar1_cell_1, interface_cell1_bar1_1, interface_cell2_bar1_1,
     interface_plate_cell_1, interface_cell1_plate_1, interface_cell2_plate_1, interface_duanban_cell_1,
     interface_plate_fluid_1, interface_fluid_platete_1, cell1_1, cell2_1] = Mesh_1.GetGroups()
    interface_cell2_cell1_1 = Mesh_1.GroupOnGeom(interface_cell2_cell1, 'interface_cell2_cell1', SMESH.FACE)
    [duanban_1, yelengban_1, fluid_1, guoliuyuanjian_1, inlet_1, outlet_1, interface_cell_duanban_1,
     interface_cell1_cell2_1, interface_bar1_cell_1, interface_cell1_bar1_1, interface_cell2_bar1_1,
     interface_plate_cell_1, interface_cell1_plate_1, interface_cell2_plate_1, interface_duanban_cell_1,
     interface_plate_fluid_1, interface_fluid_platete_1, cell1_1, cell2_1, interface_cell2_cell1_1] = Mesh_1.GetGroups()
    aCriteria = []
    aCriterion = smesh.GetCriterion(SMESH.VOLUME, SMESH.FT_Volume3D, SMESH.FT_LessThan, 0)
    aCriteria.append(aCriterion)
    aCriteria = []
    aCriterion = smesh.GetCriterion(SMESH.VOLUME, SMESH.FT_Volume3D, SMESH.FT_LessThan, 0)
    aCriteria.append(aCriterion)
    Body_Fitting_Parameters_1.SetSizeThreshold(6)
    Body_Fitting_Parameters_1.SetToAddEdges(1)
    Body_Fitting_Parameters_1.SetToCreateFaces(0)
    Body_Fitting_Parameters_1.SetToConsiderInternalFaces(0)
    Body_Fitting_Parameters_1.SetGridSpacing(['15'], [0, 1], 0)
    Body_Fitting_Parameters_1.SetGridSpacing(['10'], [0, 1], 1)
    Body_Fitting_Parameters_1.SetGridSpacing(['25'], [0, 1], 2)
    [duanban_1, yelengban_1, fluid_1, guoliuyuanjian_1, inlet_1, outlet_1, interface_cell_duanban_1,
     interface_cell1_cell2_1, interface_bar1_cell_1, interface_cell1_bar1_1, interface_cell2_bar1_1,
     interface_plate_cell_1, interface_cell1_plate_1, interface_cell2_plate_1, interface_duanban_cell_1,
     interface_plate_fluid_1, interface_fluid_platete_1, cell1_1, cell2_1, interface_cell2_cell1_1] = Mesh_1.GetGroups()
    Body_Fitting_Parameters_1.SetSizeThreshold(6)
    Body_Fitting_Parameters_1.SetToAddEdges(1)
    Body_Fitting_Parameters_1.SetToUseThresholdForInternalFaces(0)
    Body_Fitting_Parameters_1.SetGridSpacing(['15'], [0, 1], 0)
    Body_Fitting_Parameters_1.SetGridSpacing(['10'], [0, 1], 1)
    Body_Fitting_Parameters_1.SetGridSpacing(['25'], [0, 1], 2)
    [duanban_1, yelengban_1, fluid_1, guoliuyuanjian_1, inlet_1, outlet_1, interface_cell_duanban_1,
     interface_cell1_cell2_1, interface_bar1_cell_1, interface_cell1_bar1_1, interface_cell2_bar1_1,
     interface_plate_cell_1, interface_cell1_plate_1, interface_cell2_plate_1, interface_duanban_cell_1,
     interface_plate_fluid_1, interface_fluid_platete_1, cell1_1, cell2_1, interface_cell2_cell1_1] = Mesh_1.GetGroups()
    aCriteria = []
    aCriterion = smesh.GetCriterion(SMESH.VOLUME, SMESH.FT_EntityType, SMESH.FT_Undefined, SMESH.Entity_Polyhedra)
    aCriteria.append(aCriterion)
    [duanban_1, yelengban_1, fluid_1, guoliuyuanjian_1, inlet_1, outlet_1, interface_cell_duanban_1,
     interface_cell1_cell2_1, interface_bar1_cell_1, interface_cell1_bar1_1, interface_cell2_bar1_1,
     interface_plate_cell_1, interface_cell1_plate_1, interface_cell2_plate_1, interface_duanban_cell_1,
     interface_plate_fluid_1, interface_fluid_platete_1, cell1_1, cell2_1, interface_cell2_cell1_1] = Mesh_1.GetGroups()
    aCriteria = []
    aCriterion = smesh.GetCriterion(SMESH.VOLUME, SMESH.FT_EntityType, SMESH.FT_Undefined, SMESH.Entity_Polyhedra)
    aCriteria.append(aCriterion)
    Body_Fitting_Parameters_1.SetSizeThreshold(6)
    Body_Fitting_Parameters_1.SetToAddEdges(1)
    Body_Fitting_Parameters_1.SetGridSpacing(['15'], [0, 1], 0)
    Body_Fitting_Parameters_1.SetGridSpacing(['10'], [0, 1], 1)
    Body_Fitting_Parameters_1.SetGridSpacing(['25'], [0, 1], 2)
    Body_Fitting_Parameters_1.SetSizeThreshold(6)
    Body_Fitting_Parameters_1.SetToAddEdges(1)
    Body_Fitting_Parameters_1.SetGridSpacing(['15'], [0, 1], 0)
    Body_Fitting_Parameters_1.SetGridSpacing(['10'], [0, 1], 1)
    Body_Fitting_Parameters_1.SetGridSpacing(['25'], [0, 1], 2)
    [duanban_1, yelengban_1, fluid_1, guoliuyuanjian_1, inlet_1, outlet_1, interface_cell_duanban_1,
     interface_cell1_cell2_1, interface_bar1_cell_1, interface_cell1_bar1_1, interface_cell2_bar1_1,
     interface_plate_cell_1, interface_cell1_plate_1, interface_cell2_plate_1, interface_duanban_cell_1,
     interface_plate_fluid_1, interface_fluid_platete_1, cell1_1, cell2_1, interface_cell2_cell1_1] = Mesh_1.GetGroups()
    status = Mesh_1.RemoveHypothesis(Cartesian_3D, cell1)
    NETGEN_1D_2D_3 = Mesh_1.Triangle(algo=smeshBuilder.NETGEN_1D2D, geom=cell1)
    PolyhedronPerSolid_3D = Mesh_1.Polyhedron(geom=cell1)
    [duanban_1, yelengban_1, fluid_1, guoliuyuanjian_1, inlet_1, outlet_1, interface_cell_duanban_1,
     interface_cell1_cell2_1, interface_bar1_cell_1, interface_cell1_bar1_1, interface_cell2_bar1_1,
     interface_plate_cell_1, interface_cell1_plate_1, interface_cell2_plate_1, interface_duanban_cell_1,
     interface_plate_fluid_1, interface_fluid_platete_1, cell1_1, cell2_1, interface_cell2_cell1_1] = Mesh_1.GetGroups()
    status = Mesh_1.RemoveHypothesis(PolyhedronPerSolid_3D, cell1)
    Hexa_3D = Mesh_1.Hexahedron(algo=smeshBuilder.Hexa, geom=cell1)
    Renumber_1 = Hexa_3D.Renumber()
    Renumber_1.SetBlocksOrientation([])
    [duanban_1, yelengban_1, fluid_1, guoliuyuanjian_1, inlet_1, outlet_1, interface_cell_duanban_1,
     interface_cell1_cell2_1, interface_bar1_cell_1, interface_cell1_bar1_1, interface_cell2_bar1_1,
     interface_plate_cell_1, interface_cell1_plate_1, interface_cell2_plate_1, interface_duanban_cell_1,
     interface_plate_fluid_1, interface_fluid_platete_1, cell1_1, cell2_1, interface_cell2_cell1_1] = Mesh_1.GetGroups()
    status = Mesh_1.RemoveHypothesis(Hexa_3D, cell1)
    cell_1 = NETGEN_1D_2D_3.Parameters()
    cell_1.SetSecondOrder(0)
    cell_1.SetOptimize(1)
    cell_1.SetFineness(5)
    cell_1.SetNbSegPerEdge(1)
    cell_1.SetNbSegPerRadius(12)
    cell_1.SetChordalError(-1)
    cell_1.SetChordalErrorEnabled(0)
    cell_1.SetUseSurfaceCurvature(1)
    cell_1.SetElemSizeWeight(0.3)
    cell_1.SetNbSurfOptSteps(5)
    cell_1.SetFuseEdges(1)
    cell_1.SetUseDelauney(0)
    cell_1.SetQuadAllowed(0)
    NETGEN_3D_3 = Mesh_1.Tetrahedron(geom=cell1)
    status = Mesh_1.RemoveHypothesis(Renumber_1, cell1)
    [duanban_1, yelengban_1, fluid_1, guoliuyuanjian_1, inlet_1, outlet_1, interface_cell_duanban_1,
     interface_cell1_cell2_1, interface_bar1_cell_1, interface_cell1_bar1_1, interface_cell2_bar1_1,
     interface_plate_cell_1, interface_cell1_plate_1, interface_cell2_plate_1, interface_duanban_cell_1,
     interface_plate_fluid_1, interface_fluid_platete_1, cell1_1, cell2_1, interface_cell2_cell1_1] = Mesh_1.GetGroups()
    cell_1.SetMinSize(5)
    cell_1.SetGrowthRate(0.2)
    cell3d = NETGEN_3D_3.Parameters()
    cell3d.SetMinSize(4)
    cell3d.SetOptimize(1)
    cell3d.SetFineness(3)
    cell3d.SetNbVolOptSteps(5)
    cell3d.SetCheckOverlapping(0)
    [duanban_1, yelengban_1, fluid_1, guoliuyuanjian_1, inlet_1, outlet_1, interface_cell_duanban_1,
     interface_cell1_cell2_1, interface_bar1_cell_1, interface_cell1_bar1_1, interface_cell2_bar1_1,
     interface_plate_cell_1, interface_cell1_plate_1, interface_cell2_plate_1, interface_duanban_cell_1,
     interface_plate_fluid_1, interface_fluid_platete_1, cell1_1, cell2_1, interface_cell2_cell1_1] = Mesh_1.GetGroups()
    cell3d.SetMaxSize(12)
    [duanban_1, yelengban_1, fluid_1, guoliuyuanjian_1, inlet_1, outlet_1, interface_cell_duanban_1,
     interface_cell1_cell2_1, interface_bar1_cell_1, interface_cell1_bar1_1, interface_cell2_bar1_1,
     interface_plate_cell_1, interface_cell1_plate_1, interface_cell2_plate_1, interface_duanban_cell_1,
     interface_plate_fluid_1, interface_fluid_platete_1, cell1_1, cell2_1, interface_cell2_cell1_1] = Mesh_1.GetGroups()
    cell_1.SetMaxSize(12)
    cell_1.SetWorstElemMeasure(2)
    cell_1.SetCheckChartBoundary(128)
    cell3d.SetElemSizeWeight(1.05492e-311)
    cell3d.SetCheckChartBoundary(128)
    [duanban_1, yelengban_1, fluid_1, guoliuyuanjian_1, inlet_1, outlet_1, interface_cell_duanban_1,
     interface_cell1_cell2_1, interface_bar1_cell_1, interface_cell1_bar1_1, interface_cell2_bar1_1,
     interface_plate_cell_1, interface_cell1_plate_1, interface_cell2_plate_1, interface_duanban_cell_1,
     interface_plate_fluid_1, interface_fluid_platete_1, cell1_1, cell2_1, interface_cell2_cell1_1] = Mesh_1.GetGroups()
    status = Mesh_1.RemoveHypothesis(Cartesian_3D, cell2)
    NETGEN_1D_2D_4 = Mesh_1.Triangle(algo=smeshBuilder.NETGEN_1D2D, geom=cell2)
    status = Mesh_1.AddHypothesis(cell_1, cell2)
    NETGEN_3D_4 = Mesh_1.Tetrahedron(geom=cell2)
    status = Mesh_1.AddHypothesis(cell3d, cell2)
    [duanban_1, yelengban_1, fluid_1, guoliuyuanjian_1, inlet_1, outlet_1, interface_cell_duanban_1,
     interface_cell1_cell2_1, interface_bar1_cell_1, interface_cell1_bar1_1, interface_cell2_bar1_1,
     interface_plate_cell_1, interface_cell1_plate_1, interface_cell2_plate_1, interface_duanban_cell_1,
     interface_plate_fluid_1, interface_fluid_platete_1, cell1_1, cell2_1, interface_cell2_cell1_1] = Mesh_1.GetGroups()
    aCriteria = []
    aCriterion = smesh.GetCriterion(SMESH.FACE, SMESH.FT_Skew, SMESH.FT_MoreThan, 80)
    aCriteria.append(aCriterion)
    isDone = Mesh_1.Compute()
    mesh_yelengban = NETGEN_1D_2D_1.GetSubMesh()
    mesh_fluid = NETGEN_1D_2D_2.GetSubMesh()
    mesh_cell2 = Cartesian_3D_4.GetSubMesh()

    ## some objects were removed
    aStudyBuilder = salome.myStudy.NewBuilder()
    SO = salome.myStudy.FindObjectIOR(salome.myStudy.ConvertObjectToIOR(smeshObj_2))
    if SO: aStudyBuilder.RemoveObjectWithChildren(SO)
    SO = salome.myStudy.FindObjectIOR(salome.myStudy.ConvertObjectToIOR(smeshObj_3))
    if SO: aStudyBuilder.RemoveObjectWithChildren(SO)
    SO = salome.myStudy.FindObjectIOR(salome.myStudy.ConvertObjectToIOR(smeshObj_6))
    if SO: aStudyBuilder.RemoveObjectWithChildren(SO)
    SO = salome.myStudy.FindObjectIOR(salome.myStudy.ConvertObjectToIOR(smeshObj_1))
    if SO: aStudyBuilder.RemoveObjectWithChildren(SO)
    SO = salome.myStudy.FindObjectIOR(salome.myStudy.ConvertObjectToIOR(smeshObj_4))
    if SO: aStudyBuilder.RemoveObjectWithChildren(SO)
    SO = salome.myStudy.FindObjectIOR(salome.myStudy.ConvertObjectToIOR(smeshObj_5))
    if SO: aStudyBuilder.RemoveObjectWithChildren(SO)

    ## Set names of Mesh objects
    smesh.SetName(Cartesian_3D.GetAlgorithm(), 'Cartesian_3D')
    smesh.SetName(interface_bar1_cell_1, 'interface_bar1_cell')
    smesh.SetName(NETGEN_1D_2D.GetAlgorithm(), 'NETGEN 1D-2D')
    smesh.SetName(interface_cell1_bar1_1, 'interface_cell1_bar1')
    smesh.SetName(NETGEN_1D_2D_3D.GetAlgorithm(), 'NETGEN 1D-2D-3D')
    smesh.SetName(PolyhedronPerSolid_3D.GetAlgorithm(), 'PolyhedronPerSolid_3D')
    smesh.SetName(Body_Fitting_Parameters_1, 'Body Fitting Parameters_1')
    smesh.SetName(NETGEN_3D.GetAlgorithm(), 'NETGEN 3D')
    smesh.SetName(yuanjian_para, 'yuanjian_para')
    smesh.SetName(Hexa_3D.GetAlgorithm(), 'Hexa_3D')
    smesh.SetName(NETGEN_3D_Parameters_1_1, 'NETGEN 3D Parameters_1')
    smesh.SetName(NETGEN_3D_Parameters_1, 'NETGEN 3D Parameters_1')
    smesh.SetName(NETGEN_2D_Parameters_1, 'NETGEN 2D Parameters_1')
    smesh.SetName(inlet_1, 'inlet')
    smesh.SetName(outlet_1, 'outlet')
    smesh.SetName(yelengban2d, 'yelengban2d')
    smesh.SetName(interface_cell_duanban_1, 'interface_cell_duanban')
    smesh.SetName(yelengban3d, 'yelengban3d')
    smesh.SetName(interface_cell1_cell2_1, 'interface_cell1_cell2')
    smesh.SetName(Mesh_1.GetMesh(), 'Mesh_1')
    smesh.SetName(mesh_yuanjian, 'mesh_yuanjian')
    smesh.SetName(mesh_fluid, 'mesh_fluid')
    smesh.SetName(mesh_yelengban, 'mesh_yelengban')
    smesh.SetName(mesh_duanban, 'mesh_duanban')
    smesh.SetName(cell2_1, 'cell2')
    smesh.SetName(cell1_1, 'cell1')
    smesh.SetName(interface_plate_cell_1, 'interface_plate_cell')
    smesh.SetName(interface_cell2_bar1_1, 'interface_cell2_bar1')
    smesh.SetName(interface_cell2_plate_1, 'interface_cell2_plate')
    smesh.SetName(guoliuyuanjian_1, 'guoliuyuanjian')
    smesh.SetName(Body_Fitting_Parameters_2, 'Body Fitting Parameters_2')
    smesh.SetName(interface_cell1_plate_1, 'interface_cell1_plate')
    smesh.SetName(fluid_1, 'fluid')
    smesh.SetName(interface_plate_fluid_1, 'interface_plate_fluid')
    smesh.SetName(fluid3d, 'fluid3d')
    smesh.SetName(interface_duanban_cell_1, 'interface_duanban_cell')
    smesh.SetName(fluid2D, 'fluid2D')
    smesh.SetName(yelengban_1, 'yelengban')
    smesh.SetName(cell3d, 'cell3d')
    smesh.SetName(interface_cell2_cell1_1, 'interface_cell2_cell1')
    smesh.SetName(duanban_1, 'duanban')
    smesh.SetName(cell_1, 'cell')
    smesh.SetName(interface_fluid_platete_1, 'interface_fluid_platete')
    smesh.SetName(Renumber_1, 'Renumber_1')
    smesh.SetName(mesh_cell2, 'mesh_cell2')
    smesh.SetName(mesh_cell1, 'mesh_cell1')

    pass


if __name__ == '__main__':
    SMESH_RebuildData = RebuildData
    exec('import ' + re.sub('SMESH$', 'GEOM', thisModule) + ' as GEOM_dump')
    GEOM_dump.RebuildData()
    exec('from ' + re.sub('SMESH$', 'GEOM', thisModule) + ' import * ')
    SMESH_RebuildData()
