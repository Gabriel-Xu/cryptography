alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

eng_freq = [.0817, .0149, .0278, .0425, .1270, .0223, .0202, .0609, .0697, .0015, .0077, .0403, .0241, .0675, .0751,
            .0193, .0010, .0599, .0633, .0906, .0276, .0098, .0236, .0015, .0197, .0007]

eng_freq_squared = []
for freq in eng_freq:
    eng_freq_squared.append(freq * freq)
engIoC = sum(eng_freq_squared)

def vigenere_encode_helper(message, key, encoded):
    for index, value in enumerate(message):
        encoded+=alpha[(alpha.index(value)+alpha.index(key[index%len(key)]))%26]
    return encoded

def vigenere_encode(message, key):
    return vigenere_encode_helper(message, key, "")

def vigenere_decode_helper(message, key, decoded):
    for index, value in enumerate(message):
        decoded+=alpha[(alpha.index(value)-alpha.index(key[index%len(key)]))%26]
    return decoded

def vigenere_decode(message, key):
    return vigenere_decode_helper(message, key, "")

def i_of_c(text):
    ioc = 0
    for value in alpha:
        ioc+=text.count(value)*(text.count(value)-1)/(len(text)*(len(text)-1))
    return ioc

def friedman_test(text):
    return (len(text)*(engIoC-1/26))/(i_of_c(text)*(len(text)-1)+engIoC-len(text)*1/26)

def gcd(x, y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)

def gcd_of_list_helper(int_list, index):
    if index == len(int_list)-1:
        return int_list[index]
    else:
        return gcd(int_list[index], gcd_of_list_helper(int_list, index+1))

def gcd_of_list(int_list):
    return gcd_of_list_helper(int_list, 0)

def find_plausible_gcd(int_list, minimum):
    new_list=[]
    for value in int_list:
        if int_list.count(value)>=minimum and new_list.count(value)==0:
            new_list.append(value)
    if gcd_of_list(new_list)>1:
        return gcd_of_list(new_list)
    else:
        return find_plausible_gcd(int_list, minimum+1)

def kasiski_test(text):
    trigraphs=[]
    lengths=[]
    for index in range(len(text)-3):
        trigraphs.append(text[index:index+3])
        if text[index:index+3] in trigraphs:
            lengths.append(index-text.index(text[index:index+3]))
    return find_plausible_gcd(lengths, 0)

def make_cosets(text, n):
    coset_list=[]
    for num in range(n):
        coset_list.append(text[num:len(text):n])
    return coset_list

def find_total_difference(l1, l2):
    new_list=[]
    for index in range(len(l1)):
        new_list.append(abs(l1[index]-l2[index]))
    return sum(new_list)

def find_likely_letter(coset):
    frequency_list=[]
    for value in alpha:
        frequency_list.append(coset.count(value)/len(coset))
    difference_list=[]
    differences = frequency_list
    for index in range(len(alpha)):
        difference_list.append(find_total_difference(eng_freq, differences))        
        differences.append(frequency_list[0])
        del(differences[0])
    return alpha[difference_list.index(min(difference_list))]

def crack(ciphertext):
    print("The Friedman test gives", friedman_test(ciphertext))
    print("The Kasiski test gives", kasiski_test(ciphertext))
    keywordlength=int(input("Choose the key length you'd like to try: "))
    coset_list = make_cosets(ciphertext, keywordlength)
    for index, value in enumerate(coset_list):
        print("For coset", index+1, end="")
        print(", the most likely letter is", find_likely_letter(value))
    keyword=input("Type the key you would like to use to decipher: ")
    print(vigenere_decode(ciphertext, keyword))