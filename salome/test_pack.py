import salome
import GEOM
from salome.geom import geomBuilder
import math
import SALOMEDS
import os
import itertools

# ============input parameter============
input_step = r"E:\project_simulation\energy_container\container_V1\pack_simple_V1\pack_simple5.stp"
output_mesh = r"E:\project_simulation\energy_container\container_V1\pack_simple_V1\mesh_pack.unv"
save_study_file = r"E:\project_simulation\energy_container\container_V1\pack_simple_V1\study_new.hdf"
stp_name = os.path.split(input_step)[1]
stp_name = os.path.splitext(stp_name)[0]
compound_list = list()
solid_list = list()
solid_str_list = list()
BCg_list = list()
BCg_name_list = list()
BCmg_list = list()
compound_str_list = ['yelengban', 'fluid', "duanban", 'guoliuyuanjian', 'cell']
face_id_dict = {"inlet": 204, "outlet": 186}
BCg_name_list.extend(face_id_dict.keys())
# =========================Geometry init ================
geompy = geomBuilder.New()
O = geompy.MakeVertex(0, 0, 0)
OX = geompy.MakeVectorDXDYDZ(1, 0, 0)
OY = geompy.MakeVectorDXDYDZ(0, 1, 0)
OZ = geompy.MakeVectorDXDYDZ(0, 0, 1)
# ================import step into study===============
geo_obj = geompy.ImportSTEP(input_step, True, True)
geompy.addToStudy(geo_obj, stp_name)

# =================explode sub shape of stp, rename, add to study============
compound_list = geompy.ExtractShapes(geo_obj, geompy.ShapeType["COMPOUND"], False)
for c_id, comp in enumerate(compound_list):
    compound_name = str(compound_str_list[c_id])
    geompy.addToStudyInFather(geo_obj, comp, compound_name)
    solids = geompy.ExtractShapes(comp, geompy.ShapeType["SOLID"], False)
    solid_list.extend(solids)
    for s_id, solid in enumerate(solids):
        solid_name = f'{compound_name}{s_id + 1}'
        geompy.addToStudyInFather(comp, solid, solid_name)
        solid_str_list.append(solid_name)

id_list = geompy.SubShapeAllIDs(geo_obj, geompy.ShapeType["FACE"])
for bc in face_id_dict.keys():
    # use sequence to lock BC name, and build connection with group
    face_indices = id_list[face_id_dict[bc]]
    bc_group = geompy.CreateGroup(geo_obj, geompy.ShapeType["FACE"])
    geompy.UnionIDs(bc_group, [face_indices])
    # add group to study under main object
    geompy.addToStudyInFather(geo_obj, bc_group, bc)
    BCg_list.append(bc_group)

# ===================contact detection=====================================
interface_list = list()
for detect_combo in itertools.combinations(enumerate(solid_list), 2):
    solid1_obj = detect_combo[0][1]
    solid2_obj = detect_combo[1][1]
    solid1_name = solid_str_list[detect_combo[0][0]]
    solid2_name = solid_str_list[detect_combo[1][0]]
    # try fast intersect to detect all intersect obj
    try:
        isOk, res1, res2 = geompy.FastIntersect(solid1_obj, solid2_obj)
    except Exception as e:
        print('error: ', e)
        isOk = False
    else:
        if isOk:
            cont1 = geompy.SubShapes(solid1_obj, res1)
            cont2 = geompy.SubShapes(solid2_obj, res2)
            cont1_sf = list()
            cont2_sf = list()
            for common_combo in itertools.product(enumerate(cont1), enumerate(cont2)):
                # print(common_combo)
                cont1_obj = common_combo[0][1]
                cont2_obj = common_combo[1][1]
                cont1_ID = res1[common_combo[0][0]]
                cont2_ID = res2[common_combo[1][0]]
                common = geompy.MakeCommon(cont1_obj, cont2_obj)  # detect common
                props = geompy.BasicProperties(common)
                com_area_size = props[1]  # get area size property
                # ===get only the contacted surface
                if com_area_size > 0:
                    cont1_sf.append(cont1_obj)
                    cont2_sf.append(cont2_obj)
            # =====make contact group for first solid
            cont1_group = geompy.CreateGroup(geo_obj, geompy.ShapeType["FACE"])
            geompy.UnionList(cont1_group, cont1_sf)
            cont1_indices = cont1_group.GetSubShapeIndices()        # collect indices of contact surface
            # add to study only if group are not repeated
            if cont1_indices not in interface_list:
                name_group_i = f'interface_{solid1_name}_{solid2_name}'
                geompy.addToStudyInFather(geo_obj, cont1_group, name_group_i)
                interface_list.append(cont1_indices)
                BCg_list.append(cont1_group)
                BCg_name_list.append(name_group_i)
            # ====make contact group for second solid
            cont2_group = geompy.CreateGroup(geo_obj, geompy.ShapeType["FACE"])
            geompy.UnionList(cont2_group, cont2_sf)
            cont2_indices = cont2_group.GetSubShapeIndices()        # collect indices of contact surface
            # add to study only if group are not repeated
            if cont2_indices not in interface_list:
                # geompy.UnionIDs(cont2_group, cont2_sf)
                # comp_sf_j = geompy.MakeCompound(cont2_sf)
                name_group_j = f'interface_{solid2_name}_{solid1_name}'
                geompy.addToStudyInFather(geo_obj, cont2_group, name_group_j)
                interface_list.append(cont2_indices)
                BCg_list.append(cont2_group)
                BCg_name_list.append(name_group_j)

