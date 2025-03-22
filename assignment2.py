# 1)  Დაწერეთ პროგრამა რომელიც მიიღებს true ან false. Თუ პროგრამამ მიიღო true, ეკრანზე დაბეჭდეთ “whoala”.
genderIsMale = input("type your gender (male/female): ").lower() == "male"

if genderIsMale:
    print("whoala")
else:
    print("it can be a whoala in future if you want to, just think about it :D")


# ან თუ აუცილებლად სტრინგი true უნდა იყოს ინფუთი მაშინ:
_input = input("type true or false ").lower() == "true"

if _input:
    print("whoala")
else:
    print("you did not type true") 


# 2) Დაწერეთ პროგრამა რომელიც მიიღებს ორ რიცხვს, დაადგენს პირველი რიცხვი არის თუ არა მეორე რიცხვის ჯერადი და დაბეჭდავს ეკრანზე. A რიცხვს ეწოდება B რიცხვის ჯერადი, თუ A = B * n,  სადაც n ნატურალური რიცხვია.
firstNumber = int(input("type first number: "))
secondNumber = int(input("type second number: "))

if firstNumber % secondNumber == 0:
    print(firstNumber, " is factor of ", secondNumber)
else:
    print(firstNumber, " is not factor of ", secondNumber)


# 3) Დაწერეთ პროგრამა რომელიც მიიღებს მთელ რიცხვს. Პროგრამამ უნდა დაბეჭდოს ყველა მარტივი გამყოფი ერთ ხაზზე. Შემოსული რიცხვის მაქსიმალური მნიშვნელობა უნდა იყოს 10. Მაგალითი: თუ პროგრამას გადავეცით 6, გამოსავალზე უნდა დაიბეჭდოს 2, 3. ახსნა: 6 იყოფა 2-ზეც და 3-ზეც. 2 და 3 არის მარტივი რიცხვები. Დაიცავით პროგრამა ისეთი არგუმენტებისგან, რომლებიც არ არის დასაშვები.
intNumber = int(input("type int number from 0 to 10: "))

if intNumber > 10 or intNumber < 1:
    print("wrong number, type from 0 to 10")
else:
    if intNumber % 10 == 0:
        print("divisor of number is: 5")
    elif intNumber % 9 == 0: 
        print("divisor of number is: 3")
    elif intNumber % 8 == 0: 
        print("divisor of number is: 2")
    elif intNumber % 7 == 0: 
        print("divisor of number is: 7")
    elif intNumber % 6 == 0: 
        print("divisors of number is: 3 and 2")
    elif intNumber % 5 == 0:
        print("divisor of number is: 5")
    elif intNumber % 4 == 0:
        print("divisor of number is: 2")
    elif intNumber % 3 == 0:
        print("divisor of number is: 3")
    elif intNumber % 2 == 0:
        print("divisor of number is: 2")
    elif intNumber % 1 == 0:
        print("number 1 has no easy divisor")
    else:
        print("wrong number")


# Დაწერეთ პროგრამა რომელიც არგუმენტად მიიღებს მანქანის სიჩქარეს, განსაზღვრავს მისი სიჩქარის კატეგორიას და დაბეჭდავს ეკრანზე. Სიჩქარის კატეგორიები განისაზღვრება შემდეგნაირად. Თუ ავტომობილის სიჩქარე 30 კმ/სთ-ზე ნაკლებია, მისი კატეგორიაა - SLOW. Როცა ავტომობილის სიჩქარე  120 კმ/სთ-ზე მეტია, მისი კატეგორიაა - VERY FAST. Თუ ავტომობილის სიჩქარე მეტია 60 კმ/სთ-ზე, მისი კატეგორიაა - FAST. Ხოლო თუ ავტომობილის სიჩქარე მეტია 30 კმ/სთ-ზე, მისი კატეგორიაა - MODERATE. (თუ ავტომობლი ხვდება ორ კატეგორაიში, უნდა შეირჩეს უფრო სწრაფი კატეგორია)
carSpeed = int(input("type speed of car: "))
categoryOfSpeed = "no category yet"

if carSpeed > 0:
    if carSpeed < 30:
        categoryOfSpeed = "SLOW"
    if carSpeed > 30: 
        categoryOfSpeed = "MODERABLE"
    if carSpeed > 60:
        categoryOfSpeed = "FAST"
    if carSpeed > 120:
        categoryOfSpeed = "VERY FAST"
else:
    categoryOfSpeed = "Can't find out category because you typed negative speed"
print("category of speed is ", categoryOfSpeed)