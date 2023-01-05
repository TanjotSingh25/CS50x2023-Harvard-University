#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int h;//h=Height of Pyramid
    do
    {
        h = get_int("Height : "); 
    }
    while (h > 8 || h < 1);
    for (int i = 1; i <= h; i++) //Line wise loop
    {
        for (int j = 0; j < (h - i); j++) //Prints starting spaces
        {
            printf(" ");
        }
        for (int k = 0; k < i; k++) //Prints #s according to Line
        {
            printf("#");
        }
        printf("  "); //Prints spaces between Pyramids
        for (int l = 0; l < i; l++) //Prints second Pyramid
        {
            printf("#");
        }
        printf("\n"); //Moves to next line
    }
}