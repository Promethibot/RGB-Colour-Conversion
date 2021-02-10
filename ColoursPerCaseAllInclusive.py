coloursFile = open("coloursPerCaseAll.txt", "w")

def converter():
    global typeName
    typeName = input("What's the name of this value? ")
    try:
        typeColour = int(input("What type of colour code is this? 0 for 0 - 1 values, 1 for RGB. Any number greater will save and exit the program. "))
    except ValueError:
        print("That's not a valid answer! Please try again.")
        typeColour = int(input("What type of colour code is this? 0 for 0 - 1 values, 1 for RGB. Any number greater will save and exit the program. "))
    if (typeColour > 1):
        coloursFile.close()
        exit()
    try:
        r1 = float(input("What is the R value? "))
    except ValueError:
        print("That's not a number! Please try again.")
        r1 = float(input("What is the R value? "))
    else:
        try:
            g1 = float(input("What is the G value? "))
        except ValueError:
            print("That's not a number! Please try again.")
            g1 = float(input("What is the G value? "))
        try:
                b1 = float(input("What is the B value? "))
        except ValueError:
                print("That's not a number! Please try again.")
                b1 = float(input("What is the B value? "))
        if typeColour == 0:
            r1 = int(round((r1 * 255), 0))
            g1 = int(round((g1 * 255), 0))
            b1 = int(round((b1 * 255), 0))
        else:
            r1 = int(r1)
            g1 = int(g1)
            b1 = int(b1)
        h1 = hex(r1)[2:].zfill(2)
        h2 = hex(g1)[2:].zfill(2)
        h3 = hex(b1)[2:].zfill(2)
        rgbFinal = ("rgb(" + str(r1) + ", " + str(g1) + ", " + str(b1) + ");")
        hexFinal = ("#" + str(h1) + str(h2) + str(h3))
        print(rgbFinal + " " + hexFinal)
        coloursFile.write(typeName + ": " + rgbFinal + " HEX: " + hexFinal + "\n")




i = 1
while (i != 2):
    converter()

