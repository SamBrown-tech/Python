# 7_1
invoer = int(input("Geef een getal: "))
som = 0
aantal = 0
while invoer != 0:
    aantal += 1
    som += invoer
    invoer = int(input("Geef een getal: "))
print(som)
print("aantal getallen is " + str(aantal))

# # 7_2
# invoer = input("Geef een woord met 4 letters: ")
# while len(invoer) != 4:
#     print(invoer + " heeft " + str(len(invoer)) + " letters.")
#     invoer = input("Geef een woord met 4 letters: ")
# print("Correct! Het woord '" + invoer + "' heeft 4 letters.")


# # 7_3
# dict = {'joost':8, 'karel':9, 'santino':10, 'lucas': 10, 'tim':6, 'tom': 7, 'chris': 9, 'jaap':7}
# for value in dict:
#     if dict[value] >= 9:
#         print(value + " " + str(dict[value]))

# # 7_4
# def ticker():
#     infile = open('ticker.txt', 'r+')
#     readlines = infile.readlines()
#     lijst = []
#     lijst2 = []
#     for char in readlines:
#         splitsen = char.split(':')
#         namen = splitsen[0]
#         afkortingen = splitsen[1]
#         lijst.append(namen.strip())
#         # strip haalt \n weg of wat er tussen () staat.
#         lijst2.append(afkortingen.strip())
#     print(lijst)
#     print(lijst2)
#     invoer = input("voer iets in: ")
#     if invoer in lijst:
#         waarde = lijst.index(invoer)
#         print(lijst2[waarde])
#     elif invoer in lijst2:
#         waarde = lijst2.index(invoer)
#         print(lijst[waarde])
#     else: print('Voer een geldige naam of afkorting in')
# ticker()
