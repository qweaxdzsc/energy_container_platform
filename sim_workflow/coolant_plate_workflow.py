from salome.salome_py_command import SalomeScript, call_salome
from openfoam.foam_py import FoamPy, call_wsl_openfoam
import os


class CoolantPlateWorkflow(object):
    def __init__(self, project_path, param_dict, logger, call_config):
        self.project_path = project_path
        self.param = param_dict
        self.logger = logger
        self.salome_path = call_config['salome']
        self.openfoam_bashrc = call_config['openfoam']

        self.study_file_path_geo = f"{project_path}\\coolant_plate_geo.hdf"
        self.study_file_path_mesh = f"{project_path}\\coolant_plate_mesh.hdf"
        self.output_unv = f"{project_path}\\coolant_plate_mesh.unv"
        self.output_fms = f"{project_path}\\coolant_plate_fms.fms"

    def geo_struct(self):
        input_step = f"{self.project_path}\\{self.param['input_step']}"
        script_file_name = "salome_cp_geo.py"
        script_file_path = f"{self.project_path}\\{script_file_name}"
        preprocess_script = SalomeScript(self.project_path, script_file_name, self.logger,
                                         compound_str_list=self.param['compound_str_list'],
                                         bc_id_dict=self.param['bc_id_dict'])
        preprocess_script.salome_init()
        preprocess_script.geom.geo_init()
        preprocess_script.geom.import_step(input_step)
        preprocess_script.geom.extract_all_solids()
        # preprocess_script.geom.get_face_id_list()
        preprocess_script.geom.build_face_group()
        preprocess_script.update_gui()
        preprocess_script.save_study(self.study_file_path_geo)
        preprocess_script.exit_salome()
        preprocess_script.done_output()
        call_salome(self.salome_path, script_file_path, self.logger)

        interface_group = {}

        return interface_group

    def mesh(self):
        input_step = f"{self.project_path}\\{self.param['input_step']}"
        fms_py = r"./salome/salomeTriSurf.py"
        script_file_name = "salome_cp_mesh.py"
        script_file_path = f"{self.project_path}\\{script_file_name}"
        preprocess_script = SalomeScript(self.project_path, script_file_name, self.logger,
                                         compound_str_list=self.param['compound_str_list'],
                                         bc_id_dict=self.param['bc_id_dict'])
        # geometry process
        preprocess_script.salome_init()
        preprocess_script.geom.geo_init()
        preprocess_script.geom.import_step(input_step)
        preprocess_script.geom.extract_all_solids()
        # preprocess_script.geom.get_face_id_list()
        preprocess_script.geom.build_face_group()
        preprocess_script.update_gui()
        # mesh process
        preprocess_script.mesh.mesh_init()
        preprocess_script.mesh.create_main_mesh()
        preprocess_script.mesh.group_from_geo()
        preprocess_script.mesh.clear_tet_param()
        for compound in self.param['compound_str_list']:
            preprocess_script.mesh.add_2D_tet_param(compound, 14, 2.5)
        preprocess_script.mesh.compute_all()
        preprocess_script.mesh.export_unv(self.output_unv)
        preprocess_script.mesh.export_fms(self.output_fms, fms_py)
        preprocess_script.update_gui()
        preprocess_script.save_study(self.study_file_path_mesh)
        preprocess_script.exit_salome()
        preprocess_script.done_output()
        call_salome(self.salome_path, script_file_path, self.logger)
        self.logger.critical("surface mesh stage finished")
        self.logger.debug("salome surface mesh and export fms mesh finished")
        # use cfmesh
        command = "sh command.sh"
        run_directory = "cfmesh_test_V2"
        foam = FoamPy(self.project_path, "cfmesh_test_V2", self.logger)
        min_size = self.param["mesh"]['min_size']
        nlayers = self.param["mesh"]['nlayers']
        foam.system.mesh_dict.mesh_file("coolant_plate_fms.fms")
        foam.system.mesh_dict.global_settings(min_size, 0.1 * min_size, 20, min_size)
        foam.system.mesh_dict.prism_settings("defaultFaces", 1, nlayers, 1.4)
        foam.system.mesh_dict.write_file()
        call_wsl_openfoam(self.project_path, run_directory, self.openfoam_bashrc, command, self.logger)
        self.logger.debug("wsl openfoam cfMesh complete")

    def solve(self):
        pass

    def post(self):
        pass

    def all_run(self):
        self.geo_struct()
        self.mesh()
        self.solve()
        self.post()
