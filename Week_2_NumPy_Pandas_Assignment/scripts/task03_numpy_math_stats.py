import numpy as np

data = np.array([12, 18, 25, 30, 22, 35, 40, 28, 15, 32], dtype=float)
other = np.array([2, 3, 5, 6, 2, 5, 4, 7, 3, 4], dtype=float)

print("Dataset:", data)
print("\nMathematical Operations")
print("Addition:", data + other)
print("Subtraction:", data - other)
print("Multiplication:", data * other)
print("Division:", np.round(data / other, 2))

print("\nStatistical Operations")
print("Mean:", np.mean(data))
print("Median:", np.median(data))
print("Minimum:", np.min(data))
print("Maximum:", np.max(data))
print("Standard Deviation:", round(np.std(data), 2))
print("Sum:", np.sum(data))
