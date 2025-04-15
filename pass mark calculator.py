'''get input as string with comma seperated number denoting marks of list of student in class room.
print the array containg pass/fail respective to the input marks.
consider 35 and above are pass marks

sample input: 20,46,75,10
sample output: fail,pass,pass,fail
'''

mark=input("enter the mark:").split(" ")
list_1=mark
#print(list_1)
pass_or_fail=[]
for i in list_1:
    intger=int(i)
    if intger>=30:
        pass_or_fail.append("pass")
    else:
        pass_or_fail.append("fail")
#print(pass_or_fail)
for j in pass_or_fail:
    print(j,end=",")



students = [
    ("Alice", {"Tamil": 65, "English": 90, "Maths": 92, "Science": 88, "Social Science": 91}),
    ("Bob", {"Tamil": 70, "English": 75, "Maths": 65, "Science": 60, "Social Science": 80}),
    ("Charlie", {"Tamil": 45, "English": 50, "Maths": 55, "Science": 58, "Social Science": 60})
]

# Function to calculate total, percentage, and classification
def calculate_results(students):
    for student in students:
        name, marks = student
        
        # Calculate total marks
        total_marks = sum(marks.values())
        
        # Calculate percentage (assuming each subject is out of 100)
        percentage = total_marks / len(marks)
        
        # Classification based on percentage
        if percentage >= 75:
            classification = "Distinction"
        elif percentage >= 60:
            classification = "First Class"
        elif percentage >= 50:
            classification = "Second Class"
        else:
            classification = "Fail"
        
        # Print the result for the student
        print(f"Student: {name}")
        print(f"Total Marks: {total_marks}")
        print(f"Percentage: {percentage:.2f}%")
        print(f"Classification: {classification}")
        print("-" * 30)

# Call the function with the student data
calculate_results(students)
