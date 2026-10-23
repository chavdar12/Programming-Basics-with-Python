import math

income_leva = float(input())
average_grade = float(input())
minimum_wage = float(input())

social_scholarship = 0
excellent_scholarship = 0

if income_leva < minimum_wage and average_grade > 4.50:
    social_scholarship = math.floor(0.35 * minimum_wage)
if average_grade >= 5.50:
    excellent_scholarship = math.floor(average_grade * 25)

if social_scholarship == 0 and excellent_scholarship == 0:
    print(f"You cannot get a scholarship!")
elif social_scholarship > excellent_scholarship:
    print(f"You get a Social scholarship {social_scholarship} BGN")
else:
    print(f"You get a scholarship for excellent results {excellent_scholarship} BGN")
