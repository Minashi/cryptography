from encrypt import generate_Key, encrypt_Message
from decrypt import decrypt_Message


def encrypt():
    generate_Key()
    print("What would you like to encrypt?")
    message = input()
    encrypt_Message(message)


def decrypt():
    decrypt_Message(b'gAAAAABhGBtBeFEPA0xKXRuHvD_Mhew72YGI3N_CCKJCbNQXIm4Ez4cthwI0oUhfBpe-tsYUosUyhEXLYtiefKl_fvDBl74NLw==')


def main():
    while True:
        print("- encrypt\n- decrypt")
        choice = input('>')
        if choice.lower() == "encrypt":
            encrypt()
        elif choice.lower() == "decrypt":
            decrypt()
        else:
            exit()


if __name__ == '__main__':
    main()
