a.out: Tarea7.o sol.o 
	@cc Tarea7.o sol.o
	@./a.out
	@python Graficador.py
	@python fourier.py


Tarea7.o: Tarea7.c
	@cc -c Tarea7.c

sol.o: sol.c
	@cc -c sol.c

all: a.out

clean: 
	@rm -f *.o
	@rm -f a.out
	@rm -f *.jpg

