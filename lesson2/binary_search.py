from random import randint, choice


def binary_search(data: list[int], value: int) -> int:
    middle = 0
    start = 0
    end = len(data)
    step = 0

    while start <= end:
        print(f'List in step {step}: {str(data[start:end + 1])}')
        step += 1
        middle = (start + end) // 2

        if value == data[middle]:
            return middle

        if value < data[middle]:
            end = middle - 1

        else:
            start = middle + 1

    return -1


numbers = []
for _ in range(20):
    numbers.append(randint(1, 100))

random_number = choice(numbers)
numbers.sort()
# print(numbers)
#
# random_number = choice(numbers)
#
# print(len(numbers) // 2)
# print(numbers[len(numbers) // 2])
print(binary_search(numbers, random_number))
