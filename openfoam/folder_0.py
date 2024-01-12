import os


class Folder0(object):
    def __init__(self, foam):
        self.foam = foam
        self.foam.logger.info('create_object_mesh')
        self.file_content = ""
        self.folder_path = f"{self.foam.main_folder}\\0"
        if not os.path.exists(self.folder_path):
            os.mkdir(self.folder_path)
        else:
            self.foam.logger.warning("The 0 file is already exist")

    def UDF_file(self):
        pass

    def T_file(self):
        self.file_content = ""
        self.set_dimensions(0, 0, 0, 1, 0, 0, 0)
        self.set_internal_field(300)
        bc_field = self.BoundaryField(self)
        bc_field.BC_zero_gradient()
        bc_field.BC_interface("interface_test")
        self.write_file("T", "volScalarField", "0", "T")

    def U_file(self):
        self.file_content = ""
        self.set_con_Uinlet(0, -3.18, 0)
        self.set_dimensions(0, 1, -1, 0, 0, 0, 0)
        self.set_internal_Ufield(0, 0, 0)
        bc_field = self.BoundaryField(self)
        bc_field.BC_U_inlet("inlet")
        bc_field.BC_U_outlet("outlet")
        bc_field.BC_U_wall("wall_plate")
        self.write_file("U", "volVectorField", "0", "U")

    def p_file(self):
        self.file_content = ""
        self.set_dimensions(0, 2, -2, 0, 0, 0, 0)
        self.set_internal_field(0)
        bc_field = self.BoundaryField(self)
        bc_field.BC_p_inlet("inlet")
        bc_field.BC_p_outlet("outlet")
        bc_field.BC_p_wall("wall_plate")
        self.write_file("p", "volScalarField", "0", "p")

    def epsilon_file(self):
        self.file_content = ""
        self.set_con_epsiloninlet(5.2e-4)
        self.set_dimensions(0, 2, -3, 0, 0, 0, 0)
        self.set_internal_epsilonfield()
        bc_field = self.BoundaryField(self)
        bc_field.BC_epsilon_inlet("inlet")
        bc_field.BC_epsilon_outlet("outlet")
        bc_field.BC_epsilon_wall("wall_plate")
        self.write_file("epsilon", "volScalarField", "0", "epsilon")

    def k_file(self):
        self.file_content = ""
        self.set_con_kinlet(0.0015)
        self.set_dimensions(0, 2, -2, 0, 0, 0, 0)
        self.set_internal_kfield()
        bc_field = self.BoundaryField(self)
        bc_field.BC_k_inlet("inlet")
        bc_field.BC_k_outlet("outlet")
        bc_field.BC_k_wall("wall_plate")
        self.write_file("k", "volScalarField", "0", "k")

    def nut_file(self):
        self.file_content = ""
        self.set_dimensions(0, 2, -1, 0, 0, 0, 0)
        self.set_internal_field(0)
        bc_field = self.BoundaryField(self)
        bc_field.BC_nut_inlet("inlet")
        bc_field.BC_nut_outlet("outlet")
        bc_field.BC_nut_wall("wall_plate")
        self.write_file("nut", "volScalarField", "0", "nut")

    def set_dimensions(self, mass, length, time, temperature, quantity, current, Luminous_intensity):
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
dimensions      [ {mass} {length} {time} {temperature} {quantity} {current} {Luminous_intensity} ];
"""

    def set_internal_field(self, value, uniform=True):
        if uniform:
            if isinstance(value, int) or isinstance(value, float):
                self.file_content += f"""
internalField   uniform {value};
"""

    def set_con_Uinlet(self, uinx, uiny, uinz):

        self.file_content += f"""
Uinlet   ({uinx} {uiny} {uinz});
"""

    def set_internal_Ufield(self, ux, uy, uz, uniform=True):

        if uniform:
            if isinstance(ux, int) or isinstance(ux, float):
                self.file_content += f"""
internalField   uniform ({ux} {uy} {uz});
"""

    def set_con_epsiloninlet(self, epsilon):

        self.file_content += f"""
epsilonInlet   {epsilon};
"""

    def set_con_kinlet(self, k):

        self.file_content += f"""
kInlet   {k};
"""

    def set_internal_epsilonfield(self, value=" $epsilonInlet", uniform=True):
        self.file_content += f"""
internalField   uniform{value};
"""

    def set_internal_kfield(self, value=" $kInlet", uniform=True):
        self.file_content += f"""
