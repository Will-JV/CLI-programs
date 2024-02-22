#include<stdio.h>
#include<stdlib.h>
#include<math.h>
double a=1.0;
double b=100.0;

double function(double x){                     //BISECTION METHOD
double ans = 0.033*x*x*x-5*x*x+210*x-2700;
return ans;
}


double recursion(double a,double b){          //recursion

double e=0.000001,c,s,value;

value = fabs(b-a);
printf("value = %lf\n",value);

if(fabs(b-a)>e){

c = (a+b)/2;
s = function(a)*function(c);
	if(s<0){b=c;
			return recursion(a,b);
	}
	else{a=c;
		return recursion(a,b);
	}
}

else{return a;}

}


int main(){									//main
double ans;
ans = recursion(a,b);
printf("Solution of x = %lf\n",ans);
}



