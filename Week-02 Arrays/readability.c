#include <stdio.h>
#include <math.h>
#include <cs50.h>
#include <ctype.h>
#include <string.h>

int main(void)
{
    int l = 0; //l = Letters
    int w = 1; //w = Words
    int s = 0; //s = Sentences
    string text = get_string("Text: "); //Accepts text
    for (int i = 0, n = strlen(text); i < n; i++)
    {
        char c = toupper(text[i]);
        if (c >= 'A' && c <= 'Z')
        {
            l++; // counts letters
        }
        else if (c == ' ')
        {
            w++; // counts words
        }
        else if (c == '.' || c == '?' || c == '!')
        {
            s++; // counts puntuations which equals number of sentences
        }
    }
    float L = (l * 100.0) / w; // Average Letters per 100 words
    float S = (s * 100.0) / w; // Average Sentences per 100 words
    int index = round((0.0588 * L) - (0.296 * S) - 15.8);
    if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (index >= 16)
    {
        printf("Grade 16+\n");
    }
    else 
    {
        printf("Grade %i\n", index);
    }
}