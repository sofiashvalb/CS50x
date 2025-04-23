// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>

#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 26;
int count = 0;

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    int hnum = hash(word);
    node *cursor = table[hnum];
    while (cursor != NULL)
    {
        if (strcasecmp(cursor->word, word) == 0)
        {
            return true;
        }
        cursor = cursor->next;
    }

    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    return toupper(word[0]) - 'A';
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // TODO
    FILE *dicfile = fopen(dictionary, "r");
    if (dicfile == NULL)
    {
        printf("File not found\n");
        return false;
    }
    char mila[LENGTH + 1];
    while (fscanf(dicfile, "%s", mila) != EOF)
    {
        node *temp = malloc(sizeof(node));
        if (temp == NULL)
        {
            return false;
        }
        strcpy(temp->word, mila);
        int hnum = hash(mila);
        if (table[hnum] == NULL)
        {
            temp->next = NULL;
        }
        else
        {
            temp->next = table[hnum];
        }
        table[hnum] = temp;
        count += 1;
    }
    fclose(dicfile);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    return count;
}

// Unloads dictionary from memory, returning true if successful, else false
void freee(node *n)
{
    if (n->next != NULL)
    {
        freee(n->next);
    }
    free(n);
}

bool unload(void)
{
    // TODO
    for (int i = 0; i < N; i++)
    {
        if (table[i] != NULL)
        {
            freee(table[i]);
        }
    }
    return true;
}
