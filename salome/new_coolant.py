#!/usr/bin/env python

###
### This file is generated automatically by SALOME v9.10.0 with dump python functionality
###

import sys
import salome

salome.salome_init()
import salome_notebook
notebook = salome_notebook.NoteBook()
sys.path.insert(0, r'E:/project_simulation/energy_container/container_V1/coolant_V1')

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
coolant_plate_V1_simplified = geompy.ImportSTEP("E:/test/energy_container_test/true_model_V1/coolant_plate/coolant_plate_V1_simplified.stp", True, True)
[Volume] = geompy.ExtractShapes(coolant_plate_V1_simplified, geompy.ShapeType["COMPOUND"], True)
inlet = geompy.CreateGroup(coolant_plate_V1_simplified, geompy.ShapeType["FACE"])
geompy.UnionIDs(inlet, [1813])
outlet = geompy.CreateGroup(coolant_plate_V1_simplified, geompy.ShapeType["FACE"])
geompy.UnionIDs(outlet, [1808])
[Volume, inlet, outlet] = geompy.GetExistingSubObjects(coolant_plate_V1_simplified, False)
[Volume, inlet, outlet] = geompy.GetExistingSubObjects(coolant_plate_V1_simplified, False)
[Volume, inlet, outlet] = geompy.GetExistingSubObjects(coolant_plate_V1_simplified, False)
[Volume, inlet, outlet] = geompy.GetExistingSubObjects(coolant_plate_V1_simplified, False)
geompy.addToStudy( O, 'O' )
geompy.addToStudy( OX, 'OX' )
geompy.addToStudy( OY, 'OY' )
geompy.addToStudy( OZ, 'OZ' )
geompy.addToStudy( coolant_plate_V1_simplified, 'coolant_plate_V1_simplified' )
geompy.addToStudyInFather( coolant_plate_V1_simplified, inlet, 'inlet' )
geompy.addToStudyInFather( coolant_plate_V1_simplified, Volume, 'Volume' )
geompy.addToStudyInFather( coolant_plate_V1_simplified, outlet, 'outlet' )

###
### SMESH component
###

import  SMESH, SALOMEDS
from salome.smesh import smeshBuilder

smesh = smeshBuilder.New()
#smesh.SetEnablePublish( False ) # Set to False to avoid publish in study if not needed or in some particular situations:
                                 # multiples meshes built in parallel, complex and numerous mesh edition (performance)

