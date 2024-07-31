import tkinter as tk
import random
import string
def generate_password():
    length = int(length_entry.get())
    characters = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    result_label.config(text=f"The generated password is: {password}")
root = tk.Tk()
root.title("Password Generator")
length_label = tk.Label(root, text="Enter the password length:")
length_label.pack(pady=5)
length_entry = tk.Entry(root)
length_entry.pack(pady=5)
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)
result_label = tk.Label(root, text="")
result_label.pack(pady=5)
root.mainloop()