# Write a function that takes a dictionary of student names and their corresponding scores as input and returns the name of the student with the highest score.


def student_highest_score(student_score):
    
    highest_score=-1
    top_student=""
    
    for student,score in student_score.items():
        if score>highest_score:
            highest_score=score
            top_student=student
            
    return top_student

user_dict={}

num_entries= int(input("Enter the number of entries you want to add: "))

for i in range(num_entries):
    key=input("enter a student name:")
    value=int(input("enter a student score:"))
    user_dict.update({key:value})
    
top_student=student_highest_score(user_dict)
print(f"The student with the highest score is: {top_student}")




