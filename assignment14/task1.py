grades = {"ნიკა": 85, "თამარი": 92, "ლევანი": 78, "მარიამი": 88}
for student, grade in grades.items():
    print(f"{student}: {grade}")
print(f"Max graded student is: {max(grades, key=grades.get)}")
print(f"Average grade is: {sum(grades.values()) / len(grades)}")