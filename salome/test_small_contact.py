import salome
import GEOM
from salome.geom import geomBuilder
import math
import SALOMEDS
import os
import itertools

# ============input parameter============
input_step = r"E:\project_simulation\energy_container\container_V1\pack_simple_V1\small_contact_test.stp"
stp_name = os.path.split(input_step)[1]
stp_name = os.path.splitext(stp_name)[0]
compound_list = list()
solid_list = list()
solid_str_list = list()
# compound_list = [yelengban, fluid, duanban, guoliuyuanjian, cell]
compound_str_list = ['comp1', 'comp2', 'comp3']
face_id_dict = {"inlet": 204, "outlet": 186}
# ========== init ================
geompy = geomBuilder.New()

# ================import step into study===============
geo_obj = geompy.ImportSTEP(input_step, True, True)
geompy.addToStudy(geo_obj, stp_name)

# =================explode sub shape of stp, rename, add to study============
compound_list = geompy.ExtractShapes(geo_obj, geompy.ShapeType["COMPOUND"], False)
for c_id, comp in enumerate(compound_list):
    compound_name = str(compound_str_list[c_id])
    geompy.addToStudyInFather(geo_obj, comp, compound_name)
    solids = geompy.ExtractShapes(comp, geompy.ShapeType["SOLID"], False)
    solid_list.extend(solids)
    for s_id, solid in enumerate(solids):
        solid_name = f'{compound_name}{s_id + 1}'
        geompy.addToStudyInFather(comp, solid, solid_name)
        solid_str_list.append(solid_name)

# ===================contact detection=====================================
interface_list = list()
for detect_combo in itertools.combinations(enumerate(solid_list), 2):
    solid1_obj = detect_combo[0][1]
    solid2_obj = detect_combo[1][1]
    solid1_name = solid_str_list[detect_combo[0][0]]
    solid2_name = solid_str_list[detect_combo[1][0]]
    # try fast intersect to detect all intersect obj
    try:
        isOk, res1, res2 = geompy.FastIntersect(solid1_obj, solid2_obj)
    except Exception as e:
        print('error: ', e)
        isOk = False
    else:
        if isOk:
            cont1 = geompy.SubShapes(solid1_obj, res1)
            cont2 = geompy.SubShapes(solid2_obj, res2)
            cont1_sf = list()
            cont2_sf = list()
            for common_combo in itertools.product(enumerate(cont1), enumerate(cont2)):
                # print(common_combo)
                cont1_obj = common_combo[0][1]
                cont2_obj = common_combo[1][1]
                cont1_ID = res1[common_combo[0][0]]
                cont2_ID = res2[common_combo[1][0]]
                common = geompy.MakeCommon(cont1_obj, cont2_obj)  # detect common
                props = geompy.BasicProperties(common)
                com_area_size = props[1]  # get area size property
                # ===get only the contacted surface
                if com_area_size > 0:
                    cont1_sf.append(cont1_obj)
                    cont2_sf.append(cont2_obj)
            # =====make contact group for first solid
            cont1_group = geompy.CreateGroup(geo_obj, geompy.ShapeType["FACE"])
            geompy.UnionList(cont1_group, cont1_sf)
            cont1_indices = cont1_group.GetSubShapeIndices()
            if cont1_indices not in interface_list:
                name_group_i = f'interface_{solid1_name}_{solid2_name}'
                geompy.addToStudyInFather(geo_obj, cont1_group, name_group_i)
                interface_list.append(cont1_indices)
            # ====make contact group for second solid
            cont2_group = geompy.CreateGroup(geo_obj, geompy.ShapeType["FACE"])
            geompy.UnionList(cont2_group, cont2_sf)
            cont2_indices = cont2_group.GetSubShapeIndices()
            if cont2_indices not in interface_list:
                # geompy.UnionIDs(cont2_group, cont2_sf)
                # comp_sf_j = geompy.MakeCompound(cont2_sf)
                name_group_j = f'interface_{solid2_name}_{solid1_name}'
                geompy.addToStudyInFather(geo_obj, cont2_group, name_group_j)
                interface_list.append(cont2_indices)

# print(interface_list)
if salome.sg.hasDesktop():
    salome.sg.updateObjBrowser()

# =================Get geometry object from current study========================
from salome.geom import geomtools

geotool = geomtools.GeomStudyTools()
small_test = geotool.getGeomObjectFromEntry("0:1:1:5")
small_test.GetName()
# geomtools.getGeompy()
# geo_obj = geompy.GetObject("0:1:5")
