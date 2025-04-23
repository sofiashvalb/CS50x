#include <cs50.h>
#include <stdio.h>

int main(void)
{
    string name = get_string("What's your name? ");
    int age = get_int ("And your age? ");
    string phone = get_string ("Your phone number? ");
    printf ("Age is %i. Name is %s. Phone is %s.\n", age, name, phone);

}