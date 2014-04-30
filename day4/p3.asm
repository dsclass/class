[bits 32]

global main

extern scanf
extern printf
extern exit

message:
    push ebp
    mov ebp, esp
    sub esp, 0x14
    mov dword [ebp-4], 42

    push prompt
    call printf
    add esp, 4

    lea eax, [ebp-0x14]
    push eax
    push inputfmt
    call scanf
    add esp, 8

    push dword [ebp-4]
    lea eax, [ebp-0x14]
    push eax
    push namefmt
    call printf
    add esp, 8

    mov esp, ebp
    pop ebp
    ret


main:
    push ebp
    mov ebp, esp

    call message

    mov esp, ebp
    pop ebp
    ret

prompt:
    db "Please enter your name: ",0

namefmt:
    db "Hello %s : Your number is 0x%x",0xa,0

inputfmt:
    db "%s",0
