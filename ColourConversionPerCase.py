coloursFile = open("coloursPerCase.txt", "w")

def converter():
    global typeName
    typeName = input("What's the name of this value? ")
    try:
        r1 = float(input("What is the R value? "))
    except ValueError:
        print("That's not a number! Please try again.")
        r1 = float(input("What is the R value? "))
    if (r1 > 1):
        coloursFile.close()
        exit()
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
        r2 = int(round((r1 * 255), 0))
        g2 = int(round((g1 * 255), 0))
        b2 = int(round((b1 * 255), 0))
        h1 = hex(r2)[2:]
        h2 = hex(g2)[2:]
        h3 = hex(b2)[2:]
        rgbFinal = ("rgb(" + str(r2) + ", " + str(g2) + ", " + str(b2) + ");")
        hexFinal = ("#" + str(h1) + str(h2) + str(h3))
        print(rgbFinal + " " + hexFinal)
        coloursFile.write(typeName + ": " + rgbFinal + " HEX: " + hexFinal + "\n")




i = 1
while (i != 2):
    converter()

