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

# print(max)

# -----------------------
# *build display tool to display all pair numbers from 1 to n
numbers = 20
for n in range(numbers):
    if n % 2 == 0 and n != 0:
        n
       # print(n)
# -----------------------
# *found logic to add all naturals numbers to var in using for and while
natural = 0
input_num = 30
for i in range(input_num+1):
    natural += i

# print(natural)
# ------------------------
# *use prompt and display multiplication table with for or while
print("Donnez un nombre : ")
user_choice = input()
print("User number choice : " + user_choice)
for number in range(10+1):
    print(number, "x", user_choice, "=", number*int(user_choice))
# -------------------------
# *
