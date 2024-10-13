import unittest
import os
from file_encryptorTDD import FileEncryptor  # Это класс, который мы будем реализовывать

class TestFileEncryptor(unittest.TestCase):

    def setUp(self):
        # Создаем тестовую папку и файлы для тестов
        self.test_dir = 'test_folder'
        os.makedirs(self.test_dir, exist_ok=True)
        self.test_file_path = os.path.join(self.test_dir, 'test_file.txt')
        with open(self.test_file_path, 'w') as f:
            f.write("Hello World")

    def tearDown(self):
        # Удаляем тестовые файлы и папку после каждого теста
        if os.path.exists(self.test_file_path):
            os.remove(self.test_file_path)
        if os.path.exists(self.test_dir):
            os.rmdir(self.test_dir)

    def test_encrypt_xor(self):
        # Тестируем шифрование методом XOR
        encryptor = FileEncryptor(self.test_dir)
        encryptor.encrypt_files(method='xor', key='my_secret_key')
        with open(self.test_file_path, 'r') as f:
            content = f.read()
        self.assertNotEqual(content, "Hello World")  # Проверяем, что файл зашифрован

    def test_decrypt_xor(self):
        # Тестируем дешифрование методом XOR
        encryptor = FileEncryptor(self.test_dir)
        encryptor.encrypt_files(method='xor', key='my_secret_key')
        encryptor.decrypt_files(method='xor', key='my_secret_key')
        with open(self.test_file_path, 'r') as f:
            content = f.read()
        self.assertEqual(content, "Hello World")  # Проверяем, что файл расшифрован

    def test_encrypt_caesar(self):
        # Тестируем шифрование методом Цезаря
        encryptor = FileEncryptor(self.test_dir)
        encryptor.encrypt_files(method='caesar', key=3)
        with open(self.test_file_path, 'r') as f:
            content = f.read()
        self.assertNotEqual(content, "Hello World")  # Проверяем, что файл зашифрован

    def test_decrypt_caesar(self):
        # Тестируем дешифрование методом Цезаря
        encryptor = FileEncryptor(self.test_dir)
        encryptor.encrypt_files(method='caesar', key=3)
        encryptor.decrypt_files(method='caesar', key=3)
        with open(self.test_file_path, 'r') as f:
            content = f.read()
        self.assertEqual(content, "Hello World")  # Проверяем, что файл расшифрован

if __name__ == '__main__':
    unittest.main()