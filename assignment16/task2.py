import json

with open("assignment16/data.txt") as file:
    content = file.readlines()
    sold_products = [line.strip().split(",") for line in content]

max_quantity_sold_product = 0
max_revenue_product = 0
average_value_product = 0
average_quantity_product = 0
max_quantity_sold_product_owner = []
max_quantity_sold_product_owner = []

for product in sold_products:
    if int(product[2]) > max_quantity_sold_product:
        max_quantity_sold_product = int(product[2])
    if int(product[2]) * float(product[3]) > max_revenue_product:
        max_revenue_product = int(product[2]) * float(product[3])
    average_value_product += (int(product[2]) * float(product[3])) / len(sold_products)
    average_quantity_product += int(product[2]) / len(sold_products)

max_quantity_sold_product_owner = [product[0] for product in sold_products if int(product[2]) == max_quantity_sold_product]
max_revenue_product_owner = [product[0] for product in sold_products if int(product[2]) * float(product[3]) == max_revenue_product]
most_valued_product = [product[1] for product in sold_products if int(product[2]) == max_quantity_sold_product]

print(f"Max quantity sold product owner is/are: {max_quantity_sold_product_owner}")
print(f"Max revenue product owner is/are: {max_revenue_product_owner}")
print(f"Average value product is: {average_value_product}")
print(f"Average quantity product is: {average_quantity_product}")
print(f"Most valued product is/are: {most_valued_product}")

with open("assignment16/stats.json", "w") as file:
    json.dump({
        "max_quantity_sold_product": max_quantity_sold_product,
        "max_revenue_product": max_revenue_product,
        "average_value_product": average_value_product,
        "average_quantity_product": average_quantity_product,
        "max_quantity_sold_product_owner": max_quantity_sold_product_owner if len(max_quantity_sold_product_owner) > 1 else max_quantity_sold_product_owner[0],
        "max_revenue_product_owner": max_revenue_product_owner if len(max_revenue_product_owner) > 1 else max_revenue_product_owner[0],
        "most_valued_product": most_valued_product if len(most_valued_product) > 1 else most_valued_product[0]
    }, file)