aFilterManager = smesh.CreateFilterManager()
Mesh_1 = smesh.Mesh(coolant_plate_V1_simplified, 'Mesh_1')
Volume_1 = Mesh_1.GroupOnGeom(Volume, 'Volume', SMESH.VOLUME)
inlet_1 = Mesh_1.GroupOnGeom(inlet, 'inlet', SMESH.FACE)
outlet_1 = Mesh_1.GroupOnGeom(outlet, 'outlet', SMESH.FACE)
isDone = Mesh_1.Compute()
[ Volume_1, inlet_1, outlet_1 ] = Mesh_1.GetGroups()
isDone = Mesh_1.Compute()
[ Volume_1, inlet_1, outlet_1 ] = Mesh_1.GetGroups()
NETGEN_1D_2D = Mesh_1.Triangle(algo=smeshBuilder.NETGEN_1D2D)
NETGEN_2D_Parameters_1 = NETGEN_1D_2D.Parameters()
NETGEN_2D_Parameters_1.SetMaxSize( 12 )
NETGEN_2D_Parameters_1.SetMinSize( 3 )
NETGEN_2D_Parameters_1.SetSecondOrder( 0 )
NETGEN_2D_Parameters_1.SetOptimize( 1 )
NETGEN_2D_Parameters_1.SetFineness( 5 )
NETGEN_2D_Parameters_1.SetGrowthRate( 0.2 )
NETGEN_2D_Parameters_1.SetNbSegPerEdge( 1 )
NETGEN_2D_Parameters_1.SetNbSegPerRadius( 12 )
NETGEN_2D_Parameters_1.SetChordalError( -1 )
NETGEN_2D_Parameters_1.SetChordalErrorEnabled( 0 )
NETGEN_2D_Parameters_1.SetUseSurfaceCurvature( 1 )
NETGEN_2D_Parameters_1.SetNbSurfOptSteps( 4 )
NETGEN_2D_Parameters_1.SetFuseEdges( 1 )
NETGEN_2D_Parameters_1.SetUseDelauney( 0 )
NETGEN_2D_Parameters_1.SetCheckChartBoundary( 0 )
NETGEN_2D_Parameters_1.SetQuadAllowed( 0 )
NETGEN_2D_Parameters_1.SetWorstElemMeasure( 223 )
isDone = Mesh_1.Compute()
[ Volume_1, inlet_1, outlet_1 ] = Mesh_1.GetGroups()
isDone = Mesh_1.Compute()
[ Volume_1, inlet_1, outlet_1 ] = Mesh_1.GetGroups()
NETGEN_2D_Parameters_1.SetMaxSize( 14 )
NETGEN_2D_Parameters_1.SetMinSize( 3 )
NETGEN_2D_Parameters_1.SetSecondOrder( 0 )
NETGEN_2D_Parameters_1.SetOptimize( 1 )
NETGEN_2D_Parameters_1.SetFineness( 5 )
NETGEN_2D_Parameters_1.SetGrowthRate( 0.2 )
NETGEN_2D_Parameters_1.SetNbSegPerEdge( 1 )
NETGEN_2D_Parameters_1.SetNbSegPerRadius( 12 )
NETGEN_2D_Parameters_1.SetChordalError( 0 )
NETGEN_2D_Parameters_1.SetChordalErrorEnabled( 0 )
NETGEN_2D_Parameters_1.SetUseSurfaceCurvature( 1 )
NETGEN_2D_Parameters_1.SetFuseEdges( 1 )
NETGEN_2D_Parameters_1.SetQuadAllowed( 0 )
NETGEN_2D_Parameters_1.SetWorstElemMeasure( 175 )
NETGEN_2D_Parameters_1.SetCheckChartBoundary( 144 )
isDone = Mesh_1.Compute()
[ Volume_1, inlet_1, outlet_1 ] = Mesh_1.GetGroups()
isDone = Mesh_1.Compute()
[ Volume_1, inlet_1, outlet_1 ] = Mesh_1.GetGroups()
isDone = Mesh_1.Compute()
[ Volume_1, inlet_1, outlet_1 ] = Mesh_1.GetGroups()
isDone = Mesh_1.Compute()
[ Volume_1, inlet_1, outlet_1 ] = Mesh_1.GetGroups()
isDone = Mesh_1.Compute()
[ Volume_1, inlet_1, outlet_1 ] = Mesh_1.GetGroups()
isDone = Mesh_1.Compute()
[ Volume_1, inlet_1, outlet_1 ] = Mesh_1.GetGroups()
NETGEN_2D_Parameters_1.SetNbSegPerRadius( 14 )
NETGEN_2D_Parameters_1.SetWorstElemMeasure( 175 )
NETGEN_2D_Parameters_1.SetCheckChartBoundary( 144 )
isDone = Mesh_1.Compute()
[ Volume_1, inlet_1, outlet_1 ] = Mesh_1.GetGroups()
isDone = Mesh_1.Compute()
[ Volume_1, inlet_1, outlet_1 ] = Mesh_1.GetGroups()
NETGEN_2D_Parameters_1.SetMinSize( 4 )
NETGEN_2D_Parameters_1.SetNbSegPerRadius( 10 )
NETGEN_2D_Parameters_1.SetElemSizeWeight( 0.3 )
NETGEN_2D_Parameters_1.SetNbSurfOptSteps( 5 )
NETGEN_2D_Parameters_1.SetWorstElemMeasure( 175 )
NETGEN_2D_Parameters_1.SetCheckChartBoundary( 144 )
isDone = Mesh_1.Compute()
[ Volume_1, inlet_1, outlet_1 ] = Mesh_1.GetGroups()
isDone = Mesh_1.Compute()
[ Volume_1, inlet_1, outlet_1 ] = Mesh_1.GetGroups()
isDone = Mesh_1.Compute()
[ Volume_1, inlet_1, outlet_1 ] = Mesh_1.GetGroups()
isDone = Mesh_1.Compute()
[ Volume_1, inlet_1, outlet_1 ] = Mesh_1.GetGroups()
NETGEN_2D_Parameters_1.SetMinSize( 2.5 )
NETGEN_2D_Parameters_1.SetNbSegPerRadius( 18 )
NETGEN_2D_Parameters_1.SetWorstElemMeasure( 175 )
NETGEN_2D_Parameters_1.SetCheckChartBoundary( 144 )
isDone = Mesh_1.Compute()
[ Volume_1, inlet_1, outlet_1 ] = Mesh_1.GetGroups()
isDone = Mesh_1.Compute()
[ Volume_1, inlet_1, outlet_1 ] = Mesh_1.GetGroups()
isDone = Mesh_1.Compute()
[ Volume_1, inlet_1, outlet_1 ] = Mesh_1.GetGroups()
Mesh_1.SetAutoColor( 1 )
[ Volume_1, inlet_1, outlet_1 ] = Mesh_1.GetGroups()
Volume_1.SetColor( SALOMEDS.Color( 0.8, 0.8, 0.396078 ))
inlet_1.SetColor( SALOMEDS.Color( 0.396078, 0.8, 0.396078 ))
outlet_1.SetColor( SALOMEDS.Color( 0.396078, 0.8, 0.8 ))
Mesh_1.SetAutoColor( 0 )
[ Volume_1, inlet_1, outlet_1 ] = Mesh_1.GetGroups()
isDone = Mesh_1.Compute()
[ Volume_1, inlet_1, outlet_1 ] = Mesh_1.GetGroups()
isDone = Mesh_1.Compute()
[ Volume_1, inlet_1, outlet_1 ] = Mesh_1.GetGroups()
isDone = Mesh_1.Compute()
[ Volume_1, inlet_1, outlet_1 ] = Mesh_1.GetGroups()
isDone = Mesh_1.Compute()
[ Volume_1, inlet_1, outlet_1 ] = Mesh_1.GetGroups()
aCriteria = []
aCriterion = smesh.GetCriterion(SMESH.EDGE, SMESH.FT_FreeFaces, '=', 0)
aCriteria.append(aCriterion)
[Volume_1, inlet_1, outlet_1] = Mesh_1.GetGroups()
aCriteria = []
aCriterion = smesh.GetCriterion(SMESH.EDGE, SMESH.FT_FreeFaces, '=', 0)
aCriteria.append(aCriterion)
NETGEN_2D_Parameters_1.SetMaxSize( 14 )
NETGEN_2D_Parameters_1.SetMinSize( 2.5 )
NETGEN_2D_Parameters_1.SetSecondOrder( 0 )
NETGEN_2D_Parameters_1.SetOptimize( 1 )
NETGEN_2D_Parameters_1.SetFineness( 5 )
NETGEN_2D_Parameters_1.SetGrowthRate( 0.2 )
NETGEN_2D_Parameters_1.SetNbSegPerEdge( 1 )
NETGEN_2D_Parameters_1.SetNbSegPerRadius( 20 )
NETGEN_2D_Parameters_1.SetChordalError( 0 )
NETGEN_2D_Parameters_1.SetChordalErrorEnabled( 0 )
NETGEN_2D_Parameters_1.SetUseSurfaceCurvature( 1 )
NETGEN_2D_Parameters_1.SetFuseEdges( 1 )
NETGEN_2D_Parameters_1.SetQuadAllowed( 0 )
NETGEN_2D_Parameters_1.SetWorstElemMeasure( 147 )
NETGEN_2D_Parameters_1.SetCheckChartBoundary( 144 )
isDone = Mesh_1.Compute()
theNbElems = Mesh_1.Evaluate(coolant_plate_V1_simplified)
aFilterLibrary00000246297CF560 = aFilterManager.LoadLibrary('C:/Users/DELL/FilterLib.xml')
aCriteria = []
aCriterion = smesh.GetCriterion(SMESH.FACE,SMESH.FT_Skew,SMESH.FT_MoreThan,80,SMESH.FT_Undefined,SMESH.FT_Undefined,5.92879e-323); aCriterion.Precision = 32765
aCriteria.append(aCriterion)
aFilterLibrary00000246297CF560.Add('FaceFilter_1',aFilter000002464AE19870)
aCriteria = []
aCriterion = smesh.GetCriterion(SMESH.FACE,SMESH.FT_Skew,SMESH.FT_MoreThan,80)
aCriteria.append(aCriterion)
aFilterLibrary00000246297CF560.Copy('FaceFilter_1')
aFilterLibrary000002465A06D300 = aFilterManager.LoadLibrary('C:/Users/DELL/FilterLib.xml')
aCriteria = []
aCriterion = smesh.GetCriterion(SMESH.FACE,SMESH.FT_Skew,SMESH.FT_MoreThan,80)
aCriteria.append(aCriterion)
aFilterLibrary00000246297CFCB0 = aFilterManager.LoadLibrary('C:/Users/DELL/FilterLib.xml')
aCriteria = []
aFilterLibrary00000246297CFCB0.AddEmpty('VolumeFilter_1',SMESH.VOLUME)
aCriteria = []
aFilterLibrary00000246297CFCB0.Copy('VolumeFilter_1')
aFilter000002464AE199A0 = aFilterManager.CreateFilter()
aCriteria = []
aCriterion = smesh.GetCriterion(SMESH.FACE,SMESH.FT_Skew,SMESH.FT_MoreThan,80,SMESH.FT_Undefined,SMESH.FT_Undefined,1.23699e-311)
aCriteria.append(aCriterion)
aCriteria = []
aCriterion = smesh.GetCriterion(SMESH.FACE,SMESH.FT_Skew,SMESH.FT_MoreThan,80,SMESH.FT_Undefined,SMESH.FT_Undefined,1.23699e-311)
aCriteria.append(aCriterion)
aCriteria = []
aCriterion = smesh.GetCriterion(SMESH.FACE,SMESH.FT_Skew,SMESH.FT_MoreThan,80,SMESH.FT_Undefined,SMESH.FT_Undefined,1.23699e-311)
aCriteria.append(aCriterion)
NETGEN_2D_Parameters_1.SetNbSurfOptSteps( 6 )
NETGEN_2D_Parameters_1.SetWorstElemMeasure( 147 )
NETGEN_2D_Parameters_1.SetCheckChartBoundary( 144 )
isDone = Mesh_1.Compute()
aFilterLibrary0000024629EE8980 = aFilterManager.LoadLibrary('C:/Users/DELL/FilterLib.xml')
aCriteria = []
aFilterLibrary0000024629EE8980.AddEmpty('VolumeFilter_1',SMESH.VOLUME)
aCriteria = []
aFilterLibrary0000024629EE8980.Copy('VolumeFilter_1')
aFilterLibrary0000024629EE8980.Delete('VolumeFilter_1')
aCriteria = []
aFilterLibrary0000024629EE8980.AddEmpty('FaceFilter_1',SMESH.FACE)
aCriteria = []
aFilterLibrary0000024629EE8980.Copy('FaceFilter_1')
aCriteria = []
aCriterion = smesh.GetCriterion(SMESH.FACE,SMESH.FT_Skew,SMESH.FT_MoreThan,80); aCriterion.Precision = 147
aCriteria.append(aCriterion)
aFilterLibrary0000024629EE8980.Replace('FaceFilter_1','FaceFilter_1',aFilter000002461FB97700)
aFilterLibrary0000024629EE8980.Save()
aFilterLibrary0000024629EE83D0 = aFilterManager.LoadLibrary('C:/Users/DELL/FilterLib.xml')
aCriteria = []
aCriterion = smesh.GetCriterion(SMESH.FACE,SMESH.FT_Skew,SMESH.FT_MoreThan,80)
aCriteria.append(aCriterion)
aFilterLibrary0000024629EE83D0.Copy('FaceFilter_1')
aFilterLibrary0000024629EE7050 = aFilterManager.LoadLibrary('C:/Users/DELL/FilterLib.xml')
aCriteria = []
aCriterion = smesh.GetCriterion(SMESH.FACE,SMESH.FT_Skew,SMESH.FT_MoreThan,80)
aCriteria.append(aCriterion)
aFilterLibrary0000024629EE7050.Copy('FaceFilter_1')
aFilterLibrary000002462B03D2B0 = aFilterManager.LoadLibrary('C:/Users/DELL/FilterLib.xml')
aCriteria = []
aFilterLibrary000002462B03D2B0.AddEmpty('FaceFilter_2',SMESH.FACE)
aCriteria = []
aFilterLibrary000002462B03D2B0.Copy('FaceFilter_2')
aCriteria = []
aCriterion = smesh.GetCriterion(SMESH.FACE,SMESH.FT_Skew,SMESH.FT_MoreThan,80)
aCriteria.append(aCriterion)
aFilterLibrary000002462B03D2B0.Copy('FaceFilter_1')
aCriteria = []
aCriterion = smesh.GetCriterion(SMESH.FACE,SMESH.FT_Skew,SMESH.FT_MoreThan,80); aCriterion.Precision = 147
aCriteria.append(aCriterion)
aFilterLibrary000002462B03D2B0.Replace('FaceFilter_1','FaceFilter_1',aFilter000002463A7923A0)
aFilterLibrary000002462B03D2B0.Save()
aFilterLibrary000002462B03F810 = aFilterManager.LoadLibrary('C:/Users/DELL/FilterLib.xml')
aCriteria = []
aFilterLibrary000002462B03F810.AddEmpty('FaceFilter_3',SMESH.FACE)
aCriteria = []
aFilterLibrary000002462B03F810.Copy('FaceFilter_3')
aFilterLibrary000002462B03D930 = aFilterManager.LoadLibrary('C:/Users/DELL/FilterLib.xml')
aCriteria = []
aCriterion = smesh.GetCriterion(SMESH.FACE,SMESH.FT_Skew,SMESH.FT_MoreThan,80)
aCriteria.append(aCriterion)
aFilterLibrary000002462B03D930.Copy('FaceFilter_1')
aCriteria = []
aFilterLibrary000002462B03D930.Copy('FaceFilter_2')
aCriteria = []
aCriterion = smesh.GetCriterion(SMESH.FACE,SMESH.FT_Skew,SMESH.FT_MoreThan,80)
aCriteria.append(aCriterion)
aFilterLibrary000002462B03D930.Copy('FaceFilter_1')
aCriteria = []
aCriterion = smesh.GetCriterion(SMESH.FACE,SMESH.FT_Skew,SMESH.FT_MoreThan,80)
aCriteria.append(aCriterion)
aCriteria = []
aCriterion = smesh.GetCriterion(SMESH.FACE,SMESH.FT_Skew,SMESH.FT_MoreThan,80,SMESH.FT_Undefined,SMESH.FT_Undefined,1.23912e-311)
aCriteria.append(aCriterion)
aFilterLibrary000002462B043B80 = aFilterManager.LoadLibrary('C:/Users/DELL/FilterLib.xml')
aCriteria = []
aFilterLibrary000002462B043B80.Copy('FaceFilter_2')
aCriteria = []
aCriterion = smesh.GetCriterion(SMESH.FACE,SMESH.FT_Skew,SMESH.FT_MoreThan,80)
aCriteria.append(aCriterion)
aFilterLibrary000002462B043B80.Copy('FaceFilter_1')
aCriteria = []
aCriterion = smesh.GetCriterion(SMESH.FACE,SMESH.FT_AspectRatio,SMESH.FT_MoreThan,10)
aCriteria.append(aCriterion)
isDone = Mesh_1.Compute()
aFilterLibrary000002462B03D790 = aFilterManager.LoadLibrary('C:/Users/DELL/FilterLib.xml')
aFilterLibrary000002462B0409F0 = aFilterManager.LoadLibrary('C:/Users/DELL/FilterLib.xml')
aFilterLibrary000002462B044FD0 = aFilterManager.LoadLibrary('C:/Users/DELL/FilterLib.xml')
aCriteria = []
aFilterLibrary000002462B044FD0.Copy('FaceFilter_2')
aCriteria = []
aFilterLibrary000002462B044FD0.Replace('FaceFilter_2','FaceFilter_2',aFilter000002463A790850)
aCriteria = []
aCriterion = smesh.GetCriterion(SMESH.FACE,SMESH.FT_Skew,SMESH.FT_MoreThan,80)
aCriteria.append(aCriterion)
aFilterLibrary000002462B044FD0.Copy('FaceFilter_1')
aFilterLibrary000002462B044C90 = aFilterManager.LoadLibrary('C:/Users/DELL/FilterLib.xml')
aFilterLibrary000002462B04BD80 = aFilterManager.LoadLibrary('C:/Users/DELL/FilterLib.xml')
aFilterLibrary000002462B04B3C0 = aFilterManager.LoadLibrary('C:/Users/DELL/FilterLib.xml')
aFilterLibrary000002462B0495B0 = aFilterManager.LoadLibrary('C:/Users/DELL/FilterLib.xml')
aFilterLibrary000002462B043500 = aFilterManager.LoadLibrary('C:/Users/DELL/FilterLib.xml')
aCriteria = []
aFilterLibrary000002462B043500.Copy('FaceFilter_2')
aCriteria = []
aFilterLibrary000002462B043500.Replace('FaceFilter_2','FaceFilter_2',aFilter000002463A7943B0)
aCriteria = []
aCriterion = smesh.GetCriterion(SMESH.FACE,SMESH.FT_Skew,SMESH.FT_MoreThan,80)
aCriteria.append(aCriterion)
aFilterLibrary000002462B043500.Copy('FaceFilter_1')
aCriteria = []
aCriterion = smesh.GetCriterion(SMESH.FACE,SMESH.FT_Skew,SMESH.FT_MoreThan,80); aCriterion.Precision = 0
aCriteria.append(aCriterion)
aFilterLibrary000002462B043500.Replace('FaceFilter_1','FaceFilter_1',aFilter000002463A7956B0)
aCriteria = []
aFilterLibrary000002462B043500.AddEmpty('NodeFilter_1',SMESH.NODE)
aCriteria = []
aFilterLibrary000002462B043500.Copy('NodeFilter_1')
isDone = Mesh_1.SmoothParametricObject( Mesh_1, [], 20, 1.1, SMESH.SMESH_MeshEditor.LAPLACIAN_SMOOTH )
isDone = Mesh_1.SmoothParametricObject( Mesh_1, [], 20, 1.1, SMESH.SMESH_MeshEditor.CENTROIDAL_SMOOTH )
aFilterLibrary000002462B040440 = aFilterManager.LoadLibrary('C:/Users/DELL/FilterLib.xml')
aCriteria = []
aFilterLibrary000002462B040440.Copy('FaceFilter_2')
aCriteria = []
aCriterion = smesh.GetCriterion(SMESH.FACE,SMESH.FT_Skew,SMESH.FT_MoreThan,80)
aCriteria.append(aCriterion)
aFilterLibrary000002462B040440.Copy('FaceFilter_1')
aCriteria = []
aCriterion = smesh.GetCriterion(SMESH.FACE,SMESH.FT_Skew,SMESH.FT_MoreThan,80)
aCriteria.append(aCriterion)
aFilterLibrary000002462B04B630 = aFilterManager.LoadLibrary('C:/Users/DELL/FilterLib.xml')
aCriteria = []
aCriterion = smesh.GetCriterion(SMESH.FACE,SMESH.FT_Skew,SMESH.FT_MoreThan,80); aCriterion.Precision = 147
aCriteria.append(aCriterion)
aFilterLibrary000002462B04B630.Save()
aCriteria = []
aCriterion = smesh.GetCriterion(SMESH.FACE,SMESH.FT_Skew,SMESH.FT_MoreThan,80); aCriterion.Precision = 147
aCriteria.append(aCriterion)
aFilterLibrary000002462B04B630.Save()
aFilterLibrary000002462B0464F0 = aFilterManager.LoadLibrary('C:/Users/DELL/FilterLib.xml')
aFilterLibrary000002462B038A60 = aFilterManager.LoadLibrary('C:/Users/DELL/FilterLib.xml')
aCriteria = []
aFilterLibrary000002462B038A60.Copy('FaceFilter_2')
aCriteria = []
aCriterion = smesh.GetCriterion(SMESH.FACE,SMESH.FT_Skew,SMESH.FT_MoreThan,80)
aCriteria.append(aCriterion)
aFilterLibrary000002462B038A60.Copy('FaceFilter_1')
aCriteria = []
aCriterion = smesh.GetCriterion(SMESH.FACE,SMESH.FT_Skew,SMESH.FT_MoreThan,80)
aCriteria.append(aCriterion)
aCriteria = []
aCriterion = smesh.GetCriterion(SMESH.FACE,SMESH.FT_Skew,SMESH.FT_MoreThan,80,SMESH.FT_Undefined,SMESH.FT_Undefined,1.23912e-311)
aCriteria.append(aCriterion)
#isDone = Mesh_1.SmoothParametricObject( smeshObj_1, [], 20, 1.1, SMESH.SMESH_MeshEditor.LAPLACIAN_SMOOTH ) ### smeshObj_1 has not been yet created
#isDone = Mesh_1.SmoothParametricObject( smeshObj_1, [], 20, 1.1, SMESH.SMESH_MeshEditor.LAPLACIAN_SMOOTH ) ### smeshObj_1 has not been yet created
#isDone = Mesh_1.SmoothParametricObject( smeshObj_1, [], 20, 1.1, SMESH.SMESH_MeshEditor.CENTROIDAL_SMOOTH ) ### smeshObj_1 has not been yet created
#isDone = Mesh_1.SmoothObject( smeshObj_1, [], 20, 1.1, SMESH.SMESH_MeshEditor.CENTROIDAL_SMOOTH ) ### smeshObj_1 has not been yet created
#isDone = Mesh_1.SmoothObject( smeshObj_1, [], 20, 1.1, SMESH.SMESH_MeshEditor.CENTROIDAL_SMOOTH ) ### smeshObj_1 has not been yet created
#isDone = Mesh_1.SmoothObject( smeshObj_1, [], 20, 1.1, SMESH.SMESH_MeshEditor.LAPLACIAN_SMOOTH ) ### smeshObj_1 has not been yet created
#isDone = Mesh_1.SmoothObject( smeshObj_1, [], 20, 1.1, SMESH.SMESH_MeshEditor.LAPLACIAN_SMOOTH ) ### smeshObj_1 has not been yet created
NETGEN_2D_Parameters_1.SetMaxSize( 14 )
NETGEN_2D_Parameters_1.SetMinSize( 2.5 )
NETGEN_2D_Parameters_1.SetSecondOrder( 0 )
NETGEN_2D_Parameters_1.SetOptimize( 1 )
NETGEN_2D_Parameters_1.SetFineness( 5 )
NETGEN_2D_Parameters_1.SetGrowthRate( 0.2 )
NETGEN_2D_Parameters_1.SetNbSegPerEdge( 1 )
NETGEN_2D_Parameters_1.SetNbSegPerRadius( 20 )
NETGEN_2D_Parameters_1.SetChordalError( 0 )
NETGEN_2D_Parameters_1.SetChordalErrorEnabled( 0 )
NETGEN_2D_Parameters_1.SetUseSurfaceCurvature( 1 )
NETGEN_2D_Parameters_1.SetFuseEdges( 1 )
NETGEN_2D_Parameters_1.SetQuadAllowed( 0 )
NETGEN_2D_Parameters_1.SetWorstElemMeasure( 67 )
NETGEN_2D_Parameters_1.SetCheckChartBoundary( 224 )
isDone = Mesh_1.Compute()
isDone = Mesh_1.SmoothParametricObject( Mesh_1, [], 20, 1.1, SMESH.SMESH_MeshEditor.LAPLACIAN_SMOOTH )
isDone = Mesh_1.SmoothParametricObject( Mesh_1, [], 20, 1.1, SMESH.SMESH_MeshEditor.CENTROIDAL_SMOOTH )
isDone = Mesh_1.SmoothParametricObject( Mesh_1, [], 40, 1.1, SMESH.SMESH_MeshEditor.LAPLACIAN_SMOOTH )
isDone = Mesh_1.SmoothParametricObject( Mesh_1, [], 20, 1.1, SMESH.SMESH_MeshEditor.CENTROIDAL_SMOOTH )
isDone = Mesh_1.SmoothParametricObject( Mesh_1, [], 100, 1.1, SMESH.SMESH_MeshEditor.LAPLACIAN_SMOOTH )
NETGEN_3D = Mesh_1.Tetrahedron()
NETGEN_3D_Parameters_1 = NETGEN_3D.Parameters()
NETGEN_3D_Parameters_1.SetMaxSize( 4 )
NETGEN_3D_Parameters_1.SetMinSize( 0.75 )
NETGEN_3D_Parameters_1.SetOptimize( 1 )
NETGEN_3D_Parameters_1.SetFineness( 3 )
NETGEN_3D_Parameters_1.SetNbVolOptSteps( 5 )
NETGEN_3D_Parameters_1.SetCheckOverlapping( 0 )
NETGEN_3D_Parameters_1.SetElemSizeWeight( 9.86529e-312 )
NETGEN_3D_Parameters_1.SetCheckChartBoundary( 224 )
isDone = Mesh_1.Compute()


## Set names of Mesh objects
smesh.SetName(NETGEN_1D_2D.GetAlgorithm(), 'NETGEN 1D-2D')
smesh.SetName(NETGEN_3D.GetAlgorithm(), 'NETGEN 3D')
smesh.SetName(NETGEN_2D_Parameters_1, 'NETGEN 2D Parameters_1')
smesh.SetName(NETGEN_3D_Parameters_1, 'NETGEN 3D Parameters_1')
smesh.SetName(Mesh_1.GetMesh(), 'Mesh_1')
smesh.SetName(Volume_1, 'Volume')
smesh.SetName(outlet_1, 'outlet')
smesh.SetName(inlet_1, 'inlet')


if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser()
