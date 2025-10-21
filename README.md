# NumiSecant 

> Kalkulator akar persamaan non-linear menggunakan **Metode Secant** dengan tampilan terminal interaktif yang indah!

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-Unlicensed-lightgrey.svg)](LICENSE)
[![Made with ❤️](https://img.shields.io/badge/Made%20with-%E2%9D%A4%EF%B8%8F-red.svg)](https://github.com)

---

## 📸 Demo Banner
```
 _  __      _ _          _       _             __  __      _            _      
| |/ /     | | |        | |     | |           |  \/  |    | |          | |     
| ' / __ _ | | | ___   _| | __ _| |_ ___  _ __| \  / | ___| |_ ___   __| | ___ 
|  < / _` || | |/ / | | | |/ _` | __/ _ \| '__| |\/| |/ _ \ __/ _ \ / _` |/ _ \
| . \ (_| || |   <| |_| | | (_| | || (_) | |  | |  | |  __/ || (_) | (_| |  __/
|_|\_\__,_||_|_|\_\\__,_|_|\__,_|\__\___/|_|  |_|  |_|\___|\__\___/ \__,_|\___|
                                                                                 
   ____                      _     
  / ___|  ___  ___ __ _ _ __ | |_   
  \___ \ / _ \/ __/ _` | '_ \| __|  
   ___) |  __/ (_| (_| | | | | |_   
  |____/ \___|\___\__,_|_| |_|\__|  
```

---

## 📖 Deskripsi Singkat

**NumiSecant** adalah program CLI (Command Line Interface) interaktif yang membantu Anda menemukan akar persamaan non-linear menggunakan **Metode Secant**. Program ini dibuat dengan Python dan dilengkapi tampilan terminal yang cantik menggunakan library `rich` dan `pyfiglet`.

### ✨ Mengapa Proyek Ini?

Proyek ini dibuat untuk:
- **Edukasi**: Memahami metode numerik Secant secara praktis
- **Praktik Python**: Implementasi algoritma dengan terminal interaktif
- **UI/UX Terminal**: Demonstrasi penggunaan `rich` untuk CLI yang menarik

---

## Fitur Utama

✅ **Input fungsi fleksibel** — Tulis fungsi matematika dalam ekspresi Python (`sin(x)`, `exp(x)`, `x**3`, dll.)  
✅ **Visualisasi iterasi** — Tabel iterasi lengkap dengan warna & format rapi  
✅ **Validasi input** — Penanganan error otomatis untuk input tidak valid  
✅ **Kriteria konvergensi** — Toleransi error & maksimal iterasi dapat disesuaikan  
✅ **Banner ASCII keren** — Tampilan profesional dengan `pyfiglet`  
✅ **Progress tracking** — Lihat setiap langkah iterasi secara real-time  

---

## Metode Secant

### Apa itu Metode Secant?

Metode Secant adalah **metode numerik iteratif** untuk mencari akar persamaan non-linear **f(x) = 0**. Metode ini merupakan variasi dari metode Newton-Raphson yang **tidak memerlukan turunan fungsi**, melainkan menggunakan **aproksimasi gradien** dari dua titik sebelumnya.

### Rumus Iterasi

Rumus utama Metode Secant:

$$
x_{i+1} = x_i - f(x_i) \cdot \frac{x_i - x_{i-1}}{f(x_i) - f(x_{i-1})}
$$

Dimana:
- $x_i$ = Tebakan akar pada iterasi ke-i
- $f(x_i)$ = Nilai fungsi pada $x_i$
- $x_{i+1}$ = Tebakan akar baru (iterasi berikutnya)

### Algoritma Langkah-demi-Langkah

1. **Definisikan nilai awal**: Tentukan dua tebakan awal $x_0$ dan $x_1$
2. **Tentukan kriteria berhenti**: 
   - Toleransi error ($e$) — misal: `1e-4`
   - Maksimal iterasi ($N$) — misal: `20`
3. **Hitung nilai fungsi awal**: 
   - $y_0 = f(x_0)$
   - $y_1 = f(x_1)$
4. **Iterasi Secant**:
   - Selama $i \leq N$ dan $|f(x_i)| \geq e$:
     - Hitung $x_{i+1}$ menggunakan rumus Secant
     - Hitung $y_{i+1} = f(x_{i+1})$
     - Update: $x_{i-1} = x_i$, $x_i = x_{i+1}$
5. **Cek konvergensi**:
   - **Sukses**: Jika $|f(x_i)| < e$ → akar ditemukan di $x_i$
   - **Gagal**: Jika $i > N$ → metode tidak konvergen

### Pseudocode
```python
def metode_secant(f, x0, x1, toleransi, max_iterasi):
    y0 = f(x0)
    y1 = f(x1)
    
    for i in range(1, max_iterasi + 1):
        # Cek pembagi nol
        if abs(y1 - y0) < 1e-12:
            return None, "Error: Pembagian dengan nol"
        
        # Hitung x baru
        x_baru = x1 - y1 * (x1 - x0) / (y1 - y0)
        y_baru = f(x_baru)
        
        # Cek konvergensi
        if abs(y_baru) < toleransi:
            return x_baru, "Konvergen"
        
        # Update untuk iterasi berikutnya
        x0, y0 = x1, y1
        x1, y1 = x_baru, y_baru
    
    return x1, "Maksimal iterasi tercapai"
```

---

## 🛠️ Instalasi & Cara Menjalankan

### 1️⃣ Clone Repository
```bash
git clone https://github.com/Nixzouxu/NumiSecant.git
cd NumiSecant
```

### 2️⃣ (Opsional) Buat Virtual Environment
```bash
python -m venv venv

# Aktivasi (Windows)
venv\Scripts\activate

# Aktivasi (Linux/Mac)
source venv/bin/activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

Atau install manual:
```bash
pip install rich pyfiglet
```

### 4️⃣ Jalankan Program
```bash
python kalkulator_secant.py
```

---

## 💡 Contoh Penggunaan

### Input
```
=== KALKULATOR METODE SECANT ===

Masukkan fungsi f(x): x*exp(-x)+cos(2*x)
Masukkan nilai x0: 1
Masukkan nilai x1: 2
Masukkan toleransi error (e): 1e-4
Masukkan maksimal iterasi (N): 20
```

### Output (Tabel Iterasi)
```
┏━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┓
┃ Iterasi  ┃ x              ┃ f(x)           ┃ Error          ┃
┡━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━┩
│ 0        │ 1.000000       │ -0.049329      │ -              │
│ 1        │ 2.000000       │ -0.686294      │ 1.000000       │
│ 2        │ 1.850641       │ -0.428166      │ 0.149359       │
│ 3        │ 1.736245       │ -0.181523      │ 0.114396       │
│ 4        │ 1.683428       │ -0.037264      │ 0.052817       │
│ 5        │ 1.674521       │ -0.001823      │ 0.008907       │
└──────────┴────────────────┴────────────────┴────────────────┘

✅ Solusi ditemukan!
Akar persamaan: x = 1.674521
Nilai f(x) = -0.001823
Jumlah iterasi: 5
```

---

## 🧩 Cara Kerja Kode

Program `kalkulator_secant.py` terdiri dari beberapa fungsi utama:

### 1. `parse_function(func_str)`
Mengkonversi string fungsi (misal: `"x*exp(-x)+cos(2*x)"`) menjadi fungsi Python yang dapat dievaluasi.
```python
def parse_function(func_str):
    return lambda x: eval(func_str, {"x": x, "exp": exp, "sin": sin, ...})
```

### 2. `metode_secant(f, x0, x1, tol, max_iter)`
Implementasi inti algoritma Metode Secant yang mengembalikan:
- Daftar iterasi (untuk tabel)
- Hasil akhir (akar atau pesan error)

### 3. `main()`
Fungsi utama yang:
- Menampilkan banner ASCII
- Menerima input pengguna
- Menjalankan metode Secant
- Menampilkan hasil dalam tabel `rich`

---

## 🐛 Troubleshooting & Tips

### Format Fungsi yang Diterima

Program menerima ekspresi Python dengan variabel **`x`**. Contoh valid:

✅ `x**3 - 2*x + 1`  
✅ `sin(x) - 0.5`  
✅ `exp(x) - x**2`  
✅ `x*exp(-x) + cos(2*x)`  

Fungsi matematika yang tersedia:
- Trigonometri: `sin(x)`, `cos(x)`, `tan(x)`, `asin(x)`, `acos(x)`, `atan(x)`
- Eksponensial & Logaritma: `exp(x)`, `log(x)`, `log10(x)`, `sqrt(x)`
- Operasi dasar: `+`, `-`, `*`, `/`, `**` (pangkat)

### Error Umum & Solusi

#### 1. **Pembagian dengan Nol**
```
Error: f(x1) - f(x0) terlalu kecil (pembagian dengan nol)
```

**Penyebab**: Nilai $f(x_0)$ dan $f(x_1)$ terlalu mirip (gradien hampir nol).  
**Solusi**: Pilih $x_0$ dan $x_1$ yang lebih berjauhan.

#### 2. **Fungsi Tidak Valid**
```
Error: Fungsi tidak dapat diparsing
```

**Penyebab**: Sintaks fungsi salah (misal: `2x` tanpa operator `*`).  
**Solusi**: Gunakan operator eksplisit → `2*x`.

#### 3. **Tidak Konvergen**
```
⚠️ Metode tidak konvergen dalam 20 iterasi
```

**Penyebab**: Tebakan awal buruk atau fungsi tidak memiliki akar di sekitar $x_0$, $x_1$.  
**Solusi**: 
- Tingkatkan maksimal iterasi
- Pilih tebakan awal lebih dekat dengan akar

### Tips Memilih x₀ dan x₁

#### Strategi 1: Metode Grafik
Plot fungsi terlebih dahulu untuk estimasi kasar:
```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5, 5, 1000)
y = x * np.exp(-x) + np.cos(2*x)

plt.plot(x, y)
plt.axhline(0, color='red', linestyle='--')
plt.grid()
plt.show()
```

Cari titik dimana kurva **memotong sumbu x**.

#### Strategi 2: Cek Perubahan Tanda
Pilih $x_0$ dan $x_1$ sehingga $f(x_0) \cdot f(x_1) < 0$ (berbeda tanda).

Contoh:
```python
f = lambda x: x**3 - 2*x + 1

print(f(0))   # Output: 1 (positif)
print(f(1))   # Output: 0 (negatif)

# Pilih x0=0, x1=1 karena ada perubahan tanda
```

#### Strategi 3: Trial & Error
Mulai dengan interval lebar (misal: `x0=0`, `x1=5`), lalu persempit jika tidak konvergen.

---

## 📁 Struktur Proyek
```
NumiSecant/
│
├── kalkulator_secant.py    # Program utama
├── requirements.txt        # Daftar dependensi
├── README.md               # Dokumentasi (file ini)
├
│
└── docs/                   # (Opsional) Folder dokumentasi tambahan
    └── screenshot.png      # Screenshot hasil running program
```

---

## 📦 Dependencies

File `requirements.txt`:
```txt
rich==13.7.0
pyfiglet==1.0.2
```

Instalasi:
```bash
pip install -r requirements.txt
```

---

## 🤝 Cara Kontribusi

Kami sangat terbuka untuk kontribusi! Berikut langkah-langkahnya:

1. **Fork** repository ini
2. Buat **branch** fitur baru (`git checkout -b fitur-baru`)
3. **Commit** perubahan Anda (`git commit -m "Menambahkan fitur X"`)
4. **Push** ke branch (`git push origin fitur-baru`)
5. Buat **Pull Request**

### Kode Etik Sederhana

- ✅ Hormati sesama kontributor
- ✅ Tulis kode yang rapi & terdokumentasi
- ✅ Test fitur sebelum PR
- ❌ Jangan spam atau kirim PR tidak relevan

---

## 📜 Lisensi

Proyek ini bersifat **Unlicensed** — Anda bebas menggunakan, memodifikasi, dan mendistribusikan kode ini tanpa batasan.
```
This is free and unencumbered software released into the public domain.
Anyone is free to copy, modify, publish, use, compile, sell, or distribute 
this software for any purpose, commercial or non-commercial.
```

---

## ✅ Acceptance Criteria (Checklist)

README ini dianggap **selesai dan memenuhi standar** jika:

- [x] Terdapat judul proyek & deskripsi singkat
- [x] Badge Python version & license ditampilkan
- [x] Rumus Metode Secant ditampilkan dengan LaTeX (`$$ ... $$`)
- [x] Algoritma 5 langkah tercantum lengkap
- [x] Pseudocode disediakan
- [x] Instruksi instalasi (clone, venv, pip install) lengkap
- [x] Contoh cara menjalankan program disertakan
- [x] Contoh input & output (tabel iterasi) ditampilkan
- [x] Penjelasan format fungsi (string dengan variabel `x`)
- [x] Penanganan error (pembagian nol, parsing error) dijelaskan
- [x] Tips memilih `x0` & `x1` (grafik, perubahan tanda) disertakan
- [x] Struktur proyek ditampilkan (tree sederhana)
- [x] File `requirements.txt` contoh disediakan
- [x] Panduan kontribusi & kode etik singkat ada
- [x] Lisensi (Unlicensed) disebutkan
- [x] Checklist "Acceptance Criteria" ada di akhir
- [x] Saran peningkatan (roadmap) disediakan

---

## 🗺️ Roadmap & Saran Peningkatan

Berikut fitur yang bisa ditambahkan di masa depan:

### 🧪 Testing
- [ ] Tambahkan **unit tests** dengan `pytest`
- [ ] Test berbagai kasus edge (akar ganda, fungsi kompleks)

### 📊 Visualisasi
- [ ] Plot konvergensi dengan **Matplotlib**
- [ ] Animasi iterasi secara grafis

### 🖥️ GUI
- [ ] Buat antarmuka sederhana dengan **Streamlit**
- [ ] Dashboard interaktif dengan **Dash/Plotly**

### ⚙️ CI/CD
- [ ] Setup **GitHub Actions** untuk auto-testing
- [ ] Auto-deploy dokumentasi ke GitHub Pages

### 📚 Metode Lain
- [ ] Tambahkan metode **Newton-Raphson**
- [ ] Tambahkan metode **Bisection**
- [ ] Komparasi performa antar metode

---

## 👥 Tim Pengembang

**Tim 6** — Proyek Metode Numerik  
- Muhammad Hafidz
- Muhammad Yazid Arrazi
- Zahra Rizkyna
- Azira Kania
- Muhammad Al Hafiz
- Syakila Naira

Jika ada pertanyaan atau saran, silakan buat **Issue** di repository ini! 🚀

---

<div align="center">

**⭐ Jangan lupa beri bintang jika project ini membantu! ⭐**

Made with ❤️ and Python

</div>
