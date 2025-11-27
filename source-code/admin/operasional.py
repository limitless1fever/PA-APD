# Operasional Kos / Kontrakan
from fungsi.utilitas import clear
from akun import dataUser, tagihan

def buatTagihan():
    clear()
    print("BUAT TAGIHAN BULANAN")
    print("=" * 50)

    # Input bulan dan tahun secara manual
    print("Masukkan periode tagihan:")
    bulan = input("Bulan (contoh: November): ").strip()
    tahun = input("Tahun (contoh: 2025): ").strip()

    if not bulan or not tahun:
        print("Bulan dan tahun tidak boleh kosong!")
        input("Tekan Enter untuk kembali...")
        return

    # Validasi tahun (harus angka)
    if not tahun.isdigit():
        print("Tahun harus berupa angka (contoh: 2025)!")
        input("Tekan Enter untuk kembali...")
        return

    # Pilih penyewa
    print("\nPilih opsi:")
    print("[1] Buat tagihan untuk SEMUA penyewa aktif")
    print("[2] Buat tagihan untuk PENYEWA TERTENTU")
    pilih = input("> ").strip()

    target_penyewa = {}

    if pilih == "1":
        # Ambil semua penyewa aktif
        for user_id, data in dataUser.items():
            if data["akun"]["role"] == "MEMBER" and data["akun"].get("status") == "AKTIF":
                target_penyewa[user_id] = data["akun"]["nama"]
        if not target_penyewa:
            print("Tidak ada penyewa aktif!")
            input("Tekan Enter untuk kembali...")
            return

    elif pilih == "2":
        # Tampilkan daftar penyewa aktif (hanya nama)
        daftar_aktif = []
        for user_id, data in dataUser.items():
            if data["akun"]["role"] == "MEMBER" and data["akun"].get("status") == "AKTIF":
                nama = data["akun"]["nama"]
                daftar_aktif.append((user_id, nama))

        if not daftar_aktif:
            print("Tidak ada penyewa aktif!")
            input("Tekan Enter untuk kembali...")
            return

        print("\nDaftar Penyewa Aktif:")
        for i, (user_id, nama) in enumerate(daftar_aktif, start=1):
            print(f"{i}. {nama}")

        pilih_aktif = input("\nPilih nomor penyewa: ").strip()
        try:
            nomor_aktif = int(pilih_aktif)
            if nomor_aktif < 1 or nomor_aktif > len(daftar_aktif):
                raise ValueError
            user_id_pilih, nama_pilih = daftar_aktif[nomor_aktif - 1]
            target_penyewa = {user_id_pilih: nama_pilih}
        except ValueError:
            print("Nomor tidak valid!")
            input("Tekan Enter untuk kembali...")
            return

    else:
        print("Pilihan tidak valid!")
        input("Tekan Enter untuk kembali...")
        return

    # Input jumlah tagihan 
    try:
        jumlah_str = input("\nMasukkan jumlah tagihan (angka): ").strip()
        # Hapus titik/koma jika ada (misal: 1.500.000)
        jumlah_bersih = jumlah_str.replace(".", "").replace(",", "")
        jumlah = int(jumlah_bersih)
        if jumlah <= 0:
            print("Jumlah harus lebih dari 0!")
            input("Tekan Enter untuk kembali...")
            return
    except ValueError:
        print("Jumlah harus berupa angka!")
        input("Tekan Enter untuk kembali...")
        return

    # Buat tagihan untuk setiap penyewa
    periode = f"{bulan} {tahun}"
    tagihan_dibuat = 0

    for user_id in target_penyewa:
        # Pastikan ada entri tagihan untuk user ini
        if user_id not in tagihan:
            tagihan[user_id] = {}

        # Cek duplikasi: apakah sudah ada tagihan dengan bulan & tahun ini?
        sudah_ada = False
        for data_tagihan in tagihan[user_id].values():
            if data_tagihan["bulan"] == bulan and data_tagihan["tahun"] == tahun:
                sudah_ada = True
                break

        if sudah_ada:
            print(f"Tagihan untuk {target_penyewa[user_id]} pada {periode} sudah ada.")
            continue

        # Buat id tagihan baru: TGHN01, TGHN02, ...
        nomor = len(tagihan[user_id]) + 1
        id_tagihan = f"TGHN{nomor:02d}"

        # Simpan tagihan
        tagihan[user_id][id_tagihan] = {
            "bulan": bulan,
            "tahun": tahun,
            "jumlah": jumlah,
            "status": "BELUM BAYAR"
        }
        tagihan_dibuat += 1

    print(f"\nBerhasil membuat {tagihan_dibuat} tagihan untuk periode: {periode}")
    input("\nTekan Enter untuk kembali...")

