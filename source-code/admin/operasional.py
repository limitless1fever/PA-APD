# Operasional Kos / Kontrakan
from fungsi.utilitas import clear
from akun import dataUser, tagihan

def buatTagihan():
    clear()
    print("BUAT TAGIHAN BULANAN")
    print("=" * 50)

    # === 1. Input bulan dan tahun secara manual ===
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

    # === 2. Pilih target penyewa ===
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
        # Tampilkan daftar penyewa aktif
        print("\nDaftar Penyewa Aktif:")
        penyewa_aktif = {}
        for user_id, data in dataUser.items():
            if data["akun"]["role"] == "MEMBER" and data["akun"].get("status") == "AKTIF":
                nama = data["akun"]["nama"]
                penyewa_aktif[user_id] = nama
                print(f"- {user_id} ({nama})")

        if not penyewa_aktif:
            print("Tidak ada penyewa aktif!")
            input("Tekan Enter untuk kembali...")
            return

        user_id_pilih = input("\nMasukkan ID Penyewa: ").strip()
        if user_id_pilih not in penyewa_aktif:
            print("ID Penyewa tidak valid!")
            input("Tekan Enter untuk kembali...")
            return
        target_penyewa = {user_id_pilih: penyewa_aktif[user_id_pilih]}

    else:
        print("Pilihan tidak valid!")
        input("Tekan Enter untuk kembali...")
        return

    # === 3. Input jumlah tagihan ===
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

    # === 4. Buat tagihan untuk setiap target ===
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
            print(f"⚠️  Tagihan untuk {target_penyewa[user_id]} pada {periode} sudah ada.")
            continue

        # Buat ID tagihan baru: TGHN01, TGHN02, ...
        nomor = len(tagihan[user_id]) + 1
        id_tagihan = f"TGHN{nomor:02d}"  # → TGHN01, TGHN02, dst.

        # Simpan tagihan
        tagihan[user_id][id_tagihan] = {
            "bulan": bulan,
            "tahun": tahun,
            "jumlah": jumlah,
            "status": "BELUM BAYAR"
        }
        tagihan_dibuat += 1

    # === 5. Selesai ===
    print(f"\nBerhasil membuat {tagihan_dibuat} tagihan untuk periode: {periode}")
    input("\nTekan Enter untuk kembali...")

def lihatKamar_kosong():
    clear()
    print("DAFTAR KAMAR KOSONG")
    print("=" * 50)

    # === 1. DEFINISI SEMUA KAMAR YANG TERSEDIA ===
    # Kamu bisa sesuaikan ini sesuai kontrakanmu
    SEMUA_KAMAR = [
        "A1", "A2", "A3", "A4", "A5",
        "B1", "B2", "B3", "B4", "B5"
    ]

    # === 2. KUMPULKAN KAMAR YANG SUDAH DITEMPATI ===
    kamar_terisi = set()
    for user_id, data in dataUser.items():
        if data["akun"]["role"] == "MEMBER":
            if data["akun"].get("status") == "AKTIF":
                kamar = data["akun"].get("kamar", "").strip()
                if kamar and kamar in SEMUA_KAMAR:
                    kamar_terisi.add(kamar)

    # === 3. HITUNG KAMAR KOSONG ===
    kamar_kosong = [kamar for kamar in SEMUA_KAMAR if kamar not in kamar_terisi]

    # === 4. TAMPILKAN HASIL ===
    print(f"Total kamar       : {len(SEMUA_KAMAR)}")
    print(f"Terisi            : {len(kamar_terisi)}")
    print(f"Kosong            : {len(kamar_kosong)}")
    print("-" * 50)

    if kamar_kosong:
        print("Daftar kamar kosong:")
        # Tampilkan dalam format rapi (5 kolom)
        for i, kamar in enumerate(kamar_kosong, 1):
            print(f"{kamar:>4}", end="  ")
            if i % 5 == 0:  # ganti baris tiap 5 kamar
                print()
        if len(kamar_kosong) % 5 != 0:
            print()  # newline akhir
    else:
        print("Semua kamar telah terisi!")

    print("=" * 50)
    input("Tekan Enter untuk kembali...")

