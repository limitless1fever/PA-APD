from akun import dataPenyewa
from fungsi.utilitas import clear

user_login = None
role_login = None
id_login = None
login_password = None
nama_login = None

def login():
    while True:
        global user_login, role_login, id_login, login_password, nama_login
        clear()
        print("=== LOGIN ===")
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

                # cek apakah member
                if data_akun["role"] == "MEMBER":
                    nama_login = data_akun["nama"]
                else:
                    nama_login = "Admin"

                print("\nLogin berhasil!")
                input("Tekan Enter untuk melanjutkan...")
                clear()
                return True

        # Jika tidak ditemukan
        print("\nUsername atau password salah!")
        input("Tekan Enter untuk mengulang...")
        clear()


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