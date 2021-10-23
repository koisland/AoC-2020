# FBFBBFFRLR
# F, L = lower half
# B, R = upper half
import re

def seat_col_splitter(b_pass):
  splt_ptn = re.compile("[BF][LR]")
  q = re.search(splt_ptn, b_pass)
  q_str = list(q.group())
  q_str.insert(1, '|')
  return re.sub(splt_ptn, ''.join(q_str), b_pass)

def find_middle(start, end):
  return start + round((end-start) / 2)

def find_seat(s_input, start, end):
  middle = find_middle(start, end)
  if len(s_input) == 1:
    if s_input[0] in ('F', 'L'):
      return start
    else:
      return end
  else:
    if s_input[0] in ('F', 'L'):
      end = middle
    else:
      start = middle
    return find_seat(s_input[1:], start, end)

with open('board_pass_test.txt', 'r') as txt_obj:
  passes = (line.strip() for line in txt_obj.readlines())
  # ids = []
  # for p in passes:
  #   split_pass = seat_col_splitter(p)
  #   row_chks, col_chks = split_pass.split("|")
  #   row = find_seat(row_chks, 0, 127)
  #   col = find_seat(col_chks, 0, 7)
  #   seat_id = row * 8 + col
  #   ids.append(seat_id)
  # print(ids)
  # print(len(ids))
  # print(max(ids))

# ^^^^ 
# My solution sucks. :\

all_seats = [int((l.replace('B','1').replace('F','0').replace('R','1').replace('L','0')),2) for l in open('board_pass.txt')]
print(min(all_seats), max(all_seats))
print([s for s in range(min(all_seats), max(all_seats)) if s not in all_seats])