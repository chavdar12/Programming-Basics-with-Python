needed_nylon = int(input())
paint = int(input())
deluter = int(input())
hours = int(input())

print(
    (((needed_nylon + 2) * 1.50) + ((paint + (paint * (10 / 100))) * 14.50) + (deluter * 5.00) + 0.40) +
    ((((needed_nylon + 2) * 1.50) + ((paint + (paint * (10 / 100))) * 14.50) + (
            deluter * 5.00) + 0.40) * 30 / 100) * hours)
