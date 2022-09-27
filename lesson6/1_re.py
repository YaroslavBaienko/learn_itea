# regexr.com
import re

# result_match = re.match(r'\w+', 'AVG Analytics Vidhya AV')
#
# if result_match is not None:
#     print(result_match.start(), result_match.end())
#     print(result_match.group(0))

# special_word = r'Analytics[0-9]+'
# result_search = re.search(special_word, 'AV Analytics11 Vidhya AV')
#
# if result_search is not None:
#     print(result_search.group(0))


result_findall = re.findall(r'\w{1,3}', 'AV Analytics Vidhya AV')

if result_findall is not None:
    print(result_findall)
