import torch

a=[[2,1,4],[2,1,2],[3,4,3]]
a=torch.tensor(a,dtype=torch.int)
a

b=[[1,2,3],[4,5,6],[7,8,9]]
b=torch.tensor(b,dtype=torch.int)
b

r=[[0,0,0],[0,0,0],[0,0,0]]
r=torch.tensor(r,dtype=torch.int)
r

for i in range(len(a)):
    for j in range (len(b[0])):
        for k in range (len(b)):
            r[i][j]+= a[i][k]*b[k][j]
r

A=[[1,0,1],[0,1,1],[1,1,1]]
A=torch.tensor(A,dtype=torch.int)
f,h=A.shape
print(f)

import numpy as np

I = np.identity(n=f)
I=torch.tensor(I,dtype=torch.int)
print(I)
M = np.concatenate((A,I),axis=1)
M=torch.tensor(M,dtype=torch.int)
print(M)

for i in range (0,f):
    pivot = M[i][i]
    row =M[i]
    M[i] = row / pivot
    for j in [k for k in range(0,f) if k!=i]:
        M[j] = M[j]-M[i]*M[j][i]
    inverse = M[:,f:]
    print(inverse)