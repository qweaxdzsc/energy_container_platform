import os


class FolderSystem(object):
    def __init__(self, foam):
        self.foam = foam
        self.foam.logger.info('create_object_mesh')
        self.file_content = ""
        self.folder_path = f"{self.foam.main_folder}\\system"
        if not os.path.exists(self.folder_path):
            os.mkdir(self.folder_path)
        else:
            self.foam.logger.warning("The system file is already exist")

        self.mesh_dict = self.MeshDict(self)
        self.control_dict = self.ControlDict(self)

    class MeshDict(object):
        def __init__(self, fsystem):
            self.fsystem = fsystem
            self.general = self.fsystem.foam
            self.file_content = ""

        def default(self, file, max_size, min_size):
            self.mesh_file(file)
            self.global_settings(min_size, 0.1 * min_size, max_size, min_size)
            self.write_file()

        def mesh_file(self, file):
            text = f"""
surfaceFile	"{file}";
"""
            self.file_content += text

        def global_settings(self, boundary_cell_size, bcs_affect_range, max_size, min_size, keep_cell_intersect_b=1):
            text = f"""
boundaryCellSize	{boundary_cell_size};
boundaryCellSizeRefinementThickness {bcs_affect_range};
keepCellsIntersectingBoundary	{keep_cell_intersect_b};
maxCellSize	{max_size};
minCellSize	{min_size};
"""
            self.file_content += text

        def prism_settings(self, wall_patch, first_thickness, nlayers, growth_ratio):
            text = """
boundaryLayers
{
    // maxFirstLayerThickness	0.1;
    // nLayers	1;
    // thicknessRatio	1.5;
    patchBoundaryLayers
    {
        %s
        {
            allowDiscontinuity	1;
            maxFirstLayerThickness	%s;
            nLayers %s;
            thicknessRatio	%s;
        }
    } 
    //activates smoothing of boundary layers(optional)
    //deactivate by default
    optimiseLayer 1;
    //deactivate untangling of boundary layers
    //(optional)activated by default
    untangleLayers 1;
    optimisationParameters
    {
        //number of iterations in the procedure
        //for redcing normal variation(optional)
        nSmoothNormals 3;

        //maximum number of iterations
        //of the whole procedure(optional)
        maxNumIterations 5;

        //ratio between the maxximum layer thickness
        //and the estimated feature size(optional)
        featuresizeFactor 0.4;

        //activate 1 or deactivate 0 calculation of normal
        //(optional)
        recalculateNormals 1;

        //maximum allowed thickness variation of thickness
        //between two neighbouring points,divided by//the distance between the points(optional)
        relThicknessTol 0.1;
    }
    
}
""" % (wall_patch, first_thickness, nlayers, growth_ratio)
            self.file_content += text

        def local_settings(self, patch_list=[]):
            patch_dict = ""
            if patch_list:
                for patch in patch_list:
                    patch_dict += """
%s
{
    additionalRefinementLevels	2;
}
""" % patch

            text = """
localRefinement
{
    %s
}
""" % patch_dict
            self.file_content += text

        def edge_settings(self, edge_file, refine_level=4, refine_range=1):
            text = """
edgeMeshRefinement
{
    //name of the refinement region
    edgeMeshExample
    {
        //path to the edge mesh file
        edgeFile "%s";
        //additional refinement levels
        //to the maxCellsize
        additionalRefinementLevels %s;
        //thickness of the refinement region
        //away from the surface
        refinementThickness %s;
    }

}
""" % (edge_file, refine_level, refine_range)
            self.file_content += text

        def workflow_settings(self):
            pass

        def write_file(self):
            file = f"{self.fsystem.folder_path}\\meshDict"
            # assemble mesh dict file
            content = ""
            content = self.general.general_header(content, "dictionary", "system", "meshDict")
            content += self.general.general_separator()
            content += self.file_content
            content += self.general.general_separator()
            # determine if exist file, and overwrite by default
            if os.path.exists(file):
                self.general.logger.critical("path already have meshDict, overwrite by default")
            # write
            with open(file, 'w') as f:
                f.write(content)
            # reset
            self.file_content = ""

    class ControlDict(object):
        def __init__(self, fsystem):
            self.fsystem = fsystem
            self.general = self.fsystem.foam
            self.file_content = ""
            self.control_dict = dict()

        def default(self):
            self.default_dict()
            self.write_file()

        def template(self):
            text = f"""
application     {self.control_dict["application"]};

startFrom       {self.control_dict["startFrom"]};

startTime       {self.control_dict["startTime"]};

stopAt          {self.control_dict["stopAt"]};

endTime         {self.control_dict["endTime"]};

deltaT          {self.control_dict["deltaT"]};

writeControl    {self.control_dict["writeControl"]};

writeInterval   {self.control_dict["writeInterval"]};

purgeWrite      {self.control_dict["purgeWrite"]};

writeFormat     {self.control_dict["writeFormat"]};

writePrecision  {self.control_dict["writePrecision"]};

writeCompression {self.control_dict["writeCompression"]};

timeFormat      {self.control_dict["timeFormat"]};

timePrecision   {self.control_dict["timePrecision"]};

runTimeModifiable {self.control_dict["runTimeModifiable"]};

functions
{{
   {self.control_dict["function"]}
}}
"""
            return text

        def default_dict(self):
            self.control_dict["application"] = "simpleFoam"
            self.control_dict["startFrom"] = "latestTime"
            self.control_dict["startTime"] = "0"
            self.control_dict["stopAt"] = "endTime"
            self.control_dict["endTime"] = "400"
            self.control_dict["deltaT"] = "1"
            self.control_dict["writeControl"] = "timeStep"
            self.control_dict["writeInterval"] = "50"
            self.control_dict["purgeWrite"] = "0"
            self.control_dict["writeFormat"] = "ascii"
            self.control_dict["writePrecision"] = "6"
            self.control_dict["writeCompression"] = "off"
            self.control_dict["timeFormat"] = "general"
            self.control_dict["timePrecision"] = "6"
            self.control_dict["runTimeModifiable"] = "true"
            self.control_dict["function"] = ""

        def write_file(self):
            file = f"{self.fsystem.folder_path}\\controlDict"
            self.file_content += self.template()
            # assemble mesh dict file
            content = ""
            content = self.general.general_header(content, "dictionary", "system", "controlDict")
            content += self.general.general_separator()
            content += self.file_content
            content += self.general.general_separator()
            # determine if exist file, and overwrite by default
            if os.path.exists(file):
                self.general.logger.critical("path already have controlDict, overwrite by default")
            # write
            with open(file, 'w') as f:
                f.write(content)
            # reset
            self.file_content = ""