import auth
from fungsi.utilitas import clear
from admin.menuAdmin import menuAdmin
from user.menuUser import menuUser

# KODE MAIN
while True:
    try: 
        clear()
        print("=" * 75)
        print("SISTEM MANAJEMEN KOS")
        print("=" * 75)
        print("[1] - Login")
        print("[0] - Keluar")
        print("=" * 75)

        pilih_menu = input("Pilih menu yang anda inginkan: ").strip()
        print("=" * 75)
        clear()

        if pilih_menu == "0": 
            print("Program Selesai!")
            print("Terimakasih telah menggunakan program ini!")
            break

        elif pilih_menu == "1": 
            if auth.login():
                if auth.role_login == "ADMIN": 
                    print("Anda Login sebagai Admin")
                    menuAdmin()
                else: 
                    print("Anda Login sebagai Member")
                    menuUser()
                # Logout otomatis setelah keluar dari menu
                auth.logout()
            # Jika login gagal (3x salah), langsung kembali ke menu utama
        else: 
            raise ValueError("Pilihan Tidak Valid")
    
    except ValueError as e: 
        print("=" * 75)
        print(e)
        print("=" * 75)
        input("Tekan Enter untuk lanjut...")
        clear()