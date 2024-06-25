from pyqrcode import create
import tkinter as tk
from tkinter import messagebox

# Create the main application window
root = tk.Tk()
root.title('QR Code Generator')
root.geometry('500x500')
root.configure(background='white')

# Define the QR code generation function
def gen_qr():
    input_data = data_entry.get()
    if not input_data.strip():
        messagebox.showwarning("Input Error", "Please enter some data to generate a QR code.")
        return

    qr = create(input_data)
    qr_xbm = qr.xbm(scale=5)
    
    global qr_image
    qr_image = tk.BitmapImage(data=qr_xbm, foreground="blue", background='yellow')
    image_view.config(image=qr_image)
    statement.config(text=f"This is a QR code for: {input_data}")

def clear():
    data_entry.delete(0, tk.END)
    image_view.config(image='')
    statement.config(text='')

# Create and place GUI widgets
heading = tk.Label(root, text="QR Code Generator", font=("Arial", 30), bg='white')
subtitle = tk.Label(root, text="Enter the data:", font=("Arial", 15), bg='white')

data_entry = tk.Entry(root, font=("Arial", 15), width=30, bd=2, relief='solid')

make_button = tk.Button(root, text="Generate QR Code", font=("Arial", 15), command=gen_qr, bg='blue', fg='white', activebackground='lightblue', activeforeground='black')
clear_button = tk.Button(root, text="Clear", font=("Arial", 15), command=clear, bg='red', fg='white', activebackground='lightcoral', activeforeground='black')

image_view = tk.Label(root, bg='white')
statement = tk.Label(root, font=("Arial", 12), bg='white')

# Layout the widgets
heading.pack(pady=20)
subtitle.pack(pady=10)
data_entry.pack(pady=10)
make_button.pack(pady=10)
clear_button.pack(pady=5)
image_view.pack(pady=20)
statement.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()
