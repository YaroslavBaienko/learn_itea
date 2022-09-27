import os
import random

print(os.getcwd())
with open('files/example_write.txt', 'w') as file:
    nums = [random.randrange(1, 1000) for _ in range(1, 1000300, 2)]
    for i in nums:
        file.writelines(str(i))
        file.writelines('\n')
print(f'Write into file complete')

with open('files/example_write.txt', 'rt') as file:
    normilizied = list()
    file = file.readlines()
    for line in file:
        normilizied.append(int(line.strip()))
    print(sorted(normilizied))