# print(interface_list)
if salome.sg.hasDesktop():
    salome.sg.updateObjBrowser()

# =================Get geometry object from current study========================
# from salome.geom import geomtools
#
# geotool = geomtools.GeomStudyTools()
# small_test = geotool.getGeomObjectFromEntry("0:1:1:5")
# small_test.GetName()
# # cell_comp = salome.myStudy.FindObject("cell").GetObject()
# geomtools.getGeompy()
# geo_obj = geompy.GetObject("0:1:5")

# ==================================== Mesh Part ==================================================
# =================================================================================================
import salome, SMESH, SALOMEDS
from salome.smesh import smeshBuilder

smesh = smeshBuilder.New()

# create mesh
Mesh_All = smesh.Mesh(geo_obj, 'Mesh_All')

# create group from geometry module
for index, solid in enumerate(solid_list):
    mg_solid1 = Mesh_All.GroupOnGeom(solid, solid_str_list[index], SMESH.VOLUME)

for index, group in enumerate(BCg_list):
    mesh_group = Mesh_All.GroupOnGeom(group, BCg_name_list[index], SMESH.FACE)
    BCmg_list.append(mesh_group)

def netgen1D2D_param():
    pass
    # algo_2D_param.SetMaxSize(max_size_2d)
    # algo_2D_param.SetMinSize(min_size_2d)
    # algo_2D_param.SetFineness(5)
    # algo_2D_param.SetGrowthRate(0.2)
    # algo_2D_param.SetNbSegPerEdge(1)
    # algo_2D_param.SetNbSegPerRadius(20)
    # algo_2D_param.SetChordalErrorEnabled(0)
    # algo_2D_param.SetChordalError(0)
    # algo_2D_param.SetUseSurfaceCurvature(1)
    # algo_2D_param.SetQuadAllowed(0)
    # algo_2D_param.SetSecondOrder(0)
    # algo_2D_param.SetOptimize(1)
    # algo_2D_param.SetFuseEdges(1)
    # algo_2D_param.SetWorstElemMeasure(2)
    # algo_2D_param.SetElemSizeWeight(0.3)
    # algo_2D_param.SetNbSurfOptSteps(3)
    # algo_2D_param.SetCheckChartBoundary(128)


