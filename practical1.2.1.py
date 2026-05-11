n = int(input())
marks = list(map(int, input().split()))
if len(marks) !=n:
	print("Invalid input")
else:
	if any (mark < 40 for mark in marks):
		print("Fail")
	else:
		aggregate = sum(marks) / n
		print(f"Aggregate Percentage: {aggregate:.2f}")
		if aggregate > 75:
			print("Grade: Distinction")
		elif 60 <= aggregate < 75:
			print("Grade: First Division")
		elif 50 <= aggregate < 60:
			print("Grade: Second Division")
		elif 40 <= aggregate < 50:
			print("Grade: Third Division") 
