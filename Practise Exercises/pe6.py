# 6_1
nummer = int(input("vul een maandnummer in: "))
def seizoen(maand):
    if maand >= 3 and maand <= 5:
        return("Het is lente")
    elif maand >= 6 and maand <= 8:
        return("Het is zomer")
    elif maand >= 9 and maand <= 11:
        return("Het is herfst")
    elif maand == 12 or maand == 1 or maand == 2:
        return("Het is winter")
    else: return("Vul een geldig nummer in tussen de 1 en 12.")

print(seizoen(nummer))

# # 6_2
# def lists():
#     list = eval(input("Geef een lijst met minimaal 10 strings: ")) # vb ["boter", "kaas", "bier", "pizza", "thee", "drop", "koek", "cola", "boterham", "stampot"]
#     secondlist = []
#     for char in list:
#         if len(char) == 4:
#             secondlist.append(char)
#     print("De vier-letterwoorden zijn " + str(secondlist))
# lists()

# # 6_3
# def split():
#     invoer = "5-9-7-1-7-8-3-2-4-8-7-9"
#     split = invoer.split("-")
#     numbers = list(map(int, split))
#     numbers.sort()
#     print("Gesorteerde list van ints: " + str(numbers) +
#         "\nGrootste getal: " + str(max(numbers)) + " en Kleinste getal: " + str(min(numbers)) +
#         "\nAantal getallen: " + str(len(numbers)) + " en Som van de getallen: " + str(sum(numbers)) +
#         "\nGemiddelde: " + str(sum(numbers) / len(numbers)))
# split()

# # 6_4
# cijfers = [ [95, 92, 86],[66, 75, 54],[89, 72, 100],[34, 0, 0] ]
# def gem_students(cijfers):
#     list = []
#     for char in cijfers:
#          list.append(int(round(sum(char)/len(char))))
#     return(list)
#
# def gem_all_students(cijfers):
#     list = gem_students(cijfers)
#     return(int(sum(list) / len(list)))
#
# print("Het gemiddelde per student is " + str(gem_students(cijfers)) + ".")
# print("Het gemiddelde van alle studenten samen is " + str(gem_all_students(cijfers)) + ".")

# # 6_5
# def tables():
#     x = 1
#     y = 1
#     for y in range(1,11):
#         for x in range(1,11):
#             z = x * y
#             print(str(x) + " x " + str(y) + " = " + str(z))
# tables()