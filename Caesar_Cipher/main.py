
import pyperclip
SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

print("Caeser Cipher, by mehrdad ")
print("The Caesar cipher encrypts letters by shifting them over by a")
print('key number. For example, a key of 2 means the letter A is')
print("encrypted into C, the letter B encrypted into D, and so on")
print()


while True:
    print("Do you want to (e)ncrypt or (d)ecrypt ?")
    response = input("> ").lower()
    if response.startswith("e"):
        mode = "encrypt"
        break
    elif response.startswith("d"):
        mode = "decrypt"
        break
    print("Please enter the letter e or d")


# let the user enter the key to use:
while True:
    maxKey = len(SYMBOLS) - 1
    print("Please enter the key(0 to {}) to use".format(maxKey))
    response = input("> ").upper()

    if not response.isdecimal():
        continue

    if 0 <= int(response) < len(SYMBOLS):
        key = int(response)
        break

# let the user enteer the message to encrypt/decrypt
print("Enter the message to {}".format(mode))
message = input("> ")
message = message.upper()

# Stores  the encrypted/decrypted form of the message
translated = ""

# Enctypy/decrypt each symbol in the message

for symbol in message:
    if symbol in SYMBOLS:
        num = SYMBOLS.find(symbol)
        if mode == "encrypt":
            num = num + key
        elif mode == "decrypt":
            num = num - key
        # Handle the wrap-around if num is larger than the lenght of

        # Symbols or less than 0
        if num >= len(SYMBOLS):
            num = num - len(SYMBOLS)
        elif num < 0:
            num = num + len(SYMBOLS)

        # Add encrypted/decrypted numbers symbol to translated:
        translated = translated + SYMBOLS[num]
    else:
        translated = translated + symbol

# Display the encrypted/decrypted string to the screen:
print(translated)
