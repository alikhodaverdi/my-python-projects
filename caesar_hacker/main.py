
print("Enter the encrypted caesar cipher message to hack.")

message = input("> ")
# Ket the user specify  the message to hack:

print("Enter the encrypterd Caesar  cipher message to hack")
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


for key in range(len(SYMBOLS)):  # Loop through  every possible key.
    translated = ""

    # Decrypt each symbol in the message

    for symbol in message:

        if symbol in SYMBOLS:
            num = SYMBOLS.find(symbol)
            num = num - key

            # Handle the warp-around if num is lesss than 0:

            if num < 0:
                num = num+len(symbol)

                # Add decrypted number's symbol  to translated:

                translated = translated + SYMBOLS[num]
            else:
                translated = translated + symbol


print("Key #{}:{}".format(key, translated))
