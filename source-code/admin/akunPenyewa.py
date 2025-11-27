from fungsi.utilitas import clear
from akun import dataUser, tagihan, dataPenyewa, laporan_keluhan, laporan_bayar

def tambahPenyewa():
    clear()
    print("=" * 75)
    print("REGISTRASI PENYEWA BARU")
    print("=" * 75)

    # Input username & password
    username = input(f"{'Masukkan username':<40}: ").strip()
    password = input(f"{'Masukkan password':<40}: ").strip()

    if not username or not password:
        print("\nUsername dan password tidak boleh kosong!")
        input("Tekan Enter untuk kembali...")
        return False

    # Cek duplikat username
    for info in dataPenyewa.values():
        if info.get("username") == username:
            print("\nUsername sudah digunakan! Silakan pilih yang lain.")
            input("Tekan Enter untuk kembali...")
            return False

    print("\n" + "=" * 75)
    print("LENGKAPI DATA PENYEWA")
    print("=" * 75)

    nama = input(f"{'Nama Lengkap':<40}: ").strip()
    kontak = input(f"{'Kontak (No. HP)':<40}: ").strip()
    email = input(f"{'Email':<40}: ").strip()
    tanggal_gabung = input(f"{'Tanggal Gabung (contoh: 27 November 2025)':<40}: ").strip()
    kamar = input(f"{'Nomor Kamar':<40}: ").strip()

    if not all([nama, kontak, email, tanggal_gabung, kamar]):
        print("\nSemua data wajib diisi!")
        input("Tekan Enter untuk kembali...")
        return False

    # hitung hanya penyewa (abaikan admin)
    jumlah_penyewa = sum(1 for data in dataPenyewa.values() if data.get("role") == "MEMBER")
    id_baru = f"PENYEWA{jumlah_penyewa + 1}"

    # Simpan ke dataPenyewa
    dataPenyewa[id_baru] = {
        "username": username,
        "password": password,
        "role": "MEMBER",
        "nama": nama,
        "kontak": kontak,
        "email": email,
        "tanggal_gabung": tanggal_gabung,
        "status": "AKTIF",
        "kamar": kamar
    }

    # menambahkan data baru ke dict
    tagihan[id_baru] = {}
    laporan_keluhan[id_baru] = {}
    laporan_bayar[id_baru] = {}

    #Perbarui dataUser jika digunakan
    if 'dataUser' in globals():
        dataUser[id_baru] = {
            "akun": dataPenyewa[id_baru],
            "tagihan": tagihan[id_baru],
            "laporan_keluhan": laporan_keluhan[id_baru],
            "laporan_bayar": laporan_bayar[id_baru],
        }

    print(f"\nRegistrasi berhasil! ID Penyewa: {id_baru}")
    print("Silakan login dengan akun Anda.")
    input("Tekan Enter untuk melanjutkan...")
    clear()
    return True

def lihatPenyewa(): 
    clear()
    print("=" * 100)
    print("LIHAT DATA PENYEWA")
    print("=" * 100)

    # Kumpulkan semua penyewa (role == "MEMBER")
    daftar_penyewa = []
    for id_penyewa, data in dataPenyewa.items():
        if data.get("role") == "MEMBER":
            daftar_penyewa.append((id_penyewa, data))

    if not daftar_penyewa:
        print("Belum ada penyewa terdaftar.")
        print("=" * 100)
        input("Tekan Enter untuk kembali... ")
        return

    print(f"{'No':<5} {'Nama Lengkap':<25} {'Kontak':<15} {'Tanggal Gabung':<20} {'Status':<15} {'Kamar':<10}")
    print("-" * 100)

    # Tampilkan data
    for i in range(len(daftar_penyewa)):
        id_penyewa, data = daftar_penyewa[i]
        nama = data.get("nama", "-")
        kontak = data.get("kontak", "-")
        tgl_gabung = data.get("tanggal_gabung", "-")
        status = data.get("status", "-")
        kamar = data.get("kamar", "-")
        
        print(f"{i + 1:<5} {nama:<25} {kontak:<15} {tgl_gabung:<20} {status:<15} {kamar:<10}")

    print("=" * 100)
    input("Tekan Enter untuk kembali... ")

