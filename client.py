import socket
import ki_des_algorithm
import sys
from time import sleep

def Main():
    host = "127.0.0.1"  # Alamat IP host / localhost
    port = 8000  # Nomor port untuk koneksi socket

    # Membuat objek socket dan menghubungkannya ke server
    mySocket = socket.socket()
    mySocket.connect((host, port))

    # Mengambil input pesan dari pengguna untuk dienkripsi
    pesan = input("Masukkan pesan yang ingin Anda enkripsi -> ")
    kunci = "0A1B2C3D4E5F6071"  # Kunci enkripsi yang digunakan dalam DES

    # Mengenkripsi pesan menggunakan DES
    pesanTerenkripsiAkhir = ki_des_algorithm.bin2hex(ki_des_algorithm.encrypt(pesan, kunci))
    print("Pesan Terenkripsi = " + pesanTerenkripsiAkhir)

    # Melakukan komunikasi secara terus-menerus sampai pengguna menginput "q"
    while pesan != 'q':
        # Menampilkan efek loading bar
        ki_des_algorithm.sending()

        # Mengenkripsi pesan di dalam loop
        pesanTerenkripsiAkhir = ki_des_algorithm.bin2hex(ki_des_algorithm.encrypt(pesan, kunci))

        # Mengirim pesan terenkripsi ke server
        mySocket.send(pesanTerenkripsiAkhir.encode())

        # Menerima respons dari server dan mendekode pesan tersebut
        data = mySocket.recv(1024).decode()
        print("Diterima dari server (Hex) = " + data)

        # Mendekripsi pesan yang diterima dari server
        pesanDidekripsi_binary = ki_des_algorithm.decrypt(ki_des_algorithm.hex2bin(data), kunci)
        pesanDidekripsi_text = ki_des_algorithm.bin2hex(pesanDidekripsi_binary)
        if not data:
            break
        print("Pesan Didekripsi (Binary) = " + pesanDidekripsi_binary)
        print("Pesan Didekripsi (Text) = " + pesanDidekripsi_text + "\n")

        # Meminta input pesan baru dari pengguna
        pesan = input("Masukkan pesan yang ingin Anda enkripsi -> ")
        pesanTerenkripsiAkhir = ki_des_algorithm.bin2hex(ki_des_algorithm.encrypt(pesan, kunci))
        print("Pesan Terenkripsi = " + pesanTerenkripsiAkhir)

    # Menutup koneksi socket setelah selesai
    mySocket.close()

if __name__ == '__main__':
    Main()
