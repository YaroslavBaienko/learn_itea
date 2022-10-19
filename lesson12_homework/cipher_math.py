from io import open
import matplotlib.pyplot as plt
import re
def split_len(seq, length):
    return [seq[i:i + length] for i in range(0, len(seq), length)]

#Open file txt
txtFile = open('mensaje.txt','r', encoding="utf8")
fileContent = txtFile.readlines()
txtFile.close()
plain_text = ""
for f in fileContent:
    plain_text += f.replace("\n", "").upper()
plain_text = y = re.sub(r'[^\da-zA-Z]+', '', plain_text)
print("Texto Claro: ",plain_text)
alphabet = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ0123456789'
#key
key = (input("Llave: "))
padding = (input("Padding: "))


def encode(key, plaintext):
    #key validation
    key_number = "12345678"
    lo = len(key)
    if lo == 1 or lo == 2 or lo == 9:
        print("Longitud de llave inválido")
        return False

    i = 0
    for a in key_number:
        if not a in key:
            i += 1

        elif i > 0:
            print('\n Números repetidos en clave')
            return False
    else:
        order = {
            int(val): num for num, val in enumerate(key)
        }
        # padding letter X
        extra_letters = len(plaintext) % len(key)
        dummy_characters = len(key) - extra_letters

        if extra_letters != 0:
            for i in range(dummy_characters):
                plaintext += padding.upper()

        #encrypted text
        ciphertext = ''
        for index in sorted(order.keys()):
            for part in split_len(plaintext, len(key)):
                try:
                    ciphertext += part[order[index]]
                except IndexError:
                    continue
        return ciphertext


encrypted_text = encode(key, plain_text)

print(encrypted_text)
#Save file txt
outputFile = open('FileC.txt', 'w', encoding="utf8")
outputFile.write(encrypted_text)
outputFile.close()

#Histograma
text_file = 'FileC.txt'

letters = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ1234567890'
# Initialize the dictionary of letter counts: {'A': 0, 'B': 0, ...}
lcount = dict([(l, 0) for l in letters])

# Read in the text and count the letter occurences
for l in open(text_file).read():
    try:
        lcount[l.upper()] += 1
    except KeyError:
        # Ignore characters that are not letters
        pass
# The total number of letters
norm = sum(lcount.values())

fig = plt.figure()
ax = fig.add_subplot(111)
# The bar chart, with letters along the horizontal axis and the calculated
# letter frequencies as percentages as the bar height
x = range(37)
ax.bar(x, [lcount[l] for l in letters], width=0.8,
       color='g', alpha=0.5, align='center')
ax.set_xticks(x)
ax.set_xticklabels(letters)
ax.tick_params(axis='x', direction='out')
ax.set_xlim(-0.5, 50)
ax.yaxis.grid(True)
ax.set_ylabel('HISTOGRAMA')
plt.show()