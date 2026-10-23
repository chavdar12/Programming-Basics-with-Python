import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent

S1 = "001-First-Steps-In-Coding"
E1 = "002-Exercise-First-Steps-In-Coding"
S2 = "003-Conditional-Statements"
E2 = "004-Exercise-Conditional-Statements"
S3 = "005-Conditional-Statements-Advanced"
E3 = "006-Exercise-Conditional-Statements-Advanced"
S4 = "007-For-Loops"
E4 = "008-Exercise-For-Loops"
S5 = "009-While-Loops"
E5 = "010-Exercise-While-Loops"
S6 = "011-Nested-Loops"
E6 = "012-Exercise-Nested-Loops"


def lines(*items):
    return "\n".join(str(i) for i in items)


# (script, stdin lines, expected stdout)
CASES = [
    (f"{S1}/001.py", [], "Hello SoftUni"),
    (f"{S1}/002.py", [], lines(*range(1, 11))),
    (f"{S1}/003.py", [2, 7], "14"),
    (f"{S1}/004.py", [5], "12.7"),
    (f"{S1}/005.py", ["Peter"], "Hello Peter!"),
    (f"{S1}/006.py", ["Peter", "Pan", 20, "Sofia"], "You are Peter Pan, a 20-years old person from Sofia."),
    (f"{S1}/007.py", ["George", 4], "The architect George will need 12 hours to complete 4 project/s."),
    (f"{S1}/008.py", [5, 4], "28.5"),
    (f"{S1}/009.py", [100], lines("The final price is: 624.02", "The discount is: 136.98")),

    (f"{E1}/001.py", [22], "39.50078"),
    (f"{E1}/002.py", [3.141592653589793], "180.0"),
    (f"{E1}/003.py", [200, 3, 5.7], "202.85"),
    (f"{E1}/003.py", [2350, 6, 7], "2432.25"),
    (f"{E1}/004.py", [212, 20, 2], "5"),
    (f"{E1}/005.py", [2, 3, 4, 25], "28.5"),
    (f"{E1}/005.py", [4, 2, 5, 13], "37.932"),
    (f"{E1}/006.py", [10, 11, 4, 8], "727.09"),
    (f"{E1}/007.py", [2, 4, 3], "116.2"),
    (f"{E1}/008.py", [365], "811.76"),
    (f"{E1}/009.py", [85, 75, 47, 17], "248.68875"),

    (f"{S2}/001.py", ["square", 5], "25.000"),
    (f"{S2}/001.py", ["circle", 6], "113.097"),
    (f"{S2}/002.py", [2], "even"),
    (f"{S2}/002.py", [7], "odd"),
    (f"{S2}/003.py", [6], "Excellent!"),
    (f"{S2}/003.py", [5], ""),
    (f"{S2}/004.py", [5, 3], "5"),
    (f"{S2}/005.py", [150], "Between 100 and 200"),
    (f"{S2}/006.py", ["qwerty"], "Wrong password!"),
    (f"{S2}/006.py", ["s3cr3t!P@ssw0rd"], "Welcome"),
    (f"{S2}/007.py", [40.8, 20, 25, 30, 50, 10], "Yes! 418.20 lv left."),

    (f"{E2}/001.py", [20], lines(6, 26)),
    (f"{E2}/001.py", [175], lines(37.0, 212.0)),
    (f"{E2}/002.py", [12, "m", "cm"], "1200.000"),
    (f"{E2}/003.py", [20000, 120, 55.5], lines("Action!", "Wingard starts filming with 11340.00 leva left.")),
    (f"{E2}/004.py", [23, 59], "0:14"),
    (f"{E2}/005.py", [300, 5.65, 420], "You get a Social scholarship 147 BGN"),
    (f"{E2}/005.py", [1000, 5.5, 600], "You get a scholarship for excellent results 137 BGN"),
    (f"{E2}/005.py", [480, 4.60, 450], "You cannot get a scholarship!"),
    (f"{E2}/006.py", [35, 45, 44], "2:04"),
    (f"{E2}/007.py", [8], "slow"),
    (f"{E2}/007.py", [3500], "extremely fast"),
    (f"{E2}/008.py", [10464, 1500, 20], "No, he failed! He was 20786.00 seconds slower."),
    (f"{E2}/008.py", [1000, 29, 30], "Yes, he succeeded! The new world record is 882.50 seconds."),

    (f"{S3}/001.py", ["dog"], "mammal"),
    (f"{S3}/001.py", ["cat"], "unknown"),
    (f"{S3}/002.py", ["Monday"], "12"),
    (f"{S3}/003.py", [2], "Tuesday"),
    (f"{S3}/003.py", [8], "Error"),
    (f"{S3}/004.py", ["banana"], "fruit"),
    (f"{S3}/005.py", ["apple", "Tuesday", 2], "2.40"),
    (f"{S3}/005.py", ["tomato", "Monday", 0.5], "error"),
    (f"{S3}/006.py", [75], "invalid"),
    (f"{S3}/006.py", [150], ""),
    (f"{S3}/007.py", [-25], "Yes"),
    (f"{S3}/007.py", [0], "No"),
    (f"{S3}/008.py", [12, "f"], "Miss"),
    (f"{S3}/008.py", [17, "m"], "Mr."),
    (f"{S3}/009.py", [14, "apartment", "positive"], "264.06"),
    (f"{S3}/010.py", ["coffee", "Varna", 2], "0.9"),
    (f"{S3}/011.py", ["Sofia", 1500], "120.00"),
    (f"{S3}/011.py", ["Kaspichan", 100], "error"),
    (f"{S3}/012.py", [11, "Sunday"], "closed"),
    (f"{S3}/012.py", [11, "Monday"], "open"),

    (f"{E3}/001.py", ["Premiere", 10, 12], "1440.00"),
    (f"{E3}/002.py", [3000, "Summer", 11], "Not enough money! You need 570.00 leva."),
    (f"{E3}/003.py", ["May", 15], lines("Apartment: 877.50 lv.", "Studio: 525.00 lv.")),
    (f"{E3}/004.py", [50, "summer"], lines("Somewhere in Bulgaria", "Camp - 15.00")),
    (f"{E3}/005.py", ["Roses", 55, 250], "Not enough money, you need 25.00 leva more."),
    (f"{E3}/006.py", [9, 30, 9, 50], lines("Late", "20 minutes after the start")),
    (f"{E3}/006.py", [16, 0, 15, 0], lines("Early", "1:00 hours before the start")),
    (f"{E3}/007.py", [10, 12, "+"], "10 + 12 = 22 - even"),
    (f"{E3}/007.py", [0, 5, "/"], "0 / 5 = 0.00"),
    (f"{E3}/007.py", [10, 0, "%"], "Cannot divide 10 by zero"),
    (f"{E3}/008.py", [16, "Morning"], "It's 16 degrees, get your Sweatshirt and Sneakers."),
    (f"{E3}/009.py", ["leap", 5, 2], "45"),

    (f"{S4}/001.py", ["abc"], lines("a", "b", "c")),
    (f"{S4}/002.py", [10, 170, 6], "Yes! 5.00"),
    (f"{S4}/003.py", [4], lines(1, 4, 16)),
    (f"{S4}/004.py", [2, 10, 90, 60, 40], "Yes, sum = 100"),
    (f"{S4}/005.py", [3, 1, -3, 5], lines("Max number: 5", "Min number: -3")),
    (f"{S4}/006.py", [], lines(*range(1, 101))),
    (f"{S4}/007.py", [3], lines(3, 2, 1)),
    (f"{S4}/008.py", [10], lines(1, 4, 7, 10)),
    (f"{S4}/009.py", [2, 10, 20], "30"),
    (f"{S4}/010.py", ["hello"], "6"),

    (f"{E4}/001.py", [3, 3, 6, 9], lines("33.33%", "100.00%", "0.00%")),
    (f"{E4}/002.py", [3, 3, 4, 1], lines("Yes", "Sum = 4")),
    (f"{E4}/002.py", [2, 1, 5], lines("No", "Diff = 4")),
    (f"{E4}/003.py", [3, 1, 450, 900], lines("33.33%", "0.00%", "33.33%", "0.00%", "33.33%")),
    (f"{E4}/004.py", [], lines(*range(7, 1000, 10))),
    (f"{E4}/005.py", [2, 1.5, -2.5],
     lines("OddSum=1.50,", "OddMin=1.50,", "OddMax=1.50,", "EvenSum=-2.50,", "EvenMin=-2.50,", "EvenMax=-2.50")),
    (f"{E4}/005.py", [1, 1],
     lines("OddSum=1.00,", "OddMin=1.00,", "OddMax=1.00,", "EvenSum=0.00,", "EvenMin=No,", "EvenMax=No")),
    (f"{E4}/006.py", [3, 500, "Facebook", "Instagram", "Reddit"], "200"),
    (f"{E4}/006.py", [2, 200, "Facebook", "Facebook"], "You have lost your salary."),

    (f"{S5}/001.py", [5.51, 69.42, 100, "NoMoreMoney"],
     lines("Increase: 5.51", "Increase: 69.42", "Increase: 100.00", "Total: 174.93")),
    (f"{S5}/001.py", [10, -5], lines("Increase: 10.00", "Invalid operation!", "Total: 10.00")),
    (f"{S5}/002.py", ["Gosho", 5, 5.5, 6, 5.43, 5.5, 6, 5.55, 5, 6, 6, 5.43, 5], "Gosho graduated. Average grade: 5.53"),
    (f"{S5}/002.py", ["Mimi", 5, 6, 2, 3], "Mimi has been excluded at 3 grade"),
    (f"{S5}/003.py", [100, 99, 80, 70, "Stop"], "100"),
    (f"{S5}/004.py", [100, 99, 80, 70, "Stop"], "70"),
    (f"{S5}/005.py", [10, 10, 2, 20, 20, 20, 20, 122], "No more free space! You need 2 Cubic meters more."),
    (f"{S5}/005.py", [10, 1, 2, 4, 6, "Done"], "10 Cubic meters left."),
    (f"{S5}/006.py", ["Nakov", 1234, "pass", 1324, 1234], "Welcome Nakov!"),
    (f"{S5}/007.py", ["Nakov", "SoftUni", "Stop"], lines("Nakov", "SoftUni")),
    (f"{S5}/008.py", [31], lines(1, 3, 7, 15, 31)),
    (f"{S5}/009.py", [100, 10, 20, 30, 40], "100"),

    (f"{E5}/001.py", [10, 10, 20, 20, 20, 20, 21], "No more cake left! You need 1 pieces more."),
    (f"{E5}/001.py", [10, 2, 2, 4, 6, "STOP"], "8 pieces are left."),
    (f"{E5}/002.py", [1.23], "4"),
    (f"{E5}/002.py", [1.15], "3"),
    (f"{E5}/003.py", [3, "Money", 6, "Story", 4, "Spring Time", 5, "Bus", 6, "Enough"],
     lines("Average score: 5.25", "Number of problems: 4", "Last problem: Bus")),
    (f"{E5}/003.py", [2, "Income", 3, "Game Info", 6, "Best Player", 4], "You need a break, 2 poor grades."),
    (f"{E5}/004.py", ["Troy", "Stronger", "Life Style", "Troy"], "You checked 2 books and found it."),
    (f"{E5}/004.py", ["The Spot", "Hunger Games", "Harry Potter", "Torronto", "Spotify", "No More Books"],
     lines("The book you search is not here!", "You checked 4 books.")),
    (f"{E5}/005.py", [2000, 1000, "spend", 1200, "save", 2000], "You saved the money for 2 days."),
    (f"{E5}/005.py", [110, 60] + ["spend", 10] * 5, lines("You can't save the money.", 5)),
    (f"{E5}/006.py", [1000, 1500, 2000, 6500], lines("Goal reached! Good job!", "1000 steps over the goal!")),
    (f"{E5}/006.py", [1500, 300, 2500, 3000, "Going home", 200], "2500 more steps to reach goal."),

    (f"{S6}/001.py", [3, 2], lines("L30 L31", "O20 O21", "A10 A11")),
    (f"{S6}/002.py",
     ["Taxi", 10, "standard", "kid", "student", "student", "standard", "standard", "End",
      "Scary Movie", 6] + ["student"] * 6 + ["Finish"],
     lines("Taxi - 60.00% full.", "Scary Movie - 100.00% full.", "Total tickets: 12",
           "66.67% student tickets.", "25.00% standard tickets.", "8.33% kids tickets.")),
    (f"{S6}/003.py", [], lines(*(f"{h}:{m}" for h in range(24) for m in range(60)))),
    (f"{S6}/004.py", [2], "6"),
    (f"{S6}/005.py", [], lines(*(f"{x} * {y} = {x * y}" for x in range(1, 11) for y in range(1, 11)))),
    (f"{S6}/006.py", [1, 10, 5], "Combination N:4 (1 + 4 = 5)"),
    (f"{S6}/006.py", [23, 24, 20], "4 combinations - neither equals 20"),
    (f"{S6}/007.py", ["Greece", 1000, 200, 200, 300, 100, 150, 240, "End"], "Going to Greece!"),

    (f"{E6}/001.py", [10, 30], "11 22"),
    (f"{E6}/002.py", [7], lines("1", "2 3", "4 5 6", "7")),
    (f"{E6}/003.py", [2, 1], "11aa2"),
    (f"{E6}/004.py", [3], " ".join(n for n in map(str, range(1111, 10000)) if set(n) <= {"1", "3"})),
    (f"{E6}/005.py", [3, 9, 0, 7, 19, 4, "stop"],
     lines("Sum of all prime numbers is: 29", "Sum of all non prime numbers is: 13")),
    (f"{E6}/005.py", [-5, "stop"],
     lines("Number is negative.", "Sum of all prime numbers is: 0", "Sum of all non prime numbers is: 0")),
    (f"{E6}/006.py", [2, "While-Loop", 6.00, 5.50, "For-Loop", 5.84, 5.66, "Finish"],
     lines("While-Loop - 5.75.", "For-Loop - 5.75.", "Student's final assessment is 5.75.")),
]


def normalize(text):
    return "\n".join(line.rstrip() for line in text.strip().splitlines())


@pytest.mark.parametrize("script, stdin, expected", CASES, ids=[f"{c[0]}-{i}" for i, c in enumerate(CASES)])
def test_script(script, stdin, expected):
    result = subprocess.run(
        [sys.executable, str(ROOT / script)],
        input=lines(*stdin) + "\n",
        capture_output=True,
        text=True,
        timeout=10,
    )
    assert result.returncode == 0, result.stderr
    assert normalize(result.stdout) == expected


def test_every_script_has_a_case():
    tested = {c[0] for c in CASES}
    scripts = {p.relative_to(ROOT).as_posix() for p in ROOT.glob("0*/*.py")}
    assert scripts - tested == set()
