// Check that a password has at least one lowercase letter, uppercase letter, number and symbol
// Practice iterating through a string
// Practice using the ctype library V

#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

bool valid(string password);

int main(void)
{
    string password = get_string("Enter your password: ");
    if (valid(password))
    {
        printf("Your password is valid!\n");
    }
    else
    {
        printf("Your password needs at least one uppercase letter, lowercase letter, number and symbol\n");
    }
}

// TODO: Complete the Boolean function below
bool valid(string password)
{
    int length = strlen(password);
    int upper, lower, symbol, digit;
    for (int i = 0; i < length; i++)
    {
        //checks if the is a true variable
        if (isupper(password[i]))
        {
            upper = true;
        }
        else if (islower(password[i]))
        {
            lower = true;
        }
        else if (isdigit(password[i]))
        {
            digit = true;
        }
        else if (ispunct(password[i]))
        {
            symbol = true;
        }
    }
    //if all the 4 conditions stand
    if (upper == true && lower == true && digit == true && symbol == true)
    {
        return true;
    }
    return false;
}
