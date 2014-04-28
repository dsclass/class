OPTIONS := -fno-stack-protector -z execstack -ggdb

all: program1 program2 program3

program1: p1.o
	gcc $(OPTIONS) -o program1 p1.o

p1.o: p1.asm
	nasm -felf32 p1.asm

program2: p2.o
	gcc $(OPTIONS) -o program2 p2.o

p2.o: p2.asm
	nasm -felf32 p2.asm

program3: p3.o
	gcc $(OPTIONS) -o program3 p3.o

p3.o: p3.asm
	nasm -felf32 p3.asm

clean:
	rm -f program* *.o
