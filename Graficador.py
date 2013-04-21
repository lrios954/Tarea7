import pylab
import numpy

#Creo que este programa ya no es necesario, porque fourier.py esta graficando las cosas!!!


#for i in range(10):

	#data = numpy.loadtxt(open(str(i)+'.dat', 'r'))
data = numpy.loadtxt("0.dat")
t = data[:,1]
x = data[:,2]
y = data[:,3]

pylab.plot(t, x, 'k')
pylab.xlabel('x')
pylab.ylabel('y')
pylab.title(' x-y')
#pylab.savefig(str(i)+'_x-y.png')
pylab.close()
	
pylab.plot(t, y, 'k')
pylab.xlabel('x')
pylab.ylabel('z')
pylab.title(' x-z')
#pylab.savefig(str(i)+'_x-z.png')
pylab.close()
	
	
	
print "Las graficas fueron generadas y guardadas"
