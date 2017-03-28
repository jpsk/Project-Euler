"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

"""

"""
What is prime number: A prime number is one that is divisible only by 1 and itself.

Rules to follow:
- if 1 then prime
- if 2 then prime
- if 3 then prime
- if 5 then prime

- if divisible by 2 -> notprime
- if divisible by 3 -> notprime
- if divisible by 5 -> notprime
- if divisible by prime -> notprime

"""
import time

start_time = time.time()

divs = [2, 3, 5]

prime_counter = 0
int_counter = 1


def is_prime(arg):
    if arg == 1 or arg == 2 or arg == 3 or arg == 5:
        return True
    for div in divs:
        if arg % div == 0:
            return False
    divs.append(arg)
    return True


while prime_counter < 10002:
    if is_prime(int_counter):
        prime_counter += 1
    int_counter += 1

print("\n--- The 10001'st prime number is: \t %d" % (int_counter - 1))
print("--- Runtime: \t %s sec." % (time.time() - start_time))
