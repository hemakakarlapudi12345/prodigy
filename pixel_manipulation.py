import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import numpy as np
import os
def encrypt_image(image_path, key, output_path):
    try:
        img = Image.open(image_path)
        img = img.convert("RGB")  
        img_data = np.array(img)
        encrypted_data = (img_data + key) % 256
        encrypted_img = Image.fromarray(encrypted_data.astype('uint8'), 'RGB')
        encrypted_img.save(output_path)
        display_comparison(image_path, output_path)
        messagebox.showinfo("Success", f"Image encrypted successfully and saved to {output_path}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")
def decrypt_image(image_path, key, output_path):
    try:
        img = Image.open(image_path)
        img = img.convert("RGB")  
        img_data = np.array(img)
        decrypted_data = (img_data - key) % 256
        decrypted_img = Image.fromarray(decrypted_data.astype('uint8'), 'RGB')
        decrypted_img.save(output_path)
        display_comparison(image_path, output_path)
        messagebox.showinfo("Success", f"Image decrypted successfully and saved to {output_path}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")
def display_comparison(original_path, processed_path):
    original_img = Image.open(original_path)
    processed_img = Image.open(processed_path)
    original_img = original_img.resize((300, 300))  
    processed_img = processed_img.resize((300, 300))  
    original_img_tk = ImageTk.PhotoImage(original_img)
    processed_img_tk = ImageTk.PhotoImage(processed_img)
    if not hasattr(display_comparison, "panel_original"):
        display_comparison.panel_original = tk.Label(root, image=original_img_tk)
        display_comparison.panel_original.image = original_img_tk  # Keep reference to the image to prevent garbage collection
        display_comparison.panel_original.grid(row=4, column=0, padx=10, pady=10)
        display_comparison.panel_processed = tk.Label(root, image=processed_img_tk)
        display_comparison.panel_processed.image = processed_img_tk  # Keep reference to the image to prevent garbage collection
        display_comparison.panel_processed.grid(row=4, column=1, padx=10, pady=10)
    else:
        display_comparison.panel_original.configure(image=original_img_tk)
        display_comparison.panel_original.image = original_img_tk
        display_comparison.panel_processed.configure(image=processed_img_tk)
        display_comparison.panel_processed.image = processed_img_tk
def select_image(entry_image_path):
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.bmp")])
    if file_path:
        entry_image_path.delete(0, tk.END)
        entry_image_path.insert(0, file_path)
        display_image(file_path)  
def select_output_path(entry_output_path):
    output_path = filedialog.askdirectory()
    if output_path:
        entry_output_path.delete(0, tk.END)
        entry_output_path.insert(0, output_path)
def display_image(image_path):
    img = Image.open(image_path)
    img = img.resize((300, 300))  
    img_tk = ImageTk.PhotoImage(img)
    if not hasattr(display_image, "panel"):
        display_image.panel = tk.Label(root, image=img_tk)
        display_image.panel.image = img_tk  
        display_image.panel.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
    else:
        display_image.panel.configure(image=img_tk)
        display_image.panel.image = img_tk
def gui_main():
    global root
    root = tk.Tk()
    root.title("Image Encryption/Decryption Tool")
    label_image_path = tk.Label(root, text="Image Path:")
    label_image_path.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)
    entry_image_path = tk.Entry(root, width=50)
    entry_image_path.grid(row=0, column=1, columnspan=2, padx=10, pady=10)
    button_select_image = tk.Button(root, text="Select Image", command=lambda: select_image(entry_image_path))
    button_select_image.grid(row=0, column=3, padx=10, pady=10)
    label_output_path = tk.Label(root, text="Output Path:")
    label_output_path.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)
    entry_output_path = tk.Entry(root, width=50)
    entry_output_path.grid(row=1, column=1, columnspan=2, padx=10, pady=10)
    button_select_output = tk.Button(root, text="Select Output Folder", command=lambda: select_output_path(entry_output_path))
    button_select_output.grid(row=1, column=3, padx=10, pady=10)
    key_label = tk.Label(root, text="Encryption Key:")
    key_label.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)
    entry_key = tk.Entry(root, width=20)
    entry_key.grid(row=2, column=1, padx=10, pady=10)
    button_encrypt = tk.Button(root, text="Encrypt Image", command=lambda: encrypt_image_action(entry_image_path.get(), entry_key.get(), entry_output_path.get()))
    button_encrypt.grid(row=3, column=1, padx=10, pady=10)
    button_decrypt = tk.Button(root, text="Decrypt Image", command=lambda: decrypt_image_action(entry_image_path.get(), entry_key.get(), entry_output_path.get()))
    button_decrypt.grid(row=3, column=2, padx=10, pady=10)
    root.mainloop()
def encrypt_image_action(image_path, key, output_path):
    try:
        key = int(key)  
        if image_path and output_path:
            encrypt_image(image_path, key, os.path.join(output_path, "encrypted_image.png"))
        else:
            messagebox.showerror("Error", "Please select an image and output folder.")
    except ValueError:
        messagebox.showerror("Error", "Encryption key must be an integer.")
def decrypt_image_action(image_path, key, output_path):
    try:
        key = int(key) 
        if image_path and output_path:
            decrypt_image(image_path, key, os.path.join(output_path, "decrypted_image.png"))
        else:
            messagebox.showerror("Error", "Please select an image and output folder.")
    except ValueError:
        messagebox.showerror("Error", "Decryption key must be an integer.")