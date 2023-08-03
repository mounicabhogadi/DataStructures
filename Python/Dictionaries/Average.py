# find the average of each student
students_dict = [{"name": "Apple", "math": 65, "science": 78, "english": 54},
            {"name": "Bat", "math": 35, "science": 68, "english": 84},
            {"name": "Cat", "math": 45, "science": 88, "english": 64},
            ]

for student in students_dict:
    name = student["name"]
    math_score = student["math"]
    science_score = student["science"]
    english_score = student["english"]
    average = (math_score + science_score + english_score) / 3

    print(f"Average marks of {name}: {average}")
