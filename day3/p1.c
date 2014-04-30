

int message()
{
        int a = 0x14;
        char name[0x10];

        printf("Please enter your name: ");
        scanf("%s", name);
        printf("Hello %s : Your number is 0x%x\n", name, a);

        if (a == 0x41)
            printf("You Win!\n");
}

int main()
{
    message();
}

