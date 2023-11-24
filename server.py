import socket #antarmuka komunikasi jaringan
import ki_des_algorithm

# ini akan berfungsi sebagai "server" 

def Main():
    host = "127.0.0.1" # alamat IP host/localhost 
    port = 8000 #nomor port yang akan digunakan pada host untuk koneksi socket.
   
    # perlu menginisiasi server
    mySocket = socket.socket() #membuat object socket
    mySocket.bind((host,port)) #mehubungkan socket dengan iphost dan port

    # Pesan Server Untuk Menggungu Koneksi dair User(Client)
    print("Menunggu koneksi.....")
    # Meenetapkan socket dalam mode listen dengan jumlah maksimal koneksi sebanyak 2.
    # agar pengguna(client) dapat terhubung keserver
    mySocket.listen(2)
    # Menerima iformasi koneksi dari clien yang mencoba terhubung
    # dan mengembalikan objek socket (conn) dan alamat (addr) dari klien tersebut.
    conn, addr = mySocket.accept()
    #Mencetak informasi bahwa koneksi telah berhasil dilakukan oleh klien yang beralamat addr.
    print ("Koneksi dari: " + str(addr))

    while True: #Untuk terus memulai banyak percakapan tak terbatas
            # menerima respons dari pengguna lain
            # dengan metode recv() dari objek socket conn dan mendekode pesan tersebut.
            data = conn.recv(1024).decode()
            #Mencetak pesan yang diterima dari klien.
            print("Diterima dari klien = " + data)
            # Menetapkan kunci enkripsi yang akan digunakan oleh algoritma DES ki_des_algorithm.
            kunci = "0A1B2C3D4E5F6071"

            # Mendekripsi pesan yang diterima dari klien menggunakan fungsi decrypt dari modul 
            # ki_des_algorithm.
            pesanDidekripsi = ki_des_algorithm.decrypt(data, kunci)
            if not data:  # jika tidak ada pesan yang diterima
                    break # maka keluar dari loop
            #Mencetak pesan yang telah didekripsi.
            print ("Pesan Didekripsi = " + pesanDidekripsi)
            print("\n")
            #Mengambil input pesan dari pengguna yang akan dienkripsi.
            pesan = input("Masukkan pesan yang ingin Anda enkripsi -> ")
            # Mengenkripsi pesan menggunakan fungsi encrypt dari modul ki_des_algorithm dan 
            # mengubah hasilnya menjadi representasi heksadesimal.
            pesanTerenkripsiAkhir = ki_des_algorithm.bin2hex(ki_des_algorithm.encrypt(pesan, kunci))
            #Mencetak pesan yang telah dienkripsi.
            print("Pesan Terenkripsi = " + pesanTerenkripsiAkhir)
            # Menampilkan efek loading bar menggunakan fungsi sending dari modul ki_des_algorithm.
            ki_des_algorithm.sending()
            # Mengirim pesan yang telah dienkripsi ke klien menggunakan metode send() dari objek socket conn.
            conn.send(pesanTerenkripsiAkhir.encode())
 
    conn.close() # Menutup oneksi socket setelah selesai.
     
if __name__ == '__main__':
    Main()
