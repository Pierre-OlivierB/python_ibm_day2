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
# *count middle point of students , 5 max value by student; nmb students is not defined
student = {}
name = ""
# master_choice = input(
#     "voulez-vous entrer des notes pour un étudiant (réponse attendu : y or n) ? ")
master_choice = 'n'
while master_choice == 'y':
    name = input("quel est son nom ? ")
    value_choice = 0
    values = []
    while value_choice < 5:
        value = input("quel est sa note à ajouter ? ")
        value_choice += 1
        if value_choice < 5:
            add_value_choice = input(
                "voulez-vous ajouter une autre note (y/n) ?")
        if add_value_choice == 'n':
            value_choice = 5
        values.append(int(value))
        student[name] = values
    master_choice = input(
        "voulez-vous entrer des notes pour un étudiant (réponse attendu : y or n) ? ")
# print(student)

for person in student:
    calc = 0
    moy = 0
    print(person, student[person])
    for note in student[person]:
        calc += note
    moy = calc/len(student[person])
    print("moyenne de :", person, " : ", moy)

# ---------------------------------------------------
# *calc imp el of matrice
matrice = [[1, 2, 3], [4, 5, 6, 10], [7, 8, 9]]


def add_imp(numtable):
    calc_matrice = 0
    for tabl in numtable:
        # print(tabl)
        for num in tabl:
            # print(num)
            if num % 2 == 1:
                calc_matrice += num
                print(num, calc_matrice)
    return calc_matrice


# matr = add_imp(matrice)
# print(matr)

# * display 1st/1st tab, 2sd/2sd tab... then last/1st tab, last-1/2sd tab...
first_diag = []
second_diag = []


def display_diag(numtable):
    index = 0
    for table in numtable:
        # print(table)
        # print(table[index])
        first_diag.append(table[index])
        if index < len(table)-1:
            index += 1
            # print(index)
    index = 0
    for table in numtable:
        # print(table)
        # print(table[index])
        second_diag.append(table[len(table)-1-index])
        index += 1


display_diag(matrice)
# print(first_diag, second_diag)

# *test if number display is equals between first_diag and second_diag


def verif_equals_diag(first, second):
    flag = False
    for index in range(len(first)):
        if first[index] == second[index]:
            print("oui ils sont égaux à l'index: ",
                  index, ";", first[index], "=", second[index])
            flag = True
    if flag == False:
        print("aucun élément est égal")


# verif_equals_diag(first_diag, second_diag)

# *moy of columns, svg in one array,display index of the better moy of the array equals to matrice column
matrice_two = [[9, 2, 3, 4], [4, 5, 6, 9], [7, 8, 9, 6],
               [7, 8, 9, 6], [9, 2, 3, 4], [9, 9, 6, 9], [4, 5, 6, 9]]
# svg_num_moy = [0, 0, 0, 0]
svg_moy = [0, 0, 0, 0]


def first_column(matrice_test, svg):
    range_matrice = len(matrice_test)
    for tabl in matrice_test:
        # print(tabl)
        for e in range(len(tabl)):
            # print(tabl[e])
            svg[e] += tabl[e]
    for index in range(len(svg)):
        svg[index] /= range_matrice


first_column(matrice_two, svg_moy)
# print(svg_moy)


def display_max_moy(table):
    max_value = table[0]
    index_max = 0
    for index in range(len(table)):
        if table[index] > max_value:
            max_value = table[index]
            index_max = index

    return index_max


# print(svg_num_moy)
# def moy_column(calc_matrice):
column_index = display_max_moy(svg_moy)
# print("la colonne qui a la plus grand valeur est la ", column_index+1)

# ----------------------------
# *fake BDD students : in student array add dict{num:,last-name:,first-name:} in it for each students
student = []
add_stud = input("Voulez-vous ajouter un étudiant (rép attendu: y/n) ?")
num = 0


def add_student(obj):
    last_name = input("Quel est son nom ?")
    first_name = input("Quel est son prénom ?")

    obj["num"] = num
    obj["last-name"] = last_name
    obj["first-name"] = first_name

    return obj


while add_stud == 'y':
    dict_student = {"num": "0", "last-name": "default",
                    "first-name": "default"}
    student.append(add_student(dict_student))
    num += 1

    add_stud = input("Voulez-vous ajouter un étudiant (rép attendu: y/n) ?")

print(student)

# * add search student with input letter


def display_names_choose(table, letter):
    for names in table:
        # for let in names["last-name"]:
        #     # print(let)
        #     print(names["last-name"][0])
        if names["last-name"][0] == letter:
            # print(names["last-name"])
            print(names)


choose_a_letter = input("Recherche du nom d'étudiant par lettre : ")
display_names_choose(student, choose_a_letter)
