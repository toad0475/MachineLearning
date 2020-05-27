import numpy as np

A = np.array([[1,2],
              [3,4]])

print(A ** 2)
print(3 ** A)
print(A ** A)

# 행렬곱
x = np.array([[1,2],
              [3,4]])
y = np.array([[3,4],
              [3,2]])

print(np.dot(x,y))
print((1*3)+(2*3))
print((1*4)+(2*2))
print((3*3)+(4*3))
print((3*4)+(4*2))
print(x*y)

print(np.logical_or(x,y))
print(np.sum(A))
print(A.min())
print(A.max())
print(A.sum())
print(A.argmin())
print(A.argmax())