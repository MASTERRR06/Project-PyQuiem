stu=int(input("Enter the number of students : "))
subs= int(input("Enter the number of subjects : "))
grades = []
print("Enter grades:\n")
for i in range(stu):
    stu_scores=[]
    for j in range (subs):
        score=float(input(f"Enter Student{i+1},subject{j+1}scores:"))
        stu_scores.append(score)
    grades.append(stu_scores)
print("Student averages")
for i in range (stu):
    tot_sc=sum(grades[i])
    avgsc=tot_sc/subs
    print(f"Student{i+1} avg:{avgsc:.2f}")
print("\n--- Subject Averages ---")
for j in range (subs):
    totsubssc=0
    for i in range(stu):
        totsubssc+=grades[i][j]
    avgsub=totsubssc/stu
    print(f"Subject{j+1} avg:{avgsub:.2f}")
print("\n--- Failing Grades Alert (< 50) ---")
found_failing = False
for i in range(stu):
    for j in range(subs):
        if grades[i][j] < 50:
            print(f" Student {i+1} failed Subject {j+1} with a score of {grades[i][j]}")
            found_failing = True

if not found_failing:
    print("All students passed all subjects!")