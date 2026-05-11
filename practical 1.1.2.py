n = int(input())
if n > 0 and n <10:
	print(n*n)
elif n >= 10 and n < 100:
	print(f"{n**0.5:.2f}")
elif n >= 100 and n < 1000:
	print(f"{n**(1/3):.2f}")
else:
	print("Invalid")
