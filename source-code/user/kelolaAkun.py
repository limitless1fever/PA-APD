# Pengelolaan Akun & data Pribadi
from fungsi.utilitas import clear

# Fungsi Fungsi Masih Kosong
def ubah_data_akun():
    pass

def ubah_data_pribadi():
    pass

# Menu Kelola Akun
def kelolaAkun():
    while True:
        clear
        print("=" * 75)
        print("KELOLA AKUN")
        print("=" * 75)
        print("[1] - Ubah Data pada Akun")
        print("[2] -  Ubah Data Pribadi")
        print("[0] - Kembali ke Menu Sebelumnya")
        print("=" * 75)
        pilih = input("> ")

        if pilih == "0":
            break

        elif pilih == "1":
            ubah_data_akun()
        
        elif pilih == "2":
            ubah_data_pribadi()
        
        else:
            print("Pilihan tidak valid")