internalField   uniform{value};
"""

    class BoundaryField(object):
        def __init__(self, f0):
            self.f0 = f0
            self.set_frame()

        def add(self, add_content):
            content = self.f0.file_content[::-1].replace("}", "", 1)[::-1]
            content += add_content
            content += """
}
"""
            self.f0.file_content = content

        def set_frame(self):
            self.f0.file_content += """
boundaryField
{

}
"""
            
        def BC_interface(self, bc_name, type="compressible::turbulentTemperatureCoupledBaffleMixed",
                         value="$internalField", T_name="T", thickness=0, kappa=0):
            thermal_resistance = ""
            if thickness:
                thermal_resistance = f"""
            thicknessLayers({thickness});
            kappalayers({kappa});
"""
            content = f"""
    {bc_name}
    {{
            type            {type};
            value           {value};
            Tnbr            {T_name};
            {thermal_resistance}
    }}
"""
            self.add(content)

        def BC_zero_gradient(self, bc_name=""" ".*" """):
            content = f"""
    {bc_name}
    {{
        type            zeroGradient;
    }}  
"""
            self.add(content)

        def BC_U_inlet(self, bc_name, type="fixedValue", value="uniform $Uinlet"):
            content = f"""
    {bc_name}
    {{
            type            {type};
            value           {value};
    }}
"""
            self.add(content)

        def BC_U_outlet(self, bc_name, type="pressureinletOutletVelocity", value="uniform (0 0 0)"):
            content = f"""
    {bc_name}
    {{
            type            {type};
            value           {value};
    }}
"""
            self.add(content)

        def BC_U_wall(self, bc_name, type="noslip"):
            content = f"""
    {bc_name}
    {{
            type            {type};
    }}
"""
            self.add(content)

        def BC_p_inlet(self, bc_name, type="zeroGradient"):
            content = f"""
    {bc_name}
    {{
            type            {type};
    }}
"""
            self.add(content)

        def BC_p_outlet(self, bc_name, type="totalPressure", p0="uniform 0", value="uniform 0"):
            content = f"""
    {bc_name}
    {{
            type            {type};
            p0              {p0};
            value           {value};
    }}
"""
            self.add(content)

        def BC_p_wall(self, bc_name, type="zeroGradient"):
            content = f"""
    {bc_name}
    {{
            type            {type};
    }}
"""
            self.add(content)

        def BC_epsilon_inlet(self, bc_name, type="fixedValue", value="uniform $epsilonInlet"):
            content = f"""
    {bc_name}
    {{
            type            {type};
            value           {value};
    }}
"""
            self.add(content)

        def BC_epsilon_outlet(self, bc_name, type="inletOutlet", inletValue="uniform $epsilonInlet",
                              value="uniform $epsilonInlet"):
            content = f"""
    {bc_name}
    {{
            type            {type};
            inletValue      {inletValue}:
            value           {value};
    }}
"""
            self.add(content)

        def BC_epsilon_wall(self, bc_name, type="epsilonWallFunction", value="uniform $epsilonInlet"):
            content = f"""
    {bc_name}
    {{
            type            {type};
            value           {value};
    }}
"""
            self.add(content)

        def BC_k_inlet(self, bc_name, type="fixedValue", value="uniform $kInlet"):
            content = f"""
    {bc_name}
    {{
            type            {type};
            value           {value};
    }}
"""
            self.add(content)

        def BC_k_outlet(self, bc_name, type="inletOutlet", inletValue="uniform $kInlet", value="uniform $kInlet"):
            content = f"""
    {bc_name}
    {{
            type            {type};
            inletValue      {inletValue}:
            value           {value};
    }}
"""
            self.add(content)

        def BC_k_wall(self, bc_name, type="kqRWallFunction", value="uniform $kInlet"):
            content = f"""
    {bc_name}
    {{
            type            {type};
            value           {value};
    }}
"""
            self.add(content)

        def BC_nut_inlet(self, bc_name, type="calculated", value="uniform 0"):
            content = f"""
    {bc_name}
    {{
            type            {type};
            value           {value};
    }}
"""
            self.add(content)

        def BC_nut_outlet(self, bc_name, type="calculated", value="uniform 0"):
            content = f"""
    {bc_name}
    {{
            type            {type};
            value           {value};
    }}
"""
            self.add(content)

        def BC_nut_wall(self, bc_name, type="nutkWallFunction", value="uniform 0"):
            content = f"""
    {bc_name}
    {{
            type            {type};
            value           {value};
    }}
"""
            self.add(content)

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
