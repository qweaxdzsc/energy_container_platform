import salome
import GEOM
from salome.geom import geomBuilder
import math
import SALOMEDS
import os

# ============input parameter============
input_step = r"E:\project_simulation\energy_container\container_V1\coolant_V2\coolant_plate_V1_simplified.stp"
output_mesh = r"E:\project_simulation\energy_container\container_V1\coolant_V2\mesh_coolant.unv"
save_study_file = r"E:\project_simulation\energy_container\container_V1\coolant_V2\study_new"
stp_name = os.path.split(input_step)[1]
stp_name = os.path.splitext(stp_name)[0]
compound_list = list()
solid_list = list()
solid_str_list = list()
BCg_list = list()
BCmg_list = list()
compound_str_list = ['volume']
face_id_dict = {"inlet": 204, "outlet": 186}
# ========== init ================
geompy = geomBuilder.New()

# ====================================
geo_obj = geompy.ImportSTEP(input_step, True, True)
geompy.addToStudy(geo_obj, stp_name)

compound_list = geompy.ExtractShapes(geo_obj, geompy.ShapeType["COMPOUND"], False)
for c_id, comp in enumerate(compound_list):
    compound_name = str(compound_str_list[c_id])
    geompy.addToStudyInFather(geo_obj, comp, compound_name)
    solid_list = geompy.ExtractShapes(comp, geompy.ShapeType["SOLID"], False)
    for s_id, solid in enumerate(solid_list):
        solid_name = f'{compound_name}{s_id + 1}'
        geompy.addToStudyInFather(comp, solid, solid_name)
        solid_str_list.append(solid_name)

# geompy.SubShapeAll(Shape, Type)
id_list = geompy.SubShapeAllIDs(geo_obj, geompy.ShapeType["FACE"])

# use sequence to lock BC name, and build connection with group
for bc in face_id_dict.keys():
    face_indices = id_list[face_id_dict[bc]]
    bc_group = geompy.CreateGroup(geo_obj, geompy.ShapeType["FACE"])
    geompy.UnionIDs(bc_group, [face_indices])
    # add group to study under main object
    geompy.addToStudyInFather(geo_obj, bc_group, bc)
    BCg_list.append(bc_group)

if salome.sg.hasDesktop():
    salome.sg.updateObjBrowser()

# Get geometry object from current study
# from salome.geom import geomtools
# geotool = geomtools.GeomStudyTools()
# small_test = geotool.getGeomObjectFromEntry("0:1:1:5")
# small_test.GetName()
# # geomtools.getGeompy()
# # geo_obj = geompy.GetObject("0:1:5")

# =========================== Mesh Component ===============================================
# =========================================================================================
import SMESH, SALOMEDS
from salome.smesh import smeshBuilder

# init mesh
smesh = smeshBuilder.New()

# create mesh
Mesh_All = smesh.Mesh(geo_obj, 'Mesh_All')

# create group from geometry module
for index, solid in enumerate(solid_list):
    mg_solid1 = Mesh_All.GroupOnGeom(solid, solid_str_list[index], SMESH.VOLUME)

for index, group in enumerate(BCg_list):
    mesh_group = Mesh_All.GroupOnGeom(group, list(face_id_dict.keys())[index], SMESH.FACE)
    BCmg_list.append(mesh_group)

# set Mesh parameter for 1D-2D
NETGEN_1D_2D = Mesh_All.Triangle(algo=smeshBuilder.NETGEN_1D2D)
NETGEN_2D_Parameters_1 = NETGEN_1D_2D.Parameters()
NETGEN_2D_Parameters_1.SetMaxSize(14)
NETGEN_2D_Parameters_1.SetMinSize(2.5)
NETGEN_2D_Parameters_1.SetSecondOrder(0)
NETGEN_2D_Parameters_1.SetOptimize(1)
NETGEN_2D_Parameters_1.SetFineness(5)
NETGEN_2D_Parameters_1.SetGrowthRate(0.2)
NETGEN_2D_Parameters_1.SetNbSegPerEdge(1)
NETGEN_2D_Parameters_1.SetNbSegPerRadius(20)
NETGEN_2D_Parameters_1.SetChordalError(0)
NETGEN_2D_Parameters_1.SetChordalErrorEnabled(0)
NETGEN_2D_Parameters_1.SetUseSurfaceCurvature(1)
NETGEN_2D_Parameters_1.SetFuseEdges(1)
NETGEN_2D_Parameters_1.SetQuadAllowed(0)
NETGEN_2D_Parameters_1.SetWorstElemMeasure(67)
NETGEN_2D_Parameters_1.SetCheckChartBoundary(224)

# compute 1D-2D Mesh
isDone = Mesh_All.Compute()

# smooth surface Mesh to get better quality
isDone = Mesh_All.SmoothParametricObject(Mesh_All, [], 40, 10, SMESH.SMESH_MeshEditor.LAPLACIAN_SMOOTH)
isDone = Mesh_All.SmoothParametricObject(Mesh_All, [], 40, 10, SMESH.SMESH_MeshEditor.CENTROIDAL_SMOOTH)
isDone = Mesh_All.SmoothParametricObject(Mesh_All, [], 40, 5, SMESH.SMESH_MeshEditor.LAPLACIAN_SMOOTH)
isDone = Mesh_All.SmoothParametricObject(Mesh_All, [], 40, 5, SMESH.SMESH_MeshEditor.CENTROIDAL_SMOOTH)
isDone = Mesh_All.SmoothParametricObject(Mesh_All, [], 40, 1.5, SMESH.SMESH_MeshEditor.LAPLACIAN_SMOOTH)
isDone = Mesh_All.SmoothParametricObject(Mesh_All, [], 40, 1.5, SMESH.SMESH_MeshEditor.CENTROIDAL_SMOOTH)

# set Mesh parameter for 3D
NETGEN_3D = Mesh_All.Tetrahedron()
NETGEN_3D_Parameters_1 = NETGEN_3D.Parameters()
NETGEN_3D_Parameters_1.SetMaxSize(4)
NETGEN_3D_Parameters_1.SetMinSize(0.75)
NETGEN_3D_Parameters_1.SetOptimize(1)
NETGEN_3D_Parameters_1.SetFineness(3)
NETGEN_3D_Parameters_1.SetNbVolOptSteps(5)
NETGEN_3D_Parameters_1.SetCheckOverlapping(0)
NETGEN_3D_Parameters_1.SetElemSizeWeight(9.86529e-312)
NETGEN_3D_Parameters_1.SetCheckChartBoundary(224)

# compute 3D Mesh
isDone = Mesh_All.Compute()

# Set names of Mesh objects
# smesh.SetName(NETGEN_1D_2D.GetAlgorithm(), 'NETGEN 1D-2D')
# smesh.SetName(NETGEN_3D.GetAlgorithm(), 'NETGEN 3D')
# smesh.SetName(NETGEN_2D_Parameters_1, 'NETGEN 2D Parameters_1')
# smesh.SetName(NETGEN_3D_Parameters_1, 'NETGEN 3D Parameters_1')
# smesh.SetName(Mesh_All.GetMesh(), 'Mesh_All')
# smesh.SetName(Volume_1, 'Volume')
# smesh.SetName(outlet_1, 'outlet')
# smesh.SetName(inlet_1, 'inlet')
Mesh_All.ExportUNV(output_mesh)

if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser()

salome.myStudy.SaveAs(save_study_file, 0, 0)
