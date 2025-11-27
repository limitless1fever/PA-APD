from akun import dataPenyewa, laporan_keluhan
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


# function fitur masih kosong
def buat_laporan_keluhan():
    clear()
    # print("=" * 75)
    print("BUAT LAPORAN KELUHAN")
    print("=" * 75)

    pilih_id = input("Masukkan ID Penyewa : ")

    for id_penyewa, info_penyewa in dataPenyewa.items():
        if pilih_id == id_penyewa: 
            nama_laporan = info_penyewa['nama']
            unit_laporan = info_penyewa['unit']
            kamar_laporan = info_penyewa['kamar']

            print("Nama Penyewa :", nama_laporan)
            print("Unit :", unit_laporan)
            print("Kamar :", kamar_laporan)
            print("")

            tanggal_laporan = input("Masukkan Tanggal dibuat : ")
            print("KATEGORI LAPORAN")
            print("[1] - Fasilitas Rusak")
            print("[2] - Kebersihan")
            print("[3] - Keamanan")
            print("[4] - Gangguan")
            print("[5] - Lainnya")

            print("Masukkan Kategori laporan anda : ")
            pilih_menu = input("> ")

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
                print("Pilihan Tidak valid!")

            judul_laporan = input("Masukkan Judul Laporan : ")
            deskripsi = deskripsi_laporan("Tulis deskripsi Keluhan:")
            print("\nDeskripsi final:")
            
            for id_penyewa, data_laporan in laporan_keluhan.items(): 
                print(laporan_keluhan)
                if pilih_id == id_penyewa: 
                    id_laporan = f"LK-{len(data_laporan) + 1}"
                    break

            for id_penyewa, data_laporan in laporan_keluhan.items(): 
                if id_penyewa == pilih_id: 
                    print("BERHASIL")
                    data_laporan[id_laporan] = {
                        "nama": nama_laporan, 
                        "unit": unit_laporan, 
                        "kamar": kamar_laporan, 
                        "kategori": kategori_laporan, 
                        "judul_laporan": judul_laporan, 
                        "deskripsi_laporan": deskripsi,
                        "tanggal_dibuat": tanggal_laporan, 
                        "status": "BELUM DITANGANI"
                    }
            
            # laporan_keluhan.append(deskripsi)
            # for i in laporan_keluhan: 
            #     print(i)
            print(laporan_keluhan)
            unloading = laporan_keluhan["PENYEWA1"][id_laporan]["deskripsi_laporan"]

            print(unloading)
            # for baris in unloading: 
            #     print(baris)

            # print(info_penyewa['nama']) 

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