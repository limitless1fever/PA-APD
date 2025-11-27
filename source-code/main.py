import auth
from auth import login
from fungsi.utilitas import clear
from admin.menuAdmin import menuAdmin
from user.menuUser import menuUser

# KODE MAIN
while True:
    try: 
        clear()

        print("=" * 75)
        print("SISTEM MANAJEMEN KOS DAN KONTRAKAN")
        print("=" * 75)

        print("[1] - Login")
        print("=" * 75)

        print("[0] - Keluar")
        print("=" * 75)

        print("Pilih menu yang anda inginkan")
        pilih_menu = input("> ")
        print("=" * 75) 

        clear()

        if pilih_menu == "0": 
            print("Program Selesai!")
            print("Terimakasih telah menggunakan program ini!")
            break

        if pilih_menu == "1": 
            login()
            if auth.role_login == "ADMIN": 
                print("Anda Login sebagai Admin")
                menuAdmin()
            else: 
                print("Anda Login sebagai Member")
                menuUser()
        else: 
            raise ValueError("Pilihan Tidak Valid")
    
    except ValueError as e: 
        print("=" * 75)
        print(e)
        print("=" * 75)
        clear()

