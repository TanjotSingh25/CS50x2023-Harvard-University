#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

typedef uint8_t BYTE; // declaring custom byte datatype

int main(int argc, char *argv[])
{
    if (argc != 2)
    {
        printf("Usage: ./recover image\n");
        return 1;
    }
    FILE *input = fopen(argv[1], "r");
    if (input == NULL)
    {
        printf("Image cannot be opened\n");
        return 1;
    }
    BYTE block[512]; // array containing block of jpeg images
    int j = 47; // ASCII 1 LESS THAN 0
    int a = 48; // ASCII 0
    int b = 48;
    int q = 0; 
    int u = 0;
    char *name = malloc(8); // allocate 8 bits of space for string
    FILE *image = NULL;
    while (fread(block, sizeof(BYTE), 512, input)) // store block of bits in block
    {
        if (block[0] == 0xff && block[1] == 0xd8 && block[2] == 0xff && block[3] >= 0xe0 && block[3] <= 0xef) // check for jpeg
        {
            u = 1;
            if (q != 0)
            {
                fclose(image);
            }
            j++;
            if (j > 57)
            {
                j = 48;
                b++;
            }
            if (b > 57)
            {
                a++;
                b = 48;
            }
            if (a > 57)
            {
                return 1;
            }
            // naming images order wise
            name[0] = a;
            name[1] = b;
            name[2] = j;
            name[3] = '.';
            name[4] = 'j';
            name[5] = 'p';
            name[6] = 'g';
            name[7] = '\0';
            image = fopen(name, "a");
        }
        if (u == 1)
        {
            fwrite(&block, sizeof(BYTE), 512, image);
            q = 1;
        }
    }
    fclose(input);
    fclose(image);
    free(name);
}

