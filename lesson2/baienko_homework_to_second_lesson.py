# Клітини на шахівниці ідентифікуються буквою і цифрою. Літера визначає положення клітини по горизонталі,
# а цифра – по вертикалі. Ваша програма повинна вимагати у користувача координати клітини. Використовуйте умовний
# вираз для визначення того, з якої клітини – білої чи чорної – починається стовпець. Потім, за допомогою звичайної
# арифметики, необхідно визначити колір конкретної клітини. Наприклад, якщо користувач ввів a1, програма має
# визначити, що клітина із цими координатами чорна. Якщо d5 – біла. Перевірку на хибність введення координат клітини
# виконувати не потрібно.

while True:
    coordinate = (input('Please, input chessboard coordinate to find it\'s color or tap "stop" to quit : ')).lower()
    letters = [letter for letter in 'abcdefgh']
    numbers = [num for num in '12345678']

    white_colored = []
    black_colored = []

    for letter in letters:
        for number in numbers:
            if (letter in 'aceg' and number in '2468') or (letter in 'bdfh' and number in '1357'):
                white_colored.append(letter + number)

    for number in numbers:
        for letter in letters:
            if (letter in 'bdfh' and number in '2468') or (letter in 'aceg' and number in '1357'):
                black_colored.append(letter + number)

    if coordinate in white_colored:
        print('This coordinate is white')
    elif coordinate in black_colored:
        print('This coordinate is black')
    else:
        print('There are no such coordinate in chessboard, you can try again.')
    if coordinate == "stop".lower():
        break
    else:
        continue
