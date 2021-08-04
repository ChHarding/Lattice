# Lattice - make lattice dogbones

![Python](https://img.shields.io/badge/python-%2314354C.svg?style=for-the-badge&logo=python&logoColor=white)

- Lattice is made from crossing "strands" (symmetrical)
- Lattice is defined by a radius, a number of horizontal steps h (must be ints) and a number of vertical steps v
- h and v values will be relief stamped into teh STL files, along with the angle (aXXXXX), which is useful for setting up tracks parallel to the strand orientation in 3D printing.  
- Lattice will clipped and be placed at the center of a D363 Type 1 dogbone
- The central part is 13 mm in x, 3.2 mm in y and 57 mm in z  
- The radius of the cylinders is always 1.6 mm to match the thickness of the dogbone
- Cylinder is approximated with 8 sides  

This shows the pre-clip lattice:
![](/imgs/lattice.PNG)

- before clipping 2 cylinders are posted left and right (will be clipped in half) to provide a frame. 2 cylinder with 1.6 mm radius will be added on top and bottom to connect to the non-central D363 parts

- This shows the clipped lattice:

![](/imgs/clipped.PNG)

- Realistically, h values makes only sense from 1 up to and including 4. Good v values vary depending on h. Heres h=4 for v from 24 to 60:
![](/imgs/dogbones.PNG)

### 3D printing (Cura profile, future topic)
- To increase tensile strength, I think it makes sense to set up a Cura profile with:
    - only 1 wall
    - only top/buttom (i.e. no infill!)
    - pattern as lines
    - directions along the strand orientation, flipping each layer (this is why the angle needs to be recorded!)

![](/imgs/dogbone_print_orientation.png)
- open topics:
    - layer height?
    - material (good candidates are PLA, possibly annealed and PC (tricky to print, needs 250/260 C)
    - forcing the fill to go more regularly from one side to the other, rather than jumping around:
    - ![](/imgs/3dprint.gif) </img "src=/imgs/3dprint.gif">

## File format conversions
- Initial model is created programatically in SCAD (but using https://github.com/SolidCode/SolidPython) and saved in a scad file (which are not pushed to github as it's just an intermediate format)
- I create a "no-stamp" version first (w/o the parameters relief-printed) and save this as *_ns.scad, then add the reliefs and save this as *.scad
- The no-stamp model file is then loaded/imported into FreeCAD (using its Python package/binding), rendered (which takes a long time!) and then exported into a STEP file (step folder)
- The with-stamp model file is given to the CLI version of Open SCAD, rendered and exported as STL (stl folder) 

## Preview and Downloading
- STL files can be previewed on github
- stl/combos contains some collections of models I made so that their parameter changes can more easily be compared.
- STEP files __cannot__ be previewed (well, the show up as text files ...)
- To download a STEP file, right-click on its name/link on the left column) and save it manually with something like _Save link As.._

## Tensile strength test of 3D printed dogbones - links (ongoing)
1) https://youtu.be/LTmuwfyYUJQ?t=252  Testing Carbon fiber infused Co-polyester (expensive, needs high-temp 3D printing 250 C).More info: https://www.patreon.com/posts/filament-test-16238656
2) https://youtu.be/uAoZCpXoPWo?t=344  Compares Tensile strength of normal PLA (here called Polylite) with a PLA "PLus" material  (which has some additives ...) PLA PLus is weaker but has a ductile phase that normal PLA doesn't, it just ends in brittle failure.
3) https://youtu.be/ycGDR752fT0?t=492  Tensile stength test (and other tests) on common materials, uses a hook test (not a dogbone). blog here with more details: https://www.cnckitchen.com/blog/comparing-pla-petg-amp-asa-feat-prusament  
