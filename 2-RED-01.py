alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

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

import sys
c_sub(sys.argv[1])