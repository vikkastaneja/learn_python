# Given a file, we want to create a new file with all lines from current file with a caveat that each line is appended with word count for that line
import modules.my_module as m
import random

num_words = 10
min_length = 3
max_length = 10
current_file_location = './random.txt'
with open(current_file_location, 'w') as f:
    for i in range(10):
        random_text = m.generate_random_text_lines(random.randint(0, num_words), min_length, max_length)
        f.write(random_text+'\n')

write_file = './write_file.txt'
with open(current_file_location, 'r') as r, open(write_file, 'w') as w:
    for line in r:
        text = str(line[:-1]) + ' ' + str(len(line.split())) + '\n'
        w.write(text)

with open(write_file, 'r') as r:
    print(r.read())
