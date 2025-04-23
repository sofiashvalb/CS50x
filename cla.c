#include <cs50.h>
#include <stdio.h>

//gives an array that shows evetything typed in the terminal
int main(int argc, string argv[])
{
    // so let me loop through every argument I'm given and print out as a string whatever is inside that location.
    for (int i = 0; i < argc; i++)
    {
        printf("argv is [%i]: and argc is %s\n", i, argv[i]);
    }
}