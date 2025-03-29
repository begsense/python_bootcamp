# 1. დაწერეთ პროგრამა რომელიც “ჩაიფიქრებს” მთელ რიცხვს 0-დან 100-მდე. Მომხმარებელმა უნდა შემოიყვანოს თავისი ვარიანტი ჩაფიქრებული რიცხვის. Თუ მომხმარებლის შემოყვანილი რიცხვი დაემთხვა პროგრამის ჩაფიქრებულ რიცხვს, დაბეჭდეთ You are winner. Თუ მომხმარებლის შემოყვანილი რიცხვი მეტია, კომპიუტერის ჩაფიქრებულ რიცხვზე, დაბეჭდეთ high. თუ მომხმარებლის შემოყვანილი რიცხვი ნაკლებია კომპიუტერის ჩაფიქრებულ რიცხვზე, დაბეჭდეთ low. Მომხმარებელს აქვს მაქსიმუმ 10 მცდელობა. Თუ მომხმარებელმა 10 მცდელბაში ვერ გამოიცნო რიცხვი, დაბეჭდეთ Computer is winner.
import random

input_number = int(input("Type a number (0: 100): "))
actual_number = random.randint(0, 100)
MAX_ATTEMP = 10
count = 0

if 0 < input_number < 100:
    while count < MAX_ATTEMP:
        if input_number == actual_number:
            print("You are winner")
            break
        else:
            if input_number > actual_number:
                print("Actual number is lower than yours")
            else:
                print("Actual number is higher than yours")
            count += 1
            input_number = int(input("Type a number again: "))
    if count == 10:
        print("Computer is winner")
else:
    print("Input number is not in range 0 - 100")


# 2. დაწერეთ პროგრამა რომელიც მიიღებს დადებით მთელ რიცხვს - n. 0 < n <= 1000. პროგრამამ უნდა დაბეჭდოს რიცხვების მიმდევრობა რომელიც მიიღება შემდეგი პირობით: თუ რიცხვი ლუწია, ეს რიცხვი უნდა გავყოთ 2-ზე, ხოლო თუ რიცხვი კენტია ეს რიცხვი უნდა გავამრავლოთ 3-ზე და დავუმატოთ 1, იქამდე სანამ არ მივიღებთ 1-ს. Მაგალითი:
second_input_number = int(input("Type a number (0: 1000): "))

if 0 < second_input_number <= 1000:
    print(second_input_number, end="")
    while second_input_number != 1:
        if second_input_number % 2 == 0:
            second_input_number = second_input_number // 2
        else:
            second_input_number = second_input_number * 3 + 1
        print(" ->", second_input_number, end="")
else:
    print("Input number is not in range 0 - 1000")


# 3. დაწერეთ პროგრამა რომელიც მიიღებს არაუარყოფით მთელ რიცხვს - n. 0 <= n < 10000 და დაბეჭდავს ამ რიცხვის შებრუნებულ მნიშვნელობას და ამ რიცხვში შემავალი ციფრების ჯამს. გამოიყენეთ while ციკლი მაგალითი:
# გავაკეთებ სტრინგებზე მანიპულაციების გარეშე, რადგან ეგ შემდეგი ლექციის თემაა
third_input_number = int(input("Type a number (0: 1000): "))
last_digit = 0
sum_digit = 0
reversed_number = 0

if 0 < third_input_number <= 10000:
    print("Input number is: ", third_input_number)
    while third_input_number > 0:
        last_digit = third_input_number % 10
        reversed_number = reversed_number * 10 + last_digit
        sum_digit += last_digit
        third_input_number = third_input_number // 10
    print("Reversed number is", reversed_number)
    print("Sum of digits:", sum_digit)
else:
    print("Input number is not in range 0 - 10000")


# 4. *დაწერეთ პროგრამა რომელიც მიიღებს მთელ რიცხვს - n, სადაც 0 < n < 10. Პროგრამამ უნდა დაბეჭდოს სურათზე მოცემული სტრუქტურა. Გამოიყენეთ while
fourth_input_number = int(input("Type a number (0: 10): "))
temp = 0

if 0 < fourth_input_number <= 10:
    i = 1
    while i <= fourth_input_number:
        j = 1
        while j <= i:
            print(j, end="")
            j += 1
        print()
        i += 1

    i = fourth_input_number - 1
    while i >= 1:
        j = 1
        while j <= i:
            print(j, end="")
            j += 1
        print()
        i -= 1
else:
    print("Input number is not in range 0 - 10")


# 5*. დაწერეთ პროგრამა რომელიც მიიღებს მთელ რიცხვს - n, სადაც 0 < n < 10. Პროგრამამ უნდა დაბეჭდოს სურათზე მოცემული სტრუქტურა. Გამოიყენეთ while
fifth_input_number = int(input("Type a number (0: 10): "))

if 0 < fifth_input_number <= 10:
    i = 0
    while i <= fifth_input_number:
        spaces = " " * (fifth_input_number - i)
        left = ""
        num = i
        while num >= 0:
            left += str(num)
            num -= 1

        right = ""
        num = 1
        while num <= i:
            right += str(num)
            num += 1

        line = spaces + left + right
        print(line)
        i += 1
else:
    print("Input number is not in range 0 - 10")