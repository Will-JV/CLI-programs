#include<stdio.h>
#include<stdlib.h>
#include<math.h>


int main(){									//LU Decomposition

int n;
printf("Number of variables: ");			//Inputing matrix order
scanf("%d",&n);
printf("\n");			

double A[n][n],x[n],y[n],b[n],sum,m;
int i,j,k;

for(i=0;i<n;i++){							//Inputing matrix
	for(j=0;j<n;j++){
		printf("A%d%d:",i+1,j+1);
		scanf("%lf",&A[i][j]);
		}
	printf("b%d:",i+1);
	scanf("%lf",&b[i]);	
	}
printf("\n");

for(i=0;i<n-1;i++){							
	for(j=i+1;j<n;j++){
		m = A[j][i]/A[i][i];
		for(k=i+1;k<n;k++){
			A[j][k] = A[j][k] - m*A[i][k];
			}
		A[j][i] = m;
		}	
	}
	
for(j=0;j<n;j++){							//Forward substitution
	sum = 0;
	for(k=0;k<=j-1;k++){
		sum += A[j][k]*y[k];
		}
	y[j] = b[j]-sum;
	}

for(j=n-1;j>=0;j--){						//Backward substitution
	sum = 0;
	for(k=j+1;k<n;k++){
		sum += A[j][k]*x[k];
		}
	x[j] = (y[j]-sum)/A[j][j];	
	}

for(i=0;i<n;i++){							//Output of solutions
	printf("x%d = %lf\n",i+1,x[i]);	
	}
}



