# William Burbatt
# 4/30/2019
# ACSG-470
# Week 12 Problem


# Creates a 5x5 table filled with *
def init_table(table):
    for i in range(5):
        newRow = []
        for j in range(5):
            newRow.append("*")
        table.append(newRow)


# Prints table row by row
def print_table(table):
    for row in table:
        print(row)


# Checks for specific elements in a table
def table_has(letter):
    for row in table:
        for elem in row:
            if (elem == letter):
                return True
    return False


# Cleans the secret key by removing whitespace, lowercase letters, and the letter J
def clean_key(key):
    key = key.upper()
    key = key.replace(" ", "")
    newString = ""
    for letter in key:
        if (letter == "J"):
            newString += "I"
        else:
            newString += letter
    return newString


# Sets the actual letter values in the table instead of *
def set_cell(letter):
    for i in range(5):
        for j in range(5):
            if (table[i][j] == "*"):
                table[i][j] = letter
                return


# Fills the table with the rest of the placeholder values
def create_table(key):
    tempLetters = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    init_table(table)
    cleanKey = clean_key(key)
    for letter in cleanKey:
        if (table_has(letter) == False):
            set_cell(letter)
    for letter in tempLetters:
        if (table_has(letter) == False):
            set_cell(letter)


# Finds the row and column of the inputted letter
def find_letter(letter):
    for i in range(5):
        for j in range(5):
            if (table[i][j] == letter):
                return str(i) + str(j)


# Removes all lowercase letters, whitespace, j, checks for duplicate letters, and if the result is odd
def clean_plaintext(plaintext):
    plaintext = plaintext.upper()
    plaintext = plaintext.replace(" ", "")
    plaintext = check_j(plaintext)
    plaintext = check_duplicates(plaintext)
    plaintext = check_odd(plaintext)
    return plaintext


# Removes all occurences of the letter j
def check_j(oldString):
    newString = ""
    strLen = len(oldString)
    for i in range(strLen):
        letter = oldString[i]
        if (letter == "J"):
            newString = newString + "I"
        else:
            newString = newString + letter
    return newString


# Adds an X in between duplicatre
def check_duplicates(oldString):
    newString = ""
    prev = ""
    strLen = len(oldString)
    for i in range(strLen):
        letter = oldString[i]
        if (letter == prev):
            if (letter == "X"):
                newString = newString + "Q" + letter
            else:
                newString = newString + "X" + letter
        else:
            newString = newString + letter
        prev = letter
    return newString


# Checks if the number is odd and if it is add a Z or a Q
def check_odd(oldString):
    strLen = len(oldString)
    if (strLen % 2 != 0):
        if (oldString[strLen - 1] == "Z"):
            oldString = oldString + "Q"
        else:
            oldString = oldString + "Z"

    return oldString


# Encodes based on the different encodings of the cipher
def encode_pair(a, b):
    locA = find_letter(a)
    rowA = locA[0]
    colA = locA[1]

    locB = find_letter(b)
    rowB = locB[0]
    colB = locB[1]
    result = ""
    if (rowA == rowB):
        result = encrypt_same_row(locA, locB)
    elif (colA == colB):
        result = encrypt_same_column(locA, locB)
    else:
        result = encrypt_rectangle(locA, locB)

    return result


# If they are in the same row, shift to the right.
def encrypt_same_row(a, b):
    row = int(a[0])
    aCol = int(a[1])
    bCol = int(b[1])

    newACol = (aCol + 1) % 5
    newBCol = (bCol + 1) % 5

    newA = table[row][newACol]
    newB = table[row][newBCol]
    result = "" + newA + newB
    return result


# If they are in the same column, shift down.
def encrypt_same_column(a, b):
    col = int(a[1])
    aRow = int(a[0])
    bRow = int(b[0])

    newARow = (aRow + 1) % 5
    newBRow = (bRow + 1) % 5

    newA = table[newARow][col]
    newB = table[newBRow][col]
    result = "" + newA + newB
    return result


# If they are neither, make a rectangle and swap corners
def encrypt_rectangle(a, b):
    aRow = int(a[0])
    aCol = int(a[1])
    bRow = int(b[0])
    bCol = int(b[1])

    newA = table[aRow][bCol]
    newB = table[bRow][aCol]
    result = "" + newA + newB
    return result


# Starts the encryption process by going in pairs of letters.
def encryption_actual(plaintext):
    encryptedMessage = ""
    strLen = len(plaintext)
    for i in range(0, strLen, 2):
        first = plaintext[i]
        second = plaintext[i + 1]
        encryptedMessage = encryptedMessage + encode_pair(first, second)

    encryptedMessage = format_encrypted_message(encryptedMessage)
    return encryptedMessage


# Adds a space between every 5th letter
def format_encrypted_message(message):
    newMessage = ""
    for i in range(len(message)):
        if (i % 5 == 0):
            newMessage += " "
        newMessage += message[i]

    return newMessage


# Starts decryption process
def decrypt(key, ciphertext):
    ciphertext = format_ciphertext(ciphertext)
    decryptedMessage = ""
    strLen = len(ciphertext)
    for i in range(0, strLen, 2):
        first = ciphertext[i]
        second = ciphertext[i + 1]
        decryptedMessage = decryptedMessage + decode_pairs(first, second)

    return decryptedMessage


# Formats ciphertext for decryption by removing spaces
def format_ciphertext(ciphertext):
    newText = ciphertext.replace(" ", "")
    return newText


# Decodes based on encryption type
def decode_pairs(a, b):
    locA = find_letter(a)
    rowA = locA[0]
    colA = locA[1]
    locB = find_letter(b)
    rowB = locB[0]
    colB = locB[1]
    result = ""
    if (rowA == rowB):
        result = decrypt_same_row(locA, locB)
    elif (colA == colB):
        result = decrypt_same_column(locA, locB)
    else:
        result = encrypt_rectangle(locA, locB)

    return result


# If they are in the same row, shift to the left.
def decrypt_same_row(a, b):
    row = int(a[0])
    aCol = int(a[1])
    bCol = int(b[1])

    newACol = (aCol - 1)
    if (newACol == -1):
        newACol = 4
    newBCol = (bCol - 1)
    if (newBCol == -1):
        newBCol = 4

    newA = table[row][newACol]
    newB = table[row][newBCol]
    result = "" + newA + newB
    return result


# If they are in the same col, shift up.
def decrypt_same_column(a, b):
    col = int(a[1])
    aRow = int(a[0])
    bRow = int(b[0])

    newARow = (aRow - 1)
    if (newARow == -1):
        newARow = 4

    newBRow = (bRow + 1) % 5
    if (newBRow == -1):
        newBRow = 4

    newA = table[newARow][col]
    newB = table[newBRow][col]
    result = "" + newA + newB
    return result


# Rable is global so all methods can access
table = []


# Sets and prints table, calls to encryption and decryption
def encrypt(key, plaintext):
    print("Prompt for key")
    print("Key: ", key)
    print("Prompt for plaintext")
    print("Plaintext: ", plaintext)

    create_table(key)

    print_table(table)

    cleanPlaintext = clean_plaintext(plaintext)

    print("Cleaned plaintext: ", cleanPlaintext)

    encryptedMessage = encryption_actual(cleanPlaintext)

    print("Encrypted Message Is: ", encryptedMessage)

    decryptedMessage = decrypt(key, encryptedMessage)
    print(decryptedMessage)
