# 1) Დაწერეთ ფუნქცია რომელიც არგუმენტად მიიღებს ტექსტს და დაარუნებს ამ ტექსტში ხმოვნების რაოდენობას. Გამოიძახეთ ფუნქცია რამდენჯერმე სხვადასხვა არგუმენტისთვის რომ აჩვენოთ მისი მუშაობა
def count_chars(input_string):
    return len(input_string)

    ''' თუ არ გვინდა ჩაშენებული ფუნქციის გამოყენება
    count = 0
    for i in input_string:
        count += 1
    return count '''

print(count_chars("begi"))
print(count_chars("testcase"))

# 2) Დაწერეთ ფუნქცია რომელსაც გადაეცემა განუზღვრელი რაოდენობის რიცხვიტი ტიპის არგუმენტი და აბრუნებს მაქსიმალურს. Გამოიძახეთ ფუნქცია რამდენჯერმე სხვადასხვა არგუმენტისთვის რომ აჩვენოთ მისი მუშაობა
def max_integer(*input_integers):
    return max(input_integers)

    ''' თუ არ გვინდა ჩაშენებული ფუნქციის გამოყენება
    max_int = 0
    for i in input_integers:
        if i > max_int:
            max_int = i
    return max_int '''

print(max_integer(1, 2, 5, 10))
print(max_integer(3))

# 3) Დაწერეთ ფუნქცია რომელიც დაითვლის რიცხვის ფაქტორიალს. Გამოიძახეთ ფუნქცია რამდენჯერმე სხვადასხვა არგუმენტისთვის რომ აჩვენოთ მისი მუშაობა
def calculate_factorial(input_number):
    factorial = 1
    for i in range(1, input_number + 1):
        factorial *= i
    return factorial

print(calculate_factorial(5))
print(calculate_factorial(10))

# 4) Დაწერეთ ფუნქცია, რომელიც დაადგენს გადაცემული რიცხვი მარტივია თუ არა. Გამოიძახეთ ფუნქცია რამდენჯერმე სხვადასხვა არგუმენტისთვის რომ აჩვენოთ მისი მუშაობა
def prime_number(input_number2):
    if input_number2 <= 1:
        return False
    for i in range(2, input_number2):
        if input_number2 % i == 0:
            return False
    return True

print(prime_number(3))
print(prime_number(4))

# 5) Დაწერეთ ფუნქცია რომელსაც გადაეცემა ტექტი და აბრუნებს ამ ტექსტს შებრუნებული მიმდევრობით. Გამოიძახეთ ფუნქცია რამდენჯერმე სხვადასხვა არგუმენტისთვის რომ აჩვენოთ მისი მუშაობა
def reverse_string(input_string2):
    return input_string2[::-1]

print(reverse_string("begi"))
print(reverse_string("wow"))

# 6) Დაწერეთ ფუნქცია რომელსაც გადაეცემა მანქანის მწარმოებელი და გამოშვების წელი. Მანქანის მწარმოებელი უნდა იყოს აუცილებელი არგუმენტი ხოლო გამოშვების წელის ნაგულისხმევი მნიშვნელობა უნდა იყოს მიმდინარე წელი. Ფუნქციას უნდა ჰქონდეს შესაძლებლობა, რომ გადაეცეს განუზღვრელი დასახელების და რაოდენობის კონფიგურაციის პარამეტრები. Გამოიძახეთ ფუნქცია რამდენჯერმე სხვადასხვა არგუმენტისთვის რომ აჩვენოთ მისი მუშაობა
def car_info(**kwargs):
    if "year" not in kwargs:
        kwargs["year"] = 2025
    return kwargs

print(car_info(manufacturer = "Toyota"))
print(car_info(manufacturer = "Honda", year = 2022))