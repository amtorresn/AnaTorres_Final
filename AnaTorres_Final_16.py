import numpy as np
import matplotlib.pyplot as plt

x = [4,10,12,80,50,40]
y = [100,5,80,50,50,200]
sigma = 1

def modeloy(x,y,a,b):
    y = np.zeros(len(x))
    
    for j in range(len(x)):
        for i in range(len(a)):
            y[j] += a[i]*(x[j]**i)
        
    return y

def log_likelihood(x2, y2, sigma, a, b):
    
    K = np.sum ( np.log(1/( np.sqrt(2*np.pi*(sigma**2)) ) ) )
    z = y2-modelo2(x,y,a,b)
    return K -0.5*np.sum((z/sigma)**2)

def log_prior(a):
   
    return np.log(0.5)

    
##


N = 50000
a = [np.random.random()]
b = [np.random.random()]
logposterior = [log_likelihood(x, y, sigma, a[0], b[0])]



for i in range(1,N):
    propuesta_a  = a[i-1] + np.random.normal(loc=0.0, scale=sigma)
    propuesta_b  = b[i-1] + np.random.normal(loc=0.0, scale=sigma)

    logposterior_viejo = log_likelihood(x, y, sigma, a[i-1], b[i-1])
    logposterior_nuevo = log_likelihood(x, y, sigma, propuesta_a, propuesta_b, propuesta_c)

    r = np.exp(logposterior_nuevo-logposterior_viejo)
    if(r>1):
        r=1;
    alp = np.random.random()
    if(alp<r):
        a.append(propuesta_a)
        b.append(propuesta_b)
        logposterior.append(logposterior_nuevo)
    else:
        a.append(a[i-1])
        b.append(b[i-1])
        logposterior.append(logposterior_viejo)
a = np.array(a)
b = np.array(b)
logposterior = np.array(logposterior)

xf = np.mean(a)
yf = np.mean(b)


print("coordenada x:" + xf + "+/-" + 1)
print("coordenada y:" + yf + "+/-" + 1)
print("coordenada x:" + xf + "+/-" + 1)
