import argparse
import csv
import json
import os
import logging
import subprocess

# from salome.salome_py_command import SalomeScript
from sim_workflow.coolant_plate_workflow import CoolantPlateWorkflow


class PySimCall(object):
    def __init__(self, project_path, project_name, sim_mode, stage, param_json, logging_level=5):
        """
        :param project_path:
        :param project_name:
        :param sim_mode:
        :param stage: "geo_struct", "mesh", "solve", "post", "all"
        :param param_json:
        :param logging_level:
        """
        # get variable
        self.project_path = project_path
        self.project_name = project_name
        self.sim_mode = sim_mode
        self.stage = stage
        self.param_json = param_json
        self.logging_level = logging_level
        # ======parameter init =================
        self.salome_path = str()
        self.openfoam_bashrc = str()
        self.param = dict()
        self.progress = float()
        self.abnormal = str()
        # ======function==================
        self.logger = logging.getLogger('mylogger')
        self.logging_config(logging_level)
        self.logger.debug(f"python current working directory: {os.getcwd()}")
        self.parse_param()

    def parse_param(self):
        try:
            self.param = json.loads(self.param_json)
            self.param["input_step"] = self.param['geoModel']['stpFile']
            # parse compound names
            self.param["compound_str_list"] = []
            for item in self.param['geoModel']['structure']['subTokens']:
                if item['name'] == "ADVANCED_BREP_SHAPE_REPRESENTATION":
                    self.param["compound_str_list"].append(item['normalName'])
            # parse boundary names
            self.param["bc_id_dict"] = {}
            for i in self.param["geoModel"]["groupNames"]:
                self.param["bc_id_dict"][i["name"]] = i["faces"]
        except Exception as e:
            self.logger.error(e)
        else:
            self.logger.info("json loading success")
            self.logger.debug(self.param)

    def config_salome(self, salome_path):
        if os.path.exists(salome_path):
            self.salome_path = salome_path
        else:
            self.logger.error("salome path is not exist")

    def config_openfoam(self, openfoam_bashrc):
        self.openfoam_bashrc = openfoam_bashrc

    def do_task(self):
        # script_file = r"E:\project_simulation\energy_container\container_V1\coolant_V1\test2.py"
        if self.salome_path:
            if self.sim_mode == "pack":
                pass
            elif self.sim_mode == "coolant_plate":
                if self.stage == "all":
                    pass
                    # wf.all_run()
                    # self.call_salome(self.salome_path, script_file_path)
                    # self.coolant_plate_workflow()
                elif self.stage == "geo_struct":
                    wf = CoolantPlateWorkflow(self.project_path, self.param, self.logger)
                    script_file_path, interface_group = wf.geo_struct()
                    self.call_salome(self.salome_path, script_file_path)
                    self.logger.critical("geometry renaming finished")

                    return interface_group

                elif self.stage == "geo_finish":
                    self.logger.critical("geometry stage all finished")
                    pass

                elif self.stage == "mesh":
                    wf = CoolantPlateWorkflow(self.project_path, self.param, self.logger)
                    script_file_path = wf.mesh()
                    # self.call_salome(self.salome_path, script_file_path)
                    self.logger.critical("surface mesh stage finished")
                    self.logger.debug("salome surface mesh and export fms mesh finished")
                    command = "sh command.sh"
                    run_directory = "cfmesh_test_V2"
                    self.call_wsl_openfoam(run_directory, command)
                    self.logger.critical("mesh stage finished")

                elif self.stage == "solve":
                    pass

            elif self.sim_mode == "coolant_tube":
                pass
            elif self.sim_mode == "container":
                pass
        else:
            self.logger.error("salome path is not exist")

    # def coolant_plate_workflow(self):
    #     study_file_path = f"{project_path}\\new_coolant_plate_study.hdf"
    #     input_step = f"{project_path}\\{self.param['input_step']}"
    #     output_mesh = f"{project_path}\\coolant_plate_mesh.unv"
    #     script_file_name = "coolant_plate_workflow.py"
    #     script_file_path = f"{project_path}\\{script_file_name}"
    #
    #     preprocess_script = SalomeScript(project_path, script_file_name, self.logger,
    #                                      compound_str_list=self.param['compound_str_list'],
    #                                      bc_id_dict=self.param['bc_id_dict'])
    #     preprocess_script.salome_init()
    #     # ====== GEOM script: Salome====================
    #     preprocess_script.geom.geo_init()
    #     preprocess_script.geom.import_step(input_step)
    #     preprocess_script.geom.extract_all_solids()
    #     preprocess_script.geom.get_face_id_list()
    #     preprocess_script.geom.build_face_group()
    #     preprocess_script.update_gui()
    #     preprocess_script.save_study(study_file_path)
    #     # =========Mesh script: Salome ========================
    #     preprocess_script.mesh.mesh_init()
    #     preprocess_script.mesh.create_main_mesh()
    #     preprocess_script.mesh.group_from_geo()
    #     preprocess_script.mesh.clear_tet_param()
    #     for compound in self.param['compound_str_list']:
    #         preprocess_script.mesh.add_tet_param(compound, 14, 2.5, 4, 0.75)
    #     preprocess_script.mesh.compute_all()
    #     preprocess_script.mesh.export_unv(output_mesh)
    #     preprocess_script.update_gui()
    #     # =========Save Salome Study and write script ===================
    #     preprocess_script.save_study(study_file_path)
    #     preprocess_script.write_script()
    #
    #     self.call_salome(self.salome_path, script_file_path)

    def call_salome(self, salome_path, script_file):
        command = f"""{script_file} """
        # command = f"""-t {script_file} --log-file "C:\\Users\\DELL\\Desktop\\onlyLog.log" """  # back end running
        p = subprocess.Popen(f"python {salome_path}\\salome {command}", shell=True, stdout=subprocess.PIPE)
        self.logger.info("calling salome through popen")
        out, err = p.communicate()
        print(out, err)
        self.logger.info("calling salome end")

    def call_wsl_openfoam(self, additional_path, command):
        path = "/mnt/" + self.project_path[0].lower() + self.project_path[2:].replace("\\", "/")
        path += f"/{additional_path}"
        self.logger.debug(f"call wsl and direct to {path}")
        source = f"source {self.openfoam_bashrc}"
        wsl_command = f"""{command} """
        # command = f"""-t {script_file} --log-file "C:\\Users\\DELL\\Desktop\\onlyLog.log" """  # back end running
        p = subprocess.Popen(f'wsl bash -c "cd {path};{wsl_command}"', shell=True, stdout=subprocess.PIPE)
        self.logger.info("calling wsl openfoam through popen")
        out, err = p.communicate()
        print(out, err)
        self.logger.info("calling wsl openfoam end")

    def script_salome(self):
        pass

    def logging_config(self, level: int):
        logger_level_dict = {
            5: logging.DEBUG,
            4: logging.INFO,
            3: logging.WARNING,
            2: logging.ERROR,
            1: logging.CRITICAL
        }
        # 创建logger对象
        self.logger.setLevel(logger_level_dict[level])
        # 创建FileHandler对象
        fh = logging.FileHandler(r'./mylog.log')
        fh.setLevel(logger_level_dict[level])
        # 创建终端handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logger_level_dict[level])
        # 创建Formatter对象
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        console_handler.setFormatter(formatter)
        # 将FileHandler对象添加到Logger对象中
        self.logger.addHandler(fh)
        self.logger.addHandler(console_handler)
        # 记录日志信息
        self.logger.debug('start debug logging')
        self.logger.info('start logging')
        # logger.warning('warning message')
        # logger.error('error message')
        # logger.critical('critical message')


if __name__ == '__main__':
    salome_path = r"C:\SALOME-9.10.0"
    openfoam_bashrc = "/usr/lib/openfoam/openfoam2306/etc/bashrc"
    project_path = r"E:\project_simulation\energy_container\container_V1\coolant_V2"
    project_name = r"coolant_V2"
    sim_mode = "coolant_plate"
    stage = "mesh"
    test_json = r"C:\Users\DELL\Desktop\energy_container_platform\sim_param.json"
    with open(test_json, 'r') as f:
        param_json = json.load(f)

    # param = {
    #     "input_step": "coolant_plate_V1_simplified.stp",
    #     "compound_str_list": ["Volume"],
    #     "bc_id_dict": {"inlet": [204], "outlet": [186]},
    # }
    param = json.dumps(param_json)
    test_call = PySimCall(project_path, project_name, sim_mode, stage, param)
    test_call.config_salome(salome_path)
    test_call.config_openfoam(openfoam_bashrc)
    test_call.do_task()
    pass

