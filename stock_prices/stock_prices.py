#!/usr/bin/python

import argparse

def find_max_profit(prices):
  # print(prices)
  max_profit = min(prices) - max(prices)
  if len(prices) < 2:
    return max_profit

  for s in range(1, len(prices)):
    for b in range(len(prices[0:s])):
      max_profit = max(max_profit, prices[s]-prices[b])
      # print("b, s", b, s)
      # print(f"prices[s]: {prices[s]}, prices[b]: {prices[b]}, max_profit: {max_profit}")

  return max_profit

if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))