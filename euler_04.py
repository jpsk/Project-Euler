""" A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit
numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers. """

import time

start_time = time.time()

x = 999
y = 999
F = 0  # flag indicating which number (x or y was decremented)
list_ = []
max_ = 0


# check palindrome function
def is_palindrome(num):
    return str(num) == str(num)[::-1]


# we don't need to check !999 times for palindromes, so we will decrement x and y in turns until we get a palindrome.
while not is_palindrome(x * y):
    if F == 0:
        x -= 1
        F = 1
    else:
        y -= 1
        F = 0

# Iterate through each x and y and make a list of palindromes
for i in range(999, x, -1):
    for j in range(999, y, -1):
        if is_palindrome(i * j):
            list_.append(i * j)
        j -= 1
    i -= 1

# Find max palindrome from list of palindromes
for l in list_:
    if l > max_:
        max_ = l
print("\nAnswer: {}".format(max_))

print("--- Runtime: %s seconds ---" % (time.time() - start_time))
