import numpy as np

marks = np.array([45, 67, 89, 56, 78, 92, 34, 88, 73, 61])

print("Mean:", marks.mean())
print("Highest:", marks.max())
print("Lowest:", marks.min())
print("Standard Deviation:", marks.std())
print("Passed Students:", len(marks[marks >= 50]))