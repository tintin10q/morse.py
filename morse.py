from io import StringIO

conversion_table = {
    'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.',
    'g': '--.', 'h': '....', 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..',
    'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.',
    's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-',
    'y': '-.--', 'z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'
}

reverse_conversion_table = {value: key for key, value in conversion_table.items()}

def encode(text: str) -> str:
    """ Converts text into morse code with spaces as #
    This allows you to just execute it char by char
    Invalid chars are ignored. The input string is lowered.
    """
    text = text.lower().strip()
    morse = StringIO()

    for index in range(len(text)):
        char = text[index]
        next_char = text[index+1] if index != len(text)-1 else None

        if char not in conversion_table:
            continue

        morse_symbol = conversion_table[char]
        morse_symbol_length = len(morse_symbol)

        for i, char in enumerate(morse_symbol):
            morse.write(char)
            if i < morse_symbol_length:
                morse.write("#")

        if next_char == ' ':
            morse.write("#######")  # Space between words is 7
        else:
            morse.write("###")  # Space between letters is 3

    morse.seek(0)
    return morse.read()

def decode(morse: str) -> bytes:
    morse = morse.replace("#######", "/")
    morse = morse.replace("###", " ")
    morse = morse.replace("#", "")
    words = morse.split("/")

    result = StringIO()

    for word in words:
        for symbol in word.split(" "):
            if symbol not in reverse_conversion_table:
                continue
            char = reverse_conversion_table[symbol]
            result.write(char)
        result.write(' ')
    result.seek(0)
    return result.read()

if __name__ == '__main__':
    msg = 'Attack at dawn'
    encoded_msg = encode(msg)
    print(encoded_msg)
    decoded_msg = decode(encoded_msg)
    print(decoded_msg)
