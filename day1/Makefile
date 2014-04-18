
program1: main.o function.o
	gcc -o program1 main.o function.o

main.o: main.c
	gcc -c main.c

function.o: function.asm
	nasm -felf32 function.asm


clean:
	rm -f program1 *.o
