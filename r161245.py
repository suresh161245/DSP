import numpy as np
a=np.matrix('3 4 3; 4 5 6; 9 9 9')
b=np.matrix('7 3 8; 6 8 3; 1 5 4')
print"matrix a=\n",a
print "matrix b=\n",b
print"inverse of a matrix =\n",np.linalg.inv(a)
print"eigenvalue of matrix a =\n",np.linalg.eig(a)
print"subtraction of two matrices=\n",np.subtract(a,b)
print"addition of two matrices=\n",np.add(a,b)
print"multiplication of two matrices a,b=\n",np.multiply(a,b)
print"maximum value of matrix b=",np.max(b)
print"minimum value of matrix a=",np.min(a)
print"Determinant of matrix a=",np.linalg.det(a)
print"Rank of matrix a=",np.linalg.matrix_rank(a)
print"Matrix b raised to power 5=\n",np.linalg.matrix_power(b, 5)
print"solution of linear equations=\n",np.linalg.solve(a, b)
print"Trace of matrix a=\n",np.trace(a)
print"transpose of matrix b=\n",np.transpose(b)
print"absolute of matrix a=\n",np.abs(a)
print"square of matrix b=\n",np.square(b)

