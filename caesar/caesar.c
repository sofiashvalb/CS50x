#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

bool only_digits(string s);
char rotate(char p, int k);

// Make sure program was run with just one command-line argument

int main(int argc, string argv[])
{
    if (argc != 2 || !only_digits(argv[1]))
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
    for (int i = 0; i < strlen(argv[1]); i++)
    {
        // Make sure every character in argv[1] is a digit

        if (!isdigit(argv[1][i]))
        {
            printf("Usage: ./caesar key\n");
            return 1;
        }
        // Convert argv[1] from a `string` to an `int`
        int k = atoi(argv[1]);
        // Prompt user for plaintext
        string p = get_string("plaintext:  ");
        int length = strlen(p);
        char c[length + 1];
        printf("ciphertext: ");
        // For each character in the plaintext:
        for (int j = 0; j < length; j++)
        {
            c[j] = rotate(p[j], k);
            printf("%c", c[j]);
        }
        printf("\n");
        return 0;
    }
}

bool only_digits(string s)
{
    for (int i = 0; i < strlen(s); i++)
    {
        // Make sure every character in argv[1] is a digit

        if (!isdigit(s[i]))
        {
            return false;
        }
    }
    return true;
}

// Rotate the character if it's a letter
char rotate(char p, int k)
{
    char c;
    if (islower(p))
    {
        c = (p - 97 + k) % 26 + 97;
    }
    else if (isupper(p))
    {
        c = (p - 65 + k) % 26 + 65;
    }
    else
    {
        return p;
    }
    return c;
}