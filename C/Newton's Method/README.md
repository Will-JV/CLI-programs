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
$$ x<sub>n+1</sub> = x<sub>n</sub> - {f(x<sub>n</sub>) \over f'(x<sub>n</sub>)} $$

When $a \ne 0$, there are two solutions to $(ax^2 + bx + c = 0)$ and they are 
$$ x = {-b \pm \sqrt{b^2-4ac} \over 2a} $$
