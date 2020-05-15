#from secret import flag
from math import gcd
from random import randint
from string import ascii_letters, digits, punctuation

CHARSET = ascii_letters + digits + punctuation
n = len(CHARSET)

def affine(m, a, b):
    c_numbered = ((a * x + b) % n for x in m_numbered)
    c_out = [i for i in c_numbered]
    print("\t", c_out);
    print(CHARSET.find('@'))
    print(CHARSET.find('['))
    return "".join(CHARSET[k] for k in c_numbered)

str="@[@[xQB@xj'jd{JR;K@O#c~1$&$y$L!{#D$Rx#XlLkd?R;]]"



a = 67
b = 84
m_numbered = (CHARSET.find(i) for i in 'haha')
m_out = [i for i in m_numbered]
print("\t", m_out);
print(CHARSET.find('@'))
print(CHARSET.find('['))
print(n)

def modinv2(k):
    x = 0
    while((a*x+b-k)%n != 0):
        x = x+1
    return x

print(modinv2(83))
print("".join(CHARSET[modinv2(k)] for k in [(CHARSET.find(k)) for k in str]))
