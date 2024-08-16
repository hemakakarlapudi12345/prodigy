from tkinter import *
from tkinter import messagebox

def GUI():
    master = Tk()
    master.geometry("800x600")

    # Title
    master.title("Caesar Cipher")

    # Header frame
    header_frame = Frame(master, bg="#2E8B57")
    header_frame.pack(fill=X)

    header_label = Label(header_frame, text="CAESAR CIPHER", font=("Helvetica", 24), bg="#2E8B57", fg="white")
    header_label.pack(pady=10)

    # Main frame
    main_frame = Frame(master, bg="white")
    main_frame.pack(pady=20)

    # Message label and text field
    text_label = Label(main_frame, text="What do you want to cipher?", font=("Helvetica", 14), bg="white", fg="blue")
    text_label.pack(pady=10)
    
    text_field = Text(main_frame, height=10, width=80, bg="cadetblue1", fg="red", font=("Helvetica", 12))
    text_field.pack(pady=10)

    # Shift label and slider
    key_label = Label(main_frame, text="SHIFT BY:", font=("Helvetica", 14), bg="white", fg="blue")
    key_label.pack(pady=10)

    key_slider = Scale(main_frame, from_=1, to=25, orient=HORIZONTAL, length=600, fg="red", font=("Helvetica", 12))
    key_slider.pack(pady=10)

    # Function definitions
    alpha = [chr(i) for i in range(97, 123)]
    alpha_upper = [chr(i) for i in range(65, 91)]

    def set_temp():
        text = text_field.get("1.0", "end-1c").strip()
        shift = key_slider.get()
        if not text:
            messagebox.showwarning("Input Error", "Please enter some text to cipher or decipher.")
        return text, shift

    def allow_to_paste(string):
        master.clipboard_clear()
        master.clipboard_append(string)

    def cipher():
        inf, shift = set_temp()
        if not inf:
            return  # Exit if no text is provided

        cipher_lower = dict(zip(alpha, [chr((ord(i) - 97 + shift) % 26 + 97) for i in alpha]))
        cipher_upper = dict(zip(alpha_upper, [chr((ord(i) - 65 + shift) % 26 + 65) for i in alpha_upper]))

        r = append(inf, cipher_upper, cipher_lower)
        result.set(r)
        allow_to_paste(r)

    def append(info, cu, cl):
        c = []
        for i in info:
            if i in alpha_upper:
                c.append(cu[i])
            elif i in alpha:
                c.append(cl[i])
            else:
                c.append(i)
        return "".join(c)

    def decipher():
        inf, shift = set_temp()
        if not inf:
            return  # Exit if no text is provided

        decipher_lower = dict(zip(alpha, [chr((ord(i) - 97 - shift) % 26 + 97) for i in alpha]))
        decipher_upper = dict(zip(alpha_upper, [chr((ord(i) - 65 - shift) % 26 + 65) for i in alpha_upper]))

        r = append(inf, decipher_upper, decipher_lower)
        result.set(r)
        allow_to_paste(r)

    # Buttons for encryption and decryption
    button_frame = Frame(main_frame, bg="white")
    button_frame.pack(pady=20)

    encrypt_button = Button(button_frame, text="ENCRYPT", command=cipher, font=("Helvetica", 14), bg="blue", fg="yellow", width=15)
    encrypt_button.grid(row=0, column=0, padx=10)

    decrypt_button = Button(button_frame, text="DECRYPT", command=decipher, font=("Helvetica", 14), bg="yellow", fg="blue", width=15)
    decrypt_button.grid(row=0, column=1, padx=10)

    # Result label and entry field
    result = StringVar()
    result.set("Ciphered/Deciphered text")
    result_label = Entry(main_frame, textvariable=result, bg="yellow", fg="red", font=("Helvetica", 12), width=80)
    result_label.pack(pady=10)

    master.mainloop()

# Running the GUI
if __name__ == "__main__":
    GUI()