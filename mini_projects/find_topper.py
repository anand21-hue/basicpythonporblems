topper_student=-1
topper=""
with open("students.txt","r") as file:
    for line in file:
        roll,name,marks=line.strip().split(",")
        marks=int(marks)
        if marks>topper_student:
            topper_stundet=marks
            topper=name
print("marks:",marks)
print("name:",topper)
