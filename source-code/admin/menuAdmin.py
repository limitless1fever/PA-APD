import fungsi
from fungsi.utilitas import clear

import auth

import admin
from admin.akunPenyewa import akunPenyewa
from admin.operasional import operasional

# Menu Admin
def menuAdmin(): 
    while True: 
        try: 
            clear()

            print("=" * 75)
            print("Selamat datang kembali,", auth.user_login)
            print("=" * 75)

            print("[1] - Data dan Akun Penyewa")
            print("[2] - Operasional Kos dan Kontrakan")
            print("=" * 75)

            print("[0] - Keluar")
            print("=" * 75)

            print("Pilih menu yang anda inginkan")
            pilih_menu = input("> ")
            print("=" * 75)

            clear()

            if pilih_menu == "0": 
                break
            if pilih_menu == "1": 
                clear()
                akunPenyewa()
            elif pilih_menu == "2": 
                clear()
                operasional()
            else: 
                raise ValueError("Pilihan Tidak Valid")
        
        except ValueError as e: 
            print("=" * 75)
            print(e)
            print("=" * 75)
            clear()