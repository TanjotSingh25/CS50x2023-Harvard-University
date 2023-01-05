#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>

int main(int argc, string argv[])
{
    if (argc != 2) 
    {
        printf("Usage: ./substitution key\n");// error message for having less than or more than 2 arguments 
        return 1;
    }
    if (strlen(argv[1]) != 26) 
    {
        printf("Key must contain 26 characters!\n");// error message for key not containing 26 characters
        return 1;
    }
    for (int i = 0; i < 26; i++)
    {
        char a = argv[1][i];
        char c = toupper(a);
        if (c < 'A' || c > 'Z')
        {
            printf("Key must contain only alphabetical characters!\n");//error message for key containing non alphabetical characters
            return 1;
        }
        for (int j = i + 1; j < 26; j++)
        {
            char b = toupper(argv[1][j]);
            if (a == b)
            {
                printf("Key should contain each character exactly once\n");// error message for repetition of characters
                return 1;
            }
        }
    }
    string PT = get_string("plaintext: "); //accepts plain text
    printf("ciphertext: ");
    for (int i = 0, l = strlen(PT); i < l; i++)
    {
        char c = PT[i];
        if (islower(c))
        {
            char r = tolower(argv[1][c - 97]); // prints cipher code in lower case
            printf("%c", r);
        }
        else if (isupper(c))
        {
            char r = toupper(argv[1][c - 65]); // prints cipher code in upper case
            printf("%c", r);
        }
        else
        {
            printf("%c", c); // prints a non alphabetical character as it is
        }
    }
    printf("\n"); //leaves a line
}