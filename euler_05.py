""" 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20? """

import time

start_time = time.time()


def is_divisible(num):
    for i in range(20, 7, -1):
        if num % i != 0:
            return False
    return True


j = 20
while not is_divisible(j):
    j += 20

print("\nAnswer: {}".format(j))
print("--- Runtime: %s seconds ---" % (time.time() - start_time))
