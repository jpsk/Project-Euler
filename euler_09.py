"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

"""
import time

start_time = time.time()


def triplet_generator(xx, yy):
    return [
        xx * xx - yy * yy if xx > yy else yy * yy - xx * xx,
        xx ** 2 + yy ** 2,
        2 * xx * yy
    ]


x = 1
y = 2

cont = True
while cont:
    z = y
    while sum(triplet_generator(x, z)) <= 1000:
        if sum(triplet_generator(x, z)) == 1000:
            prod = 1
            for i in triplet_generator(x, z):
                prod *= i
            print("--- The answer is:  \t %d" % prod)

            cont = False
            break
        z += 1
    x += 1

print("--- Runtime: \t\t\t %s sec." % (time.time() - start_time))
