# Menu Keluhan 
from fungsi.utilitas import clear

# tempat nyimpan sementara aku masih belum tau mau dipakai buat apa
laporan_keluhan = []

# function fitur masih kosong
def buat_laporan_keluhan():
    clear()
    print("=" * 75)
    print("BUAT LAPORAN KELUHAN")
    print("=" * 75)
    input("Tekan Enter untuk kembali...")

# fungsi liat laporan keluhan yang udah dibuat
def lihat_laporan_keluhan():
    clear()
    print("=" * 75)
    print("LAPORAN KELUHAN YANG TELAH DIBUAT")
    print("=" * 75)

    if len(laporan_keluhan) == 0:
        print("Belum ada laporan keluhan.")
    else:
        for i in range(len(laporan_keluhan)):
            print(f"[{i + 1}]")
            print("  Dari     :", laporan_keluhan[i]["oleh"])
            print("  Keluhan  :", laporan_keluhan[i]["keluhan"])
            print("  Status   :", laporan_keluhan[i]["status"])
            print("-" * 75)
    input("Tekan Enter untuk kembali...")

def hapus_laporan_keluhan():
    clear()
    print("=" * 75)
    print("HAPUS LAPORAN KELUHAN")
    print("=" * 75)
    input("Tekan Enter untuk kembali...")

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

        pilih = input("> ").strip()

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