def editPenyewa(): 
    while True: 
        try: 
            clear()
            print("=" * 100)
            print("EDIT DATA PENYEWA")
            print("=" * 100)

            # Kumpulkan semua penyewa (role == "MEMBER")
            daftar_penyewa = []
            for id_penyewa, data in dataPenyewa.items():
                if data.get("role") == "MEMBER":
                    daftar_penyewa.append((id_penyewa, data))

            if not daftar_penyewa:
                print("Tidak ada penyewa untuk diedit.")
                input("Tekan Enter untuk kembali...")
                break

            # Tampilkan daftar
            print(f"{'No':<5} {'Nama Lengkap':<25} {'Kontak':<15} {'Tanggal Gabung':<20} {'Status':<15} {'Kamar':<10}")
            print("-" * 100)
            for i in range(len(daftar_penyewa)):
                id_penyewa, data = daftar_penyewa[i]
                nama = data.get("nama", "-")
                kontak = data.get("kontak", "-")
                tgl_gabung = data.get("tanggal_gabung", "-")
                status = data.get("status", "-")
                kamar = data.get("kamar", "-")
                print(f"{i + 1:<5} {nama:<25} {kontak:<15} {tgl_gabung:<20} {status:<15} {kamar:<10}")

            print("-" * 100)
            print("0. Keluar")
            print("=" * 100)

            pilih = input("Pilih nomor penyewa yang ingin diubah: ").strip()
            print("=" * 100)

            if pilih == "0": 
                break

            try:
                nomor = int(pilih)
                if nomor < 1 or nomor > len(daftar_penyewa):
                    raise ValueError
                # Ambil id asli berdasarkan nomor urut
                pilih_menu = daftar_penyewa[nomor - 1][0]
            except ValueError:
                print("\nNomor tidak valid!")
                input("Tekan Enter untuk lanjut...")
                continue

            # Ambil data penyewa yang dipilih
            info_penyewa = dataPenyewa[pilih_menu]

            while True: 
                clear()
                print("=" * 75)
                print("INFORMASI PENYEWA YANG DAPAT DIUBAH")
                print("=" * 75)

                print(f"{'1 - Nama Penyewa':<30}: {info_penyewa.get('nama', '-')}")
                print(f"{'2 - Kontak Penyewa':<30}: {info_penyewa.get('kontak', '-')}")
                print(f"{'3 - Tanggal Gabung':<30}: {info_penyewa.get('tanggal_gabung', '-')}")
                print(f"{'4 - Status Penyewa':<30}: {info_penyewa.get('status', '-')}")

                print("=" * 75)
                print("0 - Keluar")
                print("=" * 75)

                pilih_edit = input("Masukkan bagian yang ingin diubah: ").strip()
                print("=" * 75)

                if pilih_edit == "0": 
                    break
                elif pilih_edit == "1": 
                    while True: 
                        clear()
                        print("=" * 75)
                        print("EDIT NAMA PENYEWA")
                        print("=" * 75)
                        print(f"{'Nama Lama':<30} : {info_penyewa.get('nama', '-')}")
                        ganti_nama = input(f"{'Masukkan nama baru':<30} : ").strip()
                        if ganti_nama:
                            dataPenyewa[pilih_menu]["nama"] = ganti_nama
                            print("Nama berhasil diubah!")
                            input("Tekan Enter untuk lanjut...")
                            break
                        else: 
                            print("\nNama tidak boleh kosong!")
                            input("Tekan Enter untuk ulang...")

                elif pilih_edit == "2": 
                    while True: 
                        clear()
                        print("=" * 75)
                        print("EDIT KONTAK PENYEWA")
                        print("=" * 75)
                        print(f"{'Kontak Lama':<30} : {info_penyewa.get('kontak', '-')}")
                        ganti_kontak = input(f"{'Masukkan kontak baru':<30} : ").strip()
                        if ganti_kontak:
                            dataPenyewa[pilih_menu]["kontak"] = ganti_kontak
                            print("Kontak berhasil diubah!")
                            input("Tekan Enter untuk lanjut...")
                            break
                        else: 
                            print("\nKontak tidak boleh kosong!")
                            input("Tekan Enter untuk ulang...")

                elif pilih_edit == "3": 
                    while True: 
                        clear()
                        print("=" * 75)
                        print("EDIT TANGGAL GABUNG PENYEWA")
                        print("=" * 75)
                        print(f"{'Tanggal Gabung Lama':<30} : {info_penyewa.get('tanggal_gabung', '-')}")
                        ganti_tanggal = input(f"{'Masukkan Tanggal Gabung baru':<30} : ").strip()
                        if ganti_tanggal:
                            dataPenyewa[pilih_menu]["tanggal_gabung"] = ganti_tanggal
                            print("Tanggal gabung berhasil diubah!")
                            input("Tekan Enter untuk lanjut...")
                            break
                        else: 
                            print("\nTanggal tidak boleh kosong!")
                            input("Tekan Enter untuk ulang...")

                elif pilih_edit == "4": 
                    while True: 
                        clear()
                        print("=" * 75)
                        print("EDIT STATUS PENYEWA")
                        print("=" * 75)
                        print(f"{'Status Sebelumnya':<45} : {info_penyewa.get('status', '-')}")
                        print("Pilih: [1] AKTIF  [2] TIDAK AKTIF")
                        pilihan_status = input("Masukkan pilihan: ").strip()
                        
                        if pilihan_status == "1":
                            dataPenyewa[pilih_menu]["status"] = "AKTIF"
                            print("Status diubah menjadi: AKTIF")
                            input("Tekan Enter untuk lanjut...")
                            break
                        elif pilihan_status == "2":
                            dataPenyewa[pilih_menu]["status"] = "TIDAK AKTIF"
                            print("Status diubah menjadi: TIDAK AKTIF")
                            input("Tekan Enter untuk lanjut...")
                            break
                        else:
                            print("\nPilihan tidak valid! Masukkan 1 atau 2.")
                            input("Tekan Enter untuk ulang...")

                else: 
                    print("\nPilihan tidak valid!")
                    input("Tekan Enter untuk lanjut...")

        except Exception as e:
            print(f"\nTerjadi kesalahan: {e}")
            input("Tekan Enter untuk lanjut...")

