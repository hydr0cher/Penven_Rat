# modules/file_manager.py

from ..encryption import encrypt_data, decrypt_data
from ..utils import MAX_SIZE

# Helper function to receive file
def receive_file(client_socket, filename):
    encrypted_data = b''
    while True:
        data = client_socket.recv(MAX_SIZE)
        if not data:
            break
        encrypted_data += data
    decrypted_data = decrypt_data(encrypted_data)
    with open(filename, 'wb') as f:
        f.write(decrypted_data)

# Helper function to send file
def send_file(client_socket, filename):
    with open(filename, 'rb') as f:
        data = f.read()
        encrypted_data = encrypt_data(data)
        client_socket.send(encrypted_data)
