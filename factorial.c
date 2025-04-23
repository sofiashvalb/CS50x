#include <cs50.h>
#include <stdio.h>

int factorial(int n);

int main(void)
{
    int number = get_int("Enter a number: ");
    printf("%i\n", factorial(number));
}

int factorial(int n)
{

    if (n == 1)
    {
        return 1;
    }

    return n * factorial(n - 1);
}