def lihatKamar_kosong():
    clear()
    print("DAFTAR KAMAR KOSONG")
    print("=" * 50)

    semua_kamar = [
        "A1", "A2", "A3", "A4", "A5",
        "B1", "B2", "B3", "B4", "B5"
    ]

    # cek kamar yang sudah di tempati
    kamar_terisi = set()
    for user_id, data in dataUser.items():
        if data["akun"]["role"] == "MEMBER":
            if data["akun"].get("status") == "AKTIF":
                kamar = data["akun"].get("kamar", "").strip()
                if kamar and kamar in semua_kamar:
                    kamar_terisi.add(kamar)

    # hitung kamar kosong
    kamar_kosong = [kamar for kamar in semua_kamar if kamar not in kamar_terisi]

    # tampilkan hasil
    print(f"Total kamar       : {len(semua_kamar)}")
    print(f"Terisi            : {len(kamar_terisi)}")
    print(f"Kosong            : {len(kamar_kosong)}")
    print("-" * 50)

    if kamar_kosong:
        print("Daftar kamar kosong:")
        for i, kamar in enumerate(kamar_kosong, 1):
            print(f"{kamar:>4}", end="  ")
            if i % 5 == 0:  # ganti baris tiap 5 kamar
                print()
        if len(kamar_kosong) % 5 != 0:
            print()
    else:
        print("Semua kamar telah terisi!")

    print("=" * 50)
    input("Tekan Enter untuk kembali...")

def lihatTagihan_lunas():
    clear()
    print("LIHAT TAGIHAN PENYEWA")
    print("=" * 50)

    # Ambil daftar semua PENYEWA (role == "MEMBER")
    daftar_penyewa = []
    for user_id, user_data in dataUser.items():
        if user_data["akun"]["role"] == "MEMBER":
            daftar_penyewa.append((user_id, user_data["akun"]["nama"]))

    if not daftar_penyewa:
        print("Belum ada penyewa terdaftar.")
        input("Tekan Enter untuk kembali...")
        return

    print("Daftar Penyewa:")
    for i, (user_id, nama) in enumerate(daftar_penyewa, start=1):
        print(f"{i}. {nama}")

    print()
    pilih = input("Pilih nomor penyewa: ").strip()

    # Validasi input nomor
    try:
        nomor = int(pilih)
        if nomor < 1 or nomor > len(daftar_penyewa):
            raise ValueError
        user_id_pilih = daftar_penyewa[nomor - 1][0]  # Ambil id asli dari tuple(hanya sementara untuk menyimpan nama penyewa)
    except ValueError:
        print("Nomor tidak valid!")
        input("Tekan Enter untuk kembali...")
        return

    # Ambil tagihan penyewa
    tagihan_user = dataUser[user_id_pilih]["tagihan"]

    if not tagihan_user:
        print(f"Tidak ada tagihan untuk {daftar_penyewa[nomor - 1][1]}.")
    else:
        print(f"\nTagihan untuk {daftar_penyewa[nomor - 1][1]}:")
        for id_tagihan, data in tagihan_user.items():
            bulan = data["bulan"]
            tahun = data["tahun"]
            jumlah = data["jumlah"]
            status = data["status"]
            print(f"- {id_tagihan} | {bulan} {tahun} | Rp{jumlah:,} | {status}")
    input("\nTekan Enter untuk kembali...")

def lihatKeluhan_penyewa():
    clear()
    print("LAPORAN KELUHAN DARI PENYEWA")
    print("=" * 60)

    # Kumpulkan semua laporan dari penyewa
    semua_laporan = []

    for user_id, user_data in dataUser.items():
        if user_data["akun"]["role"] == "MEMBER":  # hanya penyewa
            nama = user_data["akun"]["nama"]
            kamar = user_data["akun"]["kamar"]
            laporan_dict = user_data["laporan_keluhan"]
            
            for id_laporan, data in laporan_dict.items():
                semua_laporan.append({
                    "id_penyewa": user_id,
                    "id_laporan": id_laporan,
                    "nama": nama,
                    "kamar": kamar,
                    "kategori": data.get("kategori", "-"),
                    "judul_laporan": data.get("judul_laporan", "-"),
                    "status": data.get("status", "-"),
                    "tanggal_dibuat": data.get("tanggal_dibuat", "-"),
                    "deskripsi_laporan": data.get("deskripsi_laporan", "-")
                })

    if not semua_laporan:
        print("Belum ada laporan keluhan dari penyewa.")
        input("\nTekan Enter untuk kembali...")
        return

    print(f"Ditemukan {len(semua_laporan)} laporan keluhan:\n")
    for i, laporan in enumerate(semua_laporan, start=1):
        print(f"[{i}] {laporan['nama']} - {laporan['judul_laporan']}")
        print(f"    Kamar    : {laporan['kamar']}")
        print(f"    Kategori : {laporan['kategori']}")
        print(f"    Status   : {laporan['status']}")
        print(f"    Tanggal  : {laporan['tanggal_dibuat']}")
        print("    Deskripsi:")
        print(f"      {laporan['deskripsi_laporan']}")
        print("-" * 60)

    # opsi ubah status
    print("\nIngin mengubah status keluhan?")
    print("[y] Ya   [t] Tidak")
    pilih = input("> ").strip().lower()

    if pilih == "y":
        try:
            nomor = int(input(f"\nMasukkan nomor laporan (1-{len(semua_laporan)}): ")) - 1
            if nomor < 0 or nomor >= len(semua_laporan):
                print("Nomor laporan tidak valid!")
            else:
                laporan_pilih = semua_laporan[nomor]
                id_penyewa = laporan_pilih["id_penyewa"]
                id_laporan = laporan_pilih["id_laporan"]

                # Ambil data asli dari dataUser
                laporan_asli = dataUser[id_penyewa]["laporan_keluhan"][id_laporan]

                if laporan_asli["status"] == "BELUM DITANGANI":
                    konfirmasi = input("Ubah status menjadi 'SUDAH DITANGANI'? (y/n): ").strip().lower()
                    if konfirmasi == "y":
                        laporan_asli["status"] = "SUDAH DITANGANI"
                        print("\nStatus keluhan berhasil diubah!")
                    else:
                        print("\nPerubahan dibatalkan.")
                else:
                    print("\nKeluhan ini sudah ditangani.")
        except ValueError:
            print("\nInput harus berupa angka!")
    
    input("\nTekan Enter untuk kembali...")

