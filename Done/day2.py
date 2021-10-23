# https://adventofcode.com/2020/day/2 
# list of passwords in format
  # password_policy: password
  # example - 1-3 a: abcde

def logic_xor(bool_1, bool_2):
  # bool is a subclass of int so bitwise operations work
  # One input must be True for statement to evaluate to True.
  # 1 ^ 1 -> False
  # 0 ^ 0 -> False
  # 0 ^ 1 -> True
  # 1 ^ 0 -> True
  return bool_1 ^ bool_2

def in_between(value, num_range):
  num_range = [int(str_num) for str_num in num_range]
  if len(num_range) == 2:
    return num_range[0] <= value <= num_range[1]
  
def valid_char_pos(password, conditions):
  num_pos = [int(pos) for pos in conditions['indices']]
  # No zero indexing.
  char_1, char_2 = password[num_pos[0]-1], password[num_pos[1]-1]
  # One character at pos but not both. Xor.
  if logic_xor(char_1 == conditions['letter'], char_2 == conditions['letter']):
    return True
  else:
    return False
  

with open('tobo_pass.txt', 'r') as txt:
  # [policy, password]
  pass_list = [line.strip().split(': ') for line in txt.readlines()]
  # print(pass_list)

  # num_password: [number of times, letter]
  # must enumerate to avoid removing duplicate passwords
  # pass_pol_dict = {f"{num}_{pass_info[1]}": pass_info[0].split(' ') for num, pass_info in enumerate(pass_list)}

  """
    Part 1
  """
  # # num_password: T/F
  # valid_pass = {password: in_between(password.count(cond[1]), cond[0].split('-')) 
  #               for password, cond in pass_pol_dict.items()}

  # print(len(list(valid_pass.values())))
  # print(list(valid_pass.values()).count(True))

  """
    Part 2
  """
  # pass_policies = [(pass_info[1], pass_info[0].split(' ')) for pass_info in pass_list]
  # valid_pass = [valid_char_pos(password=pass_info[0], conditions={'indices':pass_info[1][0].split('-'), 'letter': pass_info[1][1]}) 
  #               for pass_info in pass_policies]
  # print(len(valid_pass))
  # print(valid_pass.count(True), valid_pass.count(False), valid_pass.count(None))
