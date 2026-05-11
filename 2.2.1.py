# Read array input
arr = list(map(int, input().split()))

# Read key element
key = int(input())

# Linear search
found = False
for i in range(len(arr)):
    if arr[i] == key:
        print(i)   # print index of first occurrence
        found = True
        break

# If not found
if not found:
    print("Not found")
