# Sistem Pakar Sederhana - Forward Chaining (Diagnosa Jaringan Wi-Fi)

## 1. Nama dan NIM
* **Nama:** Mustafida
* **NIM:** [F1D02410126]

## 2. Topik dan Cara Menjalankan Program
* **Topik:** Diagnosa Masalah Jaringan Wi-Fi Rumah
* **Bahasa Pemrograman:** Python
* **Cara Menjalankan:**
  1. Pastikan file `kb_wifi.json` dan `sistem_pakar_wifi.py` berada dalam satu direktori.
  2. Buka terminal atau command prompt.
  3. Jalankan perintah:
     ```bash
     python sistem_pakar_wifi.py
     ```

## 3. Daftar Sumber dan Tabel Aturan
* **S1:** EVALUASI KINERJA SISTEM WSN BERBASIS ESP32
DENGAN TOPOLOGI STAR DAN MESH MULTI-HOP, https://ejournal.pnl.ac.id/index.php/litek/article/download/121/95.
* **S2:** Edukasi Penggunaan Wi-Fi yang Aman dan Efisien
di Lingkungan Rumah, https://jurnalcendekia.id/index.php/jhpp/article/view/832.

### Tabel Aturan IF-THEN:
| Aturan | IF (Premis) | Mode | THEN (Kesimpulan) | Sumber |
| :--- | :--- | :--- | :--- | :--- |
| **R1** | lampu indikator router mati OR kabel daya longgar | ATAU | router tidak menyala | S1 |
| **R2** | router tidak menyala AND tidak ada koneksi internet | DAN | kegagalan catu daya utama | S1 |
| **R3** | sinar router normal AND jarak perangkat terlalu jauh dari router | DAN | redaman sinyal tinggi | S2 |
| **R4** | redaman sinyal tinggi AND kecepatan internet sangat lambat | DAN | interferensi atau jangkauan lemah | S2 |

## 4. Metode yang Dipilih
* **Metode:** Forward Chaining (Pelacakan Maju)
* **Alasan:** Proses pencarian dimulai dari fakta gejala awal yang dimasukkan pengguna, dicocokkan dengan bagian kondisi (IF) aturan, hingga menurunkan kesimpulan akhir secara bertahap.

## 5. Tiga Kasus Uji dan Screenshot
1. **Kasus 1:** Menghasilkan kesimpulan `kegagalan catu daya utama`.
2. **Kasus 2:** Menghasilkan kesimpulan `tidak ada`.
3. **Kasus 3:** Menghasilkan kesimpulan `interferensi atau jangkauan lemah`.

*Screenshot Eksekusi Program:*
- Kasus 1: `![Kasus 1](src/Kasus1.png)``
- Kasus 2: `![Kasus 2](src/Kasus2.png)``
- Kasus 3: `![Kasus 3](src/kasus3.png)``

## 6. Batas Keberlakuan
Aturan ini disusun berdasarkan dokumentasi teknis pemecahan masalah jaringan rumahan (standar umum jaringan IEEE 802.11) dan hanya mencakup masalah kabel fisik, gangguan jalur nirkabel, serta kegagalan perangkat router. Hasilnya merupakan saran awal troubleshooting, bukan keputusan akhir teknis profesional.

## 7. Penggunaan Alat Bantu AI
Digunakan sebagai alat bantu belajar dan kode program yg error.