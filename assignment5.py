# 1) დაწერეთ პროგრამა რომელიც მიიღებს ნატურალურ რიცხვს - n , სადაც 0 < n < 50 . Პროგრამამ უნდა იპოვოს n მდე არსებული ყველა რიცხვის გამყოფები. Დაბეჭდეთ მაქსიმუმ 3 ცალი გამყოფი. Მაგალითი :
input_number = int(input("Enter a natural number between 1 and 49: "))
index_of_number = 1
count_dividers = 0
if input_number > 0 and input_number < 50:
    while index_of_number <= input_number:
        print(index_of_number, "divider(s)", end=" - ")
        count_dividers = 0
        for i in range(1, index_of_number + 1):
            if index_of_number % i == 0:
                count_dividers += 1
                if count_dividers <= 3:
                    print(i, end = " ")
        print()
        index_of_number += 1
else: 
    print("Enter a number between 1 and 49.")

# ორივე ლუპი გამოვიყენე ისე მარტო ორივე ვაილი რომ ყოფილიყო, ან ორივე ფორ შეიძლებოდა. ისე ფორ მირჩევნია, მაგრამ რადგან ამ ლექციის თემა while არის ვეცდსები while ით ვწერო დავალება


# 2) დაწერეთ პროგრამა რომელიც დაბეჭდავს გამრავლების ტაბულას 1 და 9 ის ჩათვლით. ტაბულა უნდა იყოს სვეტებად შედგენილი. ყოველ მომდევნო სვეტში არ უნდა იყოს გამეორებული ნამრავლი წინა სვეტიდან. Გავიხილოთ 1x3 ის მაგალითი
max_multiplier = 9
column_of_multiplier = 1
row_of_multiplier = 1
multiplied = 0
while row_of_multiplier <= max_multiplier:
    column_of_multiplier = 1
    while column_of_multiplier <= max_multiplier:
        if column_of_multiplier + row_of_multiplier <= max_multiplier + 1:
            multiplier = column_of_multiplier * (column_of_multiplier + row_of_multiplier - 1)
            print(column_of_multiplier, " * ", column_of_multiplier + row_of_multiplier - 1, " = ", multiplier, end = "   ")
        else:
            print(end = "")
        column_of_multiplier += 1
    print()
    row_of_multiplier += 1


# 3) დაწერეთ პროგრამა რომელიც მიიღებს არაუარყოფით მთელ რიცხვს - n.  0 <= n < 20. Პროგრამამ უნდა იპოვოს მიმდევრობის 0-დან n-მდე წევრები. Მიმდევრობა განისაზღვრება შემდეგნაირად: ნულოვანი წევრი არის 0, პირველი წევრი არის 1, ხოლო ყოველი მომდევნო წევრი არის წინა ორი წევრის ჯამი. გამოიყენეთ while ციკლი და არ შეიძლება list-ის გამოყენება. Მაგალითი:
second_input_number = int(input("Enter a number beetween 1 and 49: "))
a = 0
b = 1
sum = 0
count = 0
if second_input_number >= 0 and second_input_number < 50:
    while count < second_input_number:
        if count == 0:
            print(a, end = " ")
        elif count == 1:
            print(b, end = " ")
        else:
            sum = a + b
            print(sum, end = " ")
            a = b
            b = sum
        count += 1
    print()
else:
    print("Enter a number between 1 and 49.")


# 4) დაწერეთ პროგრამა რომელიც მიიღებს ნატურალურ რიცხვს - n, სადაც 0 < n < 50. Პროგრამამ უნდა დახატოს n სიმაღლის ნაძვის ხე სიმბოლოებით *,  /, | და \ .
third_input_number = int(input("Enter a number between 1 and 49: "))
height_index = 1
if third_input_number > 0 and third_input_number < 50:
    while height_index <= third_input_number:
        print(" " * (third_input_number - height_index), end="")
        print("/", end="")
        print("*" * (2 * height_index - 2), end="")
        print("\\")
        height_index += 1
else:
    print("Enter a number between 1 and 49.")