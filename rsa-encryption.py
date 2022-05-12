import math
from sympy import nextprime, isprime
from random import randint

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

def get_d(p, q, e):
    return mod_inverse(e, (p-1)*(q-1))

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

def rsa_encode(text, m, e):
    num = convert_to_num(text)
    assert num<m, "You're trying to encode text that is too long!"
    return pow(num, e, m)

def rsa_decode(num, m, d, size):
    return convert_to_text(pow(num, d, m), size)

def make_prime(n):
    return nextprime(randint(2**(n-1), 2**n), 1)
