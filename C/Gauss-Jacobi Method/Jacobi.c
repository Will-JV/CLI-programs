#include<stdio.h>
#include<stdlib.h>
#include<math.h>


int main(){									//GAUSS-JACOBI METHOD

int n;
printf("Number of variables: ");			//Inputing matrix order
scanf("%d",&n);
printf("\n");			

double A[n][n],x[n],temp[n],b[n],value,margin,maxmargin,e=0.000001;  //e = (marginal error)
int i,j,repetitions=0,truecounter=0;          //repetitions = (iteration reps)   truecounter = (margin of error counter)

for(i=0;i<n;i++){							//Inputing matrix
	for(j=0;j<n;j++){
		printf("A%d%d:",i+1,j+1);
		scanf("%lf",&A[i][j]);
		}
	printf("b%d:",i+1);
	scanf("%lf",&b[i]);	
	}
printf("\n");

printf("Initialize variable values\n");
for(i=0;i<n;i++){                           //Initializing variable values
    printf("x%d:",i);
    scanf("%lf",&x[i]);
}
printf("\n");

FILE *f;									//Opening data file
f = fopen("graph.dat","w+");
while(truecounter!=3){
    truecounter = 0;
    maxmargin = 0;
    for(i=0;i<n;i++){                       //Calculating for Xn ... storing in temp[]
        value = b[i];
        for(j=0;j<n;j++){
            if(i != j){value -= A[i][j]*x[j];}
        }
        temp[i] = value/A[i][i];
        margin = fabs(temp[i]-x[i])/fabs(x[i]);
        if(margin < e){truecounter++;}
        if(maxmargin < margin){maxmargin = margin;}
    }
    for(i=0;i<n;i++){                       //Storing values from temp[] into x[]
        x[i]=temp[i];
    }
    repetitions++;
    fprintf(f,"%d\t%lf\n",repetitions,log(maxmargin));  //X-data = repetitions, Y-data = log(maxmargin)
}
fclose(f);

for(i=0;i<n;i++){							//Output of solutions
	printf("x%d = %lf\n",i+1,x[i]);	
	}
printf("Iteration repetition is %d\n",repetitions);

char *data = "plot 'graph.dat' w l linewidth 3";
	
FILE *gnuplotPipe = popen("gnuplot -persistent","w");    //Plotting data file with GNUPLOT
fprintf(gnuplotPipe,"%s \n",data);
fclose(gnuplotPipe);
}
