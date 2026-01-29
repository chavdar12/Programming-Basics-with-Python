holiday_price = float(input())
puzzles_count = int(input())
dolls_count = int(input())
bears_count = int(input())
minions_count = int(input())
trucks_count = (int(input()))

total_price = 2.6 * puzzles_count + 3 * dolls_count + 4.1 * bears_count + 8.2 * minions_count + 2 * trucks_count

total_toys_count = puzzles_count + dolls_count + bears_count + minions_count + trucks_count

if total_toys_count >= 50:
    total_price = total_price - (total_price * 0.25)

rent_price = total_price * 0.1
remaining_sum = total_price - rent_price

if remaining_sum >= holiday_price:
    remaining_sum -= holiday_price
    print(f"Yes! {remaining_sum:.2f} lv left.")
else:
    needed_money = holiday_price - remaining_sum
    print(f"Not enough money! {needed_money:.2f} lv needed.")
