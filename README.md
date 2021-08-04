# Lattice - make lattice dogbones

![Python](https://img.shields.io/badge/python-%2314354C.svg?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
![BootStrap](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)

- Lattice is made from crossing "strands" (symmetrical)
- Lattice is defined by a radius, a number of horizontal steps h (must be ints) and a number of vertical steps v
- Lattice will clipped and be placed at the center of a D363 Type 1 dogbone
- The central part is 13 mm in x, 3.2 mm in y and 57 mm in z  
- The radius of the cylinders is always 1.6 mm to match the thickness of the dogbone
- Cylinder is approximated with 6 sides and rotated so that a flat side is down (for 3D printing) 

This shows the pre-clip lattice:
![](/imgs/lattice.PNG)

- before clipping 2 cylinders are posted left and right (will be clipped in half) to provide a frame. 2 cylinder with 1.6 mm radius will be added on top and bottom to connect to the non-central D363 parts

- This shows the clipped lattice:

![](/imgs/clipped.PNG)

- Realistically, h values makes only sense from 1 up to and including 4. Good v values vary depending on h. Heres h=4 for v from 24 to 60:
![](/imgs/dogbones.PNG)



## Tensile strength test

- https://youtu.be/LTmuwfyYUJQ?t=252  Testing Carbon fiber infused Co-polyester (expensive, needs high-temp 3D printing 250 C).More info: https://www.patreon.com/posts/filament-test-16238656
- https://youtu.be/uAoZCpXoPWo?t=344  Compares Tensile strength of normal PLA (here called Polylite) with a PLA "PLus" material  (which has some additives ...) PLA PLus is weaker but has a ductile phase that normal PLA doesn't, it just ends in brittle failure.
- https://youtu.be/ycGDR752fT0?t=492  Tensile stength test (and other tests) on common materials, uses a hook test (not a dogbone). blog here with more details: https://www.cnckitchen.com/blog/comparing-pla-petg-amp-asa-feat-prusament  