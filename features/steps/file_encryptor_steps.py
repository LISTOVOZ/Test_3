import os
from behave import given, when, then
from file_encryptorBDD import FileEncryptor

@given('папка "{folder}" содержит файлы')
def step_given_folder_contains_files(context, folder):
    context.folder = folder
    os.makedirs(folder, exist_ok=True)
    context.test_file_path = os.path.join(folder, 'test_file.txt')
    with open(context.test_file_path, 'w') as f:
        f.write("Hello World")

@given('папка "{folder}" содержит зашифрованные файлы методом "{method}" с ключом "{key}"')
def step_given_folder_contains_encrypted_files(context, folder, method, key):
    step_given_folder_contains_files(context, folder)
    encryptor = FileEncryptor(folder)
    encryptor.encrypt_files(method=method, key=key)

@when('пользователь шифрует все файлы методом "{method}" с ключом "{key}"')
def step_when_user_encrypts_files(context, method, key):
    encryptor = FileEncryptor(context.folder)
    encryptor.encrypt_files(method=method, key=key)

@when('пользователь дешифрует все файлы методом "{method}" с ключом "{key}"')
def step_when_user_decrypts_files(context, method, key):
    encryptor = FileEncryptor(context.folder)
    encryptor.decrypt_files(method=method, key=key)

@then('все файлы в папке должны быть зашифрованы')
def step_then_files_should_be_encrypted(context):
    with open(context.test_file_path, 'r') as f:
        content = f.read()
    assert content != "Hello World", "Файлы не зашифрованы"

@then('все файлы в папке должны быть расшифрованы')
def step_then_files_should_be_decrypted(context):
    with open(context.test_file_path, 'r') as f:
        content = f.read()
    assert content == "Hello World", "Файлы не расшифрованы"

#behave