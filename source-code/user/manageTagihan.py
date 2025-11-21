# Manajemen Pembayaran & Tagihan
from fungsi.utilitas import clear

dataPenyewa = {
    "PENYEWA1": {
        "nama": "Ivan Konev", 
        "kontak": "0XXX-XXXX-XXXX",
        "tanggal_gabung": "2 November 2025", 
        "status": "AKTIF", 
        "unit": "KS01", 
        "kamar": "A1"
        }, 
    "PENYEWA2": {
        "nama": "Georgy Zhukov", 
        "kontak": "0XXX-XXXX-XXXX",
        "tanggal_gabung": "10 November 2025", 
        "status": "AKTIF", 
        "unit": "KN01", 
        "kamar": "-"
    }
}

# dict dummy tagihan
# tagihan = {
#     "November 2025": {"jumlah": 1500000, "status": "Belum Bayar"},
#     "Desember 2025": {"jumlah": 1500000, "status": "Belum Bayar"},
#     "Oktober 2025": {"jumlah": 1500000, "status": "Sudah Bayar"},
# 

# tagihan = {
#     "TGHN01": {"tahun": "2025", "bulan": "November", "jumlah": 1500000, "status": "BELUM BAYAR"},
#     "TGHN02": {"tahun": "2025", "bulan": "Desember", "jumlah": 1500000, "status": "BELUM BAYAR"}, 
#     "TGHN03": {"tahun": "2025", "bulan": "November", "jumlah": 1500000, "status": "BAYAR"},
# }

tagihan = {
    "PENYEWA1": {
        "TGHN01": {"tahun": "2025", "bulan": "November", "jumlah": 1500000, "status": "BELUM BAYAR"},
        "TGHN02": {"tahun": "2025", "bulan": "Desember", "jumlah": 1500000, "status": "BELUM BAYAR"},
        "TGHN03": {"tahun": "2025", "bulan": "Oktober", "jumlah": 1500000, "status": "BAYAR"},     
    }, 
    "PENYEWA2": {
        "TGHN01": {"tahun": "2025", "bulan": "November", "jumlah": 1500000, "status": "BAYAR"},
        "TGHN02": {"tahun": "2025", "bulan": "Desember", "jumlah": 1500000, "status": "BELUM BAYAR"},
        "TGHN03": {"tahun": "2025", "bulan": "Oktober", "jumlah": 1500000, "status": "BAYAR"},     
    }
}


# Untuk Sementara Fungsi Fungsi nya Masih Kosong
def buat_laporan_bayar(): 
    clear()
    print("=" * 75)
    print("FORMULIR LAPORAN PEMBAYARAN")
    print("=" * 75)

    input_id = input("Masukkan ID Anda : ")

    for id_penyewa, info_penyewa in dataPenyewa.items(): 
        if input_id == id_penyewa: 
            while True: 
                print("Nama Penyewa :", info_penyewa['nama'])
                print("Unit :", info_penyewa['unit'])
                print("Kamar :", info_penyewa['kamar'])

                print("Pilih periode pembayaran")
                print("Note : 1 Periode = 1 Bulan")
                
    
    # Masukkan ID Penyewa : 

    # Nama Penyewa          : <otomatis tampil>
    # Unit                  : <otomatis tampil>
    # Kamar                 : <otomatis tampil>

    # Pilih periode pembayaran
    # Note : 1 Periode = 1 Bulan

    # 1 Periode : November 2025
    # 2 Periode : Desember 2025
    # 3 Periode : Januari 2025
    # > 

    # Periode Pembayaran    : <otomatis tampil> -> <2025-11 sampai 2025-01 (3 Bulan)>
    # Jumlah Pembayaran     : <otomatis tampil> -> <Rp 4.500.000>

    # Metode Pembayaran 
    # [1] Cash  [2] Transfer
    # > 

    # If Cash 
    # Masukkan Nomor Nota yang diberikan : 

    # If Transfer
    # Masukkan Nomor referensi (No. Ref) pada resi transfer :

    # ... <Tampilkan Informasi yang sudah ada> 
    # Simpan pembayaran? (y/n): 
    
def tampilkan_laporan_konfirmasi():
    clear()
    print("=" * 75)
    print("LAPORAN KONFIRMASI PEMBAYARAN")
    print("=" * 75)
    input("Tekan Enter untuk kembali...")

# Lanjut

