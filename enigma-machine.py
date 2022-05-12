alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
rotorI = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
rotorII = "AJDKSIRUXBLHWTMCQGZNPYFVOE"
rotorIII = "BDFHJLCPRTXVZNYEIWGAKMUSQO"
rotorIV = "ESOVPZJAYQUIRHXLNFTGKDCMWB"
rotorV = "VZBRGITYUPSDNHLXAWMJQOFECK"
reflectorB = "YRUHQSLDPXNGOKMIEBFZCWVJAT"
reflectorC = "FVPJIAOYEDRZXWGCTKUQSBNMHL"
notchI = "Q"
notchII = "E"
notchIII = "V"
notchIV = "J"
notchV = "Z"

def makeplugboard(string):
    text=""
    while text != "quit":
        text = input("Type a pair of letters to connect in the plugboard, for example 'AB' would connect A and B, or type 'quit': ")
        string=string.replace(text[0], "&")
        string=string.replace(text[1], text[0])
        string=string.replace("&", text[1])
    return string

def identifyrotor(number):
    if number=="1":
        return rotorI
    if number=="2":
        return rotorII
    if number=="3":
        return rotorIII
    if number=="4":
        return rotorIV
    if number=="5":
        return rotorV

def identifyreflector(letter):
    if letter=="B":
        return reflectorB
    if letter=="C":
        return reflectorC

def inputs():
    code = input("Type the code you want to encrypt using a Wehrmacht Enigma: ")
    plugboard = makeplugboard(alpha)
    rotorone = identifyrotor(input("Type rotor number to use for rightmost rotor, for example '1' would use rotor I: "))
    rotortwo = identifyrotor(input("Type rotor number to use for middle rotor, for example '1' would use rotor I: "))
    rotorthree = identifyrotor(input("Type rotor number to use for leftmost rotor, for example '1' would use rotor I: "))
    ringone = input("Type ring settings number to use for rightmost rotor: ")
    ringtwo = input("Type ring settings number to use for middle rotor: ")
    ringthree = input("Type ring settings number to use for leftmost rotor: ")
    initialwindowletters = list(input("Type initial window letters for rotors from left to right: "))
    reflector = identifyreflector(input("Type reflector letter to use, for example 'B' would use reflector B: "))
    return [code, plugboard, rotorone, rotortwo, rotorthree, ringone, ringtwo, ringthree, initialwindowletters, reflector]

def rotorfromright(code, rotor, offset):
    return alpha[(alpha.index(rotor[(alpha.index(code)+offset)%26])-offset)%26]

def rotorfromleft(code, rotor, offset):
    return alpha[(rotor.index(alpha[(alpha.index(code)+offset)%26])-offset)%26]

def plugboardandreflector(code, plugboardorreflector):
    return plugboardorreflector[alpha.index(code)]

def changewindowletters(array):
    if (array[8][1]=="Q" and array[3]==rotorI) or (array[8][1]=="E" and array[3]==rotorII) or (array[8][1]=="V" and array[3]==rotorIII) or (array[8][1]=="J" and array[3]==rotorIV) or (array[8][1]=="Z" and array[3]==rotorV):
        array[8][0]=alpha[(alpha.index(array[8][0])+1)%26] 
    if (array[8][1]=="Q" and array[3]==rotorI) or (array[8][1]=="E" and array[3]==rotorII) or (array[8][1]=="V" and array[3]==rotorIII) or (array[8][1]=="J" and array[3]==rotorIV) or (array[8][1]=="Z" and array[3]==rotorV):
        array[8][1]=alpha[(alpha.index(array[8][1])+1)%26] 
    elif (array[8][2]=="Q" and array[2]==rotorI) or (array[8][2]=="E" and array[2]==rotorII) or (array[8][2]=="V" and array[2]==rotorIII) or (array[8][2]=="J" and array[2]==rotorIV) or (array[8][2]=="Z" and array[2]==rotorV):
        array[8][1]=alpha[(alpha.index(array[8][1])+1)%26]
    array[8][2]=alpha[(alpha.index(array[8][2])+1)%26]
    return array

def engima(array):
    code=array[0]
    plugboard=array[1]
    rotorone=array[2]
    rotortwo=array[3]
    rotorthree=array[4]
    ringone=array[5]
    ringtwo=array[6]
    ringthree=array[7]
    letters=array[8]
    reflector=array[9]
    offsetone = (alpha.index(letters[2])+1-int(ringone))%26
    offsettwo = (alpha.index(letters[1])+1-int(ringtwo))%26
    offsetthree = (alpha.index(letters[0])+1-int(ringthree))%26
    return plugboardandreflector(rotorfromleft(rotorfromleft(rotorfromleft(plugboardandreflector(rotorfromright(rotorfromright(rotorfromright(plugboardandreflector(code, plugboard), rotorone, offsetone), rotortwo, offsettwo), rotorthree, offsetthree), reflector), rotorthree, offsetthree), rotortwo, offsettwo), rotorone, offsetone), plugboard)

def encode():
    arrayofinputs = inputs()
    newarrayofinputs=arrayofinputs
    code=arrayofinputs[0]
    for index in range(len(arrayofinputs[0])):
        newarrayofinputs[0]=code[index]
        print(engima(changewindowletters(newarrayofinputs)), end="")

encode()
