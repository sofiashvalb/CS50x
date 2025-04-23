// Write a function to replace vowels with numbers
// Get practice with strings
// Get practice with command line
// Get practice with switch

#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

string replace(string input);
int main(int argc, string argv[])
{
    if (argc != 2)
    {
        printf("ERROR! \n");
        return 1;
    }
    printf("%s\n", replace(argv[1]));
}
string replace(string input)
{
    int lenght = strlen(input);
    for (int i = 0; i < lenght; i++)
    {
        char c = tolower(input[i]);
        switch (input[i])
        {
            case 'a':
                input[i] = 54; // ascii value of 6
                break;

            case 'e':
                input[i] = 51; // ascii value of 3
                break;

            case 'i':
                input[i] = 49; // ascii value of 1
                break;

            case 'o':
                input[i] = 48; // ascii value of 0
                break;
        }
    }
    return input;
}