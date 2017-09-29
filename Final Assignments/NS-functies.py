# 4 Final Assignment NS-functies
def standaardprijs(afstandKM):
    if afstandKM > 50:
        return 15 + (1.40 * afstandKM)
    elif afstandKM <= 0:
        return 0
    else:
        return 0.80 * afstandKM

afstandKM = 60
print("€" + "%.2f" % standaardprijs(afstandKM))

def ritprijs(leeftijd, weekendrit, afstandKM):
    # kinderen en ouderen korting
    if leeftijd  < 12 or leeftijd >= 65:
        # wel of geen weekend
        if weekendrit == "wel":
            return standaardprijs(afstandKM) * 0.65
        else: return standaardprijs(afstandKM) * 0.7
    # reizigers zonder korting
    else:
        # wel of geen weekend
        if weekendrit == "wel":
            return standaardprijs(afstandKM) * 0.6
        else: return standaardprijs(afstandKM)

# user input
afstandKM = int(input('Hoeveel kilometer? '))
leeftijd = int(input('Hoe oud bent u? '))
weekendrit = input('Reist u wel of niet in het weekend? ')

print("Uw ritprijs is €" + str(ritprijs(leeftijd,weekendrit,afstandKM)))