# # 4_1
# def som(getal1,getal2,getal3):
#     return getal1 + getal2 + getal3
#
# print(som(1,3,4))

# # 4_2
# def som(getallenLijst):
#     return sum(getallenLijst)
# list = [1,2,3,4,5]
#
# print(som(list))

# # 4_3
# def lang_genoeg(lengte):
#     if lengte >= 120:
#         return("Je bent lang genoeg")
#     else: return("Je bent te klein")
#
# print(lang_genoeg(180))

# # 4_4
# def new_password(oldpassword,newpassword):
#     if len(newpassword) >= 6 and oldpassword != newpassword:
#         return "true"
#     else: return "false"
#
# ww = "lama"
# ww2 = "lama21"
# print(newPassword(ww2,ww))

# # 4_5
# def kwadraten_som(grondgetallen):
#     for char in grondgetallen:
#         if char >= 0:
#             print(char**2)
#
# lst = [4,5,3,-81]
# kwadraten_som(lst)

# # 4_6
# def wijzig(lijst):
#     lijst.clear()
#     lijst.append('d')
#     lijst.append('e')
#     lijst.append('f')
#     print(lijst)
# lijst = ['a', 'b', 'c']
# wijzig(lijst)