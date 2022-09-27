import re
import os

# file = open('example.txt', mode='rt')
# print(type(file))
# file.close()

current_dir = os.getcwd()
current_dir_examples = os.path.join(current_dir, 'examples')

filename_image = os.path.join(current_dir_examples, 'example_image.png')
filename_text = os.path.join(current_dir_examples, 'example_read.txt')


user_file = filename_text

try:
    open(user_file, mode='rt').readline()
except UnicodeDecodeError:
    print('App can use only text files')
    exit()

# print(open().__enter__())
# print(open().__exit__())

with open(user_file) as file:
    counter = 1
    for line in file:
        line = line.strip()
        if line:
            print(f'{counter}: {line}')
            counter += 1
# print(file.readline())
print(f'File {user_file} closed')

# file = open(user_file, mode='rt')
# counter = 1
# for line in file:
#     line = line.strip()
#     if line:
#         print(f'{counter}: {line}')
#         counter += 1
# file.close()






