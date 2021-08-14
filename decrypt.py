from fernet import Fernet


def load_Key():
    return open("secret.key", "rb").read()


def decrypt_Message(encrypted_Message):
    key = load_Key()
    f = Fernet(key)
    decrypted_Message = f.decrypt(encrypted_Message)
    print(decrypted_Message.decode())
