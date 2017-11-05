# 2_2
cijferICOR = 5;
cijferPROG = 4;
cijferCSN = 7;
gemiddelde = (cijferICOR + cijferPROG + cijferCSN) / 3;
beloning = (cijferICOR + cijferPROG + cijferCSN) * 30;
overzicht = "Mijn cijfers (gemiddeld een " + str(round(gemiddelde,1)) + ") leveren een beloning op van €" + str(
    beloning) + " op!"

print("gemiddelde cijfer is:" + str(round(gemiddelde,1)) + " beloning is €" + str(beloning) + ". \n")
print(overzicht)

# # 2_3
# 0 == (1 == 2)
# 2 + (3 == 4) + 5 == 7
# (1 < -1) == (3 > 4)

# # 2_4
# salary = input('Wat verdien je per uur? ')
# hours = input('Hoeveel uur heb je gewerkt? ')
# totalsalary = int(salary) * int(hours)
#
# print(str(hours) + ' uur werken levert ' + str(totalsalary) + ' Euro op')
