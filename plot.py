import numpy as np
import matplotlib.pyplot as plt


data = np.loadtxt("data.dat")

plt.figure(figsize=(10,10))


plt.xlabel("x")
plt.ylabel("y")
# plt.ylim((-1.5,1.5))
# plt.xlim((0,15))
plt.plot(data[:,1], data[:,2])
plt.title("Figura punto 15")



plt.savefig("TorresAna_final_15.png")