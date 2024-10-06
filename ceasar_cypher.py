try:
    import pyperclip #for copying text to the clipboard
except ImportError:
    pass

#Symbols used for decryption/ encryption:
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

print('''The Caesar cipher encrypts letters by shifting them over by a  key number.
         For example, a key of 2 means the letter A is encrypted into C,
         the letter B encrytped into D, and so on.''')
print()

#Let the user enter if they are encrypting or decrypting:
while True: #keep asking until user enters either 'e' or 'd'.
    print('Do you want to (e)ncrypt or (d)ecrypt?')
    response = input('> ')
    if response.startswith('e'):
        mode = 'encrypt'
        break
    elif response.startswith('d'):
        mode = 'decrypt'
        break
    else:#else for clarity but can leave out the else
        print('Please enter the letter "e" or "d". ')

#Let the user enter the key to use:
while True:#Keep asking until user enters valid key.
    maxKey = len(SYMBOLS) -1 #otherwise to shift would take place
    print('Please enter the key (0 to {}) to use.'.format(maxKey))
    response = input('> ').upper() 
    if not response.isdecimal():#check that key is not a decimal number
        continue

    if 0 <= int(response) <=len(SYMBOLS):
        key = int(response)
        break

#Let the user enter message they wish encrypted or decrypted
print('Enter your message to {}.'.format(mode))
message = input('> ')

#Ceasar cipher works only on uppercase letters
message = message.upper()

#Stores the encrypted/decrypted version of the message:
translated = ''

#Encrypt/ decrypt each symbol in the message:
for symbol in message:
    if symbol in SYMBOLS:
        #get encypted or decrypted number for this symbol
        num = SYMBOLS.find(symbol) #get the number for the symbol
        if mode == 'encrypt':
            num = num + key
        elif mode == 'decrypt':
            num = num - key
        #Handle te wrap-around if num is larger than the length of SYMBOLS
        #or less than 0
        if num >= len(SYMBOLS):
            num = num - len(SYMBOLS)
        if num < 0:
            num = num + len(SYMBOLS)

        # Add ecrypted/decrypted number's symbol to translated:
        translated = translated + SYMBOLS[num]
    else:
        #Add the symbool without encrypting/ decrypting:
        translated = translated + symbol

# Display the encrypted/ decrypted string to the screen:
print(translated)

try:
    pyperclip.copy(translated)
    print('Full {}ed text copied to clipboard.'.format(mode))
except:
    pass #Do nothing if pyperclip is not installed




