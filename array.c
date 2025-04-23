#include <cs50.h>
#include <stdio.h>

int main(void)
{
    //get the legth of the array and check if it's bigger than 1
    int length;
    do
    {
        length = get_int("Length: ");
    }
    while (length < 1);
    //declare the array and set the first value
    int twice[length];
    twice[0] = 1;
    printf("%i\n", twice[0]);
    // for every array space, add i++ and print the twice[space on array] by addind *2
    for (int i = 1; i < length; i++)
    {
        // make the current element twice the previous
        twice[i] = 2 * twice[i - 1];
        printf("%i\n", twice[i]);
    }
    //so the code needs to print twice[0] by itself because it starts *2 from secont palce (twice[1])
}