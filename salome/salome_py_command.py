import os


class SalomeScript(object):
    def __init__(self, project_path, script_name, logger, compound_str_list='list()', bc_id_dict='dict()', script_content=''):
        self.project_path = project_path
        self.script_name = script_name
        self.logger = logger
        self.script_content = script_content
        self.compound_str_list = compound_str_list
        self.bc_id_dict = bc_id_dict

        self.main_geo_obj = "geo_obj"
        self.main_mesh_obj = "Mesh_All"
        self.face_id_list = "id_list"

        self.geom = Geom(self)
        self.mesh = Mesh(self)

    def salome_init(self):
        text = f"""
import salome
import os
import time
"""
        self.script_content += text

    def update_gui(self):
        text = """
if salome.sg.hasDesktop():
    salome.sg.updateObjBrowser()
"""
        self.script_content += text

    def open_study(self, file_path):
        text = f"""
salome.myStudy.Open(r"{file_path}")
"""
        self.script_content += text

    def save_study(self, file_path):
        text = f"""
salome.myStudy.SaveAs(r"{file_path}", 0, 0)
"""
        self.script_content += text

    def get_geo_obj(self, geo_obj):
        text = f"""
geo_obj = salome.myStudy.FindObject("{geo_obj}").GetObject()
"""
        self.script_content += text

    def done_output(self):
        script_file = f"{self.project_path}\\{self.script_name}"
        with open(script_file, 'w') as f:
            f.write(self.script_content)

    def exit_salome(self):
        text = f"""
exit()
"""
        self.script_content += text


class Geom(object):
    def __init__(self, salome):
        self.salome = salome
        self.salome.logger.info('create_object_mesh')

    def geo_init(self):
        text = """
from salome.geom import geomBuilder

geompy = geomBuilder.New()
project_path = r"%s"
compound_str_list = %s
compound_list = list()
solid_list = list()
solid_str_list = list()
BCg_list = list()
BCmg_list = list()
face_id_dict = %s
""" % (self.salome.project_path, self.salome.compound_str_list, self.salome.bc_id_dict)
        self.salome.script_content += text

    def import_step(self, input_step, ignore_unit=True, create_assemble=True):
        stp_name = os.path.split(input_step)[1]
        stp_name = os.path.splitext(stp_name)[0]
        text = f"""
{self.salome.main_geo_obj} = geompy.ImportSTEP(r"{input_step}", {ignore_unit}, {create_assemble})
"""
        self.salome.script_content += text
        self.add_to_study(stp_name)

    def add_to_study(self, name, father=False):
        if father:
            text = f"""
geompy.addToStudyInFather({father}, {self.salome.main_geo_obj}, "{name}")
"""
        else:
            text = f"""
geompy.addToStudy({self.salome.main_geo_obj}, "{name}")
"""
        self.salome.script_content += text

    def extract_subshapes(self, shape_type, result_obj_list, to_sort=False):
        """
        :param result_obj_list: return list[], containe shape object
        :param main_shape_obj:
        :param shape_type: such as COMPOUND, FACE
        :param to_sort:
        :return:
        """
        text = f"""
{result_obj_list} = geompy.ExtractShapes({self.salome.main_geo_obj}, geompy.ShapeType["{shape_type}"], {to_sort})
"""
        self.salome.script_content += text

    def extract_all_solids(self):
        """
        packed function to extract all compounds and solids
        :return:
        """
        text = """
compound_list = geompy.ExtractShapes(%s, geompy.ShapeType["COMPOUND"], False)
for c_id, comp in enumerate(compound_list):
    compound_name = str(compound_str_list[c_id])
    geompy.addToStudyInFather(%s, comp, compound_name)
    solids = geompy.ExtractShapes(comp, geompy.ShapeType["SOLID"], False)
    solid_list.extend(solids)
    for s_id, solid in enumerate(solids):
        solid_name = f'{compound_name}{s_id + 1}'
        geompy.addToStudyInFather(comp, solid, solid_name)
        solid_str_list.append(solid_name)
""" % (self.salome.main_geo_obj, self.salome.main_geo_obj)
        self.salome.script_content += text

    def get_face_id_list(self):
        text = f"""
{self.salome.face_id_list} = geompy.SubShapeAllIDs({self.salome.main_geo_obj}, geompy.ShapeType["FACE"])
"""
        self.salome.script_content += text

    def build_face_group(self):
        text = f"""
for bc in face_id_dict.keys():
    bc_group = geompy.CreateGroup({self.salome.main_geo_obj}, geompy.ShapeType["FACE"])
    geompy.UnionIDs(bc_group, face_id_dict[bc])
    # add group to study under main object
    geompy.addToStudyInFather({self.salome.main_geo_obj}, bc_group, bc)
    BCg_list.append(bc_group)
"""
        self.salome.script_content += text


