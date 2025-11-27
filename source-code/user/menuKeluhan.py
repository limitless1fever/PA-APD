from akun import dataUser
import auth
from fungsi.utilitas import clear

# tempat nyimpan sementara aku masih belum tau mau dipakai buat apa
# laporan_keluhan = []

def deskripsi_laporan(prompt, end_keyword="SELESAI"):
    print(f"{prompt}")
    print(f"(Ketik '{end_keyword}' di baris baru untuk selesai.)")

    lines = []
    while True:
        line = input()
        if line.strip().upper() == end_keyword:
            break
        lines.append(line)
    
    hasil = "\n".join(lines).strip()
    
    if hasil == "":
        print("Deskripsi tidak boleh kosong. Coba lagi.\n")
        return deskripsi_laporan(prompt, end_keyword)

    return hasil

def buat_laporan_keluhan():
    clear()
    print("BUAT LAPORAN KELUHAN")
    print("=" * 50)

    pilih_id = input("Masukkan ID Penyewa (contoh: PENYEWA1): ").strip()
    print()

    # Cek apakah ID ada di dataUser
    if pilih_id not in dataUser:
        print("ID Penyewa tidak ditemukan!")
        input("Tekan Enter untuk kembali...")
        return

    user = dataUser[pilih_id]
    akun = user["akun"]

    # Pastikan ini penyewa
    if akun["role"] != "MEMBER":
        print("Hanya penyewa yang dapat membuat laporan keluhan.")
        input("Tekan Enter untuk kembali...")
        return

    nama_laporan = akun["nama"]
    kamar_laporan = akun["kamar"]

    print("Nama Penyewa :", nama_laporan)
    print("Kamar        :", kamar_laporan)
    print()

    tanggal_laporan = input("Masukkan Tanggal dibuat (contoh: 27 November 2025): ").strip()
    print()

    print("KATEGORI LAPORAN")
    print("[1] Fasilitas Rusak")
    print("[2] Kebersihan")
    print("[3] Keamanan")
    print("[4] Gangguan Lingkungan")
    print("[5] Lainnya")
    print()

    pilih_menu = input("Masukkan Kategori laporan anda: ").strip()

    kategori_laporan = ""
    if pilih_menu == "1":
        kategori_laporan = "Fasilitas Rusak"
    elif pilih_menu == "2":
        kategori_laporan = "Kebersihan"
    elif pilih_menu == "3":
        kategori_laporan = "Keamanan"
    elif pilih_menu == "4":
        kategori_laporan = "Gangguan Lingkungan"
    elif pilih_menu == "5":
        kategori_laporan = "Lainnya"
    else:
        print("Pilihan tidak valid!")
        input("Tekan Enter untuk kembali...")
        return

    judul_laporan = input("Masukkan Judul Laporan: ").strip()
    if not judul_laporan:
        print("Judul tidak boleh kosong!")
        input("Tekan Enter untuk kembali...")
        return

    deskripsi = deskripsi_laporan("Tulis deskripsi keluhan:")

    # Buat ID laporan baru
    laporan_aktif = user["laporan_keluhan"]
    id_laporan_baru = f"LK-{len(laporan_aktif) + 1}"

    # Simpan laporan
    laporan_aktif[id_laporan_baru] = {
        "nama": nama_laporan,
        "kamar": kamar_laporan,
        "kategori": kategori_laporan,
        "judul_laporan": judul_laporan,
        "deskripsi_laporan": deskripsi,
        "tanggal_dibuat": tanggal_laporan,
        "status": "BELUM DITANGANI"
    }

    print("\nLaporan keluhan berhasil dibuat!")
    print(f"ID Laporan: {id_laporan_baru}")
    input("\nTekan Enter untuk kembali...")

