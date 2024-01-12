import os
import subprocess

from openfoam.folder_0 import Folder0
from openfoam.folder_system import FolderSystem
from openfoam.folder_constant import FolderConstant


class FoamPy(object):
    def __init__(self, project_path, project_name, logger):
        self.project_path = project_path
        self.project_name = project_name
        self.logger = logger
        self.main_folder = f"{project_path}\\{project_name}"
        self.create_work_folder()

        self.f0 = Folder0(self)
        self.system = FolderSystem(self)
        self.constant = FolderConstant(self)

    def create_work_folder(self):
        if not os.path.exists(self.main_folder):
            os.mkdir(self.main_folder)
        else:
            self.logger.warning("The working folder is already exist")

    def general_header(self, content, foam_class, file_location, object):
        content += f"""
FoamFile
{{
    format      ascii;
    version     2.0;
    class       {foam_class};
    location    "{file_location}";
    object      {object};
}}
"""
        return content

    def general_separator(self):
        content = f"""
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //
"""
        return content


def call_wsl_openfoam(project_path, additional_path, openfoam_bashrc, command, logger):
    path = "/mnt/" + project_path[0].lower() + project_path[2:].replace("\\", "/")
    path += f"/{additional_path}"
    logger.debug(f"call wsl and direct to {path}")
    source = f"source {openfoam_bashrc}"
    wsl_command = f"""{command} """
    # command = f"""-t {script_file} --log-file "C:\\Users\\DELL\\Desktop\\onlyLog.log" """  # back end running
    p = subprocess.Popen(f'wsl bash -c "cd {path};{wsl_command}"', shell=True, stdout=subprocess.PIPE)
    logger.info("calling wsl openfoam through popen")
    out, err = p.communicate()
    logger.info(out)
    logger.debug(err)
    logger.info("calling wsl openfoam end")


if __name__ == "__main__":
    import logging
    project_path = r"C:\Users\DELL\Desktop\energy_container_platform\test"
    project_name = "openfoam_test"
    logger = logging.getLogger('testlogger')
    foam = FoamPy(project_path, project_name, logger)
    foam.f0.T_file()
    foam.f0.U_file()
    foam.f0.p_file()
    foam.f0.epsilon_file()
    foam.f0.k_file()
    foam.f0.nut_file()
    foam.constant.momentumTransport_file()
    foam.constant.physicalProperties_file()
    foam.system.control_dict.default()
    foam.system.mesh_dict.default("1.fms", 20, 6)