alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def substitution_encode_helper(text, code_alpha, newtext):
    for index in range(len(text)):
        newtext+=code_alpha[alpha.index(text[index])]
    return newtext

def substitution_encode(text, code_alpha):
    return substitution_encode_helper(text, code_alpha, "")

def substitution_decode_helper(text, code_alpha, newtext):
    for index in range(len(text)):
        newtext+=alpha[code_alpha.index(text[index])]
    return newtext

def substitution_decode(text, code_alpha):
    return substitution_decode_helper(text, code_alpha, "")

def c_sub(string):
    text=""
    while text != "quit":
        print(string)
        for value in alpha:
            print(value, "occurs", string.count(value), "time(s)")
        print("The most common letters in English are usually ETAOINSHRDLU, in that order")
        text = input("Type a pair of letters to swap, for example AB would swap A and B, or type 'quit': ")
        string=string.replace(text[0], "&")
        string=string.replace(text[1], text[0])
        string=string.replace("&", text[1])
