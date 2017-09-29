# # 5_1
# def convert(celsius):
#     fahrenheit = celsius * 1.8 + 32
#     return fahrenheit
# celsius = int(input("Hoeveel graden celcius? "))
# print(convert(celsius))
#
# def table():
#     print('{:8} {:1}' .format(' C','F'))
#     for char in range(-30,50,10):
#         print('{:3} {:8}' .format(char, convert(char)))
# table()

# # 5_2
# def readfile():
#     infile = open('kaartnummers.txt', 'r')
#    file = infile.readlines()
#     lijst = []
#     for line in file:
#         nummer = line.split(', ')
#         naam = nummer[1].split('\n')
#         nummer = nummer[0]
#         naam = naam[0]
#         print(naam + ' heeft kaartnummer: ' + nummer)
# readfile()

# # 5_3
# def read():
#     infile = open('kaartnummers.txt', 'r')
#     file = infile.readlines()
#     print("Deze file telt " + str(len(file)) + " regels")
#     lijst = []
#     for line in file:
#         nummer = line.split(', ')
#         nummer = nummer[0]
#         lijst.append(nummer)
#     print("Het grootste kaartnummer is: " + max(lijst) + " en dat staat op regel " + str(lijst.index(max(lijst))+1))
# read()

# # 5_4
# import datetime
# def add():
#     outfile = open('hardlopers.txt', 'a')
#     add = input("voer de naam in van de nieuwe hardloper: ")
#     today = datetime.datetime.today()
#     date = today.strftime("%a %d %b %Y, %H:%M:%S")
#     return outfile.write(date + ", " + add + "\n")
# print(add())

# 5_5
# def gemiddelde():
#     string = input("Typ hier de zin: ")
#     list = string.split()
#     length = 0
#     for char in list:
#         length += len(char)
#     average = round(length/len(list),2)
#     print("De zin heeft " + str(len(list)) + " woorden en een totaal van " + str(length) + " characters. \nHet gemiddelde characters per woord is " +
#           str(average))
# gemiddelde()
