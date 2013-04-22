a.out: Tarea7.o Comp.o 
	@cc Tarea7.o Comp.o
	@./a.out
	@python fourier.py


Tarea7.o: Tarea7.c
	@cc -c Tarea7.c

Comp.o: Comp.c
	@cc -c Comp.c

all: a.out

clean: 
	@rm -f *.o
	@rm -f a.out
	@rm -f *.jpg

