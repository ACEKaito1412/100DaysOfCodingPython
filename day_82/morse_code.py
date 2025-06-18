import sys, os, winsound, time

COMMANDS = ['help', 'encode', 'decode', 'audio']
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
    'E': '.',  'F': '..-.', 'G': '--.',  'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-',  'L': '.-..',
    'M': '--', 'N': '-.',   'O': '---',  'P': '.--.',
    'Q': '--.-','R': '.-.', 'S': '...',  'T': '-',
    'U': '..-','V': '...-', 'W': '.--',  'X': '-..-',
    'Y': '-.--','Z': '--..',
    '0': '-----', '1': '.----', '2': '..---',
    '3': '...--','4': '....-', '5': '.....',
    '6': '-....','7': '--...','8': '---..','9': '----.',
    ' ': '/'
}

REVERSE_MORSE = {v: k for k, v in MORSE_CODE_DICT.items()}


def encode(text:str)->str:
    code = ''
    for char in text:
        code += " " + MORSE_CODE_DICT.get(char.upper(), '')

    return code

def decode(morse_code:str)->str:
    text = ''
    for code in morse_code.split(' '):
        text += REVERSE_MORSE.get(code, '')

    return text

def play_morse(morse_code):
    for symbol in morse_code:
        if symbol == '.':
            winsound.Beep(700, 100)  # Short beep
            time.sleep(0.2)
        elif symbol == '-':
            winsound.Beep(700, 400)  # Long beep
            time.sleep(0.2)
        elif symbol == ' ':
            time.sleep(0.3)
        elif symbol == '/':
            time.sleep(0.4)


n = len(sys.argv)

if n > 1:
    command = sys.argv[1]

    if command not in COMMANDS:
        print('Command not found, try [help] command')
        exit

    if n < 2:
        print('No file/text is given after the command')
        exit

    isfile = False
    text = ''

    if command != 'help':
        if os.path.isfile(sys.argv[2]):
            path = sys.argv[2]
            with open(path, 'r', encoding='utf8') as file:
                text = file.read()
            isfile = True
        else:
            text = sys.argv[2]

    match command:
        case 'help':
            print('list of commands: ')
            for item in COMMANDS:
                print(item)
        case 'encode':
            print('encoding: \n')
            encoded_text = encode(text)

            if not isfile:
                print(encoded_text)
            else:
                name, ext = path.split('.')
                path = f"{name}_encode.{ext}"
                with open(path, 'w', encoding='utf8') as file:
                    file.write(encoded_text)

        case 'decode':
            print('decoding: \n')

            decoded_text = decode(text)

            if not isfile:
                print(decoded_text)
            else:
                name, ext = path.split('.')
                path = f"{name}_decode.{ext}"
                with open(path, 'w', encoding='utf8') as file:
                    file.write(decoded_text)

        case 'audio':
            play_morse(text)
            


