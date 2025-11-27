import fungsi
import user
import auth
from akun import dataPenyewa, tagihan

from fungsi.utilitas import clear

from user.manageTagihan import kelolaTagihan
from user.kelolaAkun import kelolaAkun
from user.menuKeluhan import keluhan

# Menu User
def menuUser():
    while True: 
        try: 
            clear()

            print("=" * 75)
            print(f"Selamat datang kembali : {auth.nama_login}")
            print("=" * 75)

            print(f"Sekarang Bulan : {tagihan[auth.id_login]['TGHN01']['bulan']} {tagihan[auth.id_login]['TGHN01']['tahun']}")
            print(f"Status Kos : {tagihan[auth.id_login]['TGHN01']['status']}")
            print("=" * 75) 

            print("[1] - Manajemen Pembayaran & Tagihan")
            print("[2] - Layanan & Keluhan Fasilitas")
            print("[3] - Pengelolaan Akun & Data Pribadi")
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
                kelolaTagihan()

            elif pilih_menu == "2": 
                clear()
                keluhan()

            elif pilih_menu == "3": 
                clear()
                kelolaAkun()        
                
            else: 
                raise ValueError("Pilihan Tidak Valid")
        
        except ValueError as e: 
            print("=" * 75)
            print(e)
            print("=" * 75)
            clear()
