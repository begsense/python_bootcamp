with open("assignment16/data.txt") as file:
    content = file.readlines()
    sold_products = [line.strip().split(",") for line in content]
    small_priced_products = []
    high_priced_products = []
for product in sold_products:
    if int(product[2]) * float(product[3]) < 10:
        small_priced_products.append(product)
    else:
        high_priced_products.append(product)

with open("assignment16/small_priced_products.txt", "w") as file:
    for product in small_priced_products:
        file.write(f"{product[0]},{product[1]},{product[2]},{product[3]}\n")

with open("assignment16/high_priced_products.txt", "w") as file:
    for product in high_priced_products:
        file.write(f"{product[0]},{product[1]},{product[2]},{product[3]}\n")