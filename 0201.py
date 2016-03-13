##
# 2016.3.13
# by Nasy

from pylab import *
t = np.linspace(1,20,20)
k = 0.00082
p = np.zeros(20)
p[0]=9.6
for i in range(19):
	p[i+1]=k*(665-p[i])*p[i]+p[i]

scatter(t,p)
axis([0,21,0,700])
show()