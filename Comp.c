#include <stdio.h>
#include <stdlib.h>


//X es Velocidad, Y es radio


#define G 6.67259E-8
#define M 1.0E34
#define m 1.0E29
#define cte ((1.7E12)*(1.7E12)*(1.7E12)*(1.7E12)*(1.7E12))*5.6E5
#define tMax 1.5E6 
#define pi 3.1416

//Funciones
double v_prime( double v, double r) {
  
  return -G*M/(r*r) + 4*pi*cte/(m*r*r*r);
  
}

double r_prime( double v, double r) {
  
  return v;
  
}

//Metodo basado en los codigos en python vistos en clase
int rungekutta(int i, double *x,double *y,double *t, double *p, double h)
{
  //X corresponde a la velocidad	
  double kx1 = v_prime(x[i-1],y[i-1]);
  //Y corresponde al radio
  double ky1 = r_prime(x[i-1],y[i-1]);
  
  
  // first step
  double t1 = t[i-1] + (h/2.0);
  double x1 = x[i-1] + (h/2.0) * kx1;
  double y1 = y[i-1] + (h/2.0) * ky1;
  
	
  double kx2 = v_prime(x1, y1);
  double ky2 = r_prime(x1, y1);
  
  // second step
  double t2 = t[i-1] + (h/2.0);
  double x2 = x[i-1] + (h/2.0) * kx2;
  double y2 = y[i-1] + (h/2.0) * ky2;
  
  
  double kx3 = v_prime(x2, y2);
  double ky3 = r_prime(x2, y2);
  
  
	// third step  
  double t3 = t[i-1] + h;
  double x3 = x[i-1] + h * kx3;
  double y3 = y[i-1] + h * ky3;
  
  double kx4 = v_prime(x3, y3);
  double ky4 = r_prime(x3, y3);
  
  	
  	// fourth step 
  double average_kx = (1.0/6.0)*(kx1 + 2.0*kx2 + 2.0*kx3 + kx4);
  double average_ky = (1.0/6.0)*(ky1 + 2.0*ky2 + 2.0*ky3 + ky4);
  
  
  t[i] = t[i-1] + h;
  x[i] = x[i-1] + h * average_kx;
  y[i] = y[i-1] + h * average_ky;
  p[i] = 5.6E5/((y[i-1])*(y[i-1])*(y[i-1])*(y[i-1])*(y[i-1]));
  
//printf("%f" ,kx2);
	return 0;
}

int sol(double cond1, double cond2){
  
  //char num[2];
  //sprintf(num, "%d", ind);
  FILE *export;
  export = fopen("oscilacion_estelar.dat", "w");
  double h;
  int n_points;
  h = 1E3;
  n_points = (int) ((tMax+h)/h);
  
  
  double *t;
  double *x;
  double *y;
  double *p;
  
  
  x = malloc(n_points*sizeof(double));
  y = malloc(n_points*sizeof(double));
  t = malloc(n_points*sizeof(double));
  p = malloc(n_points*sizeof(double));
  
  if (!x || !y || !t){
    printf("Error en memoria");
    exit(1);
  }
  
  
  x[0] = cond1;
  y[0] = cond2;
  t[0] = 0.0;
  p[0] = 5.6E5;
  
  fprintf(export,"%f %f %f %f \n", t[0],x[0],y[0], p[0]);
  
  int i;
  
  for (i = 1; i < n_points; i ++)
    {
      rungekutta(i,x,y,t,p,h);
      fprintf(export,"%f %f %f %f \n", t[i],x[i],y[i],p[i]);
    }
  
  return 0;

}
