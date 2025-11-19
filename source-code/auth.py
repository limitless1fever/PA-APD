import fungsi
from fungsi.utilitas import clear

user_login = None
user = {              
    "admin": "admin123"
}

# === IZIN INI MAU DIHAPUS ===
# def clear():
#     os.system('cls' if os.name == 'nt' else 'clear')

# def menu_login():
#     clear()
#     print("=== SELAMAT DATANG ===")
#     print("1. Login")
#     print("2. Register")
#     print("3. Keluar")

def login():
    global user_login
    clear()
    print("=== LOGIN ===")
    username = input("Username: ").strip()
    password = input("Password: ").strip()

    if username in user and user[username] == password:
        user_login = username
        if username == "admin":
            print("Anda login sebagai Admin")
            clear()
        else:
            print("Login berhasil!")
            clear()
        return True
    else:
        print("Username atau password salah!")
        return False

def register():
    clear()
    print("=== REGISTER ===")
    username = input("Masukkan username: ").strip()
    password = input("Masukkan password: ").strip()

# ini buat ngecek kosong atau ngga nya data login
    if not username or not password:
        print("Username dan password tidak boleh kosong!")
        return False
#ini buat kalau ada yang double username nya
    if username in user:
        print("Username sudah digunakan!")
        return False

    user[username] = password
    print("Akun berhasil dibuat! Silakan login.")

    clear()
    return True

#ini biarin aja kah fitur logout nya dipisah atau nanti mau di gabung di function lain?
def logout():
    global user_login
    user_login = None
    print("Berhasil logout.")

# === IZIN INI MAU DIHAPUS ===

# Buat ngecek jalan apa tidak fiturnya
# while True:
#     menu_login()
#     pilihan = input("Pilih menu: ")

#     if pilihan == "1":
#         if login():
#             #hak admin
#             if user_login == "admin":
#                 while True:
#                     clear()
#                     print("=== MENU ADMIN ===")
#                     print("1. Logout")
#                     admin_pilihan = input("Pilih: ")

#                     if admin_pilihan == "1":
#                         logout()
#                         break
#                     else:
#                         print("Pilihan tidak valid!")
#                         input("\nTekan Enter untuk lanjut...")
#             #hak kroco
#             else:
#                 print(f"Selamat datang, {user_login}!")
#                 input("\nTekan Enter untuk logout...")
#                 logout()

#     elif pilihan == "2":
#         register()
#         input("\nTekan Enter untuk lanjut...")

#     elif pilihan == "3":
#         print("Anda telah keluar")
#         break

#     else:
#         print("Pilihan tidak valid!")
#         input("\nTekan Enter untuk lanjut...")
