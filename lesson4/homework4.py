def sort_english_grades(grades):
    if not grades:
        return []
    grades = map(str.upper, grades)
    return sorted(grades, reverse=True)


if __name__ == '__main__':
    CASES = (
        (['A', 'B', 'C', 'C', 'F', 'A'], ['F', 'C', 'C', 'B', 'A', 'A']),
        (['b', 'c', 'C', 'f', 'A'], ['F', 'C', 'C', 'B', 'A']),
        ([], [])
    )
    for case, answer in CASES:
        assert sort_english_grades(case) == answer
