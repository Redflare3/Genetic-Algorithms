
# Optimasi Numerik menggunakan Algoritma Genetika

**Laporan Case Based Kecerdasan Buatan RPL**

**Tim: The Sun and The Moon (Kelompok 7)**
* **Muhammad Zaki (103022400141)** - Ukuran populasi, rancangan kromosom, cara dekode, pemilihan orang tua, operasi genetik
* **Chris Cornelis Lukito (103022400075)** - Probabilitas operasi genetik, pergantian generasi

---

## 📌 Definisi Tugas dan Analisis Masalah
Proyek ini merupakan penyelesaian masalah **Optimasi Numerik** menggunakan **Algoritma Genetika**. Tujuannya adalah mencari kombinasi nilai $x_1$ dan $x_2$ yang menghasilkan output paling minimum (global minimum) dari suatu fungsi matematika.

**Fungsi Objektif:**
$$f(x_1, x_2) = -\left(\sin(x_1)\cos(x_2)\tan(x_1+x_2) + \frac{1}{2}\exp\left(1-\sqrt{x_2^2}\right)\right)$$

**Batasan Domain:**
* $-10 \le x_1 \le 10$
* $-10 \le x_2 \le 10$

**Tantangan Utama:** Fungsi tersebut memiliki banyak fluktuasi sehingga pencarian solusi sangat rawan terjebak dalam minimum lokal. Oleh karena itu, Algoritma Genetika digunakan karena kemampuannya dalam menjaga keberagaman dan menjelajahi banyak titik dalam domain untuk menghindari jebakan minimum lokal.

---

## ⚙️ Desain Algoritma Genetika

| Parameter / Metode | Deskripsi |
| :--- | :--- |
| **Ukuran Populasi** | `50` (Cukup untuk menjaga keberagaman genetik agar algoritma bisa menjelajah berbagai titik) |
| **Representasi Kromosom** | Biner, total `32 bit` (16 bit untuk masing-masing variabel $x_1$ dan $x_2$) |
| **Metode Dekode** | Rumus: $x = Min + \left(\frac{Max - Min}{2^N - 1}\right) \times decimal\_value$ (dengan $N=16$) |
| **Seleksi Orang Tua** | **Tournament Selection** (Efisien secara komputasi & menjaga tekanan seleksi tetap seimbang) |
| **Crossover** | **Single-point crossover** dengan probabilitas **0.8 (80%)** (Nilai tinggi agar eksploitasi solusi dilakukan secara intensif) |
| **Mutasi** | **Bit-flip mutation** dengan probabilitas **0.1 (10%)** (Nilai rendah agar tidak merusak solusi baik yang sudah didapat) |
| **Pergantian Generasi** | **Elitism** + **Generational Replacement** (Mempertahankan individu terbaik langsung ke generasi berikutnya) |
| **Kriteria Penghentian** | **Fixed Generation Count** (Berhenti setelah 100 generasi) |

---

## 💻 Implementasi Sistem

Sistem dibangun menggunakan bahasa pemrograman **Python** (tanpa menggunakan library eksternal/third-party). Program hanya menggunakan modul bawaan Python:
* `math` (untuk perhitungan fungsi objektif)
* `random` (untuk inisiasi populasi, crossover, dan mutasi)

**Struktur Fungsi Program:**
* `population_initialization`: Membangun populasi awal.
* `decode_chromosome`: Mentransformasi biner ke nilai riil pada domain masalah.
* `fitness_function`: Menghitung kualitas solusi berdasarkan fungsi objektif.
* `parent_selection`, `crossover`, `mutation`: Menjadi inti dari proses evolusi.
* `run`: Menjalankan seluruh siklus evolusi.

---

## 📊 Hasil Percobaan dan Kesimpulan

Dari 10 kali percobaan iterasi jalannya program (run), hasil minimum yang didapatkan sangat bervariasi. Hal ini membuktikan bahwa fungsi ini memiliki banyak minimum lokal.

### Hasil Terbaik
Dari ke-10 percobaan yang didokumentasikan, nilai minimum terbaik ditemukan pada **Percobaan ke-2**:
* **Kromosom Terbaik:** `[1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1]`
* **$x_1$ (Decoded):** `7.821927214465553`
* **$x_2$ (Decoded):** `3.173723964293888`
* **Minimum Value $f(x_1, x_2)$:** `-12992.05675342`

**Kesimpulan:** Koordinat solusi terbaik berada di sekitar $x_1 \approx 7.82$ dan $x_2 \approx 3.17$.
README.md
Displaying README.md.
