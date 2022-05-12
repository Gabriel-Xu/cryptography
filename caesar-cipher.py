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
