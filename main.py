import json
import os
import logging


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
        self.call_config = dict()
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
            self.param["mesh"] = {}
            self.param["mesh"]['nlayers'] = self.param["meshControl"]["boundaryLayers"]
            self.param["mesh"]['min_size'] = self.param["meshControl"]["fluidRunnerSize"]
        except Exception as e:
            self.logger.error(e)
        else:
            self.logger.info("json loading success")
            self.logger.debug(self.param)

    def config_salome(self, salome_path):
        if os.path.exists(salome_path):
            self.call_config['salome'] = salome_path
        else:
            self.logger.error("salome path is not exist")

    def config_openfoam(self, openfoam_bashrc):
        self.call_config['openfoam'] = openfoam_bashrc

    def configuration_check(self):
        config_items = ['salome', 'openfoam']
        for items in config_items:
            if items not in self.call_config.keys():
                self.logger.error(f"{items} is not configured")
                return False
            elif not self.call_config[items]:
                self.logger.error(f"{items} configuration is not correct")
                return False
        return True

    def do_task(self):
        if not self.configuration_check:
            self.logger.error("The configuration check failed, unable to do task")
            return None
        if self.sim_mode == "pack":
            pass
        elif self.sim_mode == "coolant_plate":
            if self.stage == "all":
                pass
            elif self.stage == "geo_struct":
                wf = CoolantPlateWorkflow(self.project_path, self.param, self.logger, self.call_config)
                interface_group = wf.geo_struct()
                self.logger.critical("geometry renaming finished")

                return interface_group

            elif self.stage == "geo_finish":
                self.logger.critical("geometry stage all finished")
                pass

            elif self.stage == "mesh":
                wf = CoolantPlateWorkflow(self.project_path, self.param, self.logger, self.call_config)
                wf.mesh()
                self.logger.critical("mesh stage finished")

            elif self.stage == "solve":
                pass

        elif self.sim_mode == "coolant_tube":
            pass
        elif self.sim_mode == "container":
            pass

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
    project_path = r"E:\project_simulation\energy_container\siwei\coolant_V1"
    project_name = r"coolant_V1"
    sim_mode = "coolant_plate"
    stage = "geo_struct"
    test_json = r"E:\project_simulation\energy_container\siwei\coolant_V1\sim_param.json"
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

