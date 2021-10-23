# expense report is puzzle input
# find two entries that sum to 2020
# answer is the product of said entries

import pprint
from math import prod

with open('expense_rpt.txt', 'r') as obj:
  raw_expenses = [int(item) for item in obj.read().split()]
  expenses = sorted(raw_expenses)


"""
Part 1
"""
des_sum = 2020
fin_product = 0

for item in expenses:
  if des_sum-item in expenses:
    fin_product = item * (des_sum-item)

# print(fin_product)

"""
Part 2
"""
#O(n^2) Not good.
# https://adventofcode.com/2020/day/1#part2

def trisum_prod():
  for item1 in expenses:
    for item2 in expenses:
      fin_item = des_sum - (item1 + item2)
      if item2 != item1 and fin_item in expenses:
        return prod([item1, item2, fin_item])

print(trisum_prod())
