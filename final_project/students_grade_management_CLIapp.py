import json
import uuid
import os

def load_students(file_path: str) -> list[dict]:
    """Load students from a JSON file, or return an empty list if not found or invalid."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_students(file_path: str, students: list[dict]) -> None:
    """Save the given list of students to a JSON file."""
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(students, f, indent=2, ensure_ascii=False)


def search_students(file_path: str, 
                   name: str | None = None,
                   lastname: str | None = None, 
                   score: float | None = None,
                   student_id: str | None = None,
                   search_term: str | None = None) -> list[dict]:
    """
    Universal search function for students.
    Can search by specific fields or use a general search term.
    Returns list of matching students without displaying them.
    """
    students = load_students(file_path)
    
    if not students:
        return []
    
    if search_term:
        return _search_by_term(students, search_term)
    
    filtered_students = students
    
    if student_id:
        filtered_students = [s for s in filtered_students if s['id'] == student_id]
    
    if name:
        filtered_students = [s for s in filtered_students if s['name'].lower() == name.lower()]
    
    if lastname:
        filtered_students = [s for s in filtered_students if s['lastname'].lower() == lastname.lower()]
    
    if score is not None:
        filtered_students = [s for s in filtered_students if s['score'] == score]
    
    return filtered_students

def _search_by_term(students: list[dict], search_term: str) -> list[dict]:
    """Helper function to search by a general term across all fields."""
    results = []
    for student in students:
        if (search_term == student['id'] or 
            search_term.lower() == student['name'].lower() or
            search_term.lower() == student['lastname'].lower() or
            str(search_term) == str(student['score'])):
            results.append(student)
    return results

def display_students(students: list[dict], message: str | None = None) -> None:
    """Display a list of students in a formatted table."""
    if not students:
        print("სტუდენტები ვერ მოიძებნა.")
        return
    
    if message:
        print(message)
    
    print(f"{'ID':36} | {'სახელი':12} | {'გვარი':12} | {'ქულა':6} | {'მისამართი'}")
    print("-" * 100)
    for s in students:
        print(f"{s['id']:36} | {s['name']:12} | {s['lastname']:12} | {s['score']:6.1f} | {s['address']}")

def display_search_results(file_path: str, search_criteria: str, **kwargs) -> list[dict]:
    """Search and display students with formatted output."""
    results = search_students(file_path, **kwargs)
    
    if results:
        display_students(results, f"მოძებნილი სტუდენტ(ებ)ი ({search_criteria}):")
    else:
        print(f"სტუდენტები ვერ მოიძებნა კრიტერიუმით: {search_criteria}")
    
    return results


def add_student(file_path: str, name: str, lastname: str, address: str, score: float) -> str:
    """Add a new student and return the generated ID."""
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
    return new_student["id"]

def update_student(file_path: str, identifier: str, **updates) -> tuple[bool, str]:
    """
    Update student information by ID or search term.
    Returns (success, message) tuple.
    """
    students = load_students(file_path)
    
    matches = search_students(file_path, search_term=identifier)
    
    if len(matches) == 0:
        return False, f"სტუდენტი '{identifier}' ვერ მოიძებნა."
    
    if len(matches) > 1:
        display_students(matches, "რამდენიმე სტუდენტი მოიძებნა. გთხოვთ უფრო ზუსტად მიუთითოთ:")
        return False, "ზედმეტად ბევრი შედეგია."
    
    target_student = matches[0]
    
    target_index = next(i for i, s in enumerate(students) if s['id'] == target_student['id'])
    
    updated_fields = []
    for field, value in updates.items():
        if field in target_student and value is not None:
            students[target_index][field] = value
            updated_fields.append(field)
    
    if updated_fields:
        save_students(file_path, students)
        student_name = f"{students[target_index]['name']} {students[target_index]['lastname']}"
        return True, f"სტუდენტის {student_name} ინფორმაცია განახლდა: {', '.join(updated_fields)}"
    else:
        return False, "არაფერი განახლებულა. გთხოვთ მიუთითოთ სწორი ველები."

def delete_student(file_path: str, identifier: str) -> tuple[bool, str]:
    """Delete a student by ID or search term. Returns (success, message) tuple."""
    students = load_students(file_path)
    
    matches = search_students(file_path, search_term=identifier)
    
    if len(matches) == 0:
        return False, f"სტუდენტი '{identifier}' ვერ მოიძებნა."
    
    if len(matches) > 1:
        display_students(matches, "რამდენიმე სტუდენტი მოიძებნა. გთხოვთ უფრო ზუსტად მიუთითოთ:")
        return False, "ზედმეტად ბევრი შედეგია."
    
    student_to_delete = matches[0]
    students_filtered = [s for s in students if s['id'] != student_to_delete['id']]
    save_students(file_path, students_filtered)
    
    return True, f"სტუდენტი {student_to_delete['name']} {student_to_delete['lastname']} წაშლილია."


def get_all_students(file_path: str, sort_by: str | None = None, descending: bool = False) -> list[dict]:
    """Get all students with optional sorting."""
    students = load_students(file_path)
    
    if sort_by in ['name', 'lastname', 'score']:
        students = sorted(students, key=lambda s: s[sort_by], reverse=descending)
    
    return students

def get_statistics(file_path: str) -> dict | None:
    """Calculate and return all statistics."""
    students = load_students(file_path)
    
    if not students:
        return None
    
    scores = [s['score'] for s in students]
    total_students = len(students)
    
    return {
        'total_students': total_students,
        'average_score': sum(scores) / total_students,
        'highest_score': max(scores),
        'lowest_score': min(scores),
        'highest_student': max(students, key=lambda s: s['score']),
        'lowest_student': min(students, key=lambda s: s['score'])
    }

def display_statistics(file_path: str) -> None:
    """Display all statistics."""
    stats = get_statistics(file_path)
    
    if not stats:
        print("სტუდენტები ვერ მოიძებნა.")
        return
    
    print(f"\n{'='*50}")
    print(f"სტატისტიკა")
    print(f"{'='*50}")
    print(f"სტუდენტების რაოდენობა: {stats['total_students']}")
    print(f"საშუალო ქულა: {stats['average_score']:.2f}")
    print(f"უმაღლესი ქულა: {stats['highest_score']} - {stats['highest_student']['name']} {stats['highest_student']['lastname']}")
    print(f"ყველაზე დაბალი ქულა: {stats['lowest_score']} - {stats['lowest_student']['name']} {stats['lowest_student']['lastname']}")


def save_to_file(source_file: str, target_file: str) -> tuple[bool, str]:
    """Save data from source file to target file."""
    try:
        if not target_file.endswith('.json'):
            target_file += '.json'
        
        students = load_students(source_file)
        if not students:
            return False, "მონაცემები ვერ მოიძებნა შესანახად."
        
        save_students(target_file, students)
        return True, f"მონაცემები წარმატებით შეინახა ფაილში: {target_file}"
    except Exception as e:
        return False, f"შეცდომა ფაილის შენახვისას: {e}"

def load_from_file(source_file: str, target_file: str) -> tuple[bool, str]:
    """Load data from source file to target file."""
    try:
        if not os.path.exists(source_file):
            return False, f"ფაილი {source_file} ვერ მოიძებნა."
        
        students = load_students(source_file)
        if students:
            save_students(target_file, students)
            return True, f"მონაცემები წარმატებით ჩაიტვირთა ({len(students)} სტუდენტი)"
        else:
            return False, f"ფაილი {source_file} ცარიელია ან არასწორი ფორმატისაა."
    except Exception as e:
        return False, f"შეცდომა ფაილის ჩატვირთვისას: {e}"


# Menu handlers
def handle_add_student(file_path: str) -> None:
    """Handle adding a new student."""
    print("\n📝 ახალი სტუდენტის დამატება")
    name = input("სახელი: ").strip()
    lastname = input("გვარი: ").strip()
    address = input("მისამართი: ").strip()
    
    try:
        score = float(input("ქულა: ").strip())
        student_id = add_student(file_path, name, lastname, address, score)
        print(f"✅ სტუდენტი წარმატებით დაემატა! (ID: {student_id})")
    except ValueError:
        print("❌ ქულა უნდა იყოს რიცხვი.")

def handle_view_all(file_path: str) -> None:
    """Handle viewing all students."""
    sort_option = input("დაალაგება (name/lastname/score) ან Enter გამოტოვებისთვის: ").strip().lower()
    sort_by = sort_option if sort_option in ['name', 'lastname', 'score'] else None
    
    descending = False
    if sort_by:
        descending = input("კლებადობით? (y/n): ").strip().lower() == 'y'
    
    students = get_all_students(file_path, sort_by=sort_by, descending=descending)
    display_students(students, "ყველა სტუდენტი:")

def handle_search(file_path: str) -> None:
    """Handle searching for students."""
    print("\n🔍 სტუდენტის მოძებნა")
    search_term = input("მოძებნე სახელით, გვარით, ქულით ან ID-ით: ").strip()
    
    if not search_term:
        return
    
    try:
        score_search = float(search_term)
        display_search_results(file_path, f"ქულა: {score_search}", score=score_search)
    except ValueError:
        display_search_results(file_path, f"'{search_term}'", search_term=search_term)

def handle_update(file_path: str) -> None:
    """Handle updating a student."""
    print("\n✏️ სტუდენტის განახლება")
    identifier = input("შეიყვანეთ სტუდენტის ID ან სახელი/გვარი: ").strip()
    
    if not identifier:
        return
    
    print("შეიყვანეთ ახალი მნიშვნელობები (Enter გამოტოვებისთვის):")
    updates = {}
    
    name = input("ახალი სახელი: ").strip()
    if name: 
        updates['name'] = name
    
    lastname = input("ახალი გვარი: ").strip()
    if lastname: 
        updates['lastname'] = lastname
    
    address = input("ახალი მისამართი: ").strip()
    if address: 
        updates['address'] = address
    
    score_input = input("ახალი ქულა: ").strip()
    if score_input:
        try:
            updates['score'] = float(score_input)
        except ValueError:
            print("❌ ქულა უნდა იყოს რიცხვი.")
            return
    
    success, message = update_student(file_path, identifier, **updates)
    print("✅" if success else "❌", message)

def handle_delete(file_path: str) -> None:
    """Handle deleting a student."""
    print("\n🗑️ სტუდენტის წაშლა")
    identifier = input("შეიყვანეთ სტუდენტის ID ან სახელი/გვარი: ").strip()
    
    if not identifier:
        return
    
    success, message = delete_student(file_path, identifier)
    print("✅" if success else "❌", message)

def handle_file_management(file_path: str) -> None:
    """Handle file management operations."""
    print("\n📂 ფაილის მართვა")
    print("1. მონაცემების შენახვა სხვა ფაილში")
    print("2. მონაცემების ჩატვირთვა სხვა ფაილიდან")
    
    file_choice = input("აირჩიეთ: ").strip()
    
    if file_choice == "1":
        custom_name = input("ფაილის სახელი: ").strip()
        if custom_name:
            success, message = save_to_file(file_path, custom_name)
            print("✅" if success else "❌", message)
    
    elif file_choice == "2":
        source_file = input("ფაილის მისამართი: ").strip()
        if source_file:
            success, message = load_from_file(source_file, file_path)
            print("✅" if success else "❌", message)


def interactive_menu():
    """Interactive menu for the student management app."""
    current_file = 'final_project/students.json'
    
    menu_options = {
        "1": ("სტუდენტის დამატება", handle_add_student),
        "2": ("ყველა სტუდენტის ნახვა", handle_view_all),
        "3": ("სტუდენტის მოძებნა", handle_search),
        "4": ("სტუდენტის განახლება", handle_update),
        "5": ("სტუდენტის წაშლა", handle_delete),
        "6": ("სტატისტიკა", lambda f: display_statistics(f)),
        "7": ("ფაილის მართვა", handle_file_management),
        "8": ("მუშა ფაილის შეცვლა", None),
        "0": ("გასვლა", None)
    }
    
    while True:
        print("\n" + "="*60)
        print("🎓 სტუდენტების მართვის სისტემა")
        print(f"📁 მიმდინარე ფაილი: {current_file}")
        print()
        
        for key, (description, _) in menu_options.items():
            print(f"{key}. {description}")
        
        choice = input("\n➤ აირჩიეთ ვარიანტი: ").strip()
        
        if choice not in menu_options:
            print("❌ არასწორი არჩევანი!")
            continue
        
        description, handler = menu_options[choice]
        
        if choice == "8":
            new_file = input(f"ახალი ფაილის მისამართი (მიმდინარე: {current_file}): ").strip()
            if new_file:
                current_file = new_file
                print(f"✅ მუშა ფაილი შეიცვალა: {current_file}")
        
        elif choice == "0":
            print("👋 აბა ჰე აბა ჰო!")
            break
        
        elif handler:
            try:
                handler(current_file)
            except Exception as e:
                print(f"❌ შეცდომა: {e}")


def main():
    interactive_menu()

if __name__ == '__main__':
    main()