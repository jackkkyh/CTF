global _start

section .text
_start:
    push 0
    mov rax, 0
    mov rdi, 0
    mov rsi, rsp
    mov rdx, 1
    syscall

    mov rdi, [rsp]
    sub rdi, 48
    call REC
    mov rsi, rsp
    mov [rsp], rax

    mov rax, 1
    mov rdi, 1
    mov rsi, rsp
    mov rdx, 1
    syscall

    pop rax
    mov rax, 60
    mov rdi, 0
    syscall

REC:
    cmp rdi, 1
    jg GREATER
    mov rax, 1
    ret

GREATER:
    push rdi
    dec rdi
    call REC

    pop rdi
    mul rdi
    ret
