"""The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is
3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the
sum."""

import time

start_time = time.time()

s_sum = 0
sum_s = 0
for i in range(1, 101):
    s_sum += i * i
    sum_s += i

print("\nAnswer: {}".format(abs(s_sum - (sum_s * sum_s))))
print("--- Runtime: %s seconds ---" % (time.time() - start_time))
