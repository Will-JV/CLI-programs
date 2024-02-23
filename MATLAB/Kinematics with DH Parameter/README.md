# Denavit-Hartenberg (DH) Parameter
This program calculates the coordinates of a robot arm given the origin of the base and angle of the joints.

## Usage
Run file in MATLAB. Input the necessary DH Parameters.

## Algorithm
The relationship of each link is represented with the following equation:

$$ A_{i}^{i-1} = Trans(a_{i},0,0)Rot(x,α_{i})Trans(0,0,d_{i})Rot(z,θ_{i}) $$

Trans: Translation
Rot: Rotation with respect to the particular axis
a: Offset
α: Torsion angle
d: Length
θ: Rotational angle
