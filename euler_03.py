""" The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ? """

import time

start_time = time.time()
number = 600851475143


def is_prime(n):
    fc = 0
    for i in range(2, n - 1):
        if n % i is 0:
            fc += 1
        if fc > 0:
            return False
    return True


i = 0
while i < number:
    i += 1
    if number % i == 0:
        if is_prime(number):
            print("\nAnswer: {}".format(number))
        number = int(number / i)

print("--- Runtime: %s seconds ---" % (time.time() - start_time))
