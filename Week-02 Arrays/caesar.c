#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
#include <ctype.h>

int main(int argc, string argv[]) //accepts command line value of key
{
    if (argc != 2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }
    for (int i = 0, l = strlen(argv[1]); i < l; i++) 
    { 
        if (argv[1][i] < '0' || argv[1][i] > '9')
        {
            printf("Usage: ./caesar key\n");
            return 1;
        }
    }
    int key = atoi(argv[1]); // convert string to int
    string PT = get_string("plaintext: "); // PT = Plain Text
    int n = strlen(PT); // length of plain text
    printf("ciphertext: ");
    for (int j = 0; j < n; j++)
    {
        char p = PT[j];
        char c;
        if (isupper(p)) //checks upper case
        {
            c = (((p - 65) + key) % 26) + 65; 
            printf("%c", c);
        }
        else if (islower(p)) //checks lower case
        {
            c = (((p - 97) + key) % 26) + 97;
            printf("%c", c);
        }
        else //all other characters are passed as it is
        {
            printf("%c", p);
        }
    }
    printf("\n"); //leaves line
}


