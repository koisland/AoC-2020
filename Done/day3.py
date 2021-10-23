import pprint
import math

# Tree = "#", Open = "."
# Move 3 chars right and 1 down starting from (0, 0)
# How many trees in path towards bottom?

def sled_ride(x, y, s_map):
  row_len = len(s_map[1])  # Row length is 31 chars
  xpos = 0  # X position on entire map.
  ypos = 0
  xsegpos = 0  # X position relative to just segment
  trees = 0

  while ypos < len(s_map):
    # Increment by x spaces and check if past chunk.  
    if xsegpos >= row_len:
      xsegpos = xsegpos % row_len

    if s_map[ypos][xsegpos] == "#":
      # print("Tree hit!")
      trees += 1

    xsegpos += x
    xpos += x
    ypos += y
    # print("Moving.")
    # print(f'Current xpos: {xsegpos}\nTotal traveled: {xpos}, {ypos}\n')

  print(f"Ride over.\nTotal trees encountered: {trees}")
  return trees

with open('map.txt', 'r') as map_txt:
  sled_map = {nrow: line.strip() for nrow, line in enumerate(map_txt.readlines())}
  # pprint.print(sled_map)

  rides = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

  trees_hit = math.prod(sled_ride(*ride, sled_map) for ride in rides)
  print(trees_hit)