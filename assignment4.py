# 1) დაწერეთ პროგრამა რომელიც მიიღებს მოთამაშეების რაოდენობას. Პროგრამამ თითოეული მოთამაშისთვის უნდა დააგენერიროს შემთხვევითი კამათლების წყვილი და დაბეჭდოს ეკრანზე. Მაგალითად:  
import random

players_number = int(input("Enter number of players: "))
for i in range(players_number):
    print("player ", i + 1, "dice and roll is: ", random.randint(1, 6), "and ", random.randint(1, 6))


# 2) დაწერეთ პროგრამა, რომელიც მიიღებს მთელ დადებით რიცხვს - n. Პროგრამამ, უნდა დააგენერიროს n ცალი შემთვევით მთელი რიცხვი 0 – 1000 დიაპაზონიდან და ეკრანზე დაბეჭდოს მათ შორის მაქსიმალური. 0 < n < 30.  
natural_number = int(input("Enter positive natural number: "))
random_number = 0
higher_number = 0
if natural_number < 1:
    print("You should type positive number only")
else: 
    for i in range(natural_number): 
        random_number = random.randint(1, 10000)
        print(random_number)
        if random_number > higher_number:
            higher_number = random_number
    print("Higher Number is: ", higher_number)


# 3) Დაწერეთ პროგრამა რომელიც მიიღებს მთელ დადებით რიცხვს. Პროგრამამ უნდა იპოვოს და ეკრანზე ერთ ხაზზე დაბეჭდოს ამ რიცხვის ყველა გამყოფი. 0 < n < 1000. Მაგალითად: 
second_natural_number = int(input("Enter positive natural number again: "))
if second_natural_number < 1:
    print("You should type positive number only")
else: 
    for i in range(1, second_natural_number + 1):
        if second_natural_number % i == 0:
            print(i, end=" ")


# 4) * დაწერეთ პროგრამა რომელიც მიიღებს არაუარყოფით მთელ რიცხვს - n.  0 <= n < 20. Პროგრამამ უნდა იპოვოს მიმდევრობის n-ური წევრი. Მიმდევრობა განისაზღვრება შემდეგნაირად: ნულოვანი წევრი არის 0, პირველი წევრი არის 1, ხოლო ყოველი მომდევნო წევრი არის წინა ორი წევრის ჯამი. Მაგალითად: 
print() # just for next line drop
third_natural_number = int(input("Enter positive natural number once again: "))
_sum = 0
if third_natural_number < 1:
    print("You should type positive number only")
else: 
    for i in range(third_natural_number):
        for j in range(third_natural_number):
            if i > j:
                _sum = i - 1 + j - 1
    print(_sum)