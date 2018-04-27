

def DoubleTranspition(key, message):
    text = [''] * key

    for col in range(key):
        newColumn = col

        while newColumn < len(message):
            text[col] += message[newColumn]
            newColumn += key

        return ''.join(text)

OrgMessage = input("Please enter your message for encryption: ")
key = int(input("Please enter encryption key: "))

encrypted = DoubleTranspition(key, OrgMessage)
print(encrypted)
