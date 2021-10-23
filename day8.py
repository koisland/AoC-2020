"""
# nop - no operation
# acc - increment/decrement counter
# jmp - jmp func

nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
"""

# Part 1
import pprint

with open('handheld.txt', 'r') as txt:
  code = [line.strip().split(' ') for line in txt.readlines()]
  pprint.pprint(code)

res = 0
pos = 0
actions = []

while pos != len(code):
  print('Current result:', res)
  print(code[pos])
  action, degree = code[pos]
 
  if pos in actions:
    print('Single loop result:', res)
    break
  if action == 'nop':
    pass
  elif action == 'acc':
    res += int(degree)
  elif action == 'jmp':
    pos += int(degree)
    continue
  actions.append(pos)
  pos += 1

# Part 2
  
  
  