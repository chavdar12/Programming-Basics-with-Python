chicken_menu = int(input())
fish_menu = int(input())
veggie_menu = int(input())

temp = (chicken_menu * 10.35) + (fish_menu * 12.40) + (veggie_menu * 8.15)

discount = (temp * 20 / 100)

print(round(temp + discount + 2.50, 2))
