import socket

# Inisialisasi socket klien
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Alamat dan port server yang akan dihubungi
server_address = ('192.168.0.1', 12345)

# Mencoba untuk terhubung ke server
client_socket.connect(server_address)

# Mengirim data ke server
message = "Halo, server!"
client_socket.send(message.encode('utf-8'))

# Menerima balasan dari server
data = client_socket.recv(1024)
print(f"Balasan dari server: {data.decode('utf-8')}")

# Tutup koneksi dengan server
client_socket.close()