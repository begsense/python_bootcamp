import json
import uuid

def load_students(file_path: str) -> list[dict]:
    """Load students from a JSON file, or return an empty list if not found or invalid."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_students(file_path: str, students: list[dict]) -> None:
    """Save the given list of students to a JSON file."""
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(students, f, indent=2)

def add_student(file_path: str, name: str, lastname: str, address: str, score: float) -> None: 
    """Add a new student with the given data to the JSON file."""

    students = load_students(file_path)

    new_student = {
        "id": str(uuid.uuid4()),
        "name": name,
        "lastname": lastname,
        "address": address,
        "score": score
    }

    students.append(new_student)

    save_students(file_path, students)

def get_students(file_path: str, by_name: str=None, by_lastname: str=None, by_score: float=None, sort_by: str=None, descending: bool=False) -> list[dict]:
    """Retrieve students from the file, optionally filtered and sorted."""

    students = load_students(file_path)
    
    if by_name:
        students = [s for s in students if s['name'] == by_name]
    if by_lastname:
        students = [s for s in students if s['lastname'] == by_lastname]
    if by_score is not None:
        students = [s for s in students if s['score'] == by_score]

    if sort_by in ['name', 'lastname', 'score']:
        students = sorted(students, key=lambda s: s[sort_by], reverse=descending)

    if students:
        print(f"{'ID':36} | {'Name':10} | {'Lastname':12} | {'Score':5} | {'Address'}")
        print("-" * 100)
        for s in students:
            print(f"{s['id']:36} | {s['name']:10} | {s['lastname']:12} | {s['score']:5} | {s['address']}")
    else:
        print("სტუდენტები ვერ მოიძებნა.")

    return students

def calculate_average_score(file_path: str) -> float:
    """Calculate and print the average score of all students."""

    students = load_students(file_path)

    if not students:
        print("სტუდენტები ვერ მოიძებნა.")
        return 0.0

    total_score = sum(s['score'] for s in students)
    average_score = total_score / len(students)

    print(f"საშუალო ქულა: {average_score:.2f}")
    return average_score

def calculate_highest_score(file_path: str) -> dict:
    """Find and print the student with the highest score."""

    students = load_students(file_path)

    if not students:
        print("სტუდენტები ვერ მოიძებნა.")
        return {}

    highest_score_student = max(students, key=lambda s: s['score'])
    
    print(f"მაღლესი ქულა: {highest_score_student['score']} - {highest_score_student['name']} {highest_score_student['lastname']}")
    return highest_score_student

def calculate_lowest_score(file_path: str) -> dict:
    """Find and print students with a specific score."""

    students = load_students(file_path)

    if not students:
        print("სტუდენტები ვერ მოიძებნა.")
        return {}

    lowest_score_student = min(students, key=lambda s: s['score'])
    
    print(f"დაბალი ქულა: {lowest_score_student['score']} - {lowest_score_student['name']} {lowest_score_student['lastname']}")
    return lowest_score_student

def find_student_by_score(file_path: str, score: float) -> list:
    """Delete a student by ID and update the file."""
    
    students = load_students(file_path)

    found_students = [s for s in students if s['score'] == score]

    if found_students:
        print(f"სტუდენტები, რომლებსაც ქულა {score} აქვთ:")
        for s in found_students:
            print(f"{s['id']} - {s['name']} {s['lastname']}")
    else:
        print(f"სტუდენტები, რომლებსაც ქულა {score} აქვთ, ვერ მოიძებნა.")

    return found_students

def delete_student(file_path: str, student_id: str) -> None:
    students = load_students(file_path)

    students = [s for s in students if s['id'] != student_id]

    with open(file_path, 'w') as file:
        json.dump(students, file, indent=2)

    print(f"სტუდენტი {student_id} წაშლილია.")
