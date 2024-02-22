#include<stdio.h>
#include<stdlib.h>
#include<math.h>

double neville(double *a,double*b,double x, int n){
	int i,xplus=1;					/*i=index, xplus=次数*/
	double temp,b2[n];				/*temp=temporary data, b2=temporary y-data list*/
	for(i=0;i<n;i++){b2[i]=b[i];}
	while(n>1){
		for(i=0;i<n-1;i++){
			temp = ((x-a[i])*b2[i+1]-(x-a[i+xplus])*b2[i])/(a[i+xplus]-a[i]);
			b2[i] = temp;
		}
		n--;
		xplus++;	
	}
	return b2[0];
}

int main(){
	int i,n=0;		/*i=index, n = number of data*/
	double temp[1000],x,y;        /*temp=temporary list*/	
	
	FILE *fp;
	fp = fopen("data.txt","r");
	while(fscanf(fp,"%lf",&(temp[n])) != EOF){n++;}
	fclose(fp);
	
	n=n/2;
	
	double a[n],b[n];		/*a=x,b=y*/
	
	for(i=0;i<n;i++){a[i]=temp[i];}
	for(i=n;i<n*2;i++){b[i-n]=temp[i];}
	
	for(x=1;x<=5;x=x+0.1){
		y = neville(a,b,x,n);
		printf("x = %f\ty = %f\n",x,y);
	}
}
