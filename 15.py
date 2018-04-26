from sys import argv

script, input_file = argv

def print_all(f):
  print open(f)

print_all(input_file);