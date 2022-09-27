import re

result_match = re.match(r'\w+', 'AVG Analitics Vid AV')
if result_match is not None:
    print(result_match.start(), result_match.end())
    print(result_match.group(0))


special_word = r'Analytics[0-9]+'
result_search = re.search(special_word, 'AVG Analytics11 Vid AV')
print(result_search.group(0))


special_word = r'\w{1,3}'
result_findall = re.findall(special_word, 'AVG Analytics11 Vid AV')
print(result_findall)