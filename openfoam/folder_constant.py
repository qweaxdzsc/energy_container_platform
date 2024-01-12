import os


class FolderConstant(object):
    def __init__(self, foam):
        self.foam = foam
        self.foam.logger.info('create_object_mesh')
        self.file_content = ""
        self.folder_path = f"{self.foam.main_folder}\\constant"
        if not os.path.exists(self.folder_path):
            os.mkdir(self.folder_path)
        else:
            self.foam.logger.warning("The constant file is already exist")

    def UDF_file(self):
        pass

    def momentumTransport_file(self):
        self.file_content = ""
        self.set_simulationType()
        self.RAS("RAS")
        self.write_file("momentumTransport", "dictionary", "constant", "RASProperties")

    def physicalProperties_file(self):
        self.file_content = ""
        self.set_viscosityModel()
        self.set_nu(0, 2, -1, 0, 0, 0, 0, 0.2313)
        self.write_file("physicalProperties", "dictionary", "constant", "physicalProperties")

    def set_viscosityModel(self, value="constant"):
        self.file_content += f"""
viscosityModel   {value};
"""

    def set_simulationType(self, value="RAS"):
        self.file_content += f"""
simulationType   {value};
"""

    def set_nu(self, mass, length, time, temperature, quantity, current, Luminous_intensity, value):
        """
        :param mass: unit m
        :param length: unit kg
        :param time:  unit s
        :param temperature:  unit A
        :param quantity: unit K
        :param current: unit mol
        :param Luminous_intensity: unit cd
        :return:
        """
        self.file_content += f"""
nu      [ {mass} {length} {time} {temperature} {quantity} {current} {Luminous_intensity} ] {value};
"""

    def RAS(self, stype, model="kEpsilon", turbulence="on", printCoeffs="on"):
        self.file_content += f"""
{stype}
 {{
           model            {model};

           turbulence       {turbulence};

           printCoeffs      {printCoeffs};
 }}
"""

    def write_file(self, file_name, foam_class, file_location, object):
        # assemble mesh dict file
        content = ""
        content = self.foam.general_header(content, foam_class, file_location, object)
        content += self.foam.general_separator()
        content += self.file_content
        content += self.foam.general_separator()
        file = f"{self.folder_path}\\{file_name}"
        with open(file, 'w') as f:
            f.write(content)
        self.file_content = ""
