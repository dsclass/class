[bits 32]

global main

extern scanf
extern printf
extern exit

dowin:
    push winning
    call printf
    add esp, 4
    push 0
    call exit
    ret

stackcheckfail:
    push exploitfail
    call printf
    push -1
    call exit
    ret

message:
    push ebp
    mov ebp, esp
    sub esp, 0x18
    mov dword [ebp-4], 0xc0ccface
    mov dword [ebp-8], 42

    push prompt
    call printf
    add esp, 4

    lea eax, [ebp-0x18]
    push eax
    push inputfmt
    call scanf
    add esp, 8

    push dword [ebp-8]
    lea eax, [ebp-0x18]
    push eax
    push namefmt
    call printf
    add esp, 8

    cmp dword [ebp-4], 0xc0ccface
    je cookieok
    call stackcheckfail

cookieok:
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

winning:
    db "You Win!",0xa,0

prompt:
    db "Please enter your name: ",0

namefmt:
    db "Hello %s : Your number is 0x%x",0xa,0

inputfmt:
    db "%s",0

exploitfail:
    db "EXPLOIT ATTEMPT! FAIL!",0xa,0x0

