# 4_1
# def som(getal1,getal2,getal3):
#     return getal1 + getal2 + getal3
#
# print(som(1,3,4))

# 4_2
# def som(getallenLijst):
#     return sum(getallenLijst)
# list = [1,2,3,4,5]
#
# print(som(list))

# 4_3
# def lang_genoeg(lengte):
#     if lengte >= 120:
#         return("Je bent lang genoeg")
#     else: return("Je bent te klein")
#
# print(lang_genoeg(180))

# 4_4
# def new_password(oldpassword,newpassword):
#     if len(newpassword) >= 6 and oldpassword != newpassword:
#         return "true"
#     else: return "false"
#
# ww = "lama"
# ww2 = "lama21"
# print(newPassword(ww2,ww))

# 4_5
# def kwadratenSom(grondgetallen):
#     for char in grondgetallen:
#         if char >= 0:
#             return(char)
# lst = [-1,3,4,5]
# print(kwadratenSom(lst))

def kwadraten_som






# # 4 Final Assignment NS
# def standaardprijs(afstandKM):
#     if afstandKM > 50:
#         return 15 + (1.40 * afstandKM)
#     elif afstandKM <= 0:
#         return 0
#     else:
#         return 0.80 * afstandKM
#
# afstandKM = 60
# print("€" + "%.2f" % standaardprijs(afstandKM))
#
# def ritprijs(leeftijd, weekendrit, afstandKM):
#     # kinderen en ouderen korting
#     if leeftijd  < 12 or leeftijd >= 65:
#         # wel of geen weekend
#         if weekendrit == "wel":
#             return standaardprijs(afstandKM) * 0.65
#         else: return standaardprijs(afstandKM) * 0.7
#     # reizigers zonder korting
#     else:
#         #wel of geen weekend
#         if weekendrit == "wel":
#             return standaardprijs(afstandKM) * 0.6
#         else: return standaardprijs(afstandKM)
#
#     # user input
# afstandKM = int(input('Hoeveel kilometer? '))
# leeftijd = int(input('Hoe oud bent u? '))
# weekendrit = input('Reist u wel of niet in het weekend? ')
#
# # print("Uw ritprijs is €" + "0.2f" % str(ritprijs(leeftijd,weekendrit,afstandKM)))
# print("Uw ritprijs is €" + str(ritprijs(leeftijd,weekendrit,afstandKM)))