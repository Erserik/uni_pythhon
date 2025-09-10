import numpy as np

iris = np.genfromtxt('iris.txt', skip_header=1, delimiter=',', usecols=(0,1,2,3))

print(iris)
print()

print("ex1")
iris_max = np.around(np.max(iris, axis=0), 2)
iris_min = np.around(np.min(iris, axis=0), 2)
iris_avg = np.around(np.mean(iris, axis=0), 2)
iris_std = np.around(np.std(iris, axis=0), 2)
iris_var = np.around(iris_std ** 2, 2)

print("iris_max:", iris_max)
print("iris_min:", iris_min)
print("iris_avg:", iris_avg)
print("iris_std:", iris_std)
print("iris_var:", iris_var)


print("ex2")

iris1 = iris[0:50, :]
print("iris1:\n", iris1)

iris2 = iris[50:100, :]
print("iris2:\n", iris2)

iris3 = iris[100:150, :]
print("iris3:\n", iris3)


for name, arr in zip(["iris1", "iris2", "iris3"], [iris1, iris2, iris3]):
    print(name)
    print("max:", np.around(np.max(arr, axis=0), 2))
    print("min:", np.around(np.min(arr, axis=0), 2))
    print("mean:", np.around(np.mean(arr, axis=0), 2))
    print("std:", np.around(np.std(arr, axis=0), 2))


print("ex3")
overall_min = np.min(iris, axis=0)
print(overall_min)
print("iris1:", np.min(iris1, axis=0) > overall_min)
print("iris2:", np.min(iris2, axis=0) > overall_min)
print("iris3:", np.min(iris3, axis=0) > overall_min)
