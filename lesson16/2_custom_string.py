class Word(str):
    def __new__(cls, word):
        if ' ' in word:
            print('Word contains spaces. Cut to first word.')
            word = word[:word.index(' ')]
        return str.__new__(cls, word)

    def __gt__(self, other):
        return len(self) > len(other)

    def __lt__(self, other):
        return len(self) < len(other)

    def __ge__(self, other):
        return len(self) >= len(other)

    def __le__(self, other):
        return len(self) <= len(other)


if __name__ == '__main__':
    word = Word('bob smith')
    print(word > 'four')

