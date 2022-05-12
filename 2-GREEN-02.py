alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def caesar_encode_helper(text, shift, newtext):
    for index in range(len(text)):
        newtext+=alpha[(alpha.index(text[index])+shift)%26]
    return newtext

def caesar_encode(text, shift):
    return caesar_encode_helper(text, shift, "")

def caesar_decode_helper(text, shift, newtext):
    for index in range(len(text)):
        newtext+=alpha[(alpha.index(text[index])-shift)%26]
    return newtext

def caesar_decode(text, shift):
    return caesar_decode_helper(text, shift, "")

def caesar_crack(text):
    for index in range(26):
        print(caesar_decode(text, index))

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