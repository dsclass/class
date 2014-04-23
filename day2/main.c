#include <stdio.h>

int asmfunction(void);

void win(int a, int b)
{
    printf("You win %d %d\n", a, b);
}

int main(void)
{
	int num;

	num = asmfunction();
	printf("Your function returned %d\n", num);
	return 0;
}
