#include <stdio.h>

int asmfunction(void);

int main(void)
{
	int num;

	num = asmfunction();
	printf("Your function returned %d\n", num);
	return 0;
}
