import tkinter as tk
import random
import string

def generate_password():
    chars = string.ascii_letters + string.digits + string.punctuation
    pwd = "".join(random.choice(chars) for _ in range(12))
    result.set(pwd)

def copy_password():
    root.clipboard_clear()
    root.clipboard_append(result.get())
    msg.set("Password Copied ✔")


root = tk.Tk()
root.title("🔐 Strong Password Generator")
root.geometry("400x250")
root.configure(bg="#e3f2fd")  


tk.Label(root, text="🔐 Strong Password Generator",
         font=("Arial", 16, "bold"), bg="#e3f2fd", fg="#0d47a1").pack(pady=15)

frame = tk.Frame(root, bg="#bbdefb", bd=3, relief="ridge")
frame.pack(pady=10, padx=20, fill="x")


tk.Button(frame, text="Generate Password", command=generate_password,
          bg="#1e88e5", fg="white", font=("Arial", 12, "bold"), width=20).pack(pady=10)


result = tk.StringVar()
tk.Entry(frame, textvariable=result, font=("Arial", 14), justify="center").pack(pady=5)


tk.Button(frame, text="Copy", command=copy_password,
          bg="#43a047", fg="white", font=("Arial", 12, "bold"), width=10).pack(pady=10)


msg = tk.StringVar()
tk.Label(root, textvariable=msg, bg="#e3f2fd", fg="#1b5e20",
         font=("Arial", 12, "bold")).pack(pady=5)

root.mainloop()