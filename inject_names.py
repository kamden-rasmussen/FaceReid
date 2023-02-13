import random
import string

def injectUsers():
  users = []
  f = open('names.txt', 'r')
  for line in f:
    user = (line, line+"@foobar.com", ''.join(random.choices(string.ascii_letters, k=5)))
    users.append(user)
  f.close()
  return users