import random
import string

def injectUsers():
  users = []
  f = open('names.txt', 'r')
  for line in f:
    line = line.strip()
    user = (line, line.lower()+"@foobar.com", ''.join(random.choices(string.ascii_letters, k=5)))
    users.append(user)
  f.close()
  return users