import socket
import threading
import tkinter as tk
from tkinter import simpledialog

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 5555))

window = tk.Tk()
window.title("MohanChat 💬")

chat_area = tk.Text(window)
chat_area.pack()

msg_entry = tk.Entry(window)
msg_entry.pack()

def send_message():
    message = msg_entry.get()
    client.send(message.encode())
    msg_entry.delete(0, tk.END)

def receive():
    while True:
        try:
            message = client.recv(1024).decode()
            chat_area.insert(tk.END, message + "\n")
        except:
            break

send_button = tk.Button(window, text="Send", command=send_message)
send_button.pack()

thread = threading.Thread(target=receive)
thread.start()

window.mainloop()
