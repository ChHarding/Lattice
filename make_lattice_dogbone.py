# https://github.com/SolidCode/SolidPython
# http://openscad.org/cheatsheet/
from solid import *
from solid.utils import *  # Not required, but the utils module is useful
from math import cos, radians, sin, pi, tau
from pathlib import Path
import math

from euclid3 import Point2, Point3, Vector3

# cyl_rad should always be 1.6, hsteps must be ints
def make_stl(cyl_rad, hsteps, vsteps):

    # Add D636 Type 1 model
    points = [[0, 0, 3.2], [0, 19, 3.2], [0, 0, 0], [0, 0, 0], [0, 19, 3.2], [0, 19, 0], [25, 0, 3.2], [0, 0, 3.2], [25, 0, 0], [25, 0, 0], [0, 0, 3.2], [0, 0, 0], [25, 0, 3.2], [25, 0, 0], [32.1823, 1.30988, 3.2], [32.1823, 1.30988, 3.2], [25, 0, 0], [32.1823, 1.30988, 0], [32.1823, 1.30988, 3.2], [32.1823, 1.30988, 0], [39.4226, 2.248, 3.2], [39.4226, 2.248, 3.2], [32.1823, 1.30988, 0], [39.4226, 2.248, 0], [39.4226, 2.248, 3.2], [39.4226, 2.248, 0], [46.7016, 2.81188, 3.2], [46.7016, 2.81188, 3.2], [39.4226, 2.248, 0], [46.7016, 2.81188, 0], [46.7016, 2.81188, 3.2], [46.7016, 2.81188, 0], [54, 3, 3.2], [54, 3, 3.2], [46.7016, 2.81188, 0], [54, 3, 0], [111, 3, 3.2], [54, 3, 3.2], [111, 3, 0], [111, 3, 0], [54, 3, 3.2], [54, 3, 0], [111, 3, 3.2], [111, 3, 0], [118.298, 2.81188, 3.2], [118.298, 2.81188, 3.2], [111, 3, 0], [118.298, 2.81188, 0], [118.298, 2.81188, 3.2], [118.298, 2.81188, 0], [125.577, 2.248, 3.2], [125.577, 2.248, 3.2], [118.298, 2.81188, 0], [125.577, 2.248, 0], [125.577, 2.248, 3.2], [125.577, 2.248, 0], [132.818, 1.30988, 3.2], [132.818, 1.30988, 3.2], [125.577, 2.248, 0], [132.818, 1.30988, 0], [132.818, 1.30988, 3.2], [132.818, 1.30988, 0], [140, 0, 3.2], [140, 0, 3.2], [132.818, 1.30988, 0], [140, 0, 0], [165, 0, 3.2], [140, 0, 3.2], [165, 0, 0], [165, 0, 0], [140, 0, 3.2], [140, 0, 0], [165, 19, 3.2], [165, 0, 3.2], [165, 19, 0], [165, 19, 0], [165, 0, 3.2], [165, 0, 0], [140, 19, 3.2], [165, 19, 3.2], [140, 19, 0], [140, 19, 0], [165, 19, 3.2], [165, 19, 0], [140, 19, 3.2], [140, 19, 0], [132.818, 17.6901, 3.2], [132.818, 17.6901, 3.2], [140, 19, 0], [132.818, 17.6901, 0], [132.818, 17.6901, 3.2], [132.818, 17.6901, 0], [125.577, 16.752, 3.2], [125.577, 16.752, 3.2], [132.818, 17.6901, 0], [125.577, 16.752, 0], [125.577, 16.752, 3.2], [125.577, 16.752, 0], [118.298, 16.1881, 3.2], [118.298, 16.1881, 3.2], [125.577, 16.752, 0], [118.298, 16.1881, 0], [118.298, 16.1881, 3.2], [118.298, 16.1881, 0], [111, 16, 3.2], [111, 16, 3.2], [118.298, 16.1881, 0], [111, 16, 0], [54, 16, 3.2], [111, 16, 3.2], [54, 16, 0], [54, 16, 0], [111, 16, 3.2], [111, 16, 0], [54, 16, 3.2], [54, 16, 0], [46.7016, 16.1881, 3.2], [46.7016, 16.1881, 3.2], [54, 16, 0], [46.7016, 16.1881, 0], [46.7016, 16.1881, 3.2], [46.7016, 16.1881, 0], [39.4226, 16.752, 3.2], [39.4226, 16.752, 3.2], [46.7016, 16.1881, 0], [39.4226, 16.752, 0], [39.4226, 16.752, 3.2], [39.4226, 16.752, 0], [32.1823, 17.6901, 3.2], [32.1823, 17.6901, 3.2], [39.4226, 16.752, 0], [32.1823, 17.6901, 0], [32.1823, 17.6901, 3.2], [32.1823, 17.6901, 0], [25, 19, 3.2], [25, 19, 3.2], [32.1823, 17.6901, 0], [25, 19, 0], [0, 19, 3.2], [25, 19, 3.2], [0, 19, 0], [0, 19, 0], [25, 19, 3.2], [25, 19, 0], [165, 0, 3.2], [165, 19, 3.2], [140, 0, 3.2], [140, 0, 3.2], [165, 19, 3.2], [140, 19, 3.2], [140, 0, 3.2], [140, 19, 3.2], [132.818, 1.30988, 3.2], [132.818, 1.30988, 3.2], [140, 19, 3.2], [132.818, 17.6901, 3.2], [132.818, 1.30988, 3.2], [132.818, 17.6901, 3.2], [125.577, 2.248, 3.2], [125.577, 2.248, 3.2], [132.818, 17.6901, 3.2], [125.577, 16.752, 3.2], [125.577, 2.248, 3.2], [125.577, 16.752, 3.2], [118.298, 2.81188, 3.2], [118.298, 2.81188, 3.2], [125.577, 16.752, 3.2], [118.298, 16.1881, 3.2], [118.298, 2.81188, 3.2], [118.298, 16.1881, 3.2], [111, 3, 3.2], [111, 3, 3.2], [118.298, 16.1881, 3.2], [111, 16, 3.2], [111, 3, 3.2], [111, 16, 3.2], [54, 3, 3.2], [54, 3, 3.2], [111, 16, 3.2], [54, 16, 3.2], [54, 3, 3.2], [54, 16, 3.2], [46.7016, 2.81188, 3.2], [46.7016, 2.81188, 3.2], [54, 16, 3.2], [46.7016, 16.1881, 3.2], [46.7016, 2.81188, 3.2], [46.7016, 16.1881, 3.2], [39.4226, 2.248, 3.2], [39.4226, 2.248, 3.2], [46.7016, 16.1881, 3.2], [39.4226, 16.752, 3.2], [39.4226, 2.248, 3.2], [39.4226, 16.752, 3.2], [32.1823, 1.30988, 3.2], [32.1823, 1.30988, 3.2], [39.4226, 16.752, 3.2], [32.1823, 17.6901, 3.2], [32.1823, 1.30988, 3.2], [32.1823, 17.6901, 3.2], [25, 0, 3.2], [25, 0, 3.2], [32.1823, 17.6901, 3.2], [25, 19, 3.2], [25, 0, 3.2], [25, 19, 3.2], [0, 0, 3.2], [0, 0, 3.2], [25, 19, 3.2], [0, 19, 3.2], [165, 19, 0], [165, 0, 0], [140, 19, 0], [140, 19, 0], [165, 0, 0], [140, 0, 0], [140, 19, 0], [140, 0, 0], [132.818, 17.6901, 0], [132.818, 17.6901, 0], [140, 0, 0], [132.818, 1.30988, 0], [132.818, 17.6901, 0], [132.818, 1.30988, 0], [125.577, 16.752, 0], [125.577, 16.752, 0], [132.818, 1.30988, 0], [125.577, 2.248, 0], [125.577, 16.752, 0], [125.577, 2.248, 0], [118.298, 16.1881, 0], [118.298, 16.1881, 0], [125.577, 2.248, 0], [118.298, 2.81188, 0], [118.298, 16.1881, 0], [118.298, 2.81188, 0], [111, 16, 0], [111, 16, 0], [118.298, 2.81188, 0], [111, 3, 0], [111, 16, 0], [111, 3, 0], [54, 16, 0], [54, 16, 0], [111, 3, 0], [54, 3, 0], [54, 16, 0], [54, 3, 0], [46.7016, 16.1881, 0], [46.7016, 16.1881, 0], [54, 3, 0], [46.7016, 2.81188, 0], [46.7016, 16.1881, 0], [46.7016, 2.81188, 0], [39.4226, 16.752, 0], [39.4226, 16.752, 0], [46.7016, 2.81188, 0], [39.4226, 2.248, 0], [39.4226, 16.752, 0], [39.4226, 2.248, 0], [32.1823, 17.6901, 0], [32.1823, 17.6901, 0], [39.4226, 2.248, 0], [32.1823, 1.30988, 0], [32.1823, 17.6901, 0], [32.1823, 1.30988, 0], [25, 19, 0], [25, 19, 0], [32.1823, 1.30988, 0], [25, 0, 0], [25, 19, 0], [25, 0, 0], [0, 19, 0], [0, 19, 0], [25, 0, 0], [0, 0, 0]]

    faces = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11], [12, 13, 14], [15, 16, 17], [18, 19, 20], [21, 22, 23], [24, 25, 26], [27, 28, 29], [30, 31, 32], [33, 34, 35], [36, 37, 38], [39, 40, 41], [42, 43, 44], [45, 46, 47], [48, 49, 50], [51, 52, 53], [54, 55, 56], [57, 58, 59], [60, 61, 62], [63, 64, 65], [66, 67, 68], [69, 70, 71], [72, 73, 74], [75, 76, 77], [78, 79, 80], [81, 82, 83], [84, 85, 86], [87, 88, 89], [90, 91, 92], [93, 94, 95], [96, 97, 98], [99, 100, 101], [102, 103, 104], [105, 106, 107], [108, 109, 110], [111, 112, 113], [114, 115, 116], [117, 118, 119], [120, 121, 122], [123, 124, 125], [126, 127, 128], [129, 130, 131], [132, 133, 134], [135, 136, 137], [138, 139, 140], [141, 142, 143], [144, 145, 146], [147, 148, 149], [150, 151, 152], [153, 154, 155], [156, 157, 158], [159, 160, 161], [162, 163, 164], [165, 166, 167], [168, 169, 170], [171, 172, 173], [174, 175, 176], [177, 178, 179], [180, 181, 182], [183, 184, 185], [186, 187, 188], [189, 190, 191], [192, 193, 194], [195, 196, 197], [198, 199, 200], [201, 202, 203], [204, 205, 206], [207, 208, 209], [210, 211, 212], [213, 214, 215], [216, 217, 218], [219, 220, 221], [222, 223, 224], [225, 226, 227], [228, 229, 230], [231, 232, 233], [234, 235, 236], [237, 238, 239], [240, 241, 242], [243, 244, 245], [246, 247, 248], [249, 250, 251], [252, 253, 254], [255, 256, 257], [258, 259, 260], [261, 262, 263], [264, 265, 266], [267, 268, 269], [270, 271, 272], [273, 274, 275]]

    lat_hgt = 57 / vsteps   #
    gap = 13 / hsteps
    r_angle = math.atan2(lat_hgt, gap)
    angle = math.degrees(r_angle)

    # compensate for width  - not working
    #thick_comp = cyl_rad / math.cos(r_angle)
    #gap -= -0.06739619875222156 


    # define each strand as cylinder
    cyl_ht = 200  # make very long so they can be rotated by sth like 45 dgs and still fill the area
    cyl_lst = []
    num_cyls = 20 # always make that many cyls, will get clipped (TODO: set this based on angle)
    fn = 8 # number of facets
    for c in range(0, num_cyls):
        c = cylinder(r=cyl_rad, h=cyl_ht, center=True).add_param('$fn', fn) # set fidelity
        #c = rotate([0, 0, 60])(c) # flat side on bottom, depends on facets
        #c = scale((1, 1.6/cyl_rad, 1))(c) # make y dimension always be 3.2
        cyl_lst.append(c)

    # collects all strands
    strands = union()

    hwidth = (gap * num_cyls) / 2

    # rotate right
    for i,c in enumerate(cyl_lst):
        rc = rotate([0, angle, 0])(c)

        # move right    
        tc = translate((gap*i - hwidth, 0, 0))(rc)

        strands.add(tc) # add to union

    # rotate left
    for i,c in enumerate(cyl_lst):
        rc = rotate([0, -angle, 0])(c)

        # move right    
        tc = translate((gap*i - hwidth, 0, 0))(rc)

        strands.add(tc) # add to union

    scad_render_to_file(strands, "strands.scad")


    # make  clipping box that delineates the actual latice body filled with strands
    box_width = 13
    box_height = 57
    box_depth = 3.2
    hbw = box_width / 2
    box = cube((box_width, box_depth, box_height),  center=True)
    #box = translate((0, 0, 0))(box)

    '''
    # side pillars
    lp = cylinder(r=cyl_rad, h=cyl_ht, center=True).add_param('$fn', fn)
    lp = scale((1, 1.6/cyl_rad, 1))(lp)
    lp = translate((-hbw,0,0))(lp)
    strands.add(lp)
    rp = cylinder(r=cyl_rad, h=cyl_ht, center=True).add_param('$fn', fn)
    rp = scale((1, 1.6/cyl_rad, 1))(rp)
    rp = translate((hbw,0,0))(rp)
    strands.add(rp)
    

    # top/bottom filler (to fit clipped poly)
    tf = cylinder(r=3.2, h=13, center=True).add_param('$fn', fn)
    tf = rotate((0, -90, 0))(tf)
    tf = translate((0, 0, 57/2))(tf)
    strands.add(tf)
    bf = cylinder(r=3.2, h=13, center=True).add_param('$fn', fn)
    bf = rotate((0, -90, 0))(bf)
    bf = translate((0, 0, -57/2))(bf)
    strands.add(bf)
    '''
    # only keep strands that are inside that box
    isect  = intersection()
    isect.add(box)
    isect.add(strands)
    scad_render_to_file(isect, "isect.scad")



    # Make digbone poly and center
    p = polyhedron(points=points, faces=faces, convexity=1)
    p = rotate((-90,90,0))(p)
    p = translate((9.5, -1.6,82.5))(p)

    # slightly fatter box in center
    box2 = cube((box_width+1, box_depth+1, box_height), center=True)

    # remove box from poly
    pdiff = difference()
    pdiff.add(p)
    pdiff.add(box2)

    # export no-stamp scad file for better FEA (via STEP)
    base_fname = f"lattice_dogbone_h{hsteps}_v{vsteps}"
    scad_fname_ns = base_fname + "_ns.scad"
    
    # combine lattice with clipped poly (but w/o text!)
    full_model = union()
    full_model.add(pdiff)
    full_model.add(isect)
    full_model = rotate((-90, 0, 0))(full_model)

    scad_render_to_file(full_model, scad_fname_ns)

    # make text and remove from dogbone (=> relief)
    txt = union()
    t = text(text=f"h{hsteps}", size=6, spacing=1.2)  # g{gap} a{angle}
    t = linear_extrude(height=1)(t)
    t = rotate((90,0,0))(t)
    t = translate((-8,-1, 75))(t)
    txt.add(t)
    t = text(text=f"v{vsteps}", size=6, spacing=1.2)  # g{gap} a{angle}
    t = linear_extrude(height=1)(t)
    t = rotate((90,0,0))(t)
    t = translate((-8, -1, 68))(t)
    txt.add(t)
    angle = round(angle,2)
    t = text(text=f"a{angle}", size=6, spacing=1.2)  # g{gap} a{angle}
    t = linear_extrude(height=1)(t)
    t = rotate((90,0,0))(t)
    t = rotate((0,90,0))(t)
    t = translate((-3, -1, 66))(t)
    txt.add(t)
    scad_render_to_file(txt, "text.scad")
    pdiff.add(txt)

    # combine lattice with clipped poly this time with text
    full_model = union()
    full_model.add(pdiff)
    full_model.add(isect)
    full_model = rotate((-90, 0, 0))(full_model)

    # Convert *_ns.scad to STEP using FreeCAD https://gist.github.com/slazav/4853bd36669bb9313ddb83f51ee1cb82
    # path to FreeCAD.so (dll module on Win10)
    FREECADPATH = r'C:\Program Files\FreeCAD 0.19\bin'
    import sys
    sys.path.append(FREECADPATH)

    import FreeCAD
    import Part

    # Openscad import settings according to https://forum.lulzbot.com/viewtopic.php?t=243
    p=FreeCAD.ParamGet("User parameter:BaseApp/Preferences/Mod/OpenSCAD")
    p.SetBool('useViewProviderTree',True)
    p.SetBool('useMultmatrixFeature',True)
    # For some reason conversion does not work with cylinders created from extruded 2d circles.
    # So I set MaxFN large enough and use smaller $fn in my step files to export such cylinders as polygons.
    # If you use only normal cylinders, no need to use so large number here.
    p.SetInt('useMaxFN',99)

    print("Rendering ", scad_fname_ns)
    FreeCAD.loadFile(scad_fname_ns) # load scad file and render(!), so this may take a couple of minutes!


    # iterate through all objects
    for o in App.ActiveDocument.Objects: # no idea where App comes from ...
        # find root object and export the shape
        if len(o.InList) == 0:
            STEP_fname_ns = "step\\" + base_fname + "_ns.STEP"
            o.Shape.exportStep(STEP_fname_ns)
            print("Exported", scad_fname_ns, "to", base_fname + "_ns.STEP")
    
    # Save with-stamp scad file and convert to STL using opencad CLI
    stl_fname = "stl\\" + base_fname + ".stl"
    scad_fname = base_fname + ".scad"
    scad_render_to_file(full_model, scad_fname)

    # https://en.m.wikibooks.org/wiki/OpenSCAD_User_Manual/Using_OpenSCAD_in_a_command_line_environment
    command = f"openscad -o {stl_fname} {scad_fname}"

    print(f"Converting {scad_fname} to {stl_fname}")
    import os
    os.system(command)   # render with stamp version of scad into STL
    print("Exported",  stl_fname)
# MAIN

rad = 1.6
hsteps = 2  # must be int
vsteps = 12


#make_stl(rad, hsteps, vsteps)
#make_stl(rad, 1, 1.78)
#make_stl(rad, 1, 6)

for vsteps in (1.5, 2, 2.5, 3, 5, 6):
    make_stl(rad, 1, vsteps)
for vsteps in range(8, 33, 4):
    make_stl(rad, 2, vsteps)
for vsteps in range(12, 41, 4):
    make_stl(rad, 3, vsteps)
for vsteps in range(20, 61, 4):
    make_stl(rad, 4, vsteps)

print("done")