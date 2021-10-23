import pprint

with open('customs.txt', 'r') as txt:
  raw_ctext = txt.read().split('\n\n')
  list_ctext = [group.split('\n') for group in raw_ctext]
  grp_answers_set = [[set(ans) for ans in set_txt] for set_txt in list_ctext]
  shared_grp_answers = [group[0].intersection(*group) for group in grp_answers_set]

  print(sum(len(s) for s in shared_grp_answers))