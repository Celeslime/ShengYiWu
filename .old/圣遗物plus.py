from matplotlib import pyplot as plt
import numpy as np
K= np.array([])
X= np.array([])
Y= np.array([])
S=0.1
s=0.005
for k in np.arange(S,10,S):
    max=0
    for x in np.arange(0,1,s):
        for y in np.arange(0,1,s):
            z=1-x-y
            if z<-0.0001:
                continue
            t=(845*(1.413+0.466*k*x)+343)*((0.844+0.622*k*y)*(0.25+0.311*k*z)+1)
            if max < t :
                max = t
                x0 = x
                y0 = y
    K=np.append(K,k)
    X=np.append(X,x0)
    Y=np.append(Y,y0)
plt.plot(K,X)
plt.plot(K,Y)
plt.plot(K,1-X-Y)
plt.show()

