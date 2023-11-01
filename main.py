from art import logo

morse_code = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....',
              'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.',
              'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-',
              'y': '-.--', 'z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
              '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', ',': '--..--', '.': '.-.-.-',
              '?': '..--..'}


# Function to encode text into Morse code
def text_to_morse(text):
    text = text.lower()  # Convert the input text to lowercase to handle both upper and lower case letters
    morse_list = []

    for char in text:
        if char in morse_code:
            morse_list.append(morse_code[char])
        elif char == ' ':
            morse_list.append(' ')  # Use space to separate words

    return ' '.join(morse_list)


# Function to decode Morse code into text
def morse_to_text(morse):
    morse_code_reverse = {v: k for k, v in morse_code.items()}  # Reverse the morse_code dictionary
    morse_list = morse.split(' ')
    text = []

    for morse_char in morse_list:
        if morse_char in morse_code_reverse:
            text.append(morse_code_reverse[morse_char])
        elif morse_char == '':
            text.append(' ')  # Use space to separate words

    return ''.join(text)


print(logo)


while True:

    choice = input("Choose an option (encode/decode/quit): ").lower()

    if choice == 'encode':
        text = input("Enter the text to encode: ")
        morse = text_to_morse(text)
        print(f"Morse code: {morse}")
    elif choice == 'decode':
        morse = input("Enter the Morse code to decode: ")
        text = morse_to_text(morse)
        print(f"Decoded text: {text}")
    elif choice == 'quit':
        break
    else:
        print("Invalid option. Please choose 'encode', 'decode', or 'quit'.")
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        print("Goodbye")
        break
