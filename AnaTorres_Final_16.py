import numpy as np
import matplotlib.pyplot as plt

x = [4,10,12,80,50,40]
y = [100,5,80,50,50,200]
sigma = 1

def modeloy(x,y,a):
    y = np.zeros(len(x))
    
    for j in range(len(x)):
        for i in range(len(a)):
            y[j] += a[i]*(x[j]**i)
        
    return y

def log_likelihood(x2, y2, sigma, a):
    
    K = np.sum ( np.log(1/( np.sqrt(2*np.pi*(sigma**2)) ) ) )
    z = y2-modeloy(x,y,a)
    return K -0.5*np.sum((z/sigma)**2)

def log_prior(a):
   
    return np.log(0.5)

    
##


N = 5000
a = np.random.rand(5000,6)
logposterior = [log_likelihood(x, y, sigma, a[0])]



for i in range(1,N):
    propuesta_a  = a[i-1] + np.random.normal(loc=0.0, scale=sigma)

    logposterior_viejo = log_likelihood(x, y, sigma, a[i-1])
    logposterior_nuevo = log_likelihood(x, y, sigma, propuesta_a)

    r = np.exp(logposterior_nuevo-logposterior_viejo)
    if(r>1):
        r=1;
    alp = np.random.random()
    if(alp<r):
        a[i] = (propuesta_a)
        logposterior.append(logposterior_nuevo)
    else:
        a[i] = (a[i-1])
        logposterior.append(logposterior_viejo)
a = np.array(a)
logposterior = np.array(logposterior)

x = np.mean(a, axis=0)
yf = modeloy(x, y, np.mean(a, axis=0))
yf = np.mean(yf)
x = np.mean(x)


print("coordenada x:" + str(x) + "+/-" + str(1))
print("coordenada y:" + str(yf) + "+/-" + str(1))
