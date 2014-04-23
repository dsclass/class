#include <stdio.h>

int asmfunction(void);

int win(int a, int b)
{
    int a = 5;
    int b = 6;

    printf("You win %d %d\n", a, b);
    return 9;
}

int main(void)
{
    win(1,2);
	return 0;
}
