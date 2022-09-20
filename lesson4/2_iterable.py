name = 'bob'

counter = 0

while counter < len(name):
    # print(name.__getitem__(counter))
    counter += 1

# print(name + '!')
name = name.__add__('!')
# print(name)

name_iter = iter(name)
# print(next(name_iter))
# print(next(name_iter))
# print(next(name_iter))
# print(next(name_iter))
#
# name_iter = name.__iter__()
# print(name_iter.__next__())
# print(name_iter.__next__())
# print(name_iter.__next__())
# print(name_iter.__next__())
# print(name_iter.__next__())

iter_name = iter(name)
while True:
    try:
        print(next(iter_name))
    except StopIteration:
        break

for char in name:
    print(char)
