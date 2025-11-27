import fungsi
import akun
from akun import dataPenyewa

from fungsi.utilitas import clear

user_login = None

# Variabel global untuk menyimpan info login
user_login = None
role_login = None
id_login = None

def login():
    global user_login, role_login, id_login
    while True:
        clear()
        print("=== LOGIN ===")
        username = input("Username: ").strip()
        password = input("Password: ").strip()

        for id_akun, info in dataPenyewa.items(): 
            if username == info['username'] and password == info['password']:
                user_login = username
                role_login = info['role']
                id_login = id_akun
                print("Login Berhasil!")
                clear()
                return  # keluar dari fungsi, bukan hanya loop

        print("Login gagal, silakan coba lagi!")
        input("Tekan Enter untuk lanjut...")

def register():
    clear()
    print("=== REGISTER ===")
    username = input("Masukkan username: ").strip()
    password = input("Masukkan password: ").strip()

    if not username or not password:
        print("Username dan password tidak boleh kosong!")
        input("Tekan Enter untuk kembali...")
        return

    # Cek apakah username sudah ada
    for info in dataPenyewa.values():
        if info["username"] == username:
            print("Username sudah digunakan!")
            input("Tekan Enter untuk kembali...")
            return

    # Buat ID akun baru
    id_baru = f"acc{len(dataPenyewa) + 1}"

    # Tambahkan akun baru (hanya dengan data dasar dulu)
    dataPenyewa[id_baru] = {
        "username": username,
        "password": password,
        "role": "MEMBER",
        # Jika butuh, kamu bisa tambahkan field lain dengan nilai default
        "nama": "",
        "kontak": "",
        "email": "",
        "tanggal_gabung": "27 November 2025",
        "status": "AKTIF",
        "unit": "",
        "kamar": ""
    }

    print("Akun berhasil dibuat! Silakan login.")
    input("Tekan Enter untuk kembali...")

#ini biarin aja kah fitur logout nya dipisah atau nanti mau di gabung di function lain?
def logout():
    global user_login
    user_login = None
    print("Berhasil logout.")