def tet_mesh(solid_obj, solid_name, max_size_2d, min_size_2d, max_size_3d, min_size_3d, skew_criteria=60, area_criteria=0.5):
    algo_2D = Mesh_All.Triangle(algo=smeshBuilder.GMSH_2D, geom=solid_obj)
    algo_2D_param = algo_2D.Parameters()
    algo_2D_param.Set2DAlgo(1)
    algo_2D_param.SetMinSize(min_size_2d)
    algo_2D_param.SetMaxSize(max_size_2d)
    algo_2D_param.SetMeshCurvatureSize(10)
    algo_2D_param.SetSizeFactor(1)
    algo_2D_param.SetRemeshAlgo(1)
    algo_2D_param.SetSmouthSteps(3)
    algo_2D_param.SetIs2d(1)
    # compute 1D-2D Mesh
    sub_mesh = algo_2D.GetSubMesh()
    isDone = sub_mesh.Compute()
    # ====collapse bad Mesh to get better quality===
    # set bad skew criteria
    criterion_area = smesh.GetCriterion(SMESH.FACE, SMESH.FT_Area, SMESH.FT_LessThan, area_criteria, SMESH.FT_Undefined, SMESH.FT_LogicalOR)
    criterion_skew = smesh.GetCriterion(SMESH.FACE, SMESH.FT_Skew, SMESH.FT_MoreThan, skew_criteria)

    skew_filter = smesh.GetFilterFromCriteria([criterion_area, criterion_skew])
    skew_filter.SetMesh(Mesh_All.GetMesh())
    # construct group to contain bad face
    bad_face_group = Mesh_All.GroupOnFilter(SMESH.FACE, 'bad_face_group', skew_filter)
    bad_face_nodes = bad_face_group.GetNumberOfNodes()
    # find all nodes on group
    collapse_iter = 30
    merge_tolerance = 0.1
    merge_max_tolerance = 5
    for i in range(collapse_iter):
        if bad_face_nodes == 0:
            break
        coincident_nodes_on_part = Mesh_All.FindCoincidentNodesOnPart([bad_face_group], merge_tolerance, [], 0)
        # MergeNodes to collapse bad face
        while len(coincident_nodes_on_part) == 0:
            if merge_tolerance < merge_max_tolerance:
                merge_tolerance *= 1.2
                coincident_nodes_on_part = Mesh_All.FindCoincidentNodesOnPart([bad_face_group], merge_tolerance, [], 0)
        if len(coincident_nodes_on_part) > 0:
            Mesh_All.MergeNodes(coincident_nodes_on_part, [], 1)
            bad_face_nodes = bad_face_group.GetNumberOfNodes()
    Mesh_All.RemoveGroup(bad_face_group)
    # isDone = Mesh_All.SmoothParametricObject(sub_mesh, [], 40, 10, SMESH.SMESH_MeshEditor.LAPLACIAN_SMOOTH)
    # set Mesh parameter for 3D
    algo_3D = Mesh_All.Tetrahedron(geom=solid_obj)
    algo_3D_param = algo_3D.Parameters()
    algo_3D_param.SetMaxSize(max_size_3d)
    algo_3D_param.SetMinSize(min_size_3d)
    algo_3D_param.SetFineness(3)
    algo_3D_param.SetNbVolOptSteps(5)
    algo_3D_param.SetOptimize(1)
    algo_3D_param.SetCheckOverlapping(0)
    algo_3D_param.SetElemSizeWeight(9.86529e-312)
    algo_3D_param.SetCheckChartBoundary(128)
    # compute 3D Mesh
    isDone = sub_mesh.Compute()
    smesh.SetName(sub_mesh, f'mesh_{solid_name}')
    smesh.SetName(algo_2D_param, f'param2D_{solid_name}')
    smesh.SetName(algo_3D_param, f'param3D_{solid_name}')
    # smesh.SetName(algo_2D.GetAlgorithm(), f'algo2D_{solid_name}')
    # smesh.SetName(algo_3D.GetAlgorithm(), f'algo3D_{solid_name}')
    return isDone


# =============== Mesh Part: Cell ================================
for index, solid_name in enumerate(solid_str_list):
    if "guoliuyuanjian" in solid_name:
        tet_mesh(solid_list[index], solid_name, 5, 3, 3, 0.5)
    elif "duanban" in solid_name:
        tet_mesh(solid_list[index], solid_name, 4.5, 3.5, 10, 4)
    elif "cell" in solid_name:
        tet_mesh(solid_list[index], solid_name, 12, 3, 12, 4)
    elif "yelengban" in solid_name:
        tet_mesh(solid_list[index], solid_name, 6, 2.5, 4, 0.75)
    elif "fluid" in solid_name:
        tet_mesh(solid_list[index], solid_name, 6, 2.5, 4, 0.75)

if salome.sg.hasDesktop():
  salome.sg.updateObjBrowser()
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
