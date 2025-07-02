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
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(students, f, indent=2, ensure_ascii=False)

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

def display_students(students: list[dict], message: str = None) -> None:
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

def find_students(file_path: str, **kwargs) -> list[dict]:
    """
    Universal search function for students.
    Supports searching by: name, lastname, score, id, or any combination.
    Uses EXACT matching for name, lastname, and score.
    """
    students = load_students(file_path)
    
    if not students:
        return []
    
    filtered_students = students
    search_criteria = []
    
    name = kwargs.get('name')
    lastname = kwargs.get('lastname') 
    score = kwargs.get('score')
    student_id = kwargs.get('id')
    search_term = kwargs.get('search_term')
    
    if search_term:
        filtered_students = []

        for student in students:
            if (search_term == student['id'] or 
                search_term.lower() == student['name'].lower() or
                search_term.lower() == student['lastname'].lower() or
                str(search_term) == str(student['score'])):
                filtered_students.append(student)
        
        search_criteria.append(f"'{search_term}'")
    
    else:
        if student_id:
            filtered_students = [s for s in filtered_students if s['id'] == student_id]
            search_criteria.append(f"ID: {student_id}")
        
        if name:
            filtered_students = [s for s in filtered_students if s['name'].lower() == name.lower()]
            search_criteria.append(f"სახელი: {name}")
        
        if lastname:
            filtered_students = [s for s in filtered_students if s['lastname'].lower() == lastname.lower()]
            search_criteria.append(f"გვარი: {lastname}")
        
        if score is not None:
            filtered_students = [s for s in filtered_students if s['score'] == score]
            search_criteria.append(f"ქულა: {score}")
    
    if search_criteria:
        criteria_text = ", ".join(search_criteria)
        if filtered_students:
            display_students(filtered_students, f"მოძებნილი სტუდენტ(ებ)ი ({criteria_text}):")
        else:
            print(f"სტუდენტები ვერ მოიძებნა კრიტერიუმით: {criteria_text}")
    
    return filtered_students

def get_students(file_path: str, sort_by: str = None, descending: bool = False, **filters) -> list[dict]:
    """
    Retrieve and display students with optional filtering and sorting.
    Consolidates the original get_students functionality.
    """
    students = load_students(file_path)
    
    if filters:
        students = find_students(file_path, **filters)
        if not students:
            return []
    
    if sort_by in ['name', 'lastname', 'score']:
        students = sorted(students, key=lambda s: s[sort_by], reverse=descending)
    
    if not filters:
        display_students(students, "ყველა სტუდენტი:")
    
    return students

def update_student(file_path: str, student_id: str = None, search_term: str = None, **updates) -> bool:
    """
    Update student information. Can find student by ID or search term.
    Only provided fields will be updated.
    """
    students = load_students(file_path)
    
    target_student = None
    target_index = None
    
    if student_id:
        for i, student in enumerate(students):
            if student['id'] == student_id:
                target_student = student
                target_index = i
                break
    elif search_term:
        matching_students = []
        for i, student in enumerate(students):
            if (search_term == student['id'] or 
                search_term.lower() == student['name'].lower() or
                search_term.lower() == student['lastname'].lower() or
                str(search_term) == str(student['score'])):
                matching_students.append((i, student))
        
        if len(matching_students) == 1:
            target_index, target_student = matching_students[0]
        elif len(matching_students) > 1:
            print("რამდენიმე სტუდენტი მოიძებნა. გთხოვთ უფრო ზუსტად მიუთითოთ:")
            matches = [student for _, student in matching_students]
            display_students(matches)
            return False
    
    if not target_student:
        identifier = student_id or search_term
        print(f"სტუდენტი '{identifier}' ვერ მოიძებნა.")
        return False
    
    updated_fields = []
    for field, value in updates.items():
        if field in target_student and value is not None:
            students[target_index][field] = value
            updated_fields.append(field)
    
    if updated_fields:
        save_students(file_path, students)
        print(f"სტუდენტის {students[target_index]['name']} {students[target_index]['lastname']} ინფორმაცია განახლდა: {', '.join(updated_fields)}")
        return True
    else:
        print("არაფერი განახლებულა. გთხოვთ მიუთითოთ სწორი ველები.")
        return False