def lihatTagihan_lunas():
    clear()
    print("LIHAT TAGIHAN PENYEWA")
    print("=" * 50)

    # Ambil daftar semua PENYEWA (role == "MEMBER")
    daftar_penyewa = {}
    for user_id, user_data in dataUser.items():
        if user_data["akun"]["role"] == "MEMBER":
            daftar_penyewa[user_id] = user_data

    if not daftar_penyewa:
        print("Belum ada penyewa terdaftar.")
        input("Tekan Enter untuk kembali...")
        return

    # Tampilkan daftar penyewa
    print("Daftar Penyewa:")
    for user_id in daftar_penyewa:
        nama = daftar_penyewa[user_id]["akun"]["nama"]
        print(f"- {user_id} ({nama})")

    print()
    user_id_pilih = input("Masukkan ID Penyewa (contoh: PENYEWA1): ").strip()

    if not user_id_pilih:
        print("ID tidak boleh kosong!")
        input("Tekan Enter untuk kembali...")
        return

    if user_id_pilih not in daftar_penyewa:
        print("ID Penyewa tidak ditemukan.")
        print("Pastikan mengetik sesuai daftar di atas.")
        input("Tekan Enter untuk kembali...")
        return

    # Ambil tagihan penyewa
    tagihan_user = daftar_penyewa[user_id_pilih]["tagihan"]

    if not tagihan_user:
        print(f"Tidak ada tagihan untuk {user_id_pilih}.")
    else:
        print(f"\nTagihan untuk {user_id_pilih}:")
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
                    "nama": nama,
                    "kamar": kamar,
                    "id_laporan": id_laporan,
                    **data
                })

    if not semua_laporan:
        print("Belum ada laporan keluhan dari penyewa.")
        input("\nTekan Enter untuk kembali...")
        return

    print(f"Ditemukan {len(semua_laporan)} laporan keluhan:\n")
    for i, laporan in enumerate(semua_laporan, start=1):
        print(f"[{i}] ID Laporan : {laporan['id_laporan']}")
        print(f"    Dari        : {laporan['nama']} ({laporan['id_penyewa']})")
        print(f"    Kamar       : {laporan['kamar']}")
        print(f"    Kategori    : {laporan['kategori']}")
        print(f"    Judul       : {laporan['judul_laporan']}")
        print(f"    Status      : {laporan['status']}")
        print(f"    Tanggal     : {laporan['tanggal_dibuat']}")
        print("    Deskripsi   :")
        print(f"      {laporan['deskripsi_laporan']}")
        print("-" * 60)

    # === OPSI UBAH STATUS ===
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
                    print("\nℹKeluhan ini sudah ditangani.")
        except ValueError:
            print("\nInput harus berupa angka!")
    
    input("\nTekan Enter untuk kembali...")

