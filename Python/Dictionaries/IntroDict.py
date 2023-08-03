# my_dict = {"key1": "value1",
#            "key2": "value2",
#            "key3": "value3"
#            }

my_dict = {"name": "mounica",
           "city": "Phoenix"
           }
print(my_dict["name"])
my_dict["name"] = "python"
print(my_dict["name"])

print(my_dict.keys())
print(my_dict.values())

# change key to "value"
for key in my_dict:
    my_dict[key] = "value"
print(my_dict)

# array VS dictionary

student_array = ["A", "B", "C", "D", "E"]
target = "C"

found = False
for student in student_array:
    if target == student:
        found = True
if found:
    print(f"Student {target} found")
else:
    print(f"Student {target} not found")

# time complexity is O(1)
student_dict = {"A": True,
                "B": True,
                "C": True,
                "D": True,
                "E": True
                }
if target in student_dict:
    print(f"Student {target} found")
else:
    print(f"Student {target} not found")