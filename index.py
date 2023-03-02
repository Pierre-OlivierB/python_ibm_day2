# ! Lvl 1
# ------------------
# *found max in using if /else for 3 numbers

a = 40
b = 20
c = 30

max = 0

if a > b and a > c:
    max = a
elif b > a and b > c:
    max = b
else:
    max = c

print(max)

# -----------------------
# *build display tool to display all pair numbers from 1 to n
numbers = 20
for n in range(numbers):
    if n % 2 == 0 and n != 0:
        print(n)
# -----------------------
# *
