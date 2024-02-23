#include<stdio.h>
#include<stdlib.h>
#include<math.h>


int main(){									//GAUSS-SEIDEL METHOD with Successive Over Relaxation

int n;
printf("Number of variables: ");			//Inputing matrix order
scanf("%d",&n);
printf("\n");			

double A[n][n],x[n],before,b[n],value,temp,margin,maxmargin,e=0.000001,omega;  //e = (marginal error)
int i,j,repetitions,truecounter;          //repetitions = (iteration reps)   truecounter = (margin of error counter)

for(i=0;i<n;i++){							//Inputing matrix
	for(j=0;j<n;j++){
		printf("A%d%d:",i+1,j+1);
		scanf("%lf",&A[i][j]);
		}
	printf("b%d:",i+1);
	scanf("%lf",&b[i]);	
	}
printf("\n");

FILE *f;									//Opening data file
f = fopen("graph.dat","w+");
for(omega=0.1;omega<=1.9;omega+=0.1){		//Iterating from 0.1,0.2, ... ,1.9 for omega
	truecounter = 0;
	repetitions = 0;
	for(i=0;i<n;i++){						//Initializing variables to be 0 vector
		x[i] = 0;
	}
	while(truecounter!=3){
    	truecounter = 0;
    	maxmargin = 0;
    	for(i=0;i<n;i++){                       //Calculating for Xn ... storing in temp[]
    		before = x[i];						//before = (temporary storage used later for marginal error calculation)
        	value = b[i];
        	for(j=0;j<n;j++){
            	if(i != j){value -= A[i][j]*x[j];}
        	}
        	temp = value/A[i][i];
        	x[i] = (1-omega)*before+omega*temp;			//Omega used to speed up calculations
        	margin = fabs(x[i]-before)/fabs(before);
        	if(margin < e){truecounter++;}
    	}
    	repetitions++;
	}
	fprintf(f,"%lf\t%d\n",omega,repetitions);	//X-data = omega, Y-data = repetitions
}
fclose(f);

for(i=0;i<n;i++){							//Output of solutions
	printf("x%d = %lf\n",i+1,x[i]);	
	}

char *data = "plot 'graph.dat' w l ";
	
FILE *gnuplotPipe = popen("gnuplot -persistent","w");    //Plotting data file with GNUPLOT
fprintf(gnuplotPipe,"%s \n",data);
fclose(gnuplotPipe);
}
