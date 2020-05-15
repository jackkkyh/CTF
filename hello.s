global _start

section .text
_start:
    mov rax, 0
    mov rdi, 0
    mov rsi, ARR
    mov rdx, 10
    syscall

    mov rcx, 0

LOOP:
    push rcx

    mov rax, 0x01
    mov rdi, 0x01
    mov rsi, ARR
    add rsi, rcx
    mov rdx, 1
    syscall

    mov rax, 0x01
    mov rdi, 0x01
    mov rsi, LINE
    mov rdx, 1
    syscall

    pop rcx
    inc rcx

    cmp rcx, 10
    jl LOOP
    
    mov rax, 60
    mov rdi, 0
    syscall

section .data
LINE: db 0x0a
ARR: times 10 db 0
