import pprint
import re
from collections import defaultdict, Counter

"""
  Passport data should have
    byr
    iyr
    eyr
    hgt
    hcl
    ecl
    pid
    cid (Optional)
"""
# cid not included as it's optional
req_fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
checks = {'byr': lambda field: (1920 <= int(field) <= 2002) and re.search('^\d{4}$', field), 
          'iyr': lambda field: (2010 <= int(field) <= 2020) and re.search('^\d{4}$', field), 
          'eyr': lambda field: (2020 <= int(field) <= 2030) and re.search('^\d{4}$', field),  
          'pid': lambda field: re.search('^\d{9}$', field),
          'cid': lambda field: True,
          'hcl': lambda field: re.search('^#([0-9a-f]){6}$', field),
          'ecl': lambda field: field in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')}


def screen_field(field_type, field):
  # field_type: {num: bool, len_chk:num, cond:???}
  if field_type == 'hgt':
    if unit_val := re.search('(\d+)(cm|in)', field):
      if unit_val.group(2) == 'cm':
        return 150 <= int(unit_val.group(1)) <= 193
      else:
        return 59 <= int(unit_val.group(1)) <= 76
    else:
      return False
  else:
    if checks.get(field_type)(field):
      # print(field_type, field, checks.get(field_type)(field))
      return True

with open("passport_batch.txt", "r") as txt:
  raw_data = txt.read().split("\n")
  # pprint.pprint(raw_data)
  
  passportn = 1
  passports = defaultdict(list)

  # '' are seperators between passports
  for line in raw_data:
    if line == '':
      passportn += 1
    else:
      passports[passportn].append(line)
  
  # concatenate passport info list and split between info categ
  passports = {num: ' '.join(passport).split() for num, passport in passports.items()}
  
  #
  fmtted_passports = defaultdict(dict)
  valid_passports = Counter()

  for num, passport_fields in passports.items():
    if req_fields.issubset({field.split(":")[0] for field in passport_fields}):
      if all(screen_field(*field.split(":")) for field in passport_fields):
        valid_passports['Valid'] += 1
        # print(passport_fields)
      else:
        valid_passports['Invalid'] += 1
    else: 
      valid_passports['Invalid'] += 1
      # (categ, entry) = field.split(":")
      # fmtted_passports[num][categ] = entry
  # pprint.pprint(fmtted_passports)


  # for num, pspt in fmtted_passports.items():
  #   if req_fields.issubset(set(pspt.keys())):
  #     valid_passports['Valid'] += 1
  #   else:
  #     valid_passports['Invalid'] += 1
  print(valid_passports)