def get_statistics(file_path: str) -> dict:
    """Calculate and return all statistics in one function."""
    students = load_students(file_path)
    
    if not students:
        print("სტუდენტები ვერ მოიძებნა.")
        return {}
    
    scores = [s['score'] for s in students]
    total_students = len(students)
    
    stats = {
        'total_students': total_students,
        'average_score': sum(scores) / total_students,
        'highest_score': max(scores),
        'lowest_score': min(scores),
        'highest_student': max(students, key=lambda s: s['score']),
        'lowest_student': min(students, key=lambda s: s['score'])
    }
    
    return stats

def display_statistics(file_path: str) -> None:
    """Display all statistics."""
    stats = get_statistics(file_path)
    
    if not stats:
        return
    
    print(f"\n{'='*50}")
    print(f"სტატისტიკა")
    print(f"{'='*50}")
    print(f"სტუდენტების რაოდენობა: {stats['total_students']}")
    print(f"საშუალო ქულა: {stats['average_score']:.2f}")
    print(f"უმაღლესი ქულა: {stats['highest_score']} - {stats['highest_student']['name']} {stats['highest_student']['lastname']}")
    print(f"ყველაზე დაბალი ქულა: {stats['lowest_score']} - {stats['lowest_student']['name']} {stats['lowest_student']['lastname']}")

def delete_student(file_path: str, identifier: str) -> bool:
    """Delete a student by ID or search term."""
    students = load_students(file_path)
    original_count = len(students)
    
    student_to_delete = next((s for s in students if s['id'] == identifier), None)
    
    if not student_to_delete:
        matches = find_students(file_path, search_term=identifier)
        if len(matches) == 1:
            student_to_delete = matches[0]
        elif len(matches) > 1:
            print("რამდენიმე სტუდენტი მოიძებნა. გთხოვთ უფრო ზუსტად მიუთითოთ:")
            display_students(matches)
            return False
    
    if student_to_delete:
        students = [s for s in students if s['id'] != student_to_delete['id']]
        save_students(file_path, students)
        print(f"სტუდენტი {student_to_delete['name']} {student_to_delete['lastname']} წაშლილია.")
        return True
    else:
        print(f"სტუდენტი '{identifier}' ვერ მოიძებნა.")
        return False

def manage_files(action: str, file_path: str, **kwargs) -> bool:
    """Universal file management function."""
    try:
        if action == "save_as":
            custom_name = kwargs.get('custom_name')
            if not custom_name.endswith('.json'):
                custom_name += '.json'
            
            students = load_students(file_path)
            if not students:
                print("მონაცემები ვერ მოიძებნა შესანახად.")
                return False
            
            save_students(custom_name, students)
            print(f"მონაცემები წარმატებით შეინახა ფაილში: {custom_name}")
            return True
        
        elif action == "load_from":
            source_file = kwargs.get('source_file')
            target_file = kwargs.get('target_file', file_path)
            
            if not os.path.exists(source_file):
                print(f"ფაილი {source_file} ვერ მოიძებნა.")
                return False
            
            students = load_students(source_file)
            if students:
                save_students(target_file, students)
                print(f"მონაცემები წარმატებით ჩაიტვირთა ({len(students)} სტუდენტი)")
                return True
            else:
                print(f"ფაილი {source_file} ცარიელია ან არასწორი ფორმატისაა.")
                return False
        
    except Exception as e:
        print(f"შეცდომა ფაილთან მუშაობისას: {e}")
        return False

