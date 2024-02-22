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

$$ x_{n+1} = x_n - {f(x_{n}) \over f'(x_{n})} $$

2. Calculate $x_{n+1}$ with the above equation.
3. End if $|x_{n+1}-x_n|/|x_n| < e$. Else, let n = n+1 and repeat from step 2.

### (※) Note
Change function in program as necessary


