# 2D Finite Element Method (FEM)
FEM is a numerical method used to approximate the solution of boundary and initial value problems characterized by partial differential equations. Used to find the temperature distribution, tensile strength of a material and so on.

## Usage
Type in the following command in terminal:
```bash
python3 filename.py
```
Input the necessary filenames and boundary conditions.

## Algorithm
1. Create a 2D mesh using triangle shell meshes
2. Set the boundary conditions ($0^{o}C$ and $100^{o}C$ nodes)
3. Calculate the Coefficient Matrix K
4. Calculate the solution to temperature matrix T
5. View the temperature distribution by opening the VTK file with Paraview

## FEM with Parallel Computation
Computes the solution faster by using parallel computation on the LU Decomposition.

### For further information, click [here](https://drive.google.com/drive/folders/1pQpr1v-Ymj-nqMAJMWeqEa7Eaac_J47L?usp=share_link)
