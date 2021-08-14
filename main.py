from encrypt import generate_Key, encrypt_Message
from decrypt import decrypt_Message


def encrypt():
    generate_Key()
    print("What would you like to encrypt?")
    message = input()
    encrypted_Message = encrypt_Message(message)
    return encrypted_Message


def decrypt(encrypted_Message):
    decrypt_Message(encrypted_Message)


def main():
    encrypted_Message = ''
    while True:
        print("- encrypt\n- decrypt")
        choice = input('>')
        if choice.lower() == "encrypt":
            encrypted_Message = encrypt()
        elif choice.lower() == "decrypt":
            decrypt(encrypted_Message)
        else:
            exit()


if __name__ == '__main__':
    main()
