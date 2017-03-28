"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

"""


import time
start_time = time.time()

COUNT_TO = 2000000


divs = [2, 3, 5]


def is_prime(arg):
    if arg == 1:
        return False
    if arg in divs:
        return True
    for div in divs:
        if arg % div == 0:
            return False
    # divs.append(arg)
    return True

sum_ = 0
for i in range(COUNT_TO):
    if is_prime(i):
        sum_ += i

answer = sum_

print("\n--- The answer is:  \t %d" % answer)
print("--- Runtime: \t\t\t %s sec." % (time.time() - start_time))
