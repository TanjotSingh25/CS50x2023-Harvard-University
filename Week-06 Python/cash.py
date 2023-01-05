# import get_float form cs50 library
from cs50 import get_float

# checks if change is a positive number
while True:
    c = get_float("Change owed: ")
    if c >= 0:
        break

# convert the change in dollars to cents
c = c * 100
coins = 0

# calculates the number of coins required
while c != 0:
    if c >= 25:
        c = c - 25
        coins += 1
    elif c >= 10:
        c = c - 10
        coins += 1
    elif c >= 5:
        c = c - 5
        coins += 1
    elif c >= 1:
        c = c - 1
        coins += 1

print(coins)