#  1) Is palindrome or not
input_string = input("Enter a string: ")
filtered_string = ""

for i in input_string:
    if (65 <= ord(i) <= 90) or (97 <= ord(i) <= 122):
        filtered_string += i

filtered_string = filtered_string.lower()
if filtered_string == filtered_string[::-1] and len(filtered_string) > 1:
    print("The string is palindrome")
else:        
    print("The string is not palindrome")


# 2) strings with same chars
input_string1 = input("Enter a first string: ")
input_string2 = input("Enter a second string: ")
count = 0

if len(input_string1) == len(input_string2):
    for char in input_string2:
        if char in input_string1:
            count += 1
    if count == len(input_string1):
        print("The strings have same chars")
    else:
        print("The strings do not have same chars")
else:
    print("The strings do not have same chars")


# 3) format date
input_date = input("Enter a date: ")
is_T_founder = False
date_part = ""
time_part = ""

for i in input_date:
    if i == "T":
        is_T_founder = True
    if is_T_founder == False:
        date_part += i
    else:
        if i != "T":
            time_part += i

year = date_part[0:4]
month = date_part[5:7]
day = date_part[8:10]
hour = time_part[0:2]
minute = time_part[3:5]
second = time_part[6:8]
timezone_part = input_date[-6:]
time_zone_sign = timezone_part[0]  
time_zone_hour = timezone_part[1:3]
time_zone_hour = str(int(time_zone_hour))

print(f"{day}-{month}-{year} {hour}:{minute}:{second} {time_zone_sign}{time_zone_hour}")