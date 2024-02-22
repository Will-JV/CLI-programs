#Bisection Method
##Usage
To find the solution to a function

##Algorithm
1. Find a,b, where f(a)f(b)<0. Set e to be a small positive real number.
2. End if |b-a|<e. Solution is a or b.
3. Let c=(a+b)/2. Calculate s=f(a)f(c).
4. Set b=c if s<0, else set a=c. Return to step 2. 
