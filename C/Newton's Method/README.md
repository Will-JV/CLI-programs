# Newton's Method
To find the solution of a function using gradient

## Usage
```bash
gcc filename.c -lm
```
```bash
./a.out
```

## Algorithm
1. Initiate x<sub>0</sub> as an arbitrary value. Let n=0.
2. Calculate $x<sub>n+1</sub>=x<sub>n</sub>-{f(x<sub>n</sub>) \over f'(x<sub>n</sub>)}$
