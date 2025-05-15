market = {"ვაშლი": 20, "ატამი": 35, "ბანანი": 12}
market["პიტნა"] = 5
market["ბანანი"] += 8
del market["ვაშლი"]
for fruit, price in market.items():
    if price > 20:
        print(f"{fruit}: {price}")