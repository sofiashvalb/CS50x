#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

string encrypt (string p, string k);

int main(int argc, string argv[])
{
    //check if it's more than 2 arguments
    if (argc != 2)
    {
        printf("Usage: ./substitution key\n");
        return 1;
    }
    int length = strlen(argv[1]);
    for (int i = 0; i < length; i++)
    {
        //check if the argument is not alphabetical
        int letter = 0;
        if (!isalpha(argv[1][i]))
        {
            printf("Usage: ./substitution key\n");
            return 1;
        }
        //check if the argument is less than 26 characters
        else if (length != 26)
        {
            printf("Key must contain 26 characters.\n");
            return 1;
        }
        for (int j = 0; j < length; j++)
        {
            //check if the characters repeat themselves
           if (argv[1][i] == argv[1][j])
           {
            letter++;
           }
        }
        if (letter != 1)
        {
            printf("Key must contain 26 different characters.\n");
            return 1;
        }
    }
    //ask the user for a text
    string plaintext = get_string("plaintext: ");
    encrypt(plaintext, argv[1]);
    return 0;
}

string encrypt (string p, string k)
{
    int index;
    string c = "";
    for (int i = 0; i < strlen(p); i++)
    {
        if (isupper(p[i]))
        {
            index = toupper(k[p[i] - 65]);
            c[i] = k[index];
            printf("%c", c[i]);
        }
        else if (islower(p[i]))
        {
            index = tolower(k[p[i] - 97]);
            c[i] = k[index];
            printf("%c", c[i]);
        }
        else
        {
            c[i] = p[i];
            printf("%c", c[i]);
        }
    }
    printf("\n");
    return 0;
}