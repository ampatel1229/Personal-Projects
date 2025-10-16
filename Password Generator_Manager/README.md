This project is a two-part secure password management system that combines password generation, encryption, and storage to help users manage their credentials safely and conveniently.

The first script, password_gen.py, generates strong, random passwords using uppercase and lowercase letters, numbers, and special characters. The user specifies the desired password length, and the program instantly produces a secure password ready for use.

The second script, password_manager.py, serves as a local encrypted password vault. It uses the cryptography.fernet library to encrypt and decrypt passwords stored in a text file (password.txt). The system relies on a master key file (key.key) for encryption, ensuring that even if the password file is accessed, the data remains unreadable without the key. Users can add new account credentials or view existing ones via simple console commands.
