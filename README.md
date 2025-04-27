# Cedomis Waitlist Bot

Bot ini dirancang untuk mengotomatiskan pembuatan wallet Ethereum dan pendaftaran ke waitlist pada platform Cedomis. Dengan script ini, Anda dapat dengan mudah menghasilkan wallet baru dan mengirimkannya ke endpoint waitlist secara otomatis.


## 🚀 Fitur
- **Generasi Wallet Otomatis**: Membuat wallet Ethereum baru (alamat dan private key) menggunakan library `eth_account`.
- **Pendaftaran Waitlist**: Mengirimkan data wallet ke endpoint waitlist Cedomis dengan status `followed`, `retweeted`, dan `commented` secara otomatis.
- **Penyimpanan Wallet**: Menyimpan wallet yang dihasilkan ke file `wallets.json` untuk referensi.
- **Tampilan Terminal Berwarna**: Menggunakan `colorama` untuk antarmuka terminal yang lebih menarik dan informatif.
- **Error Handling**: Menangani kesalahan saat pengiriman data ke endpoint atau penyimpanan wallet.

## 🛠️ Prasyarat
Sebelum menjalankan bot, pastikan Anda telah menginstal dependensi berikut:
- Python 3.8 atau lebih tinggi
- Library Python:
  - `requests`
  - `web3`
  - `eth_account`
  - `colorama`

Anda dapat menginstal dependensi dengan perintah berikut:
```bash
pip install requests web3 eth_account colorama
```

## 📦 Cara Menggunakan
1. **Clone Repository**:
   ```bash
   git clone https://github.com/Yuurichan-N3/Cedomis-Waitlist.git
   cd Cedomis-Waitlist
   ```

2. **Install Dependensi**:
   Jalankan perintah di atas untuk menginstal library yang diperlukan.

3. **Jalankan Script**:
   ```bash
   python bot.py
   ```

4. **Ikuti Instruksi**:
   - Masukkan jumlah wallet yang ingin digenerate.
   - Bot akan menghasilkan wallet, mengirimkan ke endpoint waitlist, dan menyimpan wallet ke file `wallets.json`.

5. **Cek Hasil**:
   - Wallet yang berhasil disimpan akan tercatat di `wallets.json`.
   - Status pendaftaran akan ditampilkan di terminal dengan warna untuk memudahkan tracking.

## ⚠️ Catatan Penting
- **API Key dan Endpoint**: Script ini menggunakan API key dan endpoint spesifik. Pastikan Anda memverifikasi keabsahan dan keamanannya sebelum digunakan.
- **Penyimpanan Private Key**: Private key disimpan di `wallets.json`. Jaga kerahasiaan file ini dan jangan bagikan!
- **Penggunaan Bertanggung Jawab**: Bot ini hanya untuk tujuan pembelajaran dan pengujian. Pengguna bertanggung jawab penuh atas penggunaan script ini.

## 📜 Lisensi
Script ini didistribusikan untuk keperluan pembelajaran dan pengujian. Penggunaan di luar tanggung jawab pengembang.

Untuk update terbaru, bergabunglah di grup **Telegram**: [Klik di sini](https://t.me/sentineldiscus).

## 💡 Disclaimer
Penggunaan bot ini sepenuhnya tanggung jawab pengguna. Kami tidak bertanggung jawab atas penyalahgunaan skrip ini.
