# Operasional Kos / Kontrakan
from fungsi.utilitas import clear
from user.menuKeluhan import laporan_keluhan

# data tagihan sementara(kurang lebih begini datanya)
tagihan = {
    "Pirlo": {
        "November 2025": {"jumlah": 1500000, "status": "Belum Bayar"},
        "Desember 2025": {"jumlah": 1500000, "status": "Belum Bayar"},
    },
    "Yoga": {
        "November 2025": {"jumlah": 1200000, "status": "Belum Bayar"},
        "Oktober 2025": {"jumlah": 1200000, "status": "Sudah Bayar"},
    }
}

def buatTagihan():
    pass

def lihatKamar_kosong():
    pass

def lihatTagihan_lunas():
    pass

def lihatKeluhan_penyewa():
    clear()
    print("=" * 75)
    print("LAPORAN KELUHAN DARI PENYEWA")
    print("=" * 75)
    
    if not laporan_keluhan:
        print("Belum ada Laporan")
    else:
        for i in range(len(laporan_keluhan)):
            print(f"[{i + 1}]")
            print("  Dari     :", laporan_keluhan[i]["oleh"])
            print("  Keluhan  :", laporan_keluhan[i]["keluhan"])
            print("  Status   :", laporan_keluhan[i]["status"])
            print("-" * 75)
    input("Tekan Enter untuk kembali...")

# Asli aku belum tambahin error handling nya baru logika utamanya jadi agak kurang 
def editStatus():
    # Cek apakah ada tagihan user
    if not tagihan:
        print("Belum ada user terdaftar.")
        input("Tekan Enter untuk kembali...")
        return

    # Tampilkan daftar user yang ada
    print("Daftar User yang Memiliki Tagihan:")
    for username in tagihan:
        print(f"- {username}")

    # Masukkan Nama User yang ingin di edit
    user = input("Masukkan Nama User: ")
    if user not in tagihan:
        print("User tidak ditemukan.")
        input("Tekan Enter untuk kembali...")
        return

    # Ambil data tagihan user
    tagihan_user = tagihan[user]

    # Tampilkan daftar bulan tagihan untuk user ini
    print(f"Daftar tagihan untuk {user}:")
    for bulan, info in tagihan_user.items():
        status = info["status"]
        jumlah = info["jumlah"]
        print(f"- {bulan} : Rp{jumlah:,} ({status})")

    # untuk merubah tagihan di bulan yang sudah lunas
    bulan = input("Masukkan Bulan Tagihan Yang Ingin Diubah (contoh: November 2025): ")
    if bulan not in tagihan_user:
        print("Tagihan Untuk Bulan Tersebut Tidak Ditemukan.")
        input("Tekan Enter untuk kembali...")
        return

    # Cek apakah sudah dibayar
    if tagihan_user[bulan]["status"] == "Sudah Bayar":
        print("Tagihan Ini Sudah Lunas.")
        input("Tekan Enter untuk kembali...")
        return

    # Ubah status menjadi "Sudah Bayar"
    tagihan[user][bulan]["status"] = "Sudah Bayar"
    print(f"Status tagihan {bulan} untuk {user} berhasil diubah menjadi 'Sudah Bayar'.")
    input("Tekan Enter untuk kembali...")

def cetakLaporan():
    pass

def operasional():
    while True:
        clear() 
        print("=" * 75)
        print("OPERASIONAL KOS & KONTRAKAN")
        print("=" * 75)
        print("[1] - Buat Tagihan Bulanan")
        print("[2] - Lihat Berapa Kamar Yang Kosong")
        print("[3] - Lihat Tagihan Yang Belum Lunas")
        print("[4] - Lihat Keluhan dari Penyewa")
        print("[5] - Edit status pembayaran penyewa")
        print("[6] - Cetak Laporan Keuangan")
        print("[0] - Kembali ke Menu Sebelumnya")
        pilih = input("> ").strip()

        if pilih == "0":
            break
        elif pilih == "1":
            buatTagihan()
        elif pilih == "2":
            lihatKamar_kosong()
        elif pilih == "3":
            lihatTagihan_lunas()
        elif pilih == "4":
            lihatKeluhan_penyewa()
        elif pilih == "5":
            editStatus()
        elif pilih == "6":
            cetakLaporan()
        else:
            print("Pilihan Tidak Valid")
            input("Tekan Enter Untuk Kembali...")