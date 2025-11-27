# Manajemen Pembayaran & Tagihan
from fungsi.utilitas import clear
import auth
from akun import dataUser

def buat_laporan_bayar():
    clear()
    print("=" * 75)
    print("FORMULIR LAPORAN PEMBAYARAN")
    print("=" * 75)

    input_id = input("Masukkan ID Anda (contoh: PENYEWA1): ")
    print()

    # Cek apakah id ada di dataUser
    if input_id not in dataUser:
        print("ID tidak ditemukan!")
        input("Tekan Enter untuk kembali...")
        return

    user = dataUser[input_id]
    akun = user["akun"]

    # Hanya penyewa (MEMBER) yang boleh buat laporan bayar
    if akun["role"] != "MEMBER":
        print("Hanya penyewa yang dapat membuat laporan pembayaran.")
        input("Tekan Enter untuk kembali...")
        return

    nama_laporan = akun["nama"]
    kamar_laporan = akun["kamar"]

    print("Nama Penyewa :", nama_laporan)
    print("Kamar        :", kamar_laporan)
    print()

    # Ambil tagihan BELUM BAYAR
    tagihan_penyewa = user["tagihan"]
    tagihan_belum_bayar = []

    for id_tagihan, data_tagihan in tagihan_penyewa.items():
        if data_tagihan["status"] == "BELUM BAYAR":
            tagihan_belum_bayar.append((id_tagihan, data_tagihan))

    if not tagihan_belum_bayar:
        print("Tidak ada tagihan yang perlu dibayar.")
        input("Tekan Enter untuk kembali...")
        return

    # Tampilkan opsi periode
    print("Pilih periode pembayaran")
    print("Note: 1 Periode = 1 Bulan")
    print()
    for i, (_, data) in enumerate(tagihan_belum_bayar, start=1):
        print(f"{i}. {data['bulan']} {data['tahun']} (Rp {data['jumlah']:,})")

    print()
    try:
        jumlah_bayar = int(input("Masukkan jumlah periode yang ingin dibayar (angka): "))
        if jumlah_bayar <= 0 or jumlah_bayar > len(tagihan_belum_bayar):
            print("Jumlah periode tidak valid!")
            input("Tekan Enter untuk kembali...")
            return
    except ValueError:
        print("Input harus berupa angka!")
        input("Tekan Enter untuk kembali...")
        return

    # Hitung total dan kumpulkan data
    total_bayar = 0
    periode_list = []
    tagihan_dibayar_ids = []

    for i in range(jumlah_bayar):
        id_tagihan, data = tagihan_belum_bayar[i]
        total_bayar += data["jumlah"]
        periode_list.append(f"{data['bulan']} {data['tahun']}")
        tagihan_dibayar_ids.append(id_tagihan)

    print()
    if jumlah_bayar == 1:
        print(f"Periode Pembayaran: {periode_list[0]}")
    else:
        print(f"Periode Pembayaran: {periode_list[0]} sampai {periode_list[-1]}")
    print(f"Jumlah Pembayaran  : Rp {total_bayar:,}")
    print()

    # Metode pembayaran
    print("Metode Pembayaran")
    print("[1] CASH     [2] TRANSFER")
    pilih_pembayaran = input("> ")
    print()

    if pilih_pembayaran == "1":
        info_pembayaran = ["CASH", input("Masukkan Nomor Nota: ")]
    elif pilih_pembayaran == "2":
        info_pembayaran = ["TRANSFER", input("Masukkan Nomor Referensi: ")]
    else:
        print("Metode pembayaran tidak valid!")
        input("Tekan Enter untuk kembali...")
        return

    # Buat laporan baru
    laporan_aktif = user["laporan_bayar"]
    id_laporan_baru = f"LB-{len(laporan_aktif) + 1}"

    laporan_aktif[id_laporan_baru] = {
        "nama": nama_laporan,
        "kamar": kamar_laporan,
        "jumlah_periode": str(jumlah_bayar),
        "periode": periode_list,
        "jumlah_pembayaran": total_bayar,
        "metode_pembayaran": info_pembayaran,
    }

    # Update status tagihan
    for id_tagihan in tagihan_dibayar_ids:
        user["tagihan"][id_tagihan]["status"] = "SUDAH BAYAR"

    print()
    print("Laporan pembayaran berhasil dibuat!")
    print("Status tagihan telah diperbarui.")
    input("Tekan Enter untuk melanjutkan...")
    clear()

