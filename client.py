import socket

# Inisialisasi server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind server socket ke alamat dan port tertentu
server_address = ('192.168.0.1', 12345)
server_socket.bind(server_address)

# Mendengarkan koneksi dari klien
server_socket.listen(5)
print("Menunggu koneksi...")

while True:
    # Menerima koneksi dari klien
    client_socket, client_address = server_socket.accept()
    print(f"Terhubung ke {client_address}")

    # Menerima data dari klien
    data = client_socket.recv(1024)
    if not data:
        break
    print(f"Data diterima: {data.decode('utf-8')}")

    # Mengirim balasan ke klien
    response = "Pesan diterima"
    client_socket.send(response.encode('utf-8'))

    # Tutup koneksi dengan klien
    client_socket.close()

# Tutup socket server
server_socket.close()