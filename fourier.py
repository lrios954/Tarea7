import sys
import os
import pylab
import numpy as np
import scipy
from scipy.linalg import eigh
#from scipy.optimize import curve_fit
from scipy.fftpack import fft, fftfreq, ifft

#datosFinales=open("data.dat", "w")

data=np.loadtxt('oscilacion_estelar.dat')



Referencia=data[:,2]
Radio=[]
Tiempo = []
PromedioManchas=[]
AnioManchas=[]
ManchasMensuales=[]
Velocidad=[]

for i in range(len(Referencia)):
	
	Tiempo.append(data[i,0])
	Radio.append(data[i,2])
	Velocidad.append(data[i,1])

pylab.plot(Tiempo, Radio, '.')
pylab.xlabel('Tiempo(segundos)')
pylab.ylabel('Radio estelar')
pylab.title('Radio vs tiempo')
#pylab.savefig("Radio")
#pylab.show()

fft_x = fft(Radio) 			#/len(Tiempo) # FFT Normalized
freq = fftfreq(len(Tiempo), 1000.0) 	# Recuperamos las frecuencias. El numero es el diferencial de tiempo dt
fft_x2 = fft(Radio)			#/len(Tiempo) #Para el punto 5to
pylab.plot(freq,np.abs(fft_x))



#Calcula el cuadrado de las potencias y prepara la grafica de estas versus la frecuencia

potencias = np.abs(fft_x)**2
pylab.plot(freq, potencias, '.')
pylab.xlabel('Frecuencias')
pylab.ylabel('Potencia')
pylab.title('Frecuencias vs Potencia')
#pylab.savefig("Potencia")
#pylab.show()


#Crea una tabla que solo incluye las potencias de frecuecias entre 1 y 20 anios
tabla1=[]
tabla2=[]

for i in range(len(freq)):
	if (freq[i]!=0.0):
		peri=1/freq[i]
		if (peri>=1.0 and peri<=20.0):
			tabla1.append(peri)
			tabla2.append(potencias[i])

pylab.plot(tabla1, tabla2, '.')
pylab.xlabel('Periodo (segundos)')
pylab.ylabel('Potencia')
pylab.title('Periodo vs Potencia')
#pylab.savefig("Periodo")
#pylab.show()

#Filtra las frecuencias
for i in range(len(freq)):
	if (freq[i]>=1.0/20.0): #Creo que la frecuencia debe ser menor a 1/20
		fft_x2[i]=0.0 
	if (freq[i]<=-1.0/20.0):
		fft_x2[i]=0.0

Inv_limpia= ifft(fft_x2)
Inv_limpia_real = np.real(Inv_limpia)

#Grafica el radio y la funcion ajustada contra el tiempo
pylab.plot(Tiempo, Radio, '.')
pylab.plot(Tiempo, Inv_limpia_real, linewidth=5, alpha = 0.5)
pylab.xlabel('Tiempo (1000 segs)')
pylab.ylabel('Radio')
pylab.title('Radio vs tiempo')
pylab.savefig("Ajuste")
pylab.show()

#Grafica la velocidad contra el tiempo
pylab.plot(Tiempo, Velocidad, '.')
pylab.xlabel('Tiempo(segundos)')
pylab.ylabel('Velocidad')
pylab.title('Velocidad vs tiempo')
pylab.savefig("Velocidad")
pylab.show()

#Calcula el radio de equilibrio
radio_max = Inv_limpia_real.max()
radio_min = Inv_limpia_real.min()

radio_equilibrio = (radio_max + radio_min)/2.0

#Calcula el periodo de oscilacion de la estrella
pot_max = tabla2.max()
for i in range(len(tabla1)
	if (tabla2[i] == pot_max):
		periodo_seg = tabla1[i]
		#Convierte el periodo de oscilacion de la estrella de miles de segundos a dias
		periodo = periodo_seg/86.4 


#Escribe el archivo con el periodo y el radio de equilibrio
f = open("period_amplitude.txt", "w")

f.write("El periodo de oscilacion de la estrella (en dias) es de ") 
f.write(periodo ".")
f.write(" El radio de equilibrio de la estrella (en cm) es de ")
f.write(radio_equilibrio ".")
f.close()




