import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import cv2
import numpy as np

# Create the main window
window = tk.Tk()
window.geometry("1000x700")
window.title("Image Encryption Decryption")

# Global variables
file_path = None
image_original = None
image_encrypted = None
encryption_key = None

def open_file():
    global file_path, image_original
    file_path = filedialog.askopenfilename(title='Open', filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
    if file_path:
        image_original = Image.open(file_path)
        display_image(image_original, original_label)
    else:
        messagebox.showwarning("Warning", "No image selected.")

def display_image(image, label):
    image.thumbnail((400, 400))
    img = ImageTk.PhotoImage(image)
    label.configure(image=img)
    label.image = img

def encrypt_image():
    global image_encrypted, encryption_key
    if image_original:
        np_image = np.array(image_original.convert('L'))
        np_image = np_image.astype(float) / 255.0
        mu, sigma = 0, 0.1
        encryption_key = np.random.normal(mu, sigma, np_image.shape) + np.finfo(float).eps
        image_encrypted = np_image / encryption_key
        encrypted_image = Image.fromarray((image_encrypted * 255).astype(np.uint8))
        display_image(encrypted_image, processed_label)
        messagebox.showinfo("Encrypt Status", "Image encrypted successfully.")
    else:
        messagebox.showwarning("Warning", "No image to encrypt.")

def decrypt_image():
    if image_encrypted is not None and encryption_key is not None:
        decrypted_image = image_encrypted * encryption_key
        decrypted_image = Image.fromarray((decrypted_image * 255).astype(np.uint8))
        display_image(decrypted_image, processed_label)
        messagebox.showinfo("Decrypt Status", "Image decrypted successfully.")
    else:
        messagebox.showwarning("Warning", "No image to decrypt.")

def save_image():
    if image_encrypted is not None:
        filename = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG files", "*.jpg")])
        if filename:
            encrypted_image = Image.fromarray((image_encrypted * 255).astype(np.uint8))
            encrypted_image.save(filename)
            messagebox.showinfo("Success", "Image saved successfully.")
    else:
        messagebox.showwarning("Warning", "No image to save.")

def reset():
    global image_encrypted, encryption_key
    if image_original:
        display_image(image_original, processed_label)
        image_encrypted = None
        encryption_key = None
        messagebox.showinfo("Reset", "Image reset to original.")
    else:
        messagebox.showwarning("Warning", "No image to reset.")

def exit_app():
    if messagebox.askokcancel("Exit", "Do you want to exit?"):
        window.destroy()

# UI Elements
original_label = tk.Label(window)
original_label.pack(side="left", padx=10, pady=10)

processed_label = tk.Label(window)
processed_label.pack(side="right", padx=10, pady=10)

choose_button = tk.Button(window, text="Choose File", command=open_file, font=("Arial", 20), bg="orange", fg="blue", borderwidth=3, relief="raised")
choose_button.pack(pady=10)

encrypt_button = tk.Button(window, text="Encrypt", command=encrypt_image, font=("Arial", 20), bg="light green", fg="blue", borderwidth=3, relief="raised")
encrypt_button.pack(pady=10)

decrypt_button = tk.Button(window, text="Decrypt", command=decrypt_image, font=("Arial", 20), bg="orange", fg="blue", borderwidth=3, relief="raised")
decrypt_button.pack(pady=10)

reset_button = tk.Button(window, text="Reset", command=reset, font=("Arial", 20), bg="yellow", fg="blue", borderwidth=3, relief="raised")
reset_button.pack(pady=10)

save_button = tk.Button(window, text="Save Image", command=save_image, font=("Arial", 20), bg="orange", fg="blue", borderwidth=3, relief="raised")
save_button.pack(pady=10)

exit_button = tk.Button(window, text="EXIT", command=exit_app, font=("Arial", 20), bg="red", fg="blue", borderwidth=3, relief="raised")
exit_button.pack(pady=10)

window.protocol("WM_DELETE_WINDOW", exit_app)
window.mainloop()
