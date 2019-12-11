#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
# def eating_cookies(n, cache=None):
#   if n < 1:
#     return 1
#   if n == 1: return 1
#   ways = 0
#   for i in range(1, min(n+1,4)):
#     # print(ways)
#     ways += eating_cookies(n - i)
#   return ways

# print(eating_cookies(25))

def eating_cookies(n, cache=None):
  cache = cache or [0 for i in range(n+1)]
  if (n > 0):
    cache[0], cache[1] = 1, 1
  else:
    cache[0] = 1

  if cache[n] == 0:
    for i in range(1, min(n+1, 4)):
      cache[n] += eating_cookies(n-i, cache)

  return cache[n]


if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')


# cookies
# eat pattern
# Ways
# 1   2         3                        4
# 1   1 1, 2    1 2, 1 1 1, 2 1, 3       1111, 112, 121, 211, 22, 13, 31
# 1   2         4                        6


# 5
# 11111, 1112, 1121, 1211, 2111, 113, 131, 311, 23, 32, 122, 212, 221
# 13


# start with lowest amount eaten, increasing as you loop
# check how many ways to eat the rest