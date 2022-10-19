NATO_ALPHABET = codes = {
    'a' : "Alpha",
    'b' : "Bravo",
    'c' : "Charlie",
    'd' : "Delta",
    'e' : "Echo",
    'f' : "Foxtrot",
    'g' : "Golf",
    'h' : "Hotel",
    'i' : "India",
    'j' : "Juliet",
    'k' : "Kilo",
    'l' : "Lima",
    'm' : "Mike",
    'n' : "November",
    'o' : "Oscar",
    'p' : "Papa",
    'q' : "Quebec",
    'r' : "Romeo",
    's' : "Sierra",
    't' : "Tango",
    'u' : "Uniform",
    'v' : "Victor",
    'w' : "Whisky",
    'x' : "XRay",
    'y' : "Yankee",
    'z' : "Zulu",
    '0' : "Zero",
    '1' : "One",
    '2' : "Two",
    '3' : "Three",
    '4' : "Four",
    '5' : "Five",
    '6' : "Six",
    '7': "Seven",
    '8' : "Eight",
    '9' : "nine"
}

def get_nato_message():
    message = input('Enter the letter to convert to NATO alphabet: ')
    converted_message = []
    for letter in message:
        if letter.lower() in NATO_ALPHABET:
            converted_message.append(NATO_ALPHABET[letter.lower()])
    return converted_message

my_message = get_nato_message()
print(my_message)