import socket
import threading
from tkinter import *

# --- Networking Setup ---
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# FIX: Allow the port to be reused immediately if you restart the script
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

HOST = '127.0.0.1'  # Use localhost for reliability
PORT = 8081
s.bind((HOST, PORT))
s.listen(4)

client = None  # Global variable to hold the connection object


def accept_connections():
    """
    Runs in a background thread. Waits for a client to connect.
    """
    global client
    print(f"Server listening on {HOST}:{PORT}...")

    try:
        temp_client, address = s.accept()
        client = temp_client
        print(f"Connected to {address}")

        # Safe GUI update
        root.after(0, lambda: listbox.insert('end', f"Connected to {address}"))

        # Start listening for incoming messages from this client
        threading.Thread(target=receiver, daemon=True).start()
    except Exception as e:
        print(f"Error accepting connection: {e}")


def send(listbox, entry):
    """
    Sends the text from the Entry widget to the connected client.
    """
    global client
    message = entry.get()

    if not message:
        return  # Don't send empty messages

    if client:
        # Show on my screen
        listbox.insert('end', "You: " + message)
        entry.delete(0, 'end')

        try:
            client.send(bytes(message, "utf-8"))
        except:
            listbox.insert('end', "Error: Connection lost.")
            client = None
    else:
        # Warn if no client is connected yet
        listbox.insert('end', "Error: No Client Connected")


def receiver():
    """
    Background thread that constantly listens for messages from the Client.
    """
    global client
    while True:
        try:
            if client:
                msg_client = client.recv(1024)
                if msg_client:
                    message = msg_client.decode('utf-8')
                    # Use root.after to safely update GUI from this thread
                    root.after(0, lambda: listbox.insert('end', "Client: " + message))
                else:
                    # Empty message means client disconnected
                    root.after(0, lambda: listbox.insert('end', "Client disconnected."))
                    client = None
                    break
        except:
            client = None
            break


# --- GUI Setup ---
root = Tk()
root.title(f"Server (Port {PORT})")

listbox = Listbox(root, width=50)
listbox.pack(padx=10, pady=10)

entry = Entry(root, width=40)
entry.pack(side=LEFT, padx=10, pady=10)

# Pass arguments properly using lambda
button = Button(root, text="Send", command=lambda: send(listbox, entry))
button.pack(side=LEFT, padx=10)

# Start the connection waiter in a separate thread so GUI doesn't freeze
threading.Thread(target=accept_connections, daemon=True).start()

root.mainloop()