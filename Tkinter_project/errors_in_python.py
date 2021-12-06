students = [
    {"name": "Bob", "grades": [9,9,10,8]},
    {"name": "Stuart", "grades": []},
    {"name": "Kevin", "grades": [9,9,10,8,9,10]}
        ]

try:
    for student in students:
        name = student["name"]
        grades = student["grades"]
        average = sum(grades)/len(grades)
        print(f"{name} averaged {average}")
except ZeroDivisionError as e:
    print(f"Error: {name} has no grades!")
else:
    print("--All students average calculated")
finally:
    print("--End of student average calculation --")
