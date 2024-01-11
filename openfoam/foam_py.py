import os.path

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

    def write_script(self):
        script_file = f"{self.project_path}\\{self.script_name}"
        with open(script_file, 'w') as f:
            f.write(self.script_content)


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
    foam.system.mesh_dict.default("1.fms", 20, 6)