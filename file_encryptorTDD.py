import os

class FileEncryptor:
    def __init__(self, folder_path):
        self.folder_path = folder_path

    def encrypt_files(self, method='xor', key=None):
        for filename in os.listdir(self.folder_path):
            file_path = os.path.join(self.folder_path, filename)
            if os.path.isfile(file_path):
                with open(file_path, 'r') as f:
                    content = f.read()

                if method == 'xor':
                    encrypted_content = self.xor_encrypt(content, key)
                elif method == 'caesar':
                    encrypted_content = self.caesar_encrypt(content, key)

                with open(file_path, 'w') as f:
                    f.write(encrypted_content)

    def decrypt_files(self, method='xor', key=None):
        for filename in os.listdir(self.folder_path):
            file_path = os.path.join(self.folder_path, filename)
            if os.path.isfile(file_path):
                with open(file_path, 'r') as f:
                    content = f.read()

                if method == 'xor':
                    decrypted_content = self.xor_encrypt(content, key)  # XOR обратно так же
                elif method == 'caesar':
                    decrypted_content = self.caesar_decrypt(content, key)

                with open(file_path, 'w') as f:
                    f.write(decrypted_content)

    def xor_encrypt(self, text, key):
        key = (key * (len(text) // len(key))) + key[:len(text) % len(key)]
        return ''.join(chr(ord(c) ^ ord(k)) for c, k in zip(text, key))

    def caesar_encrypt(self, text, shift):
        encrypted = ''
        for char in text:
            if char.isalpha():
                shift_mod = shift % 26
                new_char = chr(((ord(char.lower()) - ord('a') + shift_mod) % 26) + ord('a'))
                encrypted += new_char.upper() if char.isupper() else new_char
            else:
                encrypted += char
        return encrypted

    def caesar_decrypt(self, text, shift):
        return self.caesar_encrypt(text, -shift)  # Обратный сдвиг

if __name__ == '__main__':
    folder = input("Введите путь к папке: ")
    method = input("Введите метод шифрования (xor/caesar): ")
    key = input("Введите ключ для шифрования (число для caesar или строка для xor): ")

    encryptor = FileEncryptor(folder)
    encryptor.encrypt_files(method, key)
    print(f"Файлы в папке {folder} зашифрованы методом {method}.")