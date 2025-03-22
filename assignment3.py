import math
import random
import datetime

# 1) დაწერეთ პროგრამა რომელიც მიიღებს ორ რიცხვს (x,y) და დაბეჭდავს რიცხვს რომელიც მიიღება x-ის y ხარისხში აყვანით. იხ module math
first_number = int(input("type first number: "))
second_number = int(input("type second number: "))
print(first_number, "აყვანილი ხარისხად", second_number, "არის: ", math.pow(first_number, second_number))


# 2) დაწერეთ პროგრამა რომელიც დააგენერირებს არამთელ შემთხვევით რიცხვს და  დაამრგვალებს მეათედებამდე სიზუსტით. Შედეგი დაბეჭდეთ ეკრანზე. Დამრგვალების ფუნქცია შეარჩიეთ თქვენი სურვილისამებრ. იხ module math
random_number = random.random() * 100
print(random_number, " რომ დავამრგვალოთ მეათედის სიზუსტით იქნება: ", round(random_number, 2))


# 3) დაწერეთ პროგრამა რომელიც მიიღებს 3 მნიშვნელობას: რომელ წელსაა დაბადებული ადამიანი, მერამდენე თვეშია დაბადებული და რა რიცხვშია დაბადებული. Შემდეგ კი ეკრანზე გამოიტანს კვირის რომელ დღესაა დაბადებული ადამიანი. იხ module datetime
year = int(input("type your birth year: "))
month = int(input("type your birth month: "))
day = int(input("type your birth day: "))
date_time = datetime.datetime(year, month, day)
weekday_int = date_time.weekday()

if weekday_int == 0:
    weekday_str = "Monday"
if weekday_int == 1:
    weekday_str = "Tuesday"
if weekday_int == 2:
    weekday_str = "Wednesday"
if weekday_int == 3:
    weekday_str = "Thursday"
if weekday_int == 4:
    weekday_str = "Friday"
if weekday_int == 5:
    weekday_str = "Saturday"
if weekday_int == 6:
    weekday_str = "Saturday"

print("your birth weekday was: ", weekday_str)


# 4) დაწერეთ პროგრამა რომელიც გაშვებისას დაბეჭდავს ბანქოს შემთხვევით მნიშვნელობას (სულ 52 შესაძლო მნიშვნელობა: 4 ფერი (clubs (♣), diamonds (♦), hearts (♥) and spades (♠)) და 13 მნიშვნელობა (A, K, Q, J, 10, 9, 8, 7, 6, 5, 4, 3, 2))
card_color_int = random.randint(0, 3)
card_value_int = random.randint(0, 12)

if card_color_int == 0:
    card_color_str = "clubs (♣)"
if card_color_int == 1:
    card_color_str = "diamonds (♦)"
if card_color_int == 2:
    card_color_str = "hearts (♥)"
if card_color_int == 3:
    card_color_str = "spades (♠)"

if card_value_int == 0:
    card_value_str = "A"
if card_value_int == 1:
    card_value_str = "K"
if card_value_int == 2:
    card_value_str = "Q"
if card_value_int == 3:
    card_value_str = "J"
if card_value_int == 4:
    card_value_str = "10"
if card_value_int == 5:
    card_value_str = "9"
if card_value_int == 6:
    card_value_str = "8"
if card_value_int == 7:
    card_value_str = "7"
if card_value_int == 8:
    card_value_str = "6"
if card_value_int == 9:
    card_value_str = "5"
if card_value_int == 10:
    card_value_str = "4"
if card_value_int == 11:
    card_value_str = "3"
if card_value_int == 12:
    card_value_str = "2"

print("შემთხვევითი ბანქო არის: ", card_color_str, card_value_str)