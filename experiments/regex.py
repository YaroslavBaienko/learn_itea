import re
import string

s = 'AC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DC'
result = re.match('AC', s)
print(result)
result_search = re.search('DC', s)
print(result_search[0])
result_findall = re.findall('DC', s)
print(result_findall)
result_split = re.split('/', s, maxsplit=3)
print(result_split)
result_sub = re.sub('A', "TT", s)
print(result_sub)
reuslt_fullmatch = re.fullmatch('AC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DC', s)
print(reuslt_fullmatch)
with open('zavet.txt', 'r') as file:
    readed = file.read()
arr = readed.strip().replace("  ", " ")
arr = arr.split()
arr = " ".join(arr)
lev_result1 = re.findall("Господ", arr)
lev_result2 = re.findall("Бог", arr)
lev_result3 = re.findall("Иисус", arr)
print(f'Всего в Новом завете встречается {len(lev_result1)} раз слова, начинающиеся с "Господ...", слов Бог всего раз встречается {len(lev_result2)} раз, а слово Иисус: {len(lev_result3)} раз')
