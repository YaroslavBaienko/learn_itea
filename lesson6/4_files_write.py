import os

current_dir = os.getcwd()
current_write_file = os.path.join(current_dir, 'examples', 'example_write.txt')
wrong_path_to_file = 'wrong.txt'
# print(current_write_file)

user_choice = current_write_file

try:
    open(user_choice, mode='rt').readline()
except UnicodeDecodeError:
    print('App can use only text files')
    exit()
except FileNotFoundError as error:
    print(error)
    exit()

with open(user_choice, 'w') as file:
    for number in range(10):
        line = f'{number}\n'
        file.write(line)

print(f'Write to {user_choice} complete')
