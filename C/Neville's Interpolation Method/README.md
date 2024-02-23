# Neville's Interpolation Method
Interpolates a function using Neville's algorithm

## Usage
Type the commands below in terminal
```bash
gcc filename.c -lm
```
```bash
./a.out
```
If gnuplot is not downloaded, type in the following command:
```bash
sudo apt install gnuplot
```

## Algorithm

![alt text](https://i.imgur.com/ufuv3.png)

Neville’s method can be stated as follows:

Let a function f be defined at points $ x_0 $,$ x_1 $,⋯,$ x_k $ where $ x_j $ and $ x_i $ are two distinct members. For each k, there exists a Lagrange polynomial P that interpolates the function f at the k+1 points $ x_0 $,$ x_1 $,⋯,$ x_k $. The kth Lagrange polynomial is defined as:

$$ P(x) = {(x-x_j)P_{0,1,...,j-1,j+1,...,k}(x)-(x-x_i)P_{0,1,...,i-1,i+1,...,k}(x)} \over (x_i-x_j)$$
