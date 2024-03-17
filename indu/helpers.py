def print_tabs(str):
    for str in str.split("\n"):
        print("\t" + str)

def get_key_by_value(my_dict, value):
  for key, val in my_dict.items():
    if val == value:
      return key
  return None  # If no key is found

