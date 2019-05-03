
'''
update os.environ with ./env_file vars
'''

import os

with open('./env_file', 'rt') as file:
    vars = file.readlines()


vars = [i.replace('\n', '').split('=') for i in vars]

#tuple(vars[0])

for line in vars:
    os.environ[line[0]] = line[1]

print(os.environ)



##############

