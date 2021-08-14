from fernet import Fernet


def generate_Key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_File:
        key_File.write(key)


def load_Key():
    return open("secret.key", "rb").read()


def encrypt_Message(message):
    key = load_Key()
    encoded_Message = message.encode()
    f = Fernet(key)
    encrypted_Message = f.encrypt(encoded_Message)
    print(encrypted_Message)
    return encrypted_Message
