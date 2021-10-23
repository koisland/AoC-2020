import re
import pprint

def contains_bag(bag, bags, bags_color, des_color):
  """
  Recursive function to find if a bag contains a bag with a desired color
  :param: bag - string describing starting bag
  :param: bags - dict of dict containing all bags
  :param: bags_color - set with bags containing color
  :param: des_color - string describing desired color color
  return: bool (has bag or not) and bags containing color
  """
  
  # if bag is desired color or bag is a bag that is known to contain color
  if bag == des_color or bag in bags_color:
    bags_color.add(bag)
    return True, bags_color

  # get inner bags, if empty then last bag and init bag doesn't contain colored bag
  inn_bags = bags.get(bag, "Empty")

  if des_color in inn_bags:
    bags_color.add(bag)
    return True, bags_color

  # print(f"\t{inn_bags=}")
  if inn_bags == "Empty":
    return False, bags_color
  else:
    # if bags do remain, go through each bag
    for bag in inn_bags:
      
      # otherwise, recurse checking inside that bag for desired color.
      bag_found, bags_color = contains_bag(bag, bags, bags_color, des_color)
      if bag_found:
        return True, bags_color

  return bag_found, bags_color

def main():
  DES_COLOR = "shiny gold"
  PROMPT_FILE = "bags.txt"

  # preprocessing
  with open(PROMPT_FILE, "r") as fobj:
    txt = fobj.readlines()
    bag_dict = {}
    for line in txt:
      spl_line = re.split(",\s|\scontain\s", line.strip())
      # print(f"{spl_line=}")
      col_only_line = [re.sub("\sbags*|\.", "", bag) for bag in spl_line]
      # print(f"{col_only_line=}\n")
      bag_dict[col_only_line[0]] = {num_color.split(" ", 1)[1]: num_color.split(" ", 1)[0] for num_color in col_only_line[1:]}

  # pprint.pprint(bag_dict) 
 

  bags_w_color = set()
  for bag in bag_dict:
    print(f"{bag=}")
    has_color, bags_w_color = contains_bag(bag, bag_dict, bags_w_color, DES_COLOR)
    if has_color:
      print(f"\tBag found in {bag}.")
      bags_w_color.add(bag)

  # remove shiny gold from set
  assert(DES_COLOR in bags_w_color)
  bags_w_color.remove(DES_COLOR)
  print(f"Total bags ({len(bag_dict)}) that have '{DES_COLOR}': {len(bags_w_color)}")

main()
