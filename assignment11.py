import random
# 1.Დაწერეთ პროგრამა რომელიც მოცემული ტემპერატურების [22, 25, 19, 23, 25, 26, 23] მიხედვით გამოითვლის საშუალო ტემპერატურას და დაბეჭდავს ეკრანზე.
temp_list = [22, 25, 19, 23, 25, 26, 23]

def average_temp(temp_list):
    return sum(temp_list) / len(temp_list)

print(average_temp(temp_list))


'''
2.Დაწერეთ პროგრამა რომელიც დააგენერირებს 50 ცალ შემთხვევით რიცხვს 1-დან 30-მდე და ჩაწერს სიაში. Პროგრამამ უნდა გადაუაროს სიას და თითოეული ელემენტისთვის ეს ელემენტი ჩაწეროს ახალ სიაში, იმდენჯერ, რაც არის მისი მნიშვნელობა. დაბეჭდეთ ახალი სიის სიგრძე და თვითონ სია ეკრანზე

    Მაგალითი 1: (სიმარტივისთვის მაგალითს ჩავწერთ 3 ზომის სიისთვის) .  
    ვთქვათ პროგრამამ დააგენერირა სია, [1, 4, 2]
    უნდა დაიბეჭდოს
    List - [1, 4, 4, 4, 4, 2, 2]
    Length - 7
'''
random_numbers_list = []

for i in range(50):
    random_number = random.randint(1, 30)
    for i in range(random_number):
        random_numbers_list.append(random_number) 

# ესე გამიმარტივდა, მაგრამ თუ აუცილებლად ჯერ უნდა დააგენერიროს სია, მერე ამ სიას გადაუაროს და გაამრავლოს მსგავსი ციფრები თავისივე რაოდენობიდან გამომდინარე ესე შეიძლება:
'''
for i in range(50):
    random_numbers_list.append(random.randint(1, 30))

new_list = []
for i in random_numbers_list:
    new_list.extend([i] * i)
'''
print(random_numbers_list)
print(len(random_numbers_list))


'''
3.დაწერეთ პროგრამა რომელიც დააგენერირებს 50 ცალ შემთხვევით რიცხვს 1-დან 30-მდე და ჩაწერს სიაში. Პროგრამამ უნდა გადაუაროს სიას და მოაშოროს ყველა დუპლიკატი. დაბეჭდეთ ახალი სიის სიგრძე და თვითონ სია ეკრანზე

    Მაგალითი 1: (სიმარტივისთვის მაგალითს ჩავწერთ 5 ზომის სიისთვის) .  
    ვთქვათ პროგრამამ დააგენერირა სია, [2, 1, 4, 2, 1]
    უნდა დაიბეჭდოს
    List - [2, 1,  4]
    Length - 3
'''
second_random_numbers_list = []

for i in range(50):
    second_random_number = random.randint(1, 30)
    if second_random_number not in second_random_numbers_list:
        second_random_numbers_list.append(second_random_number)

print(second_random_numbers_list)
print(len(second_random_numbers_list))


'''
4.*  დაწერეთ ფუნქცია, რომელსაც გადაეცემა ორი დალაგებული სია და დააბრუნებს ახალ სიას, რომელშიც იქნება ელემენტები ორივე სიიდან დალაგებული მიმდევრობით. Main ფუნქციიდან გატესტეთ თქვენს მიერ შექმნილი ფუნქცია სხვადასხვა ინფუთისთვის. Არ გამოიყენოთ ფუნქციები sort და sorted. Შეეცადეთ რომ თქვენ შერწყათ გადმოცემული ორი სია ისე, რომ დალაგება არ დაირღვეს.

    Მაგალითი 1
    თუ ფუნქციას გადავეცით სიები
    [1,  3, 10]
    [0, 4,7, 9]
    უნდა დააბრუნოს
    [0, 1, 3, 4, 7, 9, 10]
'''

first_list = [1, 3, 10]
second_list = [0, 4, 7, 9]

''' with sort
def merge_lists(first_list, second_list):
    merged_list = first_list + second_list
    merged_list.sort()
    return merged_list
'''

# without sort
def merge_lists(list1, list2):
    merged = []
    i = j = 0
    
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1
    
    while i < len(list1):
        merged.append(list1[i])
        i += 1

    while j < len(list2):
        merged.append(list2[j])
        j += 1
    
    return merged

print(merge_lists(first_list, second_list))