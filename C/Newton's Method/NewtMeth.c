#include<stdio.h>
#include<stdlib.h>
#include<math.h>

double function(double x){
double f = 0.033*x*x*x-5*x*x+210*x-2700;
double fprime = 0.099*x*x-10*x+210;
double ans = x-f/fprime;
return ans;
}



int main(){

double x=77,temp=1,e=0.000001,value;

while((fabs(x-temp)/fabs(temp))>e){
value = fabs(x-temp)/fabs(temp);
printf("value = %lf\n",value);

temp = x;
x = function(temp);
}

printf("Solution for x = %lf\n",x);
return 0;
}