def editStatus():
    clear()
    print("UBAH STATUS TAGIHAN PENYEWA")
    print("=" * 60)

    # Kumpulkan penyewa yang punya tagihan
    daftar_penyewa = []
    for user_id, data in dataUser.items():
        if data["akun"]["role"] == "MEMBER" and data["tagihan"]:
            nama = data["akun"]["nama"]
            daftar_penyewa.append((user_id, nama))

    if not daftar_penyewa:
        print("Belum ada penyewa dengan tagihan.")
        input("Tekan Enter untuk kembali...")
        return

    # Tampilkan daftar penyewa (hanya nama)
    print("Daftar Penyewa:")
    for i, (user_id, nama) in enumerate(daftar_penyewa, start=1):
        print(f"{i}. {nama}")

    print()
    pilih_penyewa = input("Pilih nomor penyewa: ").strip()
    
    # Validasi pilihan penyewa
    try:
        nomor_penyewa = int(pilih_penyewa)
        if nomor_penyewa < 1 or nomor_penyewa > len(daftar_penyewa):
            raise ValueError
        user_id_pilih, nama_pilih = daftar_penyewa[nomor_penyewa - 1]
    except ValueError:
        print("Nomor penyewa tidak valid!")
        input("Tekan Enter untuk kembali...")
        return

    # Ambil tagihan penyewa
    tagihan_dict = dataUser[user_id_pilih]["tagihan"]
    daftar_tagihan = list(tagihan_dict.items())  # [(id_tag, data), ...]

    # Tampilkan daftar tagihan
    print(f"\nTagihan untuk {nama_pilih}:")
    for i, (id_tag, data) in enumerate(daftar_tagihan, start=1):
        periode = f"{data['bulan']} {data['tahun']}"
        print(f"{i}. {periode} | Rp{data['jumlah']:,} | {data['status']}")

    print()
    pilih_tagihan = input("Pilih nomor tagihan yang ingin diubah: ").strip()

    # Validasi pilihan tagihan
    try:
        nomor_tagihan = int(pilih_tagihan)
        if nomor_tagihan < 1 or nomor_tagihan > len(daftar_tagihan):
            raise ValueError
        id_tag_target, data_tag_target = daftar_tagihan[nomor_tagihan - 1]
    except ValueError:
        print("Nomor tagihan tidak valid!")
        input("Tekan Enter untuk kembali...")
        return

    # Cek apakah sudah lunas
    if data_tag_target["status"] == "SUDAH BAYAR":
        print("Tagihan ini sudah lunas!")
        input("Tekan Enter untuk kembali...")
        return

    # Konfirmasi perubahan
    periode_tampil = f"{data_tag_target['bulan']} {data_tag_target['tahun']}"
    print(f"\nAnda akan mengubah status tagihan '{periode_tampil}' menjadi 'SUDAH BAYAR'.")
    konfirmasi = input("Lanjutkan? (y/n): ").strip().lower()
    
    if konfirmasi == "y":
        dataUser[user_id_pilih]["tagihan"][id_tag_target]["status"] = "SUDAH BAYAR"
        print(f"\nStatus berhasil diubah menjadi 'SUDAH BAYAR'.")
    else:
        print("\nPerubahan dibatalkan.")

    input("\nTekan Enter untuk kembali...")

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
        else:
            print("Pilihan Tidak Valid")
            input("Tekan Enter Untuk Kembali...")