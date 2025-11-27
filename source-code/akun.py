# KODE AKUN

dataPenyewa = {
    "ADMIN": {
        "username": "admin1", 
        "password": "admin123", 
        "role": "ADMIN",
        
        "nama": "Yoga Ananda Prasetya", 
        "kontak": "0XXX-XXXX-XXXX",
        "email": "myEmail@email.com",
        "tanggal_gabung": "2 November 2025", 
        "status": "AKTIF", 
        "unit": "KS01", 
        "kamar": "A1"
        }, 
    "PENYEWA1": {
        "username": "user1", 
        "password": "user123", 
        "role": "MEMBER",
        
        "nama": "Pirlo Syabila Hafuza", 
        "kontak": "0XXX-XXXX-XXXX",
        "email": "myEmail@email.com",
        "tanggal_gabung": "10 November 2025", 
        "status": "AKTIF", 
        "unit": "KS01", 
        "kamar": "A2"
    },
    "PENYEWA2": {
        "username": "user2", 
        "password": "user234", 
        "role": "MEMBER",
        
        "nama": "Fatur Rahman", 
        "kontak": "0XXX-XXXX-XXXX",
        "email": "myEmail@email.com",
        "tanggal_gabung": "10 November 2025", 
        "status": "AKTIF", 
        "unit": "KS01", 
        "kamar": "A3"
    },
}

tagihan = {
    "PENYEWA1": {
        "TGHN01": {"tahun": "2025", "bulan": "November", "jumlah": 1500000, "status": "BELUM BAYAR"},
        "TGHN02": {"tahun": "2025", "bulan": "Desember", "jumlah": 1500000, "status": "BELUM BAYAR"},
        "TGHN03": {"tahun": "2025", "bulan": "Oktober", "jumlah": 1500000, "status": "SUDAH BAYAR"},     
    }, 
    "PENYEWA2": {
        "TGHN01": {"tahun": "2025", "bulan": "November", "jumlah": 1500000, "status": "SUDAH BAYAR"},
        "TGHN02": {"tahun": "2025", "bulan": "Desember", "jumlah": 1500000, "status": "BELUM BAYAR"},
        "TGHN03": {"tahun": "2025", "bulan": "Oktober", "jumlah": 1500000, "status": "SUDAH BAYAR"},     
    },
    "PENYEWA3": {
        "TGHN01": {"tahun": "2025", "bulan": "November", "jumlah": 1500000, "status": "BELUM BAYAR"},
        "TGHN02": {"tahun": "2025", "bulan": "Desember", "jumlah": 1500000, "status": "BELUM BAYAR"},
        "TGHN03": {"tahun": "2025", "bulan": "Oktober", "jumlah": 1500000, "status": "SUDAH BAYAR"},     
    }
}

laporan_keluhan = {
    "PENYEWA1": {
        "LK-1": {
            "nama": "",
            "unit": "",
            "kamar": "", 
            "kategori": "", 
            "judul_laporan": "", 
            "deskripsi_laporan": "", 
            "tanggal_dibuat": "", 
            "status": ""
        }
    }, 
    "PENYEWA2": {
        "LK-1": {
            "nama": "",
            "unit": "",
            "kamar": "", 
            "kategori": "", 
            "judul_laporan": "", 
            "deskripsi_laporan": "", 
            "tanggal_dibuat": "", 
            "status": ""
        }
    },
    "PENYEWA3": {
        "LK-1": {
            "nama": "",
            "unit": "",
            "kamar": "", 
            "kategori": "", 
            "judul_laporan": "", 
            "deskripsi_laporan": "", 
            "tanggal_dibuat": "", 
            "status": ""
        }
    }
}

laporan_bayar = {
    "PENYEWA1": {
        "LB-1": {
            "nama": "", 
            "unit": "", 
            "kamar": "", 
            "jumlah_periode": "", 
            "periode": ["", ""], 
            "jumlah_pembayaran": 0, 
            "metode_pembayaran": ["1", "123"]
        }
    },
    "PENYEWA2": {
        "LB-1": {
            "nama": "", 
            "unit": "", 
            "kamar": "", 
            "jumlah_periode": "", 
            "periode": ["", ""], 
            "jumlah_pembayaran": 0, 
            "metode_pembayaran": ["1", "123"]
        }
    },
    "PENYEWA1": {
        "LB-1": {
            "nama": "", 
            "unit": "", 
            "kamar": "", 
            "jumlah_periode": "", 
            "periode": ["", ""], 
            "jumlah_pembayaran": 0, 
            "metode_pembayaran": ["1", "123"]
        }
    },
}