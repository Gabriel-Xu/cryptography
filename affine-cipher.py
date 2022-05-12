import math

alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def mod_inverse_helper(a, b):
    q, r = a//b, a%b
    if r == 1:
        return (1, -1 * q)
    u, v = mod_inverse_helper(b, r)
    return (v, -1 * q * v + u)

def mod_inverse(a, m):
    assert math.gcd(a, m) == 1, "You're trying to invert " + str(a) + " in mod " + str(m) + " and that doesn't work!"
    return mod_inverse_helper(m, a)[1] % m

def affine_encode(message, a, b):
    new=""
    for value in message:
        i = alpha.index(value)
        new+=alpha[(a*i+b)%26]
    return new

def affine_decode(message, a, b):
    new=""
    for value in message:
        i = alpha.index(value)
        new+=alpha[(mod_inverse(a, 26)*(i-b))%26]
    return new

def convert_to_num(ngraph):
    num=0
    for index, value in enumerate(ngraph):
        num+=alpha.index(value)*(26**index)
    return num

def convert_to_text_helper(num, n, c, ngraph):
    if c>0:
        ngraph+=alpha[(num%(26**(n-c+1)))//(26**(n-c))]
        return convert_to_text_helper(num-(num%(26**(n-c+1)))//(26**(n-c)), n, c-1, ngraph)
    else:
        return ngraph

def convert_to_text(num, n):
    return convert_to_text_helper(num, n, n, "")

def affine_n_encode(text, n, a, b):
    output=""
    for index in range(0, len(text), n):
        if index+n>len(text):
            x = text[index:index+n] + "X" * (index+n-len(text))
        else:
            x = text[index:index+n]
        y = (a*convert_to_num(x)+b)%(26**n)
        output+=convert_to_text(y, n)
    return output

def affine_n_decode(text, n, a, b):
    output=""
    for index in range(0, len(text), n):
        x = text[index:index+n]
        i=convert_to_num(x)
        y = (mod_inverse(a, 26**n)*(i-b))%(26**n)
        output+=convert_to_text(y, n)
    return output
