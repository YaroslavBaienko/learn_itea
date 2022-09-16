flag = True
if flag:
    flag = False

print(flag)
print(bool('rr'))

a = False
b = True
c = False

print(a or (b or c))

names = ['', '', 'Bob']
print(any(names))
print(all(names))