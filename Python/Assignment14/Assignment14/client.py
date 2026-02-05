import socket
import threading
from tkinter import *

# --- Networking Setup ---
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# MUST match the Server's IP and Port
HOST = '127.0.0.1'
PORT = 8081


def send(listbox, entry):
    """
    Sends the text from the Entry widget to the Server.
    """
    message = entry.get()
    if message:
        # Show on my screen
        listbox.insert('end', "You: " + message)
        entry.delete(0, 'end')

        try:
            s.send(bytes(message, "utf-8"))
        except:
            listbox.insert('end', "Error: Could not send message.")


def receive_msg():
    """
    Background thread that constantly listens for messages from the Server.
    """
    while True:
        try:
            # Wait for data (blocking call, but safe in a thread)
            message = s.recv(1024).decode("utf-8")

            if message:
                # Safe way to update GUI from background thread
                root.after(0, lambda: listbox.insert('end', "Server: " + message))
            else:
                # Empty message usually means server closed connection
                root.after(0, lambda: listbox.insert('end', "Disconnected from server."))
                s.close()
                break
        except:
            root.after(0, lambda: listbox.insert('end', "Connection lost."))
            s.close()
            break


# --- GUI Setup ---
root = Tk()
root.title(f"Client (Port {PORT})")

listbox = Listbox(root, width=50)
listbox.pack(padx=10, pady=10)

entry = Entry(root, width=40)
entry.pack(side=LEFT, padx=10, pady=10)

# Pass arguments properly using lambda
button = Button(root, text="Send", command=lambda: send(listbox, entry))
button.pack(side=LEFT, padx=10)

# --- Connect & Start ---
try:
    s.connect((HOST, PORT))
    # Start the listening thread immediately after connecting
    threading.Thread(target=receive_msg, daemon=True).start()
except ConnectionRefusedError:
    listbox.insert('end', "Error: Server is not running.")

root.mainloop()