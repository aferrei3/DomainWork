import os

i_file = open('setup/setupCommands.txt', 'r')

lines = i_file.readlines()

for line in lines:
    if line != '' and line[0] != '#':
        os.system(line)
