import numpy as np

# Read rows and columns
r, c = map(int, input().split())

# If rows and columns are 0
if r == 0 and c == 0:
    arr = np.array([]).reshape(0, 0)
else:
    elements = []
    
    # Read elements row by row
    for _ in range(r):
        row = list(map(int, input().split()))
        elements.extend(row)
    
    # Create NumPy array and reshape
    arr = np.array(elements).reshape(r, c)

# Output
print(arr)
print(arr.ndim)
print(arr.shape)
print(arr.size)
