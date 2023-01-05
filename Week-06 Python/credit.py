# import get_string from cs50 library 
from cs50 import get_string

n = get_string("Number: ")
l = len(n)  # store length of the number
number = int(n)
s1 = s2 = j = 0

for i in range(l):
    j += 1
    t = number % 10  # stores the last digit of the number
    
    if number < 100 and number >= 10:
        ft = number  # ft = first two digits
    
    if (j % 2) == 1:
        s1 = s1 + t
    else:
        t = t * 2
        if t >= 10:
            s2 = s2 + (t % 10) + (int(t / 10))
        else:
            s2 = s2 + t
    number = int(number / 10)  # removes the last number 
    
s = s1 + s2
if (s % 10) == 0:  # checks if last number of the total sum is 0
    c = 1

if l == 15 and c == 1 and (ft == 34 or ft == 37):
    print("AMEX")
elif l == 16 and c == 1 and (ft >= 51 and ft <= 55):
    print("MASTERCARD")
elif (l == 13 or l == 16) and c == 1 and (int(ft / 10)) == 4:
    print("VISA")
else:
    print("INVALID")