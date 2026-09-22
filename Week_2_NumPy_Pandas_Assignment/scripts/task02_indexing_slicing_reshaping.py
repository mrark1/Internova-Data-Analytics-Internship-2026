import numpy as np

arr = np.arange(1, 13)
print("Original 1-D Array:", arr)

print("Element at index 3:", arr[3])
print("Element at index -1:", arr[-1])
print("Slice arr[2:7]:", arr[2:7])

matrix = arr.reshape(3, 4)
print("\nOriginal 2-D Array:\n", matrix)
print("First row:", matrix[0])
print("Second column:", matrix[:, 1])
print("Element at row 2, column 3:", matrix[1, 2])

reshaped_2x6 = arr.reshape(2, 6)
reshaped_4x3 = arr.reshape(4, 3)

print("\nReshaped to 2 x 6:\n", reshaped_2x6)
print("\nReshaped to 4 x 3:\n", reshaped_4x3)
