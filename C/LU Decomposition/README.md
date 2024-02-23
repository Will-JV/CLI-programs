# LU Decomposition
This produces the solution of a linear simultaneous equation by decompositing the original matrix into a Lower Triangle Matrix (L) and Upper Triangle Matrix (U). This also incorporates Doolitle's method, meaning the diagonal values in L would all be 1. The alternative to this is Crout's method where all of the diagonal values in U would be 1.

## Usage
Type in the following command in terminal:
```bash
gcc filename.c -lm
```
```bash
./a.out
```
Input the necessary matrix values. NOTE: Matrix is in the form of 

$$ Ax = b $$

## Algorithm
1. Decompose A matrix into L and U.
2. Forward Substitution
3. Backwards Substitution
4. Output of solution $x$
