class FileObject:
    def __init__(self, filename: str = 'sample.txt'):
        self.file = open(filename)

    def __del__(self):
        print('Destroy file descriptor')
        self.file.close()
        del self.file


if __name__ == '__main__':
    sample = FileObject()
    print(sample.file.readlines())
    del sample
