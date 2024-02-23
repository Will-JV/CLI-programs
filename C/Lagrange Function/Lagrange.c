#include<stdio.h>
#include<stdlib.h>


double lagrange(double *a,double*b,double x, int n){
	int i,j;
	double f,ftot;  	                                                /*ftot = total of f*/
	for(i=0;i<n;i++){
		f = b[i];
		for(j=0;j<n;j++){
			if(i!=j){
				f=f*(x-a[i])/(a[j]-a[i]);
				}
			}
		ftot = ftot + f;
		}
	return ftot;
	}

int main(){
	int i,n=0;		                                                    /*n = number of data*/
	double temp[1000],x,y;                                            /*temp=temporary list*/	
	
	FILE *fp;
	fp = fopen("data.txt","r");
	while(fscanf(fp,"%lf",&(temp[n])) != EOF){n++;}
	fclose(fp);
	
	n=n/2;
	
	for(i=0;i<n*2;i++){printf("%lf\n",temp[i]);}
	
	double a[n],b[n];		                                             /*a=x,b=y*/
	
	for(i=0;i<n;i++){a[i]=temp[i];}
	for(i=n;i<n*2;i++){b[i-n]=temp[i];}
	
	for(x=1;x<=5;x=x+0.1){
		y = lagrange(a,b,x,n);
		printf("x = %lf\ty = %lf\n",x,y);
		}
}
