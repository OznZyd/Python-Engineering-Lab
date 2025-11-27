from tkinter import *
from tkinter import messagebox
from cryptography.fernet import Fernet, InvalidToken
import hashlib
import base64


def save_and_encrypt():
    title_str = entry1.get()
    master_key_str = entry2.get()
    secret_str = text1.get("1.0", END)

    if len(title_str) == 0:
        messagebox.showerror(title="Error!", message= "Please enter the title")
    elif len(master_key_str) == 0:
        messagebox.showerror(title="Error!", message="Please enter the password")
    elif len(secret_str) == 0:
        messagebox.showerror(title="Error", message="Please enter the Secret Text")
    else:
        password_bytes = master_key_str.encode('utf-8')
        hashed_password = hashlib.sha256(password_bytes).digest()
        fernet_key = base64.urlsafe_b64encode(hashed_password)
        cipher_suite = Fernet(fernet_key)
        encrypted_secret = cipher_suite.encrypt(secret_str.encode('utf-8'))

        with open ("cipherText", "a") as f:
            f.write(title_str + "\n")
            f.write(encrypted_secret.decode('utf-8' ) + "\n")

    entry1.delete(0, END)
    entry2.delete(0, END)
    text1.delete("1.0", END)



def decrypt():
    title_str = entry1.get()
    master_key_str = entry2.get()

    if len(title_str) == 0 or len(master_key_str) == 0:
        messagebox.showerror(title= "Error!", message="The field cannot be empty!")
    else:
        with open ("cipherText", "r") as f:
            file_lines = f.readlines()

            title_found = False

            for index, line in enumerate(file_lines):
                if title_str == line.strip():
                    try:
                        encrypted_text_from_file = file_lines[index + 1]
                        password_bytes = master_key_str.encode('utf-8')
                        hashed_password = hashlib.sha256(password_bytes).digest()
                        fernet_key = base64.urlsafe_b64encode(hashed_password)
                        cipher_suite = Fernet(fernet_key)
                        decrypted_secret = cipher_suite.decrypt(encrypted_text_from_file.strip().encode('utf-8')).decode('utf-8')
                        text1.delete("1.0", END)
                        text1.insert("1.0", decrypted_secret)
                        title_found = True
                    except InvalidToken:
                        messagebox.showerror(title="Error!", message= "Wrong password key! Please Try again!")
            if not title_found:
                messagebox.showerror(title="Error!", message= "Wrong Title! Please Try again")




secretNote = Tk()
secretNote.title("Cipher Note")
secretNote.config(padx=10, pady=10)

photoImage = PhotoImage(file= "topSecretIcon.png")

logoLabel = Label(secretNote, image= photoImage )
logoLabel.pack()


logoLabel.image = photoImage

label1 = Label(secretNote, text="Enter your title")
label1.pack()

entry1 = Entry(secretNote, width= 20)
entry1.pack()

label2 = Label(secretNote, text="Enter your secret note!")
label2.pack()

text1 = Text(secretNote, width=30, height=10)
text1.pack()

label3 = Label(secretNote, text="Enter your Password")
label3.pack()

entry2 = Entry(secretNote, width= 20, show="*")
entry2.pack()

button1 = Button(secretNote, text="Save & Encrypt", command=save_and_encrypt)
button1.pack()

button2 = Button(secretNote, text="Decrypt", command=decrypt)
button2.pack()


secretNote.mainloop()