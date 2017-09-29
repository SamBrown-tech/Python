def aantal_vrije_kluizen():
    infile = open('kluizen.txt', 'r')
    gebruikte_kluizen = len(infile.readlines())
    open_kluizen = 12 - gebruikte_kluizen
    print("Er zijn nog " + str(open_kluizen) + " kluizen beschikbaar.")


def nieuwe_kluis():
    kluizenlijst = [1, 2, 3 , 4, 5, 6, 7, 8, 9, 10, 11, 12]
    gebruiktlijst = []
    infile = open('kluizen.txt', 'r')
    text = infile.readlines()

    # leest per regel eerste character in file
    for line in text:
        kluizenlijst.remove(int(line[0]))
    infile.close()
    # checkt of er kluizen beschikbaar zijn
    if len(kluizenlijst) >= 1:
        code = input("voer uw kluiscode in: ")

        if len(code) >= 4:
            # wijst kluis toe en schrijft weg in kluizen.txt
            print("Uw kluisnummer is " + str(kluizenlijst[0]) + ".")
            outfile = open('kluizen.txt', 'a')
            outfile.write(str(kluizenlijst[0]) + ";" + code + "\n")
        else: print("De code moet minimaal 4 characters bevatten!")
    else: print("Helaas, er zijn geen kluizen meer beschikbaar")
    outfile.close()


def kluis_openen():
    # input
    nummer = int(input("Wat is uw kluisnummer? "))
    code = input("Wat is uw code? ")
    infile = open('kluizen.txt', 'r')
    text = infile.readlines()
    nummers = []
    codes = []
    for line in text:
        # de -1 is voor de /n
        nummers.append(int(line[0]))
        codes.append(line[2:-1])
    # check of de combinatie klopt
    if nummer in nummers:
        check = (nummers.index(nummer))
        if code == codes[check]:
            print("Combinatie is correct.")
        else:
            print("Het kluisnummer en wachtwoord komen niet met elkaar overeen.")
    else: print("Het kluisnummer is niet in gebruik.")


def kluis_teruggeven():
    print('nog doen')


print("1: Ik wil weten hoeveel kluizen er nog vrij zijn \n"
"2: Ik wil een nieuwe kluis \n"
"3: Ik wil even iets uit mijn kluis halen \n"
"4: Ik geef mijn kluis terug \n")

option = input('Voer uw keuze in: ')
if option == "1":
    aantal_vrije_kluizen()
elif option == "2":
    nieuwe_kluis()
elif option == "3":
    kluis_openen()
elif option == "4":
    kluis_teruggeven()
elif option == "5":
    print("nog doen")
else: print("Voer aub een getal van 1 t/m 5 in")