#include <cs50.h>
#include <stdio.h>
#include <string.h>

const int BITS_IN_BYTE = 8;

void print_bulb(int bit);

int main(void)
{
    // TODO
    string text = get_string("My massage is: ");
    int length = strlen(text);
    for (int i = 0; i < length; i++)
    {
        int decimal = text[i];
        int binary[BITS_IN_BYTE];
        for (int j = BITS_IN_BYTE - 1; j >= 0; j--)
        {
            binary[j] = decimal % 2;
            decimal /= 2;
        }
        for (int j = 0; j < BITS_IN_BYTE; j++)
        {
            print_bulb(binary[j]);
        }
        printf("\n");
    }
}

void print_bulb(int bit)
{
    if (bit == 0)
    {
        // Dark emoji
        printf("\U000026AB");
    }
    else if (bit == 1)
    {
        // Light emoji
        printf("\U0001F7E1");
    }
}
