#include <stdio.h>
#include <stdlib.h>
#include "sol.h"
int main() {
  
int i;
	srand48 (getpid());
	 
	for (i = 0; i < 10; i ++)
	{
		double cond1 = drand48()*20.0 - 10.0;
                double cond2 = drand48()*20.0 - 10.0;
                double cond3 = drand48()*20.0 - 10.0;
                sol(i,cond1,cond2,cond3);
	}
	return 0;

  }


