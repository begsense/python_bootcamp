import random
# 1) დაწერეთ პროგრამა რომელიც დააგენერირებს 100 შემთხვევით რიცხვს 10-დან 1000000000-მდე. Პროგრამამ უნდა იპოვოს ყველაზე მოკლე რიცხვი მიმდევრობაში, ყველაზე გრძელი რიცხვი. Პროგრამამ უნდა დაალაგოს რიცხვები სიგრძის მიხედვით ზრდადობით, კლებადობით. Ყველა შედეგი დაბეჭდეთ ეკრანზე. Გამოიყენეთ min, max, sorted ფუნქციები 
random_numbers_list: list[int] = []

for i in range(100): 
    random_numbers_list.append(random.randint(10, 1000000000))

# ან : random_numbers_list: list[int] = random.sample(range(10, 1000000000), 100)

min_number = min(random_numbers_list)
max_number = max(random_numbers_list)
sorted_list = sorted(random_numbers_list)
print("Min number in list is: ", min_number, "\n")
print("Max number in list is: ", max_number, "\n")
print("Sorted list is: ", sorted_list, "\n")


# 2) Შექმენით სამი სია და შეავსეთ შემთხვევითი რიცხვებით. Ეკრანზე დაბეჭდეთ ერთსა და იმავე ინდექსზე მდგარი რიცხვების ჯამები 
first_list: list[int] = [random.randint(10, 1000000000) for i in range(3)]
second_list: list[int] = [random.randint(10, 1000000000) for i in range(3)]
third_list: list[int] = [random.randint(10, 1000000000) for i in range(3)]

print("********************************")
print(first_list, "\n", second_list, "\n", third_list, "\n")

print("Sorted list by sum of first indexes: ", list(map(lambda x, y, z: x + y + z, first_list, second_list, third_list)))


# 3) Შექმენით სია და შეავსეთ სიტყვებით. Პროგრამამ უნდა გაფილტროს სია, გადაყაროს ყველა ელემენტი რომელიც შეიცავს 3 ზე მეტ სიმბოლოს და ეკრანზე უნდა დაბეჭდოს დარჩენნილი სიტყვები მაღალ რეგისტრში. 
strings_list: list[str] = ["Hi", "everyone", "my", "name", "is", "Begi", "Kopaliani"]

print("********************************")
print(list(map(lambda x: x.upper(), filter(lambda x: len(x) <= 3, strings_list))))