#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int a = 28;
    int b = 50;
    int *c = &a;

    *c = 14;
    c = &b;
    *c = 25;

    printf("%i, %p\n", a, &a);
    printf("%i, %p\n", b, &b);
    printf("%p, %p\n", c, &c);
}