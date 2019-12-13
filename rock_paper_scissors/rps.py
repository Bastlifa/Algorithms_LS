#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  choices = [['rock'], ['paper'], ['scissors']]

  if n == 0: return [[]]

  cache = {
    0: [[]],
    1: [['rock'], ['paper'], ['scissors']]
  }

  def rps_inner(n):
    
    try:
      if cache[n]:
        return cache[n]
    except:
      cache[n] = []
      for i in range(3**n):
        cache[n].append(rps_inner(n-1)[i//3] + choices[i%3])
      
      return cache[n]
  rps_inner(n)


  return cache[n]

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')