def interactive_menu():
    """Interactive menu for the student management app."""
    current_file = 'final_project/students.json'
    
    menu_options = {
        "1": ("სტუდენტის დამატება", "add_student"),
        "2": ("ყველა სტუდენტის ნახვა", "view_all"),
        "3": ("სტუდენტის მოძებნა", "search"),
        "4": ("სტუდენტის განახლება", "update"),
        "5": ("სტუდენტის წაშლა", "delete"),
        "6": ("სტატისტიკა", "statistics"),
        "7": ("ფაილის მართვა", "file_management"),
        "8": ("მუშა ფაილის შეცვლა", "change_file"),
        "0": ("გასვლა", "exit")
    }
    
    while True:
        print("\n" + "="*60)
        print("🎓 სტუდენტების მართვის სისტემა")
        print(f"📁 მიმდინარე ფაილი: {current_file}")
        print()
        
        for key, (description, _) in menu_options.items():
            print(f"{key}. {description}")
        
        choice = input("\n➤ აირჩიეთ ვარიანტი ციფრით").strip()
        
        if choice not in menu_options:
            print("❌ არასწორი არჩევანი!")
            continue
        
        action = menu_options[choice][1]
        
        if action == "add_student":
            print("\n📝 ახალი სტუდენტის დამატება")
            name = input("სახელი: ").strip()
            lastname = input("გვარი: ").strip()
            address = input("მისამართი: ").strip()
            try:
                score = float(input("ქულა: ").strip())
                add_student(current_file, name, lastname, address, score)
                print("✅ სტუდენტი წარმატებით დაემატა!")
            except ValueError:
                print("❌ ქულა უნდა იყოს რიცხვი.")
        
        elif action == "view_all":
            sort_option = input("ჩაწერე (name/lastname/score) თუ გინდა დაალაგო ქულის, გვარის და სახელის სტუდენტები.").strip().lower()
            sort_by = sort_option if sort_option in ['name', 'lastname', 'score'] else None
            
            descending = False
            if sort_by:
                descending = input("კლებადობით? (y/n): ").strip().lower() == 'y'
            
            get_students(current_file, sort_by=sort_by, descending=descending)
        
        elif action == "search":
            print("\n🔍 სტუდენტის მოძებნა")
            search_term = input("მოძებნე სახელით, გვარით, ქულით ან ID-ით: ").strip()
            if search_term:
                try:
                    score_search = float(search_term)
                    find_students(current_file, score=score_search)
                except ValueError:
                    find_students(current_file, search_term=search_term)
        
        elif action == "update":
            print("\n✏️ სტუდენტის განახლება")
            identifier = input("შეიყვანეთ სტუდენტის ID ან სახელი/გვარი: ").strip()
            if identifier:
                print("შეიყვანეთ ახალი მნიშვნელობები (Enter გამოტოვებისთვის):")
                updates = {}
                
                name = input("ახალი სახელი: ").strip()
                if name: updates['name'] = name
                
                lastname = input("ახალი გვარი: ").strip()
                if lastname: updates['lastname'] = lastname
                
                address = input("ახალი მისამართი: ").strip()
                if address: updates['address'] = address
                
                score_input = input("ახალი ქულა: ").strip()
                if score_input:
                    try:
                        updates['score'] = float(score_input)
                    except ValueError:
                        print("❌ ქულა უნდა იყოს რიცხვი.")
                        continue
                
                update_student(current_file, search_term=identifier, **updates)
        
        elif action == "delete":
            print("\n🗑️ სტუდენტის წაშლა")
            identifier = input("შეიყვანეთ სტუდენტის ID ან სახელი/გვარი: ").strip()
            if identifier:
                delete_student(current_file, identifier)
        
        elif action == "statistics":
            display_statistics(current_file)
        
        elif action == "file_management":
            print("\n📂 ფაილის მართვა")
            print("1. მონაცემების შენახვა სხვა ფაილში")
            print("2. მონაცემების ჩატვირთვა სხვა ფაილიდან")
            
            file_choice = input("აირჩიეთ: ").strip()
            
            if file_choice == "1":
                custom_name = input("ფაილის სახელი: ").strip()
                if custom_name:
                    manage_files("save_as", current_file, custom_name=custom_name)
            
            elif file_choice == "2":
                source_file = input("ფაილის მისამართი: ").strip()
                if source_file:
                    manage_files("load_from", current_file, source_file=source_file, target_file=current_file)
        
        elif action == "change_file":
            new_file = input(f"ახალი ფაილის მისამართი (მიმდინარე: {current_file}): ").strip()
            if new_file:
                current_file = new_file
                print(f"✅ მუშა ფაილი შეიცვალა: {current_file}")
        
        elif action == "exit":
            print("👋 მადლობა პროგრამის გამოყენებისთვის!")
            break

def main():
    interactive_menu()

if __name__ == '__main__':
    main()