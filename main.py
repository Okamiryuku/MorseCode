morse_code = {'a':'.-', 'b':'-...', 'c':'-.-.', 'd':'-..', 'e':'.', 'f':'..-.', 'g':'--.', 'h':'....', 'i':'..',
              'j':'.---', 'k':'-.-', 'l':'.-..', 'm':'--', 'n':'-.', 'o':'---', 'p':'.--.', 'q':'--.-', 'r':'.-.',
              's':'...', 't':'-', 'u':'..-', 'v':'...-', 'w':'.--', 'x':'-..-', 'y':'-.--', 'z':'--..','0':'-----',
              '1':'.----', '2':'..---', '3':'...--', '4':'....-', '5':'.....', '6':'-....', '7':'--...', '8':'---..',
              '9':'----.', ',':'--..--', '.':'.-.-.-', '?':'..--..'}

def morse(start_text):
    text = ""
    for char in start_text:
        if char in morse_code:
            text += morse_code[char]
        else:
            text += char
    print(f"Here's the result:\n{text}")

from art import logo
print(logo)

should_end = False
while not should_end:

    text = input("Type your message:\n").lower()

    morse(start_text=text)

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        should_end = True
        print("Goodbye")
