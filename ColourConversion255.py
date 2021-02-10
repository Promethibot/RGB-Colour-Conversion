coloursFile = open("coloursPerCase255.txt", "w")

def converter():
    global typeName
    typeName = input("What's the name of this value? ")
    try:
        r1 = float(input("What is the R value? "))
    except ValueError:
        print("That's not a number! Please try again.")
        r1 = float(input("What is the R value? "))
    if (r1 > 255):
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

