import numpy as np 

a = np.array([1,2,3,4,5])
b = np.zeros(5)
print(np.vstack((a,b,b,a,a,b)))
c = np.vstack((a,b,b,a,a,b)).transpose()
print(c)
cc = c[:,1:4].transpose()
print(cc)
d = np.vstack((cc,a))
print(d)

print(np.vstack((c[:,1:4].transpose(),a)).transpose())