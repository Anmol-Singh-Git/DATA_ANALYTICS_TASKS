# CREATING ARRAY     NumPy
import numpy as np
# 2-Dimentional Array
arr_2d = np.array([[9,8,7,6,5],[1,2,3,4,5]])
print(arr_2d)

#OUTPUT

[[9 8 7 6 5]
 [1 2 3 4 5]]

zeros = np.zeros((3,4))
print(zeros)

# OUTPUT
[[0. 0. 0. 0.]
 [0. 0. 0. 0.]
 [0. 0. 0. 0.]]

range_arr = np.arange(0, 10, 2)      # Array (start, stop, step)
print(range_arr)

#OUTPUT
[0 2 4 6 8]

lin_space = np.linspace(0, 1, 5)       # 5 evenly spaced numbers from 0 to 1
print(lin_space)

#OUTPUT
[0.   0.25 0.5  0.75 1.  ]

# ARRAY PROPERTIES

arr = np.array([[10,20,30], [40,50,60]])

print("Array Dimension :",arr.ndim)
print("Row and Column :", arr.shape)
print("Total number of element :", arr.size)
print("Data Type of element :", arr.dtype)

#OUTPUT
Array Dimension : 2
Row and Column : (2, 3)
Total number of element : 6
Data Type of element : int64

# INDEXING AND SLICING

a = np.array([10, 20, 30, 40, 50, 60, 70])

print(a[2:6])

#OUTPUT
[30 40 50 60]


a = np.array([[10, 20, 30], 
              [50, 60, 70], 
              [40, 80, 90]])
print(a)

print(a[0,1])
print(a[:, 1])                # All Rows Column 1
print(a[0:2, 1:3])            # Top right 2x2 sub-matrix

#OUTPUT
[[10 20 30]
 [50 60 70]
 [40 80 90]]
20
[20 60 80]
[[20 30]
 [60 70]]

x = np.array([1,2,3])
y = np.array([10,20,30])

print(x+y)
print(x*2)
print(x**2)

print(np.sin(x))
print(np.exp)

#OUTPUT
[11 22 33]
[2 4 6]
[1 4 9]
[0.84147098 0.90929743 0.14112001]
<ufunc 'exp'>
