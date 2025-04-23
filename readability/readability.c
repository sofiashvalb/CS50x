#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int count_letters(string text);
int count_words(string text);
int count_sentences(string text);

int main(void)
{
    string text = get_string("Text: ");
    int letters = count_letters(text);
    float words = count_words(text);
    int sentences = count_sentences(text);
    float L = (letters * 100) / words;
    float S = (sentences * 100) / words;
    float index = (0.0588 * L) - (0.296 * S) - 15.8;
    if (index >= 16)
    {
        printf("Grade 16+\n");
    }
    else if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    else
    {
        printf("Grade %.0f\n", round(index));
    }
}

int count_letters(string text)
{
    int length = strlen(text);
    int score = 0;
    for (int i = 0; i < length; i++)
    {
        if (isupper(text[i]))
        {
            score++;
        }
        else if (islower(text[i]))
        {
            score++;
        }
    }
    return score;
}

int count_words(string text)
{
    int length = strlen(text);
    int score = 1;
    for (int i = 0; i < length; i++)
    {
        if (isspace(text[i]))
        {
            score++;
        }
    }
    return score;
}

int count_sentences(string text)
{
    int length = strlen(text);
    int score = 0;
    for (int i = 0; i < length; i++)
    {
        if (text[i] == 33 || text[i] == 63 || text[i] == 46)
        {
            score++;
        }
    }
    return score;
}