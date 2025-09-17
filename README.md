# Pet Inventory GAG System

Website inventory stock untuk menampilkan dan mengelola stock Pet Age dengan tampilan yang modern dan responsif.

## Fitur

- **Tampilan Stock**: Menampilkan 3 produk Pet Age (60, 70, 75)
- **Responsive Design**: Tampilan yang responsif untuk desktop, tablet, dan mobile
- **Trade Offer System**: Section trade offer dengan offering dan wants items
- **Autentikasi Admin**: Login system untuk mengamankan admin panel
- **Admin Panel**: Panel admin untuk mengelola stock (hanya untuk admin yang login)
- **Reset Stock**: Fitur untuk mereset semua stock ke nilai default
- **Update Stock**: Dropdown terpisah untuk aksi (tambah/kurangi) dan jumlah (1-10)
- **Custom Images**: Menggunakan gambar PNG custom untuk dog, ostrich, dan peacock
- **Real-time Updates**: Data tersimpan dalam file JSON dan terupdate secara real-time

## Instalasi

1. Install Python dependencies:
```bash
pip install -r requirements.txt
```

2. Jalankan aplikasi:
```bash
python app.py
```

3. Buka browser dan akses: `http://localhost:5000`

## Struktur Proyek

```
pet-inventory-gag/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── inventory.json      # Data storage (auto-generated)
├── templates/
│   ├── base.html      # Base template
│   ├── index.html     # Main inventory display
│   ├── login.html     # Login Page
│   ├── trade.html     # Trade Page
│   └── admin.html     # Admin panel
└── README.md
```

## Penggunaan

### Halaman Utama
- Menampilkan semua produk Pet Age dengan stock masing-masing
- Custom images menggunakan PNG (dog, ostrich, peacock)
- Trade offer section dengan offering dan wants items
- Responsive design untuk semua ukuran layar

### Login Admin
- Username: `jawir`
- Password: `jawirlu`
- Akses ke `/login` untuk masuk sebagai admin

### Admin Panel (Setelah Login)
- **Reset Stock**: Mereset semua stock ke nilai default
- **Update Stock**: 
  - Dropdown 1: Pilih produk
  - Dropdown 2: Pilih aksi (Tambah/Kurangi)
  - Dropdown 3: Pilih jumlah (1-10)
- **Monitor Stock**: Melihat status stock saat ini
- **Logout**: Keluar dari session admin

## Default Stock Values
- Pet Age 60: 0 unit
- Pet Age 70: 0 unit  
- Pet Age 75: 0 unit
