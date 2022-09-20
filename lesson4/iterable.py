name = 'bob'

counter = 0

while counter < len(name):
    print(name.__getitem__(counter))
    counter += 1


print(name + '!')
name = name.__add__('!')
print(name)

name_iter = iter(name)
print(name_iter)
print(next(name_iter))
print(next(name_iter))
print(next(name_iter))
print(next(name_iter))


name_iter = name.__iter__()
print(name_iter.__next__())


for char in iter(name):
    print(char)

print('__________________________')
iter_name = iter(name)
while True:
    print(next(iter_name))

