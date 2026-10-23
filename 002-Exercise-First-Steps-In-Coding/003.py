deposit = float(input())
due = int(input())
yearly_present = float(input())

total_sum = deposit + due * (deposit * (yearly_present / 100) / 12)

print(total_sum)