# aku nambahin fungsi buat liat tagihan mendatang
def lihat_tagihan_mendatang():
    while True: 
        clear()
        print(f"{'ID Penyewa':<15} {'Nama Lengkap':<25} {'Kontak':<15} {'Tanggal Gabung':<20} {'Status':<15} {'Unit':<10} {'Kamar':<10}")
        for id_penyewa, data in dataPenyewa.items(): 
            print(f"{str(id_penyewa):<15} {data['nama']:<25} {data['kontak']:<15} {data['tanggal_gabung']:<20} {data['status']:<15} {data['unit']:<10} {data['kamar']:<10}")

        print("=" * 75)
        print(f"{'0':<15} Keluar")
        print("=" * 75)

        input_id = input("Masukkan ID : ")

        if input_id == "0": 
            break
        for id_penyewa, info_penyewa in dataPenyewa.items(): 
            if input_id == id_penyewa:
                print("=" * 75)
                print("TAGIHAN YANG AKAN DATANG")
                print("=" * 75)
                
                # ini buat dibuat kayak struk kebawah atau tetap ke samping kasih tau aja
                ada_tagihan = False
                for id_penyewa, data_penyewa in tagihan.items(): 
                    if input_id == id_penyewa: 
                        for id_tagihan, data_tagihan in data_penyewa.items():
                            if data_tagihan['status'] == "BELUM BAYAR": 
                                print("tahun     :", data_tagihan["tahun"])
                                print("Bulan     :", data_tagihan["bulan"])
                                print("Jumlah    : Rp", data_tagihan["jumlah"])
                                print("Status    :", data_tagihan["status"])
                                print("-" * 75)
                                ada_tagihan = True                            

                # for id_tagihan, data_tagihan in tagihan.items(): 
                #     print(id_tagihan)
                #     if input_id == id_tagihan: 
                #         print("tahun     :", data_tagihan["tahun"])
                #         print("Bulan     :", data_tagihan["bulan"])
                #         print("Jumlah    : Rp", data_tagihan["jumlah"])
                #         print("Status    :", data_tagihan["status"])
                #         print("-" * 75)
                #         ada_tagihan = True

                # for id_tagihan, data_tagihan in tagihan.items(): 
                #     if tagihan[id_tagihan]['status'] == "BELUM BAYAR": 
                #         print("tahun     :", tagihan[id_tagihan]["tahun"])
                #         print("Bulan     :", tagihan[id_tagihan]["bulan"])
                #         print("Jumlah    : Rp", tagihan[id_tagihan]["jumlah"])
                #         print("Status    :", tagihan[id_tagihan]["status"])
                #         print("-" * 75)
                #         ada_tagihan = True            

                # for i in range(len(tagihan)):
                #     if tagihan[i]["status"] == "Belum Bayar":
                #         print("Bulan     :", tagihan[i]["bulan"])
                #         print("Jumlah    : Rp", tagihan[i]["jumlah"])
                #         print("Status    :", tagihan[i]["status"])
                #         print("-" * 75)
                #         ada_tagihan = True
                
                if not ada_tagihan:
                    print("Tidak ada tagihan yang akan datang.")
                
                input("Tekan Enter untuk kembali...")

def riwayat_pembayaran():
    clear()
    print("=" * 75)
    print("RIWAYAT PEMBAYARAN")
    print("=" * 75)
    input("Tekan Enter untuk kembali...")

def status_kontrakan():
    clear()
    print("=" * 75)
    print("STATUS KONTRAKAN")
    print("=" * 75)
    input("Tekan Enter untuk kembali...")

def hapus_bukti_pembayaran():
    clear()
    print("=" * 75)
    print("HAPUS BUKTI PEMBAYARAN")
    print("=" * 75)
    input("Tekan Enter untuk kembali...")

# Menu Kelola Tagihan
def kelolaTagihan(): 
    while True:
        clear()
        print("=" * 75)
        print("MANAJEMEN PEMBAYARAN & TAGIHAN")
        print("=" * 75)
        print("[1] - Buat Laporan Konfirmasi Pembayaran")
        print("[2] - Lihat Tagihan yang Akan Datang")
        print("[3] - Lihat Status Kontrakan")
        print("[4] - Lihat Riwayat Pembayaran")
        print("[5] - Hapus Bukti Pembayaran")
        print("[0] - Kembali ke Menu Sebelumnya")
        print("=" * 75)

        pilih = input("> ")

        if pilih == "0":
            break
        elif pilih == "1":
            tampilkan_laporan_konfirmasi()
        elif pilih == "2":
            lihat_tagihan_mendatang()
        elif pilih == "3":
            status_kontrakan()
        elif pilih == "4":
            riwayat_pembayaran()
        elif pilih == "5":
            hapus_bukti_pembayaran()
        else:
            print("Pilihan tidak valid.")