# ============================================================================================================


class Mesh(object):
    def __init__(self, salome):
        self.salome = salome
        self.tet_param = dict()
        self.salome.logger.info('create_object_mesh')

    def mesh_init(self):
        text = """
import SMESH, SALOMEDS
from salome.smesh import smeshBuilder
# init mesh
smesh = smeshBuilder.New()
"""
        self.salome.script_content += text

    def create_main_mesh(self):
        text = f"""
# init mesh
{self.salome.main_mesh_obj} = smesh.Mesh({self.salome.main_geo_obj}, '{self.salome.main_mesh_obj}')
"""
        self.salome.script_content += text

    def group_from_geo(self):
        text = f"""
# create group from geometry module
for index, solid in enumerate(solid_list):
    mg_solid1 = {self.salome.main_mesh_obj}.GroupOnGeom(solid, solid_str_list[index], SMESH.VOLUME)

for index, group in enumerate(BCg_list):
    mesh_group = {self.salome.main_mesh_obj}.GroupOnGeom(group, list(face_id_dict.keys())[index], SMESH.FACE)
    BCmg_list.append(mesh_group)
"""
        self.salome.script_content += text

    def submesh_2D_tet(self, solid_obj, solid_name, max_size_2d, min_size_2d):
        text = f"""
algo_2D = {self.salome.main_mesh_obj}.Triangle(algo=smeshBuilder.GMSH_2D, geom={solid_obj})
algo_2D_param = algo_2D.Parameters()
algo_2D_param.Set2DAlgo(1)
algo_2D_param.SetMinSize({min_size_2d})
algo_2D_param.SetMaxSize({max_size_2d})
algo_2D_param.SetMeshCurvatureSize(18)
algo_2D_param.SetSizeFactor(1)
algo_2D_param.SetRemeshAlgo(1)
algo_2D_param.SetSmouthSteps(5)
algo_2D_param.SetIs2d(1)
# compute 1D-2D Mesh
sub_mesh = algo_2D.GetSubMesh()
isDone = sub_mesh.Compute()
# set name
smesh.SetName(sub_mesh, f'mesh_{solid_name}')
smesh.SetName(algo_2D_param, f'param2D_{solid_name}')
"""
        self.salome.script_content += text

    def collapse_sliver(self, skew_criteria=60, area_criteria=0.5, collapse_iter=30, merge_tolerance_init=0.1, merge_max_tolerance=5):
        text = f"""
# set bad skew criteria
criterion_area = smesh.GetCriterion(SMESH.FACE, SMESH.FT_Area, SMESH.FT_LessThan, {area_criteria}, SMESH.FT_Undefined, SMESH.FT_LogicalOR)
criterion_skew = smesh.GetCriterion(SMESH.FACE, SMESH.FT_Skew, SMESH.FT_MoreThan, {skew_criteria})
collapse_filter = smesh.GetFilterFromCriteria([criterion_area, criterion_skew])
collapse_filter.SetMesh({self.salome.main_mesh_obj}.GetMesh())
# construct group to contain bad face
bad_face_group = {self.salome.main_mesh_obj}.GroupOnFilter(SMESH.FACE, 'bad_face_group', collapse_filter)
bad_face_nodes = bad_face_group.GetNumberOfNodes()
# find all nodes on group
collapse_iter = {collapse_iter}
merge_tolerance = {merge_tolerance_init}
merge_max_tolerance = {merge_max_tolerance}
for i in range(collapse_iter):
    if bad_face_nodes == 0:
        break
    coincident_nodes_on_part = {self.salome.main_mesh_obj}.FindCoincidentNodesOnPart([bad_face_group], merge_tolerance, [], 0)
    # MergeNodes to collapse bad face
    while len(coincident_nodes_on_part) == 0:
        if merge_tolerance < merge_max_tolerance:
            merge_tolerance *= 1.2
            coincident_nodes_on_part = {self.salome.main_mesh_obj}.FindCoincidentNodesOnPart([bad_face_group], merge_tolerance, [], 0)
    if len(coincident_nodes_on_part) > 0:
        {self.salome.main_mesh_obj}.MergeNodes(coincident_nodes_on_part, [], 1)
        bad_face_nodes = bad_face_group.GetNumberOfNodes()
{self.salome.main_mesh_obj}.RemoveGroup(bad_face_group)
"""
        self.salome.script_content += text

    def submesh_3D_tet(self, solid_obj, solid_name, max_size_3d, min_size_3d):
        text = f"""
algo_3D = {self.salome.main_mesh_obj}.Tetrahedron(geom={solid_obj})
algo_3D_param = algo_3D.Parameters()
algo_3D_param.SetMaxSize({max_size_3d})
algo_3D_param.SetMinSize({min_size_3d})
algo_3D_param.SetFineness(3)
algo_3D_param.SetNbVolOptSteps(5)
algo_3D_param.SetOptimize(1)
algo_3D_param.SetCheckOverlapping(0)
algo_3D_param.SetElemSizeWeight(9.86529e-312)
algo_3D_param.SetCheckChartBoundary(128)
# compute 3D Mesh
isDone = sub_mesh.Compute()
smesh.SetName(sub_mesh, f'mesh_{solid_name}')
smesh.SetName(algo_3D_param, f'param3D_{solid_name}')
"""
        self.salome.script_content += text

    def make_3D_tet_function(self, function_name):
        text = f"""
def {function_name}(solid_obj, solid_name, max_size_2d, min_size_2d, max_size_3d, min_size_3d, area_criteria, skew_criteria, collapse_iter, merge_tolerance_init, merge_max_tolerance):
    algo_2D = {self.salome.main_mesh_obj}.Triangle(algo=smeshBuilder.GMSH_2D, geom=solid_obj)
    algo_2D_param = algo_2D.Parameters()
    algo_2D_param.Set2DAlgo(1)
    algo_2D_param.SetMinSize(min_size_2d)
    algo_2D_param.SetMaxSize(max_size_2d)
    algo_2D_param.SetMeshCurvatureSize(18)
    algo_2D_param.SetSizeFactor(1)
    algo_2D_param.SetRemeshAlgo(1)
    algo_2D_param.SetSmouthSteps(10)
    algo_2D_param.SetIs2d(1)
    # compute 1D-2D Mesh
    sub_mesh = algo_2D.GetSubMesh()
    isDone = sub_mesh.Compute()
    # set name
    smesh.SetName(sub_mesh, f'mesh_{{solid_name}}')
    smesh.SetName(algo_2D_param, f'param2D_{{solid_name}}')
    # set bad skew criteria
    criterion_area = smesh.GetCriterion(SMESH.FACE, SMESH.FT_Area, SMESH.FT_LessThan, area_criteria, SMESH.FT_Undefined, SMESH.FT_LogicalOR)
    criterion_skew = smesh.GetCriterion(SMESH.FACE, SMESH.FT_Skew, SMESH.FT_MoreThan, skew_criteria)
    collapse_filter = smesh.GetFilterFromCriteria([criterion_area, criterion_skew])
    collapse_filter.SetMesh({self.salome.main_mesh_obj}.GetMesh())
    # construct group to contain bad face
    bad_face_group = {self.salome.main_mesh_obj}.GroupOnFilter(SMESH.FACE, 'bad_face_group', collapse_filter)
    bad_face_nodes = bad_face_group.GetNumberOfNodes()
    # find all nodes on group
    collapse_iter = collapse_iter
    merge_tolerance = merge_tolerance_init
    merge_max_tolerance = merge_max_tolerance
    for i in range(collapse_iter):
        if bad_face_nodes == 0:
            break
        coincident_nodes_on_part = {self.salome.main_mesh_obj}.FindCoincidentNodesOnPart([bad_face_group], merge_tolerance, [], 0)
        # MergeNodes to collapse bad face
        while len(coincident_nodes_on_part) == 0:
            if merge_tolerance < merge_max_tolerance:
                merge_tolerance *= 1.2
                coincident_nodes_on_part = {self.salome.main_mesh_obj}.FindCoincidentNodesOnPart([bad_face_group], merge_tolerance, [], 0)
        if len(coincident_nodes_on_part) > 0:
            {self.salome.main_mesh_obj}.MergeNodes(coincident_nodes_on_part, [], 1)
            bad_face_nodes = bad_face_group.GetNumberOfNodes()
    {self.salome.main_mesh_obj}.RemoveGroup(bad_face_group)
    algo_3D = {self.salome.main_mesh_obj}.Tetrahedron(geom=solid_obj)
    algo_3D_param = algo_3D.Parameters()
    algo_3D_param.SetMaxSize(max_size_3d)
    algo_3D_param.SetMinSize(min_size_3d)
    algo_3D_param.SetFineness(3)
    algo_3D_param.SetNbVolOptSteps(10)
    algo_3D_param.SetOptimize(1)
    algo_3D_param.SetCheckOverlapping(0)
    algo_3D_param.SetElemSizeWeight(9.86529e-312)
    algo_3D_param.SetCheckChartBoundary(128)
    # compute 3D Mesh
    isDone = sub_mesh.Compute()
    smesh.SetName(sub_mesh, f'mesh_{{solid_name}}')
    smesh.SetName(algo_3D_param, f'param3D_{{solid_name}}')
"""
        return text

    def make_2D_tet_function(self, function_name):
        text = f"""
def {function_name}(solid_obj, solid_name, max_size_2d, min_size_2d, area_criteria, skew_criteria, collapse_iter, merge_tolerance_init, merge_max_tolerance):
    algo_2D = {self.salome.main_mesh_obj}.Triangle(algo=smeshBuilder.GMSH_2D, geom=solid_obj)
    algo_2D_param = algo_2D.Parameters()
    algo_2D_param.Set2DAlgo(1)
    algo_2D_param.SetMinSize(min_size_2d)
    algo_2D_param.SetMaxSize(max_size_2d)
    algo_2D_param.SetMeshCurvatureSize(18)
    algo_2D_param.SetSizeFactor(1)
    algo_2D_param.SetRemeshAlgo(1)
    algo_2D_param.SetSmouthSteps(10)
    algo_2D_param.SetIs2d(1)
    # compute 1D-2D Mesh
    sub_mesh = algo_2D.GetSubMesh()
    isDone = sub_mesh.Compute()
    # set name
    smesh.SetName(sub_mesh, f'mesh_{{solid_name}}')
    smesh.SetName(algo_2D_param, f'param2D_{{solid_name}}')
    # set bad skew criteria
    criterion_area = smesh.GetCriterion(SMESH.FACE, SMESH.FT_Area, SMESH.FT_LessThan, area_criteria, SMESH.FT_Undefined, SMESH.FT_LogicalOR)
    criterion_skew = smesh.GetCriterion(SMESH.FACE, SMESH.FT_Skew, SMESH.FT_MoreThan, skew_criteria)
    collapse_filter = smesh.GetFilterFromCriteria([criterion_area, criterion_skew])
    collapse_filter.SetMesh({self.salome.main_mesh_obj}.GetMesh())
    # construct group to contain bad face
    bad_face_group = {self.salome.main_mesh_obj}.GroupOnFilter(SMESH.FACE, 'bad_face_group', collapse_filter)
    bad_face_nodes = bad_face_group.GetNumberOfNodes()
    # find all nodes on group
    collapse_iter = collapse_iter
    merge_tolerance = merge_tolerance_init
    merge_max_tolerance = merge_max_tolerance
    for i in range(collapse_iter):
        if bad_face_nodes == 0:
            break
        coincident_nodes_on_part = {self.salome.main_mesh_obj}.FindCoincidentNodesOnPart([bad_face_group], merge_tolerance, [], 0)
        # MergeNodes to collapse bad face
        while len(coincident_nodes_on_part) == 0:
            if merge_tolerance < merge_max_tolerance:
                merge_tolerance *= 1.2
                coincident_nodes_on_part = {self.salome.main_mesh_obj}.FindCoincidentNodesOnPart([bad_face_group], merge_tolerance, [], 0)
        if len(coincident_nodes_on_part) > 0:
            {self.salome.main_mesh_obj}.MergeNodes(coincident_nodes_on_part, [], 1)
            bad_face_nodes = bad_face_group.GetNumberOfNodes()
    {self.salome.main_mesh_obj}.RemoveGroup(bad_face_group)
"""
        return text

    def clear_tet_param(self):
        self.tet_param = dict()

    def add_3D_tet_param(self, compound_name, max_size_2d, min_size_2d, max_size_3d, min_size_3d, area_criteria=0.5,
                         skew_criteria=60, collapse_iter=30, merge_tolerance_init=0.1, merge_max_tolerance=5):
        self.tet_param[compound_name] = {
                                         "3D": True,
                                         "max_size_2d": max_size_2d,
                                         "min_size_2d": min_size_2d,
                                         "max_size_3d": max_size_3d,
                                         "min_size_3d": min_size_3d,
                                         "area_criteria": area_criteria,
                                         "skew_criteria": skew_criteria,
                                         "collapse_iter": collapse_iter,
                                         "merge_tolerance_init": merge_tolerance_init,
                                         "merge_max_tolerance": merge_max_tolerance,
                                         }
        self.salome.logger.info("Add tet param with %s" % self.tet_param)

    def add_2D_tet_param(self, compound_name, max_size_2d, min_size_2d, area_criteria=0.5,
                                 skew_criteria=60, collapse_iter=30, merge_tolerance_init=0.1, merge_max_tolerance=5):
        self.tet_param[compound_name] = {
                                         "3D": False,
                                         "max_size_2d": max_size_2d,
                                         "min_size_2d": min_size_2d,
                                         "area_criteria": area_criteria,
                                         "skew_criteria": skew_criteria,
                                         "collapse_iter": collapse_iter,
                                         "merge_tolerance_init": merge_tolerance_init,
                                         "merge_max_tolerance": merge_max_tolerance,
                                         }
        self.salome.logger.info("Add tet param with %s" % self.tet_param)

    def compute_all(self):
        if len(self.tet_param) > 0:
            tet_2d_function_name = "tet_2D_mesh"
            tet_3d_function_name = "tet_3D_mesh"
            function2d_text = self.make_2D_tet_function(tet_2d_function_name)
            function3d_text = self.make_3D_tet_function(tet_3d_function_name)
            loop_info = ""
            for name, param in self.tet_param.items():
                loop_info += f"""elif "{name}" in solid_name:\n"""
                if param["3D"]:
                    loop_info += f"""{"":>8}{tet_3d_function_name}(solid_list[index], solid_name, {param["max_size_2d"]}, \
{param["min_size_2d"]}, {param["max_size_3d"]}, {param["min_size_3d"]}, {param["area_criteria"]}, {param["skew_criteria"]}, \
{param["collapse_iter"]}, {param["merge_tolerance_init"]}, {param["merge_max_tolerance"]})"""
                else:
                    loop_info += f"""{"":>8}{tet_2d_function_name}(solid_list[index], solid_name, {param["max_size_2d"]}, \
{param["min_size_2d"]}, {param["area_criteria"]}, {param["skew_criteria"]}, \
{param["collapse_iter"]}, {param["merge_tolerance_init"]}, {param["merge_max_tolerance"]})"""

# tet_mesh(solid_list[index], solid_name, 5, 3, 3, 0.5)
            text = f"""
{function2d_text}
{function3d_text}
for index, solid_name in enumerate(solid_str_list):
    if False:
        pass
    {loop_info}
"""
            self.salome.script_content += text
        else:
            self.salome.logger.warning("No tet param find")

    def export_unv(self, output_mesh):
        text = f"""
{self.salome.main_mesh_obj}.ExportUNV(r"{output_mesh}")
"""
        self.salome.script_content += text

    def export_fms(self, output_mesh, template="./salomeTriSurf.py"):
        if os.path.exists(template):
            export_fms_py = f"{self.salome.project_path}\\export_fms.py"
            converter_fms = ""
            with open(template, 'r') as f:
                converter_fms = f.read()
            with open(export_fms_py, 'w') as f:
                f.write(converter_fms)
            text = f"""
with open("{export_fms_py}", 'r') as f:
    py_content = f.read()
    exec(py_content)
fms_obj = triSurf(Mesh_All)
fms_obj.writeFms("{output_mesh}")
"""
            self.salome.script_content += text
        else:
            self.salome.logger.error(f"the path:{os.getcwd()}\\{template} does not exits, ")

