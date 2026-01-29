length = int(input())
wight = int(input())
height = int(input())
percent = float(input())

volume = (length * height * wight) / 1000

temp = percent / 100

print(volume * (1 - temp))
