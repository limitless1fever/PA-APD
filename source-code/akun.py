# KODE AKUN

dataPenyewa = {
    "ADMIN": {
        "username": "admin1", 
        "password": "admin123", 
        "role": "ADMIN"
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
        "kamar": "A3"
    },
}

tagihan = {
    "PENYEWA1": {
        "TGHN01": {"tahun": "2025", "bulan": "November", "jumlah": 1500000, "status": "SUDAH BAYAR"},
        "TGHN02": {"tahun": "2025", "bulan": "Desember", "jumlah": 1500000, "status": "BELUM BAYAR"},
        "TGHN03": {"tahun": "2026", "bulan": "Januari", "jumlah": 1500000, "status": "BELUM BAYAR"},     
    }, 
    "PENYEWA2": {
        "TGHN01": {"tahun": "2025", "bulan": "November", "jumlah": 1500000, "status": "SUDAH BAYAR"},
        "TGHN02": {"tahun": "2025", "bulan": "Desember", "jumlah": 1500000, "status": "BELUM BAYAR"},
        "TGHN03": {"tahun": "2026", "bulan": "Januari", "jumlah": 1500000, "status": "BELUM BAYAR"},     
    }
}

laporan_keluhan = {
    "PENYEWA1": {}, 
    "PENYEWA2": {}
}

laporan_bayar = {
    "PENYEWA1": {
        "LB-1": {
            "nama": "", 
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
            "kamar": "", 
            "jumlah_periode": "", 
            "periode": ["", ""], 
            "jumlah_pembayaran": 0, 
            "metode_pembayaran": ["1", "123"]
        }
    }
}

dataUser = {}

for key in dataPenyewa:
    dataUser[key] = {
        "akun": dataPenyewa.get(key, {}),
        "tagihan": tagihan.get(key, {}),
        "laporan_keluhan": laporan_keluhan.get(key, {}),
        "laporan_bayar": laporan_bayar.get(key, {}),
    }