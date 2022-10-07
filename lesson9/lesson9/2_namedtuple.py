from collections import namedtuple


Element = namedtuple('Element', 'proton, abbr, name')
hydrogen = Element(1, 'H', 'Hydrogen')
helium = Element(2, 'He', 'Helium')
lithium = Element(3, 'Li', 'Lithium')

elements = (lithium, hydrogen, helium)

elements_sort = sorted(elements, key=lambda item: item[1])
print(elements)
print(elements_sort)

# for element in elements:
    # proton, abbr, name = element
    # print(f'Protons: {proton}\nAbbr: {abbr}\nName: {name}')
    # print('#' * 25)
    
    # print(f'Protons: {element[0]}\nAbbr: {element[1]}\nName: {element[2]}')
    # print('#' * 25)

    # print(f'Protons: {element.proton}\nAbbr: {element.abbr}\nName: {element.name}')
    # print('#' * 25)

