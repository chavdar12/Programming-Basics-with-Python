square_meters = float(input())
total_price = square_meters * 7.61
discount = total_price * (18 / 100)

print(f'The final price is: {total_price - discount}')
print(f'The discount is: {discount}')
