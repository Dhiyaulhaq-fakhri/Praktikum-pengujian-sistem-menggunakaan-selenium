# Praktikum 7 - UI Test Automation SauceDemo

Repositori ini berisi hasil Praktikum 7 mata kuliah **Pengujian Perangkat Lunak (TI505)**.

Proyek ini merupakan kerangka otomasi pengujian antarmuka pengguna (*UI Test Automation* atau *End-to-End Testing*) untuk aplikasi e-commerce [SauceDemo](https://www.saucedemo.com/). Pengujian dikembangkan menggunakan **Python**, **Selenium WebDriver**, dan **pytest**, dengan menerapkan pola arsitektur **Page Object Model (POM)**.

## 🛠️ Teknologi yang Digunakan

| Teknologi | Keterangan |
|---|---|
| Python 3.10+ | Bahasa pemrograman |
| Selenium WebDriver 4.x | Otomasi browser |
| pytest 7.x+ | Test runner dan framework pengujian |
| Page Object Model (POM) | Pola desain untuk memisahkan representasi halaman dari logika pengujian |

## 📂 Struktur Direktori

```text
practicum-7-saucedemo/
│
├── pages/                      # Lapisan Page Objects (objek halaman)
│   ├── base_page.py            # Kelas induk dengan method pembungkus Selenium dan Explicit Wait
│   ├── login_page.py           # Kelas khusus halaman login
│   └── inventory_page.py       # Kelas khusus halaman inventori dan cart
│
├── tests/                      # Lapisan skrip pengujian (test logic dan assertions)
│   ├── test_login.py           # Test case fungsional login
│   └── test_inventory.py       # Test case fungsional inventory dan logout
│
├── conftest.py                 # Fixture pytest untuk inisialisasi browser
├── pytest.ini                  # Konfigurasi eksekusi pytest
└── requirements.txt            # Daftar dependensi pustaka Python
```

## 🚀 Cara Menjalankan Pengujian

Ikuti langkah-langkah berikut dari direktori utama (*root directory*) proyek.

### 1. Buat dan aktifkan virtual environment

Buat virtual environment dengan perintah:

```bash
python -m venv venv
```

Aktifkan virtual environment sesuai sistem operasi yang digunakan.

**Windows (PowerShell):**

```powershell
.\venv\Scripts\Activate.ps1
```

**Linux / macOS:**

```bash
source venv/bin/activate
```

### 2. Install dependensi

Pastikan virtual environment sudah aktif, kemudian jalankan:

```bash
pip install -r requirements.txt
```

### 3. Jalankan pengujian

Jalankan pytest dari direktori utama proyek:

```bash
pytest -v -s
```

Opsi `-v` menampilkan nama setiap test case secara lebih terperinci, sedangkan `-s` menampilkan output langsung dari proses pengujian.

## 📊 Hasil Eksekusi (Test Results)

Seluruh skenario pengujian yang tercantum di bawah telah berjalan dengan sukses dan memperoleh hasil **100% lulus (passed)**.

```text
============================= test session starts =============================
collected 5 items

tests/test_inventory.py::TestInventory::test_add_backpack_to_cart PASSED
tests/test_inventory.py::TestInventory::test_logout_flow PASSED
tests/test_login.py::TestLogin::test_login_positive_valid_user PASSED
tests/test_login.py::TestLogin::test_login_negative_locked_out_user PASSED
tests/test_login.py::TestLogin::test_login_negative_empty_password PASSED

============================== 5 passed in 20.16s ==============================
```

## 📝 Daftar Test Case

| ID | Nama Test Case | Skenario | Ekspektasi |
|---|---|---|---|
| TC-01 | `test_login_positive_valid_user` | Login menggunakan kredensial valid (`standard_user`). | Pengguna berhasil masuk ke halaman `/inventory.html` dan logo aplikasi tampil. |
| TC-02 | `test_login_negative_locked_out_user` | Login menggunakan akun yang diblokir (`locked_out_user`). | Sistem menampilkan pesan error `Sorry, this user has been locked out.` |
| TC-03 | `test_login_negative_empty_password` | Login dengan kolom password dikosongkan. | Sistem menampilkan pesan validasi `Password is required`. |
| TC-04 | `test_add_backpack_to_cart` | Menambahkan produk Backpack ke keranjang belanja. | Badge keranjang belanja berubah menjadi `1`. |
| TC-05 | `test_logout_flow` | Melakukan logout melalui burger menu. | Pengguna kembali ke halaman login utama dan tombol login tampil. |

---

**Praktikum 7 - Pengujian Perangkat Lunak (TI505)**
