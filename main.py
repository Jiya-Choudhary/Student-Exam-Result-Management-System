import grader
all_students = []
while True:
    roll_no = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    student_tuple = (roll_no, name) 
    
    maths = int(input("Enter Maths marks: "))
    science = int(input("Enter Science marks: "))
    marks_dict = {"Maths": maths, "Science": science} 
    
    total, percent = grader.calculate_total_and_percentage(marks_dict)
    grade = grader.calculate_grade(percent)
    
    record = [total, roll_no, name, grade]
    all_students.append(record)
    
    more = input("Add another student? (yes/no): ")
    if more != "yes":
        break
all_students.sort(reverse=True)

with open("exam_report.txt", "w") as file:
    file.write("Rank List Report:\n\n")
    
    rank = 1
    for record in all_students:
        line = "Rank " + str(rank) + " | Roll: " + record[1] + " | Name: " + record[2] + " | Total: " + str(record[0]) + " | Grade: " + record[3] + "\n"
        file.write(line)
        rank = rank + 1 

print("Done! Check 'exam_report.txt'.")
