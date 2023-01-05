// Implements a dictionary's functionality

#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>
#include <ctype.h>
#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// Number of buckets in hash table
const unsigned int N = ((26 * 26) + 26 + 26); // +26 for single character words in dictionary ; second +26 for '

// Global Variables
int error = 0;
int sized = 0;

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    int hashcode = hash(word);
    node *temp;
    for (temp = table[hashcode]; temp != NULL; temp = temp -> next)
    {
        if (strcasecmp(word, temp -> word) == 0)
        {
            return true;
        }
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    int hashcode;
    if (strlen(word) == 1)
    {
        hashcode = (26 * 26) + (tolower(word[0]) - 97);
    }
    else if (word[1] == '\'')
    {
        hashcode = (((26 * 26) + 26) + (tolower(word[0]) - 97));
    }
    else
    {
        hashcode = ((tolower(word[0]) - 97) * 26) + (tolower(word[1]) - 97);
    }
    return hashcode;
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    FILE *dict = fopen(dictionary, "r");
    if (dict == NULL)
    {
        error = 1;
        return false;
    }
    char c;
    int i = 0;
    int o = 0; // one time variable
    int index1;// new index
    int index2 = -1;// previous index
    node *temp = malloc(sizeof(node));
    node *prev = NULL;
    while (fread(&c, sizeof(char), 1, dict))
    {
        if (c != '\n')
        {
            temp -> word[i] = c;
            i++;
        }
        else
        {
            temp -> word[i] = '\0';
            temp -> next = NULL;
            i = 0;
            sized++;

            //Index allocation
            if (strlen(temp -> word) == 1)
            {
                index1 = (26 * 26) + (temp -> word[0] - 97);
            }
            else if (temp -> word[1] == '\'')
            {
                index1 = (((26 * 26) + 26) + (tolower(temp -> word[0]) - 97));
            }
            else
            {
                index1 = ((temp -> word[0] - 97) * 26) + (temp -> word[1] - 97);
            }


            if (index1 != index2)
            {
                table[index1] = temp;
                index2 = index1;
                if (o == 1)
                {
                    prev -> next = NULL;
                }

            }
            node *t = malloc(sizeof(node));
            temp -> next = t;
            prev = temp;
            temp = t;
            o = 1;
        }
    }
    free(temp);
    prev -> next = NULL;
    fclose(dict);
    return true;
    
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    if (error == 1)
    {
        return 0;
    }
    else
    {
        return sized;
    }
    return 0;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    for (int i = 0; i < 728; i++)
    {
        node *temp;
        node *t;
        for (temp = table[i]; temp != NULL; temp = t)
        {
            t = temp -> next;
            free(temp);
        }
        free(temp);
    }
    return true;
}
