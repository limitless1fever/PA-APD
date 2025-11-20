import fungsi
from akun import daftarAkun

from fungsi.utilitas import clear

user_login = None
user = {              
    "admin": "admin123"
}

def login():
    while True: 
        global user_login, role_login, id_login
        berhasil_login = False
        clear()
        print("=== LOGIN ===")
        username = input("Username: ").strip()
        password = input("Password: ").strip()

        for id_akun, info in daftarAkun.items(): 
            if username == info['username'] and password == info['password']:
                user_login = username
                role_login = info['role']
                id_login = id_akun
                berhasil_login = True

                print("Login Berhasil")
                clear()

        if berhasil_login == True: 
            break
        else: 
            print("Login gagal, silahkan coba lagi!")

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

    id_akun = f"acc{len(daftarAkun) + 1}"

    daftarAkun[id_akun] = {
        "username": username, 
        "password": password, 
        "role": "MEMBER"
    }

    # user[username] = password
    print("Akun berhasil dibuat! Silakan login.")

    clear()
    return True

#ini biarin aja kah fitur logout nya dipisah atau nanti mau di gabung di function lain?
def logout():
    global user_login
    user_login = None
    print("Berhasil logout.")