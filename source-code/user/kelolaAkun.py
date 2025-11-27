from fungsi.utilitas import clear
import auth
from akun import dataUser

def ubah_data_akun():
    clear()
    print("UBAH DATA AKUN")
    print("=" * 50)

    id_login = auth.id_login #menyimpan id user
    if id_login not in dataUser:
        print("Error: Pengguna tidak ditemukan.")
        input("Tekan Enter untuk kembali...")
        return

    akun = dataUser[id_login]["akun"]

    print("[1] Ubah Username")
    print("[2] Ubah Password")
    print("[0] Kembali")
    pilih = input("> ").strip()

    if pilih == "1":
        username_baru = input("Masukkan username baru: ").strip()
        if not username_baru:
            print("Username tidak boleh kosong!")
        elif username_baru == akun["username"]:
            print("Username baru tidak boleh sama dengan yang lama!")
        else:
            akun["username"] = username_baru
            print("Username berhasil diubah!")

    elif pilih == "2":
        password_lama = input("Masukkan password lama: ")
        if password_lama != akun["password"]:
            print("Password lama salah!")
        else:
            password_baru = input("Masukkan password baru: ").strip()
            if not password_baru:
                print("Password tidak boleh kosong!")
            elif password_baru == akun["password"]:
                print("Password baru tidak boleh sama dengan yang lama!")
            else:
                akun["password"] = password_baru
                print("Password berhasil diubah!")

    elif pilih == "0":
        return
    else:
        print("Pilihan tidak valid!")

    input("\nTekan Enter untuk lanjut...")


def ubah_data_pribadi():
    clear()
    print("UBAH DATA PRIBADI")
    print("=" * 50)

    id_login = auth.id_login
    if id_login not in dataUser:
        print("Error: Pengguna tidak ditemukan.")
        input("Tekan Enter untuk kembali...")
        return

    akun = dataUser[id_login]["akun"]

    # Hanya penyewa yang punya data pribadi
    if akun["role"] != "MEMBER":
        print("Admin tidak memiliki data pribadi untuk diubah.")
        input("Tekan Enter untuk kembali...")
        return

    print("[1] Ubah Nama Lengkap")
    print("[2] Ubah Email")
    print("[3] Ubah Nomor Telepon")
    print("[0] Kembali")
    pilih = input("> ").strip()

    if pilih == "1":
        nama_baru = input("Masukkan nama lengkap baru: ").strip()
        if not nama_baru:
            print("Nama tidak boleh kosong!")
        else:
            akun["nama"] = nama_baru
            print("Nama berhasil diubah!")

    elif pilih == "2":
        email_baru = input("Masukkan email baru: ").strip()
        if not email_baru:
            print("Email tidak boleh kosong!")
        elif "@" not in email_baru:
            print("Format email tidak valid!")
        else:
            akun["email"] = email_baru
            print("Email berhasil diubah!")

    elif pilih == "3":
        nohp_baru = input("Masukkan nomor telepon baru: ").strip()
        if not nohp_baru:
            print("Nomor telepon tidak boleh kosong!")
        else:
            # Bersihkan dari spasi dan tanda hubung
            nohp_bersih = nohp_baru.replace(" ", "").replace("-", "")
            
            # Validasi: hanya angka
            if not nohp_bersih.isdigit():
                print("Nomor telepon hanya boleh berisi angka, spasi, atau tanda hubung!")
            # Validasi: panjang 10-12 digit
            elif len(nohp_bersih) < 10 or len(nohp_bersih) > 12:
                print("Nomor telepon harus terdiri dari 10-12 digit angka!")
            # Validasi: diawali "08"
            elif not nohp_bersih.startswith("08"):
                print("Nomor telepon harus diawali dengan '08'!")
            else:
                akun["kontak"] = nohp_bersih
                print("Nomor telepon berhasil diubah!")

    elif pilih == "0":
        return
    else:
        print("Pilihan tidak valid!")

    input("\nTekan Enter untuk lanjut...")


def kelolaAkun():
    while True:
        clear()
        print("KELOLA AKUN")
        print("=" * 50)
        print("[1] Ubah Data Akun (Username/Password)")
        print("[2] Ubah Data Pribadi (Nama, Email, No. HP)")
        print("[0] Kembali ke Menu Utama")
        print("=" * 50)

        pilih = input("> ").strip()

        if pilih == "0":
            break
        elif pilih == "1":
            ubah_data_akun()
        elif pilih == "2":
            ubah_data_pribadi()
        else:
            print("Pilihan tidak valid!")
            input("Tekan Enter untuk lanjut...")