def hapusPenyewa():
    while True:
        try:
            clear()
            print("=" * 100)
            print("HAPUS PENYEWA")
            print("=" * 100)

            # Kumpulkan semua penyewa (role == "MEMBER")
            daftar_penyewa = []
            for id_penyewa, data in dataPenyewa.items():
                if data.get("role") == "MEMBER":
                    daftar_penyewa.append((id_penyewa, data))

            if not daftar_penyewa:
                print("Tidak ada penyewa untuk dihapus.")
                input("Tekan Enter untuk kembali...")
                break

            # Tampilkan dengan nomor urut 1, 2, 3, ... (sesuai urutan di dictionary)
            print(f"{'No':<5} {'ID Penyewa':<15} {'Nama Lengkap':<25} {'Kamar':<10} {'Status':<15}")
            print("-" * 100)
            for i in range(len(daftar_penyewa)):
                id_penyewa, data = daftar_penyewa[i]
                nama = data.get("nama", "-")
                kamar = data.get("kamar", "-")
                status = data.get("status", "-")
                print(f"{i + 1:<5} {id_penyewa:<15} {nama:<25} {kamar:<10} {status:<15}")

            print("-" * 100)
            print("0. Kembali")
            print("=" * 100)

            pilih = input("Pilih nomor penyewa yang ingin dihapus: ").strip()

            if pilih == "0":
                break

            try:
                nomor = int(pilih)
                if nomor < 1 or nomor > len(daftar_penyewa):
                    raise ValueError
                id_hapus = daftar_penyewa[nomor - 1][0]
            except ValueError:
                print("\nNomor tidak valid!")
                input("Tekan Enter untuk lanjut...")
                continue

            # Konfirmasi
            data_hapus = dataPenyewa[id_hapus]
            print(f"\nAnda akan menghapus:")
            print(f"  ID    : {id_hapus}")
            print(f"  Nama  : {data_hapus.get('nama', '-')}")
            print(f"  Kamar : {data_hapus.get('kamar', '-')}")
            print()

            konfirmasi = input("Yakin hapus? Semua data terkait juga akan dihapus! (y/n): ").strip().lower()
            if konfirmasi != "y":
                print("Penghapusan dibatalkan.")
                input("Tekan Enter untuk lanjut...")
                continue

            # Hapus dari semua struktur data
            for dict_global in [dataPenyewa, tagihan, laporan_keluhan, laporan_bayar, dataUser]:
                if id_hapus in dict_global:
                    del dict_global[id_hapus]

            print(f"\nPenyewa {id_hapus} berhasil dihapus.")
            input("Tekan Enter untuk lanjut...")

        except Exception as e:
            print(f"\nTerjadi kesalahan: {e}")
            input("Tekan Enter untuk lanjut...")
        break

def akunPenyewa(): 
    while True: 
        try: 
            clear()

            print("=" * 75)
            print("DATA DAN AKUN PENYEWA")
            print("=" * 75)

            print("[1] - Tambah Penyewa")
            print("[2] - Lihat Data Penyewa")
            print("[3] - Edit Data Penyewa")
            print("[4] - Hapus Data Penyewa")
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
                tambahPenyewa()
            elif pilih_menu == "2": 
                clear()
                lihatPenyewa()
            elif pilih_menu == "3": 
                clear()
                editPenyewa()
            elif pilih_menu == "4": 
                clear()
                hapusPenyewa()
            else: 
                raise ValueError("Pilihan Tidak Valid")

        except ValueError as e: 
            print("=" * 75)
            print(e)
            print("=" * 75)
            clear()