import time

print("=" * 60)
print("          FACEBOOK MARKETPLACE")
print("              COD MUSANG ")
print("=" * 60)

nama_pembeli = "Asep"
nama_penjual = "Farel"

def kirim(nama, pesan):
    print(f"\n{nama}: {pesan}")
    time.sleep(0.8)

def garis():
    print("-" * 60)

print("\nMembuka Facebook Marketplace...")
time.sleep(1)

print("\n[ FACEBOOK MARKETPLACE ]")
print("Produk: Musang Pandan")
print("Penjual:", nama_penjual)
print("Harga: Rp500.000")
print("Lokasi penjual: Cikande Permai")

garis()
print("             MESSENGER FACEBOOK")
garis()

# PERCAKAPAN AWAL
kirim(nama_pembeli, "Halo bang, saya lihat postingan musang di Facebook.")
kirim(nama_penjual, "Halo juga bang, benar. Musangnya masih tersedia.")
kirim(nama_pembeli, "Jenis musang apa bang?")
kirim(nama_penjual, "Musang pandan bang.")

kirim(nama_pembeli, "Umurnya berapa bulan?")
kirim(nama_penjual, "Sekitar 4 bulan bang.")

kirim(nama_pembeli, "Bagaimana kondisi musangnya?")
kirim(nama_penjual, "Kondisinya terlihat sehat dan aktif.")

kirim(nama_pembeli, "Sudah terbiasa dengan manusia?")
kirim(nama_penjual, "Sudah mulai terbiasa, tetapi masih perlu adaptasi.")

kirim(nama_pembeli, "Ada foto dan video terbaru?")
kirim(nama_penjual, "Ada bang, silakan lihat foto dan video yang saya kirim.")

# NEGOSIASI HARGA
garis()
print("                NEGOSIASI HARGA")
garis()

kirim(nama_pembeli, "Harga yang diposting Rp500.000 ya bang?")
kirim(nama_penjual, "Betul bang, Rp500.000.")

kirim(nama_pembeli, "Boleh kurang jadi Rp400.000?")
kirim(nama_penjual, "Maaf bang, belum bisa.")

kirim(nama_pembeli, "Kalau Rp450.000 bagaimana?")
kirim(nama_penjual, "Baik bang, Rp450.000.")

# KESEPAKATAN COD
garis()
print("                 KESEPAKATAN COD")
garis()

kirim(nama_pembeli, "Bisa COD langsung bang?")
kirim(nama_penjual, "Bisa bang, kita ketemu langsung.")

lokasi = "Cikande Permai"
waktu = "15.00 WIB"

kirim(nama_pembeli, f"Kita ketemuan di {lokasi} jam {waktu} ya bang.")
kirim(nama_penjual, "Siap bang, sampai ketemu.")

# HARI COD
garis()
print("                    HARI COD")
garis()

kirim(nama_pembeli, "Bang, saya sudah sampai di lokasi.")
kirim(nama_penjual, "Saya juga sudah sampai bang.")
kirim(nama_pembeli, "Saya pakai baju hitam bang.")
kirim(nama_penjual, "Baik bang, saya sedang menuju ke sana.")

kirim(nama_penjual, "Halo bang, saya sudah ketemu.")
kirim(nama_pembeli, "Iya bang, mari kita periksa dulu.")

# PEMERIKSAAN
garis()
print("               PEMERIKSAAN MUSANG")
garis()

kirim(nama_pembeli, "Boleh saya lihat kondisi musangnya?")
kirim(nama_penjual, "Silakan bang, ini musangnya.")

kirim(nama_pembeli, "Saya mau periksa kondisi dan dokumennya dulu.")
kirim(nama_penjual, "Silakan bang, ini dokumen asal-usulnya.")

kirim(nama_pembeli, "Baik bang, saya periksa dulu.")
kirim(nama_penjual, "Silakan, jangan terburu-buru.")

# VERIFIKASI
garis()
print("                 VERIFIKASI")
garis()

kirim(nama_pembeli, "Dokumennya sudah saya periksa.")
kirim(nama_penjual, "Bagaimana bang, sudah sesuai?")
kirim(nama_pembeli, "Dokumen dan asal-usulnya sudah terkonfirmasi.")
kirim(nama_penjual, "Alhamdulillah, terima kasih bang.")

print("\nMemproses verifikasi...")
time.sleep(2)

print("\n[✓] Identitas penjual diperiksa")
print("[✓] Dokumen asal-usul diperiksa")
print("[✓] Legalitas perdagangan dikonfirmasi")
print("[✓] Kondisi satwa diperiksa")
print("[✓] Persyaratan transaksi terpenuhi")

print("\nSTATUS VERIFIKASI: BERHASIL")

# PEMBAYARAN
garis()
print("                  PEMBAYARAN")
garis()

kirim(nama_pembeli, "Baik bang, saya setuju dengan kondisinya.")
kirim(nama_penjual, "Totalnya Rp450.000 bang.")

kirim(nama_pembeli, "Saya bayar sekarang ya bang.")
kirim(nama_penjual, "Baik bang, silakan.")

print("\nMemproses pembayaran...")
time.sleep(2)

print("[✓] Pembayaran diterima")
print("[✓] Penjual mengonfirmasi pembayaran")

kirim(nama_penjual, "Pembayaran sudah saya terima bang.")
kirim(nama_pembeli, "Terima kasih bang.")

# RINGKASAN TRANSAKSI
garis()
print("              TRANSAKSI SELESAI")
garis()

print("Platform     : Facebook Marketplace")
print("Nama Pembeli :", nama_pembeli)
print("Nama Penjual :", nama_penjual)
print("Jenis        : Musang pandan")
print("Umur         : 4 bulan")
print("Harga        : Rp450.000")
print("Lokasi       :", lokasi)
print("Waktu        :", waktu)
print("Verifikasi   : BERHASIL")
print("Pembayaran   : DITERIMA")
print("Status       : TRANSAKSI SELESAI")

garis()

kirim(nama_pembeli, "Terima kasih bang, semoga sehat selalu.")
kirim(nama_penjual, "Sama-sama bang, hati-hati di jalan.")
kirim(nama_pembeli, "Siap bang, sampai jumpa.")

print("\n" + "=" * 60)
print("       FACEBOOK COD BERHASIL!")
print("          TRANSAKSI SELESAI")
print("=" * 60)