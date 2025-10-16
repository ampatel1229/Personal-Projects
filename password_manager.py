from cryptography.fernet import Fernet 

'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

wb = write bytes
rb = read bytes
'''

#write_key() - writes the key itself

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

master_pwd = input("What is the master password? ")
key = load_key() #master_pwd.encode()
fer = Fernet(key)


def view():
    with open("password.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User: ", user, "| Password: ", fer.decrypt(passw.encode()).decode())


#What .split() does - everytime | is seen, a list is created with things before and after the |
#Ex. 
# "hello | aman" 
# user, passw = ["hello" , "aman"]

def add():
    name = input("Account Username: ")
    pwd = input("Account Password: ")
    encrypt_pwd = fer.encrypt(pwd.encode()).decode()

    with open("password.txt", "a") as f: #a(most flexible) - appead(add to the end of the file and create new file if not found); w - write a new file(override file if alr exisiting); r - read the file(cannot create/rewrite the file)
        f.write(name + " | " + encrypt_pwd + "\n")
        print("x")
    
    print("Saved: " + name + " | " + encrypt_pwd)

'''
b'hello' = byte string
'hello' = normal string

'''

while True:

    mode = input("Would you like to view(type view) or add(type add) a password? ")
    if mode == "q":
        break
    elif mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid response.")
        continue