# fungsi liat laporan keluhan yang udah dibuat
def lihat_laporan_keluhan():
    clear()
    print("LAPORAN KELUHAN YANG TELAH DIBUAT")
    print("=" * 50)

    id_login = auth.id_login

    if id_login not in dataUser:
        print("Error: Pengguna tidak ditemukan.")
        input("Tekan Enter untuk kembali...")
        return

    user = dataUser[id_login]
    akun = user["akun"]

    # Hanya penyewa yang punya laporan keluhan
    if akun["role"] != "MEMBER":
        print("Anda adalah admin. Tidak memiliki laporan keluhan.")
        input("Tekan Enter untuk kembali...")
        return

    laporan_dict = user["laporan_keluhan"]

    if not laporan_dict:
        print("Anda belum membuat laporan keluhan.")
    else:
        for id_laporan, data in laporan_dict.items():
            print(f"ID Laporan   : {id_laporan}")
            print(f"Nama         : {data['nama']}")
            print(f"Kamar        : {data['kamar']}")
            print(f"Kategori     : {data['kategori']}")
            print(f"Judul        : {data['judul_laporan']}")
            print(f"Tanggal      : {data['tanggal_dibuat']}")
            print(f"Status       : {data['status']}")
            print("Deskripsi    :")
            print(f"  {data['deskripsi_laporan']}")
            print("-" * 50)

    input("\nTekan Enter untuk kembali...")

def hapus_laporan_keluhan():
    clear()
    print("HAPUS LAPORAN KELUHAN")
    print("=" * 50)

    id_login = auth.id_login

    # Validasi pengguna
    if id_login not in dataUser:
        print("Error: Pengguna tidak ditemukan.")
        input("Tekan Enter untuk kembali...")
        return

    user = dataUser[id_login]
    akun = user["akun"]

    if akun["role"] != "MEMBER":
        print("Hanya penyewa yang dapat menghapus laporan keluhan.")
        input("Tekan Enter untuk kembali...")
        return

    laporan_dict = user["laporan_keluhan"]

    if not laporan_dict:
        print("Anda belum memiliki laporan keluhan.")
        input("Tekan Enter untuk kembali...")
        return

    # Tampilkan daftar laporan
    print("Daftar Laporan Anda:")
    for id_laporan in laporan_dict:
        print(f" - {id_laporan}: {laporan_dict[id_laporan]['judul_laporan']} "
            f"({laporan_dict[id_laporan]['status']})")
    print()

    # Input ID laporan yang ingin dihapus
    id_hapus = input("Masukkan ID Laporan yang ingin dihapus (contoh: LK-1): ").strip()

    if id_hapus not in laporan_dict:
        print("ID Laporan tidak ditemukan!")
        input("Tekan Enter untuk kembali...")
        return

    # Tampilkan detail laporan yang akan dihapus
    data_hapus = laporan_dict[id_hapus]
    print(f"\nAnda akan menghapus laporan berikut:")
    print(f"ID Laporan : {id_hapus}")
    print(f"Judul      : {data_hapus['judul_laporan']}")
    print(f"Status     : {data_hapus['status']}")
    print(f"Kategori   : {data_hapus['kategori']}")
    print()

    # Konfirmasi
    konfirmasi = input("Yakin ingin menghapus? (y/n): ").strip().lower()
    if konfirmasi == "y":
        del laporan_dict[id_hapus]
        print("\nLaporan berhasil dihapus.")
    else:
        print("\nPenghapusan dibatalkan.")

    input("\nTekan Enter untuk kembali...")

def keluhan():
    while True:
        clear()
        print("=" * 75)
        print("LAYANAN & KELUHAN FASILITAS")
        print("=" * 75)
        print("[1] - Buat Laporan Keluhan")
        print("[2] - Lihat Laporan Keluhan yang Telah Dibuat")
        print("[3] - Hapus Laporan Keluhan")
        print("[0] - Kembali ke Menu Utama")
        print("=" * 75)

        pilih = input("> ")

        if pilih == "0":
            break
        elif pilih == "1":
            buat_laporan_keluhan()
        elif pilih == "2":
            lihat_laporan_keluhan()
        elif pilih == "3":
            hapus_laporan_keluhan()
        else:
            print("Pilihan tidak valid.")