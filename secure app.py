import os
import socket
import ssl
from cryptography.fernet import Fernet

def generate_key():
    if not os.path.exists("file_transfer.key"):
        key = Fernet.generate_key()
        with open("file_transfer.key", "wb") as key_file:
            key_file.write(key)

def load_key():
    return open("file_transfer.key", "rb").read()

generate_key()
key = load_key()
cipher = Fernet(key)

def encrypt_file(filename):
    with open(filename, "rb") as file:
        encrypted_data = cipher.encrypt(file.read())
    with open(filename + ".enc", "wb") as enc_file:
        enc_file.write(encrypted_data)

def decrypt_file(encrypted_filename, output_filename):
    with open(encrypted_filename, "rb") as enc_file:
        decrypted_data = cipher.decrypt(enc_file.read())
    with open(output_filename, "wb") as dec_file:
        dec_file.write(decrypted_data)

def secure_file_server(host, port):
    context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
    context.load_cert_chain(certfile="server.crt", keyfile="server.key")
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_sock:
        server_sock.bind((host, port))
        server_sock.listen(5)
        
        with context.wrap_socket(server_sock, server_side=True) as secure_sock:
            conn, addr = secure_sock.accept()
            with conn:
                filename = conn.recv(1024).decode()
                
                with open(filename, "wb") as file:
                    while True:
                        data = conn.recv(4096)
                        if not data:
                            break
                        file.write(data)

def secure_file_client(server_host, server_port, filename):
    context = ssl.create_default_context()
    
    with socket.create_connection((server_host, server_port)) as sock:
        with context.wrap_socket(sock, server_hostname=server_host) as secure_sock:
            secure_sock.sendall(filename.encode())
            with open(filename, "rb") as file:
                while chunk := file.read(4096):
                    secure_sock.sendall(chunk)
