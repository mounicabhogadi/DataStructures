# Marks greater than 90, Grade A
# Marks in between 80-90, Grade B
# Marks in between 70-80, Grade C
# Marks less than 70, Fail

# 1 (for single student)
marks = 25
if marks >= 0 and marks <= 100:
    if marks >= 90:
        print(f"{marks} Grade A")
    elif marks >= 80 and marks < 90:
        print(f"{marks} Grade B")
    elif marks >= 70 and marks < 80:
        print(f"{marks} Grade C")
    else:
        print(f"{marks} Fail")
else:
    print(f"{marks} Invalid marks")


# 2 (for multiple students - Loop and Array)

marks_array = [51, 40, 78, 95, 80, 34, 13, 120, 3, 0]
for marks in marks_array:
    if 0 <= marks <= 100:
        if marks >= 90:
            print(f"{marks} Grade A")
        elif 80 <= marks < 90:
            print(f"{marks} Grade B")
        elif 70 <= marks < 80:
            print(f"{marks} Grade C")
        else:
            print(f"{marks} Fail")
    else:
        print(f"{marks} Invalid marks")


