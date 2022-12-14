"""Написати функцію, яка сортує список із оцінками на основі англійської системи.
Усього 5 символів, у порядку спадання: A, B, C, D, F.

Приклади:

sort_grades(['A', 'B', 'C', 'C', 'F', 'A')) -> ['F', 'C', 'C', 'B', 'A' , 'A']
sort_grades(['b', 'c', 'C', 'f', 'A')) -> ['F', 'C', 'C', 'B', 'A']
sort_grades([]) -> []
"""


def sort_grades(grades: list) -> list:
    if grades == []:
        return []
    else:
        sorted_grades = []
        for grade in grades:
            sorted_grades.append(grade.upper())
            sorted_grades.sort(reverse=True)
    return sorted_grades


print(sort_grades(['b', 'c', 'C', 'f', 'A']))
