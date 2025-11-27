from akun import dataPenyewa
from fungsi.utilitas import clear
import sys  # hanya jika ingin keluar paksa (opsional)

user_login = None
role_login = None
id_login = None
login_password = None
nama_login = None


def login():
    global user_login, role_login, id_login, login_password, nama_login
    
    max_percobaan = 3
    percobaan = 0

    while percobaan < max_percobaan:
        clear()
        print("=== LOGIN ===")
        print(f"Sisa percobaan: {max_percobaan - percobaan}")
        username = input("Username: ").strip()
        password = input("Password: ").strip()

        # Cari akun berdasarkan username dan password
        for user_id, data_akun in dataPenyewa.items():
            if (
                data_akun.get("username") == username
                and data_akun.get("password") == password
            ):
                # Simpan data sesi
                user_login = username
                login_password = password
                role_login = data_akun["role"]
                id_login = user_id

                if data_akun["role"] == "MEMBER":
                    nama_login = data_akun["nama"]
                else:
                    nama_login = "Admin"

                print("\nLogin berhasil!")
                input("Tekan Enter untuk melanjutkan...")
                clear()
                return True  # sukses login

        # Jika sampai sini, login gagal
        percobaan += 1
        print(f"\nLogin gagal! Username atau password salah.")
        if percobaan < max_percobaan:
            input("Tekan Enter untuk mencoba lagi...")
        else:
            print("\nAnda telah melebihi batas percobaan login (3 kali).")
            input("Tekan Enter untuk kembali ke menu utama...")
            clear()
            return False  # gagal login


def logout():
    global user_login, role_login, id_login, login_password, nama_login
    user_login = None
    role_login = None
    id_login = None
    login_password = None
    nama_login = None
    print("\nBerhasil logout.")
    input("Tekan Enter untuk kembali...")
    clear()