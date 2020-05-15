
from pwn import *
p = remote("ctf.firebird.gson.stream", 31334)

inp = p.recvline()
#.decode("utf-8")

print("this is inp:", inp)

stri = ""
for i in inp:
    stri += chr(i)
print("string: ", stri)

for key in range(256):
    print("key: ", key)
    s = ""
    for i in inp:
        s += chr((i+key)%256)
    print("this is s: ", s)
