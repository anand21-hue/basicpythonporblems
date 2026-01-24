students={}
with open("students.txt","r") as file:
    for line in file:
        roll,name,marks=line.strip().split(",")
        students[roll]={
            "name":name,
            "marks":int(marks)
            }
print(students)
