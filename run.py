import tkinter as tk
from tkinter import messagebox
from urllib.parse import quote, unquote


# Function to encode the URL
def encode_url():
    input_text = url_input.get("1.0", tk.END).strip()
    if input_text:
        encoded_text = quote(input_text)
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, encoded_text)
    else:
        messagebox.showwarning("Warning", "Please enter a URL to encode.")


# Function to decode the URL
def decode_url():
    input_text = url_input.get("1.0", tk.END).strip()
    if input_text:
        decoded_text = unquote(input_text)
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, decoded_text)
    else:
        messagebox.showwarning("Warning", "Please enter a URL to decode.")


# Create the main window
root = tk.Tk()
root.title("URL Encoder/Decoder")
root.geometry("450x450")

# URL Input
tk.Label(root, text="Enter URL:").pack(pady=5)
url_input = tk.Text(root, height=7, width=55)
url_input.pack(pady=5)

# Buttons for Encode and Decode
encode_button = tk.Button(root, text="Encode", command=encode_url)
encode_button.pack(pady=5)

decode_button = tk.Button(root, text="Decode", command=decode_url)
decode_button.pack(pady=5)

# Result Output
tk.Label(root, text="Result:").pack(pady=5)
result_text = tk.Text(root, height=7, width=55)
result_text.pack(pady=5)

# Run the GUI main loop
root.mainloop()