def tampilkan_laporan_konfirmasi():
    clear()
    print("LAPORAN PEMBAYARAN")
    print("=" * 75)

    id_input = input("Masukkan ID Penyewa (contoh: PENYEWA1): ").strip()
    print()

    # Cek apakah id ada di dataUser
    if id_input not in dataUser:
        print("ID Penyewa tidak ditemukan!")
        input("Tekan Enter untuk kembali...")
        return

    user = dataUser[id_input]
    akun = user["akun"]

    # Pastikan ini penyewa
    if akun["role"] != "MEMBER":
        print("ID tersebut milik admin. Tidak ada laporan pembayaran.")
        input("Tekan Enter untuk kembali...")
        return

    laporan_bayar_penyewa = user["laporan_bayar"]

    if not laporan_bayar_penyewa:
        print("Penyewa ini belum memiliki laporan pembayaran.")
        input("Tekan Enter untuk kembali...")
        return

    # Tampilkan daftar id laporan
    print("Daftar Laporan Pembayaran:")
    for id_laporan in laporan_bayar_penyewa.keys():
        print(f" - {id_laporan}")

    print()
    pilih_key = input("Masukkan ID Laporan yang ingin dilihat: ").strip()

    if pilih_key not in laporan_bayar_penyewa:
        print("ID Laporan tidak ditemukan!")
        input("Tekan Enter untuk kembali...")
        return

    # Ambil data laporan
    laporan = laporan_bayar_penyewa[pilih_key]

    print("\n" + "=" * 50)
    print("DETAIL LAPORAN PEMBAYARAN")
    print("=" * 50)
    print(f"ID Penyewa         : {id_input}")
    print(f"Nama Penyewa       : {laporan['nama']}")
    print(f"Kamar              : {laporan['kamar']}")
    print(f"Jumlah Periode     : {laporan['jumlah_periode']} bulan")
    print(f"Periode            : {', '.join(laporan['periode'])}")
    print(f"Jumlah Pembayaran  : Rp {laporan['jumlah_pembayaran']:,}")
    print(f"Metode Pembayaran  : {laporan['metode_pembayaran'][0]}")
    print(f"Nomor Nota/Ref.    : {laporan['metode_pembayaran'][1]}")
    print("=" * 50)

    input("\nTekan Enter untuk kembali...")

def lihat_tagihan_mendatang():
    clear()
    print("TAGIHAN YANG AKAN DATANG")
    print("=" * 50)

    id_login = auth.id_login #menyimpan id user

    if id_login not in dataUser:
        print("Error: Pengguna tidak ditemukan.")
        input("Tekan Enter untuk kembali...")
        return

    user = dataUser[id_login]
    akun = user["akun"]

    # Hanya tampilkan jika ini penyewa
    if akun["role"] != "MEMBER":
        print("Anda adalah admin. Tidak memiliki tagihan.")
        input("Tekan Enter untuk kembali...")
        return

    tagihan_belum_bayar = []
    for id_tagihan, data_tagihan in user["tagihan"].items():
        if data_tagihan["status"] == "BELUM BAYAR":
            tagihan_belum_bayar.append(data_tagihan)

    if not tagihan_belum_bayar:
        print("Tidak ada tagihan yang akan datang.")
    else:
        for i, t in enumerate(tagihan_belum_bayar, start=1):
            print(f"Tagihan #{i}")
            print(f"  Bulan     : {t['bulan']}")
            print(f"  Tahun     : {t['tahun']}")
            print(f"  Jumlah    : Rp {t['jumlah']:,}")
            print(f"  Status    : {t['status']}")
            print("-" * 50)

    input("\nTekan Enter untuk kembali...")

