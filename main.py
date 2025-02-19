import cv2
import os
import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog

# Function to select an image file
def select_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.png;*.bmp")])
    if file_path:
        entry_img_path.delete(0, tk.END)
        entry_img_path.insert(0, file_path)

# Function to encrypt the message into the image
def encrypt():
    img_path = entry_img_path.get()
    if not img_path:
        messagebox.showerror("Error", "Please select an image")
        return

    img = cv2.imread(img_path)
    if img is None:
        messagebox.showerror("Error", "Invalid image file")
        return

    msg = simpledialog.askstring("Input", "Enter secret message:")
    password = simpledialog.askstring("Input", "Enter a passcode:", show="*")

    d = {chr(i): i for i in range(255)}
    
    m, n, z = 0, 0, 0
    for char in msg:
        img[n, m, z] = d[char]
        n += 1
        m += 1
        z = (z + 1) % 3

    cv2.imwrite("encryptedImage.jpg", img)
    os.system("start encryptedImage.jpg")
    messagebox.showinfo("Success", "Message encrypted successfully!")

    # Save the password for later decryption
    global stored_password
    stored_password = password

# Function to decrypt the message
def decrypt():
    img_path = entry_img_path.get()
    if not img_path:
        messagebox.showerror("Error", "Please select an image")
        return

    img = cv2.imread("encryptedImage.jpg")
    if img is None:
        messagebox.showerror("Error", "Encrypted image not found")
        return

    pas = simpledialog.askstring("Input", "Enter passcode for decryption:", show="*")
    
    if pas == stored_password:
        c = {i: chr(i) for i in range(255)}
        m, n, z = 0, 0, 0
        message = ""

        for i in range(len(msg)):
            message += c[img[n, m, z]]
            n += 1
            m += 1
            z = (z + 1) % 3

        messagebox.showinfo("Decrypted Message", f"Message: {message}")
    else:
        messagebox.showerror("Error", "Incorrect passcode!")

# GUI Setup
root = tk.Tk()
root.title("Image Steganography")
root.geometry("400x300")

tk.Label(root, text="Select Image:").pack()
entry_img_path = tk.Entry(root, width=40)
entry_img_path.pack()
tk.Button(root, text="Browse", command=select_image).pack()

tk.Button(root, text="Encrypt Message", command=encrypt, bg="lightblue").pack(pady=5)
tk.Button(root, text="Decrypt Message", command=decrypt, bg="lightgreen").pack(pady=5)

root.mainloop()
