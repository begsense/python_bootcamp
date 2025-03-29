# პროგრამამ უნდა მოგვთხოვოს სტრიქონის შეყვანა. დაბეჭდოს შეყვანილი სტრიქონის ყველა ლუწი ინდექსის მქონე სიმბოლო, გარდა "e"- სიმბოლოსი.  
input_string = input("Enter a string: ")

for i in range(len(input_string)):
    if i % 2 == 0 and input_string[i] != 'e':
        print(input_string[i], end=' ')

print()


# პროგრამამ უნდა შეგვაყვანინოს სიტყვა და დაბეჭდოს ამ სიტყვიდან მხოლოდ თანხმოვანი ასოები.
second_input_string = input("Enter a string again: ")

for i in second_input_string:
    if i != "a" and i != "e" and i != "i" and i != "o" and i != "u" and i != "A" and i != "E" and i != "I" and i != "O" and i != "U":
        print(i, end=" ")

print()

# ან ესე:
third_input_string = input("Enter a string again: ")
vowels = "aeiouAEIOU"
for i in third_input_string:
    if i not in vowels:
        print(i, end=" ")

print()


# პროგრამამ შეგვაყვანინოს სიტყვა და დაბეჭდოს ბოლო, პირველი და შუა ასოები 5-ჯერ while ლუპით. თუ შემოყვანილი ტექსტის ზომა არის ლუწი, მაშინ პროგრამამ უნდა დაბეჭდოს შუა ორი სიმბოლო.\
fourth_input_number = input("Enter a string: ")
length = len(fourth_input_number)
first_char = fourth_input_number[0]
last_char = fourth_input_number[-1]

if length % 2 == 1:
    middle_char = fourth_input_number[length // 2]
    middle = middle_char
else:
    mid_pos = length // 2
    middle = fourth_input_number[mid_pos-1] + fourth_input_number[mid_pos]

count = 0
while count < 5:
    print(f"first symbol: {first_char}, last symbol: {last_char}, middle symbol: {middle}")
    count += 1


'''
*დაწერეთ პროგრამა რომელიც მომხმარებლის შემოყვანილ ტექსტს დაშიფრავს ან განშიფრავს და დაბეჭდავს ეკრანზე. Ნებისმიერი სიმბოლო რომელიც არ მიეკუთვნება a-z დატოვეთ უცვლელი.
დაშიფვრის ლოგიკა ასეთია, ყოველი სიმბოლო(a-z) უნდა შეიცვალოს კლავიატურაზე მის მარჯვნივ მდგომი სიმბოლოთი. Თუ სიმბოლოს მარჯვნივ კლავიატურაზე ინგლისური სიმბოლო არ არის, მაშინ უნდა გადავიდეს პირველ სიმბოლოში ამ სტრიქონიდან. Მაგალითად: p -> q, l -> a და ა.შ.
პროგრამამ უნდა გარდაქმნას მხოლოდ დაბალი რეგისტრის ინგლისური სიმბოლოები a-z. Მაგ. 1:
Enter action (e/d): e
Enter text: power
qpert

მაგ. 2:
Enter action (e/d): d
Enter text: quyjpm
python
'''

action = input("Enter action (e/d): ").lower()
while action not in ['e', 'd']:
    print("Invalid action. Please enter 'e' for encrypt or 'd' for decrypt.")
    action = input("Enter action (e/d): ").lower()

fifth_input_number = input("Enter text: ")
keyboard_row = "qwertyuiopasdfghjklzxcvbnm"
result = ""

for char in fifth_input_number:
    if char.islower() and char in keyboard_row:
        index = keyboard_row.index(char)
        if action == 'e':
            new_char = keyboard_row[(index + 1) % len(keyboard_row)]
        else:
            new_char = keyboard_row[(index - 1) % len(keyboard_row)]
        result += new_char
    else:
        result += char

print(result)