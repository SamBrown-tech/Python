def inlezen_beginstation(stations):
    print(stations)
    while True:
        user_beginstation = input("Wat is je beginstation? ")
        if user_beginstation not in stations:
            print('Keuze is niet op dit traject! Kies opnieuw')
            continue
        break
    return user_beginstation

def inlezen_eindstation(stations, beginstation):
    while True:
        user_eindstation = input("Waar gaat u uw reis eindigen? ")
        if user_eindstation not in stations or stations.index(beginstation) >= stations.index(user_eindstation):
            print('Keuze is niet op het traject of komt eerder dan het beginstation. Kies opnieuw.')
            continue
        break
    return user_eindstation

def omroepen_reis(stations, beginstation, eindstation):
    start_i = stations.index(beginstation)
    eind_i = stations.index(eindstation)
    afstand = eind_i - start_i
    prijs = 5
    totaal = afstand * prijs
    print()
    print(beginstation, 'is het startpunt, dit is stationnummer:', start_i + 1)
    print(eindstation, 'is het startpunt, dit is stationnummer:', eind_i + 1)
    print('De afstand bedraagt', afstand,'station(s).')
    print('De prijs van het kaartje is', totaal, 'euro.')
    print()
    print('Jij stapt in de trein in:', beginstation)
    for item in stations:
        if stations.index(item) > start_i and stations.index(item) < eind_i:
            print('\t- ', item)
    print("Jij stapt uit in:", eindstation)


# Jouw functies komen hier!!
stations = ['Schagen', 'Heerhugowaard', 'Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Sloterdijk', 'Amsterdam Centraal', 'Amsterdam Amstel', 'Utrecht Centraal', '’s-Hertogenbosch', 'Eindhoven', 'Weert', 'Roermond', 'Sittard', 'Maastricht']
beginstation = inlezen_beginstation(stations)
eindstation = inlezen_eindstation(stations, beginstation)
omroepen_reis(stations, beginstation, eindstation)
