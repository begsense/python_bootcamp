weekly_temperature = ((33, 34, 28), (24, 31, 27), (24, 23, 27), (28, 32, 34), (33, 21, 28), (20, 25, 31), (21, 31, 28))
weekly_average = []
count = 0
for day in weekly_temperature:
    count += 1
    day_average = sum(day) / len(day)
    weekly_average.append(day_average)
    day_max = max(day)
    day_min = min(day)
    print(f"{count}-ლი დღის საშუალო ტემპერატურა: {day_average}, მაქსიმალური: {day_max}, მინიმალური: {day_min}")
print(f"კვირის საშუალო ტემპერატურა: {sum(weekly_average) / len(weekly_average)}")