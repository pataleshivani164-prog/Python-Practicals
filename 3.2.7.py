import numpy as np

a = np.loadtxt("Sample.csv", delimiter=',', skiprows=1)

# 1. Print all student details
print("All student Details:\n",a)

# 2. print total students
r,c=a.shape
print("Total Students:",r)

# 3. Print all student Roll numbers
print("All Student Roll Nos",a[:,0])

# 4. Print subject 1 marks
print("Subject 1 Marks",a[:,1])

# 5. print minimum marks of Subject 2
print("Min marks in Subject 2",np.min(a[:,2]))

# 6. print maximum marks of Subject 3
print("Max marks in Subject 3",np.max(a[:,3]))

# 7. Print All subject marks
print("All subject marks:", a[:,1:])

# 8. print Total marks of students
print("Total Marks",np.sum(a[:,1:],axis=1))

# 9. print average marks of each student
avg=np.mean(a[:,1:],axis=1)
print(np.round(avg,1))

# 10. print average marks of each subject
print("Average Marks of each subject",  np.mean(a[:,1:],axis=0))

