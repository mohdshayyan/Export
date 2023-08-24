import matplotlib.pyplot as plt
import numpy as np
a = np.array([10,30,5,42,55,76,55,54,11,20,51,15,75,37,25])
print(a)

plt.hist(a, bins=[0,25,50,75,100])
plt.axis([0, 100, 0, 6]) 
plt.show()
