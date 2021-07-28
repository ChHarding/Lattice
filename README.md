# Lattice - make lattice dogbones

- Lattice is made from crossing "strands" (symmetrical)
- Lattice is defined by a radius, a number of horizontal steps h (must be ints) and a number of vertical steps v
- Lattice will clipped and be placed at the center of a D363 Type 1 dogbone
- The central part that it is clipped with is  13 mm in x, 3.2 mm in y and 57 mm in z  
- The radius is always 1.6 mm to match the thickness of the dogbone
- Cylinder is aproximated with 6 sides and rotated so that a flat side is down (for 3D printing) 

This shows the pre-clip lattice:
![](/imgs/lattice.PNG)

- before clipping 2 cylinders are posted left and right (will be clipped in half) to provide a frame. 2 cylinder with 1.6 mm radius will be added on top and bottom to connect to the non-central D363 parts

- This shows clipped lattice:

![](/imgs/clipped.PNG)

- Realistically, h values makes only sense from 1 up to and including 4. Good v values vary depending on h. Heres h=4 for v from 24 to 60:
![](/imgs/dogbones.PNG)
