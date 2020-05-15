import random
f = open("message").read()
s = ""
key = random.randint(1,255)
for i in f:
    s += chr((ord(i)+key)%256)
print s
