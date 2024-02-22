#include<stdio.h>
#include<stdlib.h>
#include<math.h>

double function(double x){
double ans = 0.033*x*x*x-5*x*x+210*x-2700;
return ans;
}



int main(){

double a=0, b=100, e=0.000001,c,s,value;

while(fabs(b-a)>e){
value = fabs(a-b);
printf("value = %lf\n",value);

c = (a+b)/2;
s = function(a)*function(c);
if(s<0){b=c;}
else{a=c;}
}

printf("Solution for x = %lf\n",a);
return 0;
}
