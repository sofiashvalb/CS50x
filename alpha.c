#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    //get a word
    string word = get_string("Word: ");
    int word_length = strlen(word);
    //start a loop that goes through the length of the array and converts it to his ascii value
    for (int i = 0; i < word_length - 1; i++)
    {
        //checks if the ascii values are alphabetise
        if (word[i] > word [i + 1])
        {
            printf("No\n");
            return 0;
        }
        printf("yes");
        return 0;
    }
}