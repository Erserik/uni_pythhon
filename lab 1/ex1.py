import numpy as np

zeros = np.zeros(10)

vowels = np.array(['a', 'e', 'i', 'o', 'u'])

ones = np.ones((2, 5), dtype=int)

myarray1 = np.array([[2.7, -2, -19],
                     [0, 3.4, 99.9],
                     [10.6, 0, 13]])

myarray2 = np.arange(4, 4 + 4 * 15, 4, dtype=float).reshape(3, 5)


#ex1
print("ex a")
print("Dimensions:", zeros.ndim, "Shape:", zeros.shape, "Size:", zeros.size, "Data type:", zeros.dtype, "Item size:", zeros.itemsize)
print("Dimensions:", vowels.ndim, "Shape:", vowels.shape, "Size:", vowels.size, "Data type:", vowels.dtype, "Item size:", vowels.itemsize)
print("Dimensions:", ones.ndim, "Shape:", ones.shape, "Size:", ones.size, "Data type:", ones.dtype, "Item size:", ones.itemsize)
print("Dimensions:", myarray1.ndim, "Shape:", myarray1.shape, "Size:", myarray1.size, "Data type:", myarray1.dtype, "Item size:", myarray1.itemsize)
print("Dimensions:", myarray2.ndim, "Shape:", myarray2.shape, "Size:", myarray2.size, "Data type:", myarray2.dtype, "Item size:", myarray2.itemsize)

#ex2
print("ex b")
print(ones.reshape(1, -1))

#ex3
print("ex c")
print(vowels[1], vowels[2])

#ex4
print("ex d")
print(myarray1[1])
print(myarray1[2])

#ex5
print("ex e")
print(myarray1[:, 0])
print(myarray1[:, 1])

#ex6
print("ex f")
print(myarray1[1:, 0])

#ex7
print("ex g")
print(vowels[::-1])