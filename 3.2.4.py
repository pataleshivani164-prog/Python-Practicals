import numpy as np

def array_operations(A, B):

	# Convert A and B to NumPy array
	a = np.array(A)
	b = np.array(B)
	# Arithmetic Operations
	sum_result = a+b
	diff_result = a-b
	prod_result = a*b

	# Statistical Operations
	mean_A = np.mean(a)
	median_A = np.median(a)
	std_dev_A = np.std(a)

	# Bitwise Operations
	and_result = np.bitwise_and(a,b)
	or_result = np.bitwise_or(a,b)
	xor_result = np.bitwise_xor(a,b)

    # Output results with one space between each element
	print("Element-wise Sum:", ' '.join(map(str, sum_result)))
	print("Element-wise Difference:", ' '.join(map(str, diff_result)))
	print("Element-wise Product:", ' '.join(map(str, prod_result)))
    
	print(f"Mean of A: {mean_A}")
	print(f"Median of A: {median_A}")
	print(f"Standard Deviation of A: {std_dev_A}")
    
	print("Bitwise AND:", ' '.join(map(str, and_result)))
	print("Bitwise OR:", ' '.join(map(str, or_result)))
	print("Bitwise XOR:", ' '.join(map(str, xor_result)))

A = list(map(int, input().split()))  # Elements of array A
