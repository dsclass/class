[bits 32]

global main

extern read
extern printf
extern strncpy
extern strlen

message:
    push ebp
    mov ebp, esp
    sub esp, 0x200

    push 0x200
    lea eax, [ebp-0x200]
    push eax
    push 0
    call read
    add esp, 12

    lea edx, [ebp-0x200]
    add edx, eax
    mov byte [edx], 0


    lea eax, [ebp-0x200]
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

namefmt:
    db "Hello %s",0xa,0

