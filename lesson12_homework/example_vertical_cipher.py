import random

alphabet = "АБВГДЕЖЗИКЛМНОПРСТУФХЦЧШЩЬЫЭЮЯ"

while True:
	do = input("Для шифрования введите 1, для расшифровки введите 0\n")
	if do == '1':
		m = True
		break
	elif do == '0':
		m = False
		break
	else:
		print("Неверное значение! ")

string = input("Введите строку: ").upper()
pos = input("Введите последовательность: ")
posLen = len(pos)

if not m:
	pos = ''.join([str(7-int(x)) for x in pos[::-1]])

worldsLen = [len(x) for x in string.split(' ')]
string = string.replace(" ", "")

if len(string) % posLen != 0:
	dif = posLen - (len(string) % posLen)
	for i in range(0, dif):
		string += alphabet[random.randint(0, len(alphabet) - 1)]

encString = ""
for i in range(0, int(len(string) / posLen)):
	for n in range(0, posLen):
		encString += string[(posLen * i) + int(pos[n]) - 1]

words = []
summa = 0
for i in worldsLen:
	words.append(encString[summa:summa+i])
	summa += i
words.append(encString[summa:])

print(" ".join(words))
input()
