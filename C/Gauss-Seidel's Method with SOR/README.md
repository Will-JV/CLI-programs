# Gauss-Seidel's Methodd with SOR
Successive overrelaxation (SOR) improves Gauss-Seidel's Method by introducing a weight.

## Usage
Type in the following commands in terminal:
```bash
gcc filename.c -lm
```
```bash
./a.out
```
If gnuplot is not installed, type in the following:
```bash
sudo apt install gnuplot
```

## Algorithm
Let the introduced weight be ω such that 0<ω<2. If ω=1, the method is exactly the Gauss-Seidel method. If 0<ω<1, the algorithm is under-relaxed, else it's over-relaxed. The equation from Gauss-Seidel's method will be represented as follow with ω:

$$ {x_{i}}^(k+1) = (1-ω){x_{i}}^(k) + ω({x_{i}}^(k+1)) $$
