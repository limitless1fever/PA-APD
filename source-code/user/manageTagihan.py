# Manajemen Pembayaran & Tagihan
from fungsi.utilitas import clear
import auth
from akun import dataPenyewa, tagihan, laporan_bayar

# Untuk Sementara Fungsi Fungsi nya Masih Kosong
def buat_laporan_bayar(): 
    indeks = 0
    i = 0
    total_bayar = 0
    periode_bulan = []
    info_pembayaran = []
    selesai_tambah = False

    # jumlah_periode = 0
    
    clear()
    print("=" * 75)
    print("FORMULIR LAPORAN PEMBAYARAN")
    print("=" * 75)

    input_id = input("Masukkan ID Anda : ")
    print("")

    for id_penyewa, info_penyewa in dataPenyewa.items(): 
        if input_id == id_penyewa: 
            while True: 
                nama_laporan = info_penyewa['nama']
                unit_laporan = info_penyewa['unit']
                kamar_laporan = info_penyewa['kamar']

                print("Nama Penyewa :", nama_laporan)
                print("Unit :", unit_laporan)
                print("Kamar :", kamar_laporan)
                print("")

                print("Pilih periode pembayaran")
                print("Note : 1 Periode = 1 Bulan")
                print("")
                for id_penyewa, data_penyewa in tagihan.items(): 
                    if input_id == id_penyewa: 
                        for id_tagihan, data_tagihan in data_penyewa.items(): 
                            if data_tagihan['status'] == "BELUM BAYAR": 
                                print(f"Periode ke-{indeks + 1} : {data_tagihan['bulan']} {data_tagihan['tahun']}")
                                data_periode = f"{data_tagihan['bulan']} {data_tagihan['tahun']}"
                                periode_bulan.append(data_periode)
                                indeks += 1
                                # print(indeks)
                                # jumlah_periode += 1

                # print(indeks)
                print("Masukkan jumlah periode yang ingin anda bayar (dalam angka)")
                pilih_periode = input("> ")
                print("")

                if pilih_periode == "0":
                    break
                elif pilih_periode == "1" and int(pilih_periode) <= int(indeks): 
                    print(f"Periode Pembayaran : {periode_bulan[0]}")
                    for id_penyewa, data_penyewa in tagihan.items(): 
                        if input_id == id_penyewa: 
                            for id_tagihan, data_tagihan in data_penyewa.items(): 
                                if data_tagihan['status'] == "BELUM BAYAR"  and i < int(pilih_periode):
                                    total_bayar += data_tagihan['jumlah']
                                    i += 1

                    print("Jumlah Pembayaran : ", total_bayar)
                    print("")
                    # input("Tekan Enter untuk Kembali...") 
                    # break

                elif pilih_periode == "2" and int(pilih_periode) <= int(indeks): 
                    print(f"Periode Pembayaran : {periode_bulan[0]} sampai {periode_bulan[1]}")
                    for id_penyewa, data_penyewa in tagihan.items(): 
                        if input_id == id_penyewa: 
                            for id_tagihan, data_tagihan in data_penyewa.items(): 
                                if data_tagihan['status'] == "BELUM BAYAR"  and i < int(pilih_periode):
                                    total_bayar += data_tagihan['jumlah']
                                    i += 1

                    print("Jumlah Pembayaran : ", total_bayar)
                    print("")
                    # input("Tekan Enter untuk Kembali...") 
                    # break

                elif pilih_periode == "3" and int(pilih_periode) <= int(indeks):
                    print(f"Periode Pembayaran : {periode_bulan[0]} sampai {periode_bulan[2]}")
                    for id_penyewa, data_penyewa in tagihan.items(): 
                        if input_id == id_penyewa: 
                            for id_tagihan, data_tagihan in data_penyewa.items(): 
                                if data_tagihan['status'] == "BELUM BAYAR"  and i < int(pilih_periode):
                                    total_bayar += data_tagihan['jumlah']
                                    i += 1

                    print("Jumlah Pembayaran : ", total_bayar)
                    print("")
                    # input("Tekan Enter untuk Kembali...") 
                    # break 
                else: 
                    print("Pilihan Tidak Valid")

                print("Metode Pembayaran")
                print("[1] CASH     [2] TRANSFER")
                pilih_pembayaran = input("> ")
                print("")

                if pilih_pembayaran == "1": 
                    metode_bayar = "CASH"
                    no_nota = input("Masukkan Nomor Nota yang telah diberikan : ")
                    info_pembayaran.append(metode_bayar)
                    info_pembayaran.append(no_nota)
                elif pilih_pembayaran == "2": 
                    metode_bayar = "TRANSFER"
                    no_ref = input("Masukkan Nomor referensi (No. Ref) pada resi transfer : ")
                    info_pembayaran.append(metode_bayar)
                    info_pembayaran.append(no_ref)
                else:
                    print("Pilihan anda tidak valid")

                print(info_pembayaran)
                print(pilih_periode)

                for id_penyewa, data_laporan in laporan_bayar.items(): 
                    print(data_laporan)
                    if input_id == id_penyewa: 
                        id_laporan = f"LB-{len(data_laporan) + 1}"
                        break
                
                # laporan_bayar[input_id]= {
                #     laporan_bayar[input_id][id_laporan] = {
                #         "nama": nama_laporan, 
                #         "unit": unit_laporan, 
                #         "kamar": kamar_laporan, 
                #         "jumlah_periode": pilih_periode, 
                #         "periode": periode_bulan, 
                #         "jumlah_pembayaran": total_bayar, 
                #         "metode_pembayaran": info_pembayaran, 
                #         "status": "DIAJUKAN"
                #     }
                # }

                for id_penyewa, data_laporan in laporan_bayar.items(): 
                    if id_penyewa == input_id: 
                        print("BERHASIL")
                        data_laporan[id_laporan] = {
                            "nama": nama_laporan, 
                            "unit": unit_laporan, 
                            "kamar": kamar_laporan, 
                            "jumlah_periode": pilih_periode, 
                            "periode": periode_bulan, 
                            "jumlah_pembayaran": total_bayar, 
                            "metode_pembayaran": info_pembayaran, 
                            "status": "DIAJUKAN"
                        }
                        selesai_tambah = True
                    
                    if selesai_tambah == True: 
                        break

                print(laporan_bayar)
                print("Laporan Berhasil Dibuat!")
                input("Tekan Enter untuk melanjutkan... ")
                clear()
                break

                # input("Tekan Enter untuk Kembali...") 

                # break

                # ada_tagihan = False
                # for id_penyewa, data_penyewa in tagihan.items(): 
                #     if input_id == id_penyewa: 
                #         for id_tagihan, data_tagihan in data_penyewa.items():
                #             if data_tagihan['status'] == "BELUM BAYAR": 
                #                 print("tahun     :", data_tagihan["tahun"])
                #                 print("Bulan     :", data_tagihan["bulan"])
                #                 print("Jumlah    : Rp", data_tagihan["jumlah"])
                #                 print("Status    :", data_tagihan["status"])
                #                 print("-" * 75)
                #                 ada_tagihan = True

                    #             if not ada_tagihan:
                    # print("Tidak ada tagihan yang akan datang.")

    
    # LAPORAN PEMBAYARAN
    # ID Penyewa            : <otomatis tampil>
    # Nama Penyewa          : <otomatis tampil>
    # Unit                  : <otomatis tampil>
    # Kamar                 : <otomatis tampil>

    # Periode Pembayaran    : <otomatis tampil> 
    # Jumlah Pembayaran     : <otomatis tampil> 

    # Metode Pembayaran     : <otomatis tampil>
    # Nomor Nota / Ref.     : <otomatis tampil>

    # LAPORAN PEMBAYARAN
    # ID Penyewa            : PENYEWA1
    # Nama Penyewa          : Ivan Konev
    # Unit                  : KS01
    # Kamar                 : A1

    # Periode Pembayaran    : November 2025 sampai Januari 2025 (3 Bulan) 
    # Jumlah Pembayaran     : Rp 3000000 

    # Metode Pembayaran     : Cash/Transfer
    # Nomor Nota / Ref.     : 123

    # INPUT LAPORAN
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

    # Periode Pembayaran    : <otomatis tampil> -> <November 2025 sampai Januari 2025 (3 Bulan)>
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
    # print("=" * 75)
    print("LAPORAN PEMBAYARAN")
    print("=" * 75)

    id_input = input("Masukkan ID Penyewa : ")
    # print(laporan_bayar)
    for id_penyewa, data_laporan in laporan_bayar.items(): 
        if id_input == id_penyewa: 
            for key in data_laporan.keys(): 
                print(f"ID Laporan : {key}")

            # print(data_laporan['nama'])
            # print("")

    print("Masukkan ID Laporan yang ingin dilihat:")
    pilih_key = input("> ")

    for id_penyewa, data_laporan in laporan_bayar.items(): 
        if id_input == id_penyewa: 
            for key in data_laporan.keys(): 
                if pilih_key == key: 
                    print(f"ID Penyewa: {id_input}")
                    print(f"Nama Penyewa: {data_laporan[pilih_key]['nama']}")
                    print(f"Unit: {data_laporan[pilih_key]['unit']}")
                    print(f"Kamar: {data_laporan[pilih_key]['kamar']}")
                    print(f"Periode Pembayaran: {data_laporan[pilih_key]['jumlah_periode']} bulan")
                    print(f"Jumlah Pembayaran: {data_laporan[pilih_key]['jumlah_pembayaran']}")
                    print(f"Metode Pembayaran: {data_laporan[pilih_key]['metode_pembayaran'][0]}")
                    print(f"Nomor Nota / Ref.: {data_laporan[pilih_key]['metode_pembayaran'][1]}")

    input("Tekan Enter untuk kembali...")

