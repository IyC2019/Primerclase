import numpy as np
import matplotlib.pyplot as plt
def coseno( x,A,phi,w,p ):
   t = np.linspace(x-50,x+50,p)
   y = A*np.cos(t/w+phi)
   z = A*np.cos(x/w+phi)
   plt.plot(t,y)
   plt.plot(x,z,'ro')
   plt.show()
   return z

coseno(1,1,0,1.5,500)