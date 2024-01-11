from salome.salome_py_command import SalomeScript
import os


class CoolantPlateWorkflow(object):
    def __init__(self, project_path, param_dict, logger):
        self.project_path = project_path
        self.param = param_dict
        self.logger = logger

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

        interface_group = {}

        return script_file_path, interface_group

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
        # preprocess_script.exit_salome()
        preprocess_script.done_output()

        return script_file_path

    def solve(self):
        pass

    def post(self):
        pass

    def all_run(self):
        self.geo_struct()
        self.mesh()
        self.solve()
        self.post()
