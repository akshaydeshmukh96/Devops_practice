"""This module demonstrates basic Python functionality."""
#Print prime numbers from 1 to 50
for num in range(2, 51):
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            break
    else:
        print(num)