def riwayat_pembayaran():
    clear()
    print("RIWAYAT PEMBAYARAN")
    print("=" * 50)

    id_login = auth.id_login #menyimpan id user

    if id_login not in dataUser:
        print("Error: Pengguna tidak ditemukan.")
        input("Tekan Enter untuk kembali...")
        return

    user = dataUser[id_login]
    akun = user["akun"]

    if akun["role"] != "MEMBER":
        print("Anda adalah admin. Tidak memiliki riwayat pembayaran.")
        input("Tekan Enter untuk kembali...")
        return

    # Ambil tagihan yang SUDAH BAYAR
    riwayat = []
    for id_tagihan, data_tagihan in user["tagihan"].items():
        if data_tagihan["status"] == "SUDAH BAYAR":
            riwayat.append(data_tagihan)

    if not riwayat:
        print("Belum ada riwayat pembayaran.")
    else:
        for i, t in enumerate(riwayat, start=1):
            print(f"Pembayaran #{i}")
            print(f"  Bulan     : {t['bulan']}")
            print(f"  Tahun     : {t['tahun']}")
            print(f"  Jumlah    : Rp {t['jumlah']:,}")
            print(f"  Status    : {t['status']}")
            print("-" * 50)

    input("\nTekan Enter untuk kembali...")

def status_kontrakan():
    clear()
    print("STATUS KONTRAKAN")
    print("=" * 50)

    id_input = input("Masukkan ID Penyewa (contoh: PENYEWA1): ").strip()
    print()

    # Cek apakah id ada di dataUser
    if id_input not in dataUser:
        print("ID Penyewa tidak ditemukan!")
        input("Tekan Enter untuk kembali...")
        return

    user = dataUser[id_input]
    akun = user["akun"]

    # Hanya penyewa yang punya laporan pembayaran
    if akun["role"] != "MEMBER":
        print("ID tersebut milik admin. Tidak memiliki laporan pembayaran.")
        input("Tekan Enter untuk kembali...")
        return

    laporan_bayar_penyewa = user["laporan_bayar"]

    if not laporan_bayar_penyewa:
        print("Penyewa ini belum memiliki laporan pembayaran.")
        input("Tekan Enter untuk kembali...")
        return

    # Tampilkan daftar laporan
    print("Daftar Laporan Pembayaran:")
    for id_laporan in laporan_bayar_penyewa.keys():
        print(f" - {id_laporan}")
    print()

    pilih_key = input("Masukkan ID Laporan yang ingin dilihat: ").strip()

    if pilih_key not in laporan_bayar_penyewa:
        print("ID Laporan tidak ditemukan!")
        input("Tekan Enter untuk kembali...")
        return

    # Tampilkan detail laporan
    laporan = laporan_bayar_penyewa[pilih_key]
    print("\n" + "=" * 50)
    print("DETAIL LAPORAN PEMBAYARAN")
    print("=" * 50)
    print(f"ID Penyewa         : {id_input}")
    print(f"Nama Penyewa       : {laporan['nama']}")
    print(f"Kamar              : {laporan['kamar']}")
    print(f"Jumlah Periode     : {laporan['jumlah_periode']} bulan")
    print(f"Periode            : {', '.join(laporan['periode'])}")
    print(f"Jumlah Pembayaran  : Rp {laporan['jumlah_pembayaran']:,}")
    print(f"Metode Pembayaran  : {laporan['metode_pembayaran'][0]}")
    print(f"Nomor Nota/Ref.    : {laporan['metode_pembayaran'][1]}")
    print("=" * 50)

    # Konfirmasi hapus
    print("\nApakah Anda ingin menghapus laporan ini? (y/n)")
    konfir_hapus = input("> ").strip().lower()

    if konfir_hapus == "y":
        try:
            periode_list = laporan["periode"]
            tagihan_user = user["tagihan"]
            for id_tagihan, data_tagihan in tagihan_user.items():
                periode_tagihan = f"{data_tagihan['bulan']} {data_tagihan['tahun']}"
                if periode_tagihan in periode_list and data_tagihan["status"] == "SUDAH BAYAR":
                    data_tagihan["status"] = "BELUM BAYAR"
        except Exception as e:
            # Jika gagal, abaikan
            pass

        # Hapus laporan
        del laporan_bayar_penyewa[pilih_key]
        print("\nLaporan berhasil dihapus.")
        print("Status tagihan terkait telah dikembalikan ke 'BELUM BAYAR'.")

    input("\nTekan Enter untuk kembali...")

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
        print("[4] - Tampilkan Laporan Pembayaran")
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
            tampilkan_laporan_konfirmasi()
        else:
            print("Pilihan tidak valid.")