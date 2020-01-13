from cryptography.fernet import Fernet

class Encryption:
    def __init__(self):
        # declaring a private key for encrypting the text
        self.__key = b'4rP7eTpVcI8Uv_aR-vme4kw_UBNEBAQBZvH-f6QtIj4='
        self.cipher_suite = Fernet(self.__key)

    # takes the string and converts it to bytes and ret
    def encryptText(self, text):
        text = text.encode()
        return self.cipher_suite.encrypt(text)

    def decryptText(self, text):
        return self.cipher_suite.decrypt(text).decode("utf-8")