import time

# 1. დაწერეთ ფუნქცია რომელსაც შეეძლება ცელსიუსის ფარენჰეიტებში გადაყვანა და პირიქით. C = (F - 32) * 5/9 , F = C * 9/5 + 32. Main ფუნქციაში დაუწერეთ რამდენიმე მაგალითი თქვენს მიერ შექმნილი ფუნქციის გამართულად მუშაობის სადემონსტარაციოდ
def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius
def celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * 9 / 5 + 32
    return fahrenheit


# 2. დაწერეთ პროგრამა რომელიც მიიღებს ორ ნატურალურ რიცხვს a და b, სადაც 0 < a,b < 10000 და ეკრანზე გამოიტანს ამ ორი რიცხვის უმცირეს საერთო ჯერადს. Მინიშნება lcm(a, b) = (a * b) / gcd(a, b). დააიმპორტეთ და გამოიყენეთ უდიდესი საერთო გამყოფის დათვლის ფუნქციონალი პირველი დავალების ფაილიდან.
''' Მაგალითი 1:
      Enter a: 1000
      Enter b: 400
      LCM of 1000 and 400 is 2000.
მაგალითი 2:
      Enter a: 500
           Enter b: 50
      LCM of 500 and 50 is 500. '''

def calculate_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def calculate_lcm(a, b):
    if 0 < a and b < 1000:
        return (a * b) // calculate_gcd(a, b)
    

def main(): 
    print(fahrenheit_to_celsius(77)) 
    print(celsius_to_fahrenheit(25)) 
    print(calculate_lcm(1000,400))
    print(calculate_lcm(500,50))
    

if __name__ == '__main__': 
    main()


# 3. * მეორე დავალებაში შექმნილი რეკურსიული და იტერაციული ფუნქციებისთვის გაზომეთ დროები და აჩვენეთ რომელი ფუნქცია უფრო სწრაფია
start = time.time()
calculate_lcm(1000,400)
end = time.time()
print(end-start)

start = time.time()
calculate_lcm(1000, 400)
end = time.time()
print(end-start)