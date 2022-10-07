from collections import namedtuple

Element = namedtuple('Element', 'proton, abbr, name')
hydrogen = Element(1, 'H', 'Hydrogen')
helium = Element(2, 'He', 'Helium')
lithium = Element(3, 'Li', 'Lithium')

print(hydrogen.proton)

elements = (hydrogen, lithium, helium)
elements_sort = sorted(elements, key=lambda x: x[1])

#     (1, 'H', 'Hydrogen'),
#     (2, 'He', 'Helium'),
#     (3, 'Li', 'Lithium')
# )
# for element in elements:
# # proton, abbr, name = element
#     print(f'Proton {element.}\nAbbr: {abbr}\nName: {name}')
# print('#' * 25)
print(elements_sort)