# Lanjut

# aku nambahin fungsi buat liat tagihan mendatang
def lihat_tagihan_mendatang():
    while True: 
        clear()
        # print("=" * 75)
        print("TAGIHAN YANG AKAN DATANG")
        print("=" * 75)
        
        # ini buat dibuat kayak struk kebawah atau tetap ke samping kasih tau aja
        ada_tagihan = False
        for id_penyewa, data_penyewa in tagihan.items(): 
            if auth.id_login == id_penyewa: 
                for id_tagihan, data_tagihan in data_penyewa.items():
                    if data_tagihan['status'] == "BELUM BAYAR": 
                        print("tahun     :", data_tagihan["tahun"])
                        print("Bulan     :", data_tagihan["bulan"])
                        print("Jumlah    : Rp", data_tagihan["jumlah"])
                        print("Status    :", data_tagihan["status"])
                        print("-" * 75)
                        ada_tagihan = True                            
        
        if not ada_tagihan:
            print("Tidak ada tagihan yang akan datang.")
        
        input("Tekan Enter untuk kembali...")
        break

def riwayat_pembayaran():
    while True:
        clear()
        print("=" * 75)
        print("RIWAYAT PEMBAYARAN")
        print("=" * 75)

        ada_riwayat = False
        for id_penyewa, data_penyewa in tagihan.items(): 
            if auth.id_login == id_penyewa: 
                for id_tagihan, data_tagihan in data_penyewa.items():
                    if data_tagihan['status'] == "SUDAH BAYAR": 
                        print("tahun     :", data_tagihan["tahun"])
                        print("Bulan     :", data_tagihan["bulan"])
                        print("Jumlah    : Rp", data_tagihan["jumlah"])
                        print("Status    :", data_tagihan["status"])
                        print("-" * 75)
                        ada_riwayat = True                            
        
        if not ada_riwayat:
            print("Tidak ada tagihan yang akan datang.")

        input("Tekan ENTER untuk melanjutkan")
        break

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

    id_input = input("Masukkan ID Penyewa : ")
    # print(laporan_bayar)
    for id_penyewa, data_laporan in laporan_bayar.items(): 
        if id_input == id_penyewa: 
            for key in data_laporan.keys(): 
                print(f"ID Laporan : {key}")

            # print(data_laporan['nama'])
            # print("")

    print("Masukkan ID Laporan yang ingin dilihat:")
    pilih_key = input("> ")

    for id_penyewa, data_laporan in laporan_bayar.items(): 
        if id_input == id_penyewa: 
            for key in data_laporan.keys(): 
                if pilih_key == key: 
                    print(f"ID Penyewa: {id_input}")
                    print(f"Nama Penyewa: {data_laporan[pilih_key]['nama']}")
                    print(f"Unit: {data_laporan[pilih_key]['unit']}")
                    print(f"Kamar: {data_laporan[pilih_key]['kamar']}")
                    print(f"Periode Pembayaran: {data_laporan[pilih_key]['jumlah_periode']} bulan")
                    print(f"Jumlah Pembayaran: {data_laporan[pilih_key]['jumlah_pembayaran']}")
                    print(f"Metode Pembayaran: {data_laporan[pilih_key]['metode_pembayaran'][0]}")
                    print(f"Nomor Nota / Ref.: {data_laporan[pilih_key]['metode_pembayaran'][1]}")

    print("Apakah Anda Ingin Menghapus Laporan ini? (y/n)")
    konfir_hapus = input("> ")

    if konfir_hapus == "y": 
        del laporan_bayar[id_input][pilih_key]

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
        print("[3] - Lihat Riwayat Pembayaran")
        print("[4] - Hapus Bukti Pembayaran")
        print("[0] - Kembali ke Menu Sebelumnya")
        print("=" * 75)

        pilih = input("> ")

        if pilih == "0":
            break
        elif pilih == "1":
            buat_laporan_bayar()
        elif pilih == "2":
            lihat_tagihan_mendatang()
        elif pilih == "3":
            riwayat_pembayaran()
        elif pilih == "4":
            hapus_bukti_pembayaran()
        elif pilih == "5": 
            tampilkan_laporan_konfirmasi()
        else:
            print("Pilihan tidak valid.")