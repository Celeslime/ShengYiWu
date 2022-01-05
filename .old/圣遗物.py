from matplotlib import pyplot as plt
import numpy as np
k0= np.array([])
x0= np.array([])
y0= np.array([])
z0= np.array([])
aa=0
bb=10
ss=0.1
s=0.5
x1=0
y1=0
z1=0
for i in np.arange(ss,10,ss):
    max = 0
    
    for x in np.arange(aa,bb,s):
        for y in np.arange(aa,bb,s):
            for z in np.arange(aa,bb,s):
                if x + y + z == i:
                    t=(845*(1.413+0.466*x)+343)*((0.844+0.622*y)*(0.25+0.311*z)+1)
                    if t>max:
                        max=t
                        x1=x
                        y1=y
                        z1=z

    k0=np.append(k0,i)
    x0=np.append(x0,x1)
    y0=np.append(y0,y1)
    z0=np.append(z0,z1)
plt.plot(k0,x0,color='red')#攻击
plt.plot(k0,y0,color='blue')#爆伤
plt.plot(k0,z0,color='green')#爆率
plt.show()
                        
                    
        
        
