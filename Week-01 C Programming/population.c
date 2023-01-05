#include <stdio.h>
#include <cs50.h>
int main(void)
{
    int ss;//ss=Start Size
    int es;//es=End Size
    do
    {
        ss = get_int("Starting Population Size : ");
    }
    while (ss < 9);
    do
    {
        es = get_int("Ending Population Size : ");
    }
    while (es < ss);
    int year = 0;
    while (ss < es)
    {
        ss = ss + (ss / 3) - (ss / 4);
        year++;
    }
    printf("Years: %i", year);
}