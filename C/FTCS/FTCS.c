#include<stdio.h>                                                                                                                                                                                                                          2 #include<math.h>
  3 #define range 10                                //range of x where graph is to be plotted
  4
  5
  6 int main(){                                                                         //CFD programming
  7 double x, t=0, dx=0.2, dt=0.01, Un[(int)(range/dx)], U[(int)(range/dx)], constant=dt/(dx*dx), e=0.0001;       //List size can be determined by range/dx
  8 int i, counter = 0, X=1;                                            //X is used to manipulate ASCII value of 'graphX.dat'
  9 char filename[] = "graphX.dat";
 10
 11 filename[5] = X + '0';                                              //Changing ('0')'s ASCII value of 48 to 49 to make filename 'graph1.dat'
 12 FILE *f;
 13 f = fopen(filename,"w+");
 14 for(x=0;x<range;x+=dx){                                         //Initializing function U
 15     if(x==0){
 16         U[counter] = 1;
 17         fprintf(f,"%lf\t%lf\n",x,U[counter]);
 18         counter++;
 19     }
 20     else if(x==10){
 21         U[counter] = 2;
 22         fprintf(f,"%lf\t%lf\n",x,U[counter]);
 23         counter++;
 24         }
 25     else{
 26         U[counter] = 0;
 27         fprintf(f,"%lf\t%lf\n",x,U[counter]);
 28         counter++;
 29     }
 30 }
 31 fclose(f);
 32
 33 while(t<=20.0){
 34 Un[0] = 1;                                          //U(0,t) = 0
 35 Un[10] = 2;                                         //U(10,t) = 0
 36 counter=1;
 37 t+=dt;                                              //t here indicates at which time frame it's in
 38 if(fabs(t-5)<e||fabs(t-10)<e||fabs(t-15)<e){     //e here is used to allow double-double comparison due to floating point error
 39     char filename[] = "graphX.dat";
 40     X++;
 41     filename[5] = X + '0';
 42     FILE *f;
 43     f = fopen(filename,"w+");
 44     for(x=0;x<range;x+=dx){
 45         Un[counter] = constant*(U[counter-1]-2*U[counter]+U[counter+1]);
 46         fprintf(f,"%lf\t%lf\n",x,Un[counter]);
 47         counter++;
 48         }
 49     fclose(f);
 50     }
 51
 52 else{
 53     for(x=0;x<range;x+=dx){
 54         Un[counter] = U[counter] - constant*(U[counter]-U[counter-1]);
 55         counter++;
 56         }
 57     }
 58 for(i=0;i<(int)(range/dx);i++){                     //Copying array for the next calculation
 59     U[i] = Un[i];
 60     }
 61 }
