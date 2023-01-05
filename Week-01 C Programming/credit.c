#include <stdio.h>
#include <cs50.h>

char check_card(long n);

char check_validity(int s);

int main(void)
{
    long cn = get_long("Number : "); //CN=Credit Card Number
    int m;
    char card; //Store Card Company
    char validity;
    int l=1;
    int s1=0; //Sum of odd digits
    int s2=0; //Sum of even digits*2
    int sum=0; //Total Sum
    while(cn!=0)
    {
        m=cn%10;
        if(l%2==1)
        {
            s1=s1+m;
        }
        else
        {
            int d=m*2;
            if(d>9)
            {
                s2=s2+(d/10)+(d%10);
            }
            else
            {
                s2=s2+d;
            }
        }
        if(cn>=10 && cn<=99)
        {
            card=check_card(cn);
        }
        cn=cn/10;
        l++;
    }
    sum=s1+s2;
    validity=check_validity(sum);
    l=l-1;
    if(validity=='V' && card=='A' && l==15)
    {
        printf("AMEX\n");
    }
    else if(validity=='V' && card=='M' && l==16)
    {
        printf("MASTERCARD\n");
    }
    else if(validity=='V' && card=='V' && ( l==13 || l==16 ))
    {
        printf("VISA\n");
    }
    else
    {
        printf("INVALID\n");
    }
}
char check_card(long n)
{
    if(n==34||n==37)
        {
            return ('A');
        }
        else if(n>=51&&n<=55)
        {
            return ('M');
        }
        else if((n/10)==4)
        {
            return ('V');
        }
        else
        {
            return ('I');
        }
}
char check_validity(int s)
{
    if(s%10==0)
    {
        return ('V');
    }
    else
    {
        return ('I');
    }
}