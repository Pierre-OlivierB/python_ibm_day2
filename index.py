from random import *

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
# print("Donnez un nombre : ")
# user_choice = input()
# print("User number choice : " + user_choice)
# for number in range(10+1):
#     print(number, "x", user_choice, "=", number*int(user_choice))
# -------------------------
# *python choose un number, you have 10 chances to find it with input
python_number = int(random()*100)+1
# print(python_number)
user_try = 0
game = input('voulez vous jouer, rep attendu : y or n ? ')
if game == 'y':
    print("Python a choisit un nombre, essayez de le trouver!")
    user_try = 10
    while user_try > 0:
        print("Nombre de tentative restante : ", user_try)
        user_choice = input("Donnez un chiffre entre 1 et 100 : ")
        print("votre choix est le : ", user_choice)
        user_try -= 1
        if int(user_choice) == python_number:
            user_try = 0
            print("vous avez gagné, le nombre a trouver est bien le : ", python_number)
        elif int(user_choice) > python_number:
            print("c'est moins")
        elif int(user_choice) < python_number:
            print("c'est plus")

    # print(user_try)
