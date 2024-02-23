#include<stdio.h>
#include<stdlib.h>
#include<float.h>
#include<math.h>
#define n 0.00000001		//n is the width of rectangle

int main(){
double x,result=0;

for(x=0;x<=M_PI+FLT_EPSILON;x+=n){
	result += sin(x-n)*n;
	}
printf("∫sin(x)dx ,{x∈R;[0,π]} = %.17lf\n",result);   // integration of sin(x)
result = 0;

for(x=0;x<=1+FLT_EPSILON;x+=n){
	result += (x-n)*n;
	}
printf("∫xdx ,{x∈R;[0,1]} = %.17lf\n",result);        // integration of x
result = 0;

for(x=0;x<=1+FLT_EPSILON;x+=n){
	result += pow(x-n,2)*n;
	}
printf("∫x^2dx ,{x∈R;[0,1]} = %.17lf\n",result);      // integration of x^2
result = 0;

for(x=0;x<=1+FLT_EPSILON;x+=n){
	result += exp(x-n)*n;
	}
printf("∫e^xdx ,{x∈R;[0,1]} = %.17lf\n",result);      // integration of e^x

system("cp test2.c /mnt/c/Users/jwill/OneDrive/Desktop/");
}

