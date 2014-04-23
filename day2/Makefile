
program2: main.o function.o
	gcc -o program2 main.o function.o

main.o: main.c
	gcc -c main.c

function.o: function.asm
	nasm -felf32 function.asm


clean:
	rm -f program2 *.o
