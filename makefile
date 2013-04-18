a.out: Tarea6.o sol.o 
	@cc Tarea6.o sol.o
	@./a.out
	@python Graficador.py


Tarea6.o: Tarea6.c
	@cc -c Tarea6.c

sol.o: sol.c
	@cc -c sol.c

all: a.out

clean: 
	@rm -f *.o
	@rm -f a.out
	@rm -f *.jpg

