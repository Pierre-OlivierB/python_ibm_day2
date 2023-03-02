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
# *python choose a number, you have 10 chances to find it with input
python_number = int(random()*100)+1
# print(python_number)
user_try = 0
# game = input('voulez vous jouer, rep attendu : y or n ? ')
game = n
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
# --------------------------------------
# *create array then catch input user to add it in array and return the two biggers values
table = []
# user_table_choice = input("Combien voulez vous entrez de valeurs ?")
# iteration = int(user_table_choice)
iteration = 0

while iteration > 0:
    user_num_choice = input("Entrez une valeur : ")
    table.append(int(user_num_choice))
    print(table)
    iteration -= 1
    # print(iteration)

table_max = []

for i in range(len(table)-1):
    if table[i] < table[i+1]:
        table[i], table[i+1] = table[i+1], table[i]
    for j in range(len(table)-1):
        if table[(len(table)-1-j)] > table[(len(table)-2-j)]:
            table[(len(table)-1-j)], table[(len(table)-2-j)
                                           ] = table[(len(table)-2-j)], table[(len(table)-1-j)]

# print("le plus grand ", table[0])
# print("le deuxième plus grand ", table[1])
# ----------------------------------------------
# *add array, then catch user input and count el num pair and imp in it
pair = 0
imp = 0
for el in table:
    if el % 2 == 0:
        pair += 1
    if el % 2 == 1:
        imp += 1
# print("nombre de pair : ", pair, "; nombre d'impair : ", imp)
# ------------------------------------------------
# *create a for in array and display each value/5. stop when value > 150
list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
list1_len = len(list1)
# print(list1_len)
index = 0
while list1_len > 0:
    # print(list1[index])
    if list1[index] > 150:
        # print("fin")
        list1_len = 0
    elif list1[index] % 5 == 0:
        # print(list1[index])
        trash = 0
    index += 1
    list1_len -= 1
# ---------------------------------------------
# *count el in number
test_num = 56894984578
test_str = str(test_num)
# print(len(test_str))
# -----------------------------
#  *display a list but in each iter the first is shift

# for i in range(len(list1)):
#     # print(item)
#     # print(list1)
#     list1.pop(0)

# --------------------------------
# *revers a list with for
list1_len = len(list1)
# print(list1_len/2)
for i in range(int(list1_len/2)):
    list1[i], list1[len(list1)-1-i] = list1[len(list1)-1-i], list1[i]
# print(list1)
# -------------------------
# *display "ok" when for is finished
for i in range(int(list1_len/2)):
    list1[i], list1[len(list1)-1-i] = list1[len(list1)-1-i], list1[i]
    if i == int(list1_len/2)-1:
        teset = 0
        # print("ok")
# print(list1)
# -----------------------------------
# !PARTIE 2
# ---------------------------------
# *palindrom verification
word = "rotor"
flag_word = 0
for letter in range(int(len(word)/2)):
    if word[letter] != word[len(word)-1-letter]:
        flag_word = 1
# if flag_word > 0:
#     print("le mot ", word, " n'est pas un palindrome")
# elif flag_word == 0:
#     print("le mot ", word, " est un palindrome")


# ---------------------------------
# *simulation of 5 drop of dices and addition of result
points = 0
# print(dice)
for i in range(6):
    dice = randint(0, 5)
    # print(dice+1)
    result = dice+1
    points += result
    # print("pts : ", points)
    # print("dice : ", result)

# print(points)
# --------------------------------------
# *