# Asli aku belum tambahin error handling nya baru logika utamanya jadi agak kurang 
def editStatus():
    clear()
    print("UBAH STATUS TAGIHAN PENYEWA")
    print("=" * 60)

    penyewa_dengan_tagihan = {}
    for user_id, data in dataUser.items():
        if data["akun"]["role"] == "MEMBER" and data["tagihan"]:
            penyewa_dengan_tagihan[user_id] = data

    if not penyewa_dengan_tagihan:
        print("Belum ada penyewa dengan tagihan.")
        input("Tekan Enter untuk kembali...")
        return

    print("Daftar Penyewa:")
    for user_id in penyewa_dengan_tagihan:
        nama = penyewa_dengan_tagihan[user_id]["akun"]["nama"]
        print(f"- {user_id} ({nama})")

    print()
    user_id_pilih = input("Masukkan ID Penyewa (contoh: PENYEWA1): ").strip()
    if not user_id_pilih or user_id_pilih not in penyewa_dengan_tagihan:
        print("ID Penyewa tidak valid!")
        input("Tekan Enter untuk kembali...")
        return

    tagihan_dict = penyewa_dengan_tagihan[user_id_pilih]["tagihan"]
    print(f"\nTagihan untuk {user_id_pilih}:")
    daftar_periode = []
    for id_tag, data in tagihan_dict.items():
        periode = f"{data['bulan']} {data['tahun']}"
        daftar_periode.append(periode)
        print(f"- {id_tag} | {periode} | Rp{data['jumlah']:,} | {data['status']}")

    print("\nMasukkan periode persis seperti di atas (contoh: November 2025)")
    input_periode = input("Periode: ").strip()
    if not input_periode or input_periode not in daftar_periode:
        print("Periode tidak valid!")
        input("Tekan Enter untuk kembali...")
        return

    # Cari ID tagihan
    id_target = next(
        id_tag for id_tag, data in tagihan_dict.items()
        if f"{data['bulan']} {data['tahun']}" == input_periode
    )
    tagihan_sekarang = tagihan_dict[id_target]

    if tagihan_sekarang["status"] == "SUDAH BAYAR":
        print("Tagihan ini sudah lunas!")
        input("Tekan Enter untuk kembali...")
        return

    # KONFIRMASI
    while True:
        konfirmasi = input("Ubah status menjadi 'SUDAH BAYAR'? (y/n): ").strip().lower()
        if konfirmasi == "y":
            tagihan_sekarang["status"] = "SUDAH BAYAR"
            print(f"\nBerhasil! Status '{input_periode}' diubah menjadi 'SUDAH BAYAR'.")
            break
        elif konfirmasi == "n":
            print("\nPerubahan dibatalkan.")
            break
        else:
            print("Input tidak valid. Ketik 'y' (ya) atau 'n' (tidak).")
    
    input("\nTekan Enter untuk kembali...")

def cetakLaporan():
    clear()
    print("CETAK LAPORAN KEUANGAN")
    print("=" * 70)

    # === 1. DAFTAR PENYEWA AKTIF ===
    print("\n1. DAFTAR PENYEWA AKTIF")
    print("-" * 50)
    penyewa_aktif = 0
    for user_id, data in dataUser.items():
        if data["akun"]["role"] == "MEMBER":
            if data["akun"].get("status") == "AKTIF":
                nama = data["akun"]["nama"]
                kamar = data["akun"]["kamar"]
                tgl_gabung = data["akun"].get("tanggal_gabung", "–")
                print(f"• {nama} | Kamar: {kamar} | Sejak: {tgl_gabung}")
                penyewa_aktif += 1

    if penyewa_aktif == 0:
        print("– Tidak ada penyewa aktif.")

    # === 2. TAGIHAN BELUM LUNAS ===
    print("\n2. TAGIHAN BELUM LUNAS")
    print("-" * 50)
    tagihan_belum_lunas = 0
    for user_id, data in dataUser.items():
        if data["akun"]["role"] == "MEMBER":
            nama = data["akun"]["nama"]
            for id_tagihan, tag in data["tagihan"].items():
                if tag["status"] == "BELUM BAYAR":
                    periode = f"{tag['bulan']} {tag['tahun']}"
                    print(f"• {nama} ({user_id}) | {periode} | Rp{tag['jumlah']:,}")
                    tagihan_belum_lunas += 1

    if tagihan_belum_lunas == 0:
        print("– Semua tagihan telah lunas.")

    # === 3. LAPORAN KELUHAN BELUM DITANGANI ===
    print("\n3. LAPORAN KELUHAN BELUM DITANGANI")
    print("-" * 50)
    keluhan_terbuka = 0
    for user_id, data in dataUser.items():
        if data["akun"]["role"] == "MEMBER":
            nama = data["akun"]["nama"]
            for id_laporan, laporan in data["laporan_keluhan"].items():
                if laporan["status"] == "BELUM DITANGANI":
                    print(f"• [{id_laporan}] {nama} | {laporan['judul_laporan']}")
                    print(f"  Kategori: {laporan['kategori']} | Tgl: {laporan['tanggal_dibuat']}")
                    keluhan_terbuka += 1

    if keluhan_terbuka == 0:
        print("– Tidak ada keluhan yang perlu ditangani.")

    # === PENUTUP ===
    print("\n" + "=" * 70)
    print("Laporan ini dicetak secara otomatis oleh sistem.")
    print(f"Tanggal: Kamis, 27 November 2025")  # sesuaikan dengan datetime jika perlu
    print("=" * 70)

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