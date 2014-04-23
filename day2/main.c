#include <stdio.h>

int asmfunction(void);

int win(int a, int b)
{
    int c = 5;
    int d = 6;

    printf("You win %d %d\n", a, b);
    printf("You win %d %d\n", c, d);
    return 9;
}

int main(void)
{
    win(1,2);
	return 0;
}
