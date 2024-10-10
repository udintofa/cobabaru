import streamlit as st
from streamlit_gsheets import GSheetsConnection
import time
import pandas as pd
import numpy as np

# Fungsi untuk membaca data dari Google Sheets
def load_data(url):
    conn = st.connection("gsheets", type=GSheetsConnection)
    data = conn.read(spreadsheet=url, usecols=[1, 2, 3, 5, 9])
    return data

# Fungsi untuk membaca data dari Google Sheets
def load_data2(url):
    conn = st.connection("gsheets", type=GSheetsConnection)
    data = conn.read(spreadsheet=url, usecols=[1, 2, 5, 9, 10])
    return data

# URL Google Sheets
url = 'https://docs.google.com/spreadsheets/d/1tU0OByLfC0ISXWk2OAhknPnrpSeOX2GtaZFG0DWjwvc/edit?usp=sharing'
url2 = 'https://docs.google.com/spreadsheets/d/1gC_9B9rcl5F9Cx12AMyD-HPeXmyPrYk8o-ey6RxSbMg/edit?usp=sharing'
    
# Memuat dan menampilkan data

data = load_data(url)
data2 = load_data2(url2)
data["Angkatan masuk JS"] = data["Angkatan masuk JS"].astype(str)
data2["Angkatan masuk JS"] = data2["Angkatan masuk JS"].astype(str)

# Menggunakan reset_index dan mulai indeks dari 1
data = data.reset_index(drop=True)  # Reset index terlebih dahulu
data.index = data.index + 1         # Mengubah index menjadi mulai dari 1

# Menggunakan reset_index dan mulai indeks dari 1
data2 = data2.reset_index(drop=True)  # Reset index terlebih dahulu
data2.index = data2.index + 1         # Mengubah index menjadi mulai dari 1

st.write('''
# :sunglasses: Selamat Datang :sunglasses:
### di Laman Departemen Jaksa :smile:
mari bermuhasabah diri, meluruskan niat, ikhlaskan pikiran, dan berusaha menjadi hamba yang baik untuk Allah SWT
''')

tab1, tab2, tab3, tab4, tab5 = st.tabs(["Home", "Panitia", "Pendaftaran", "Peserta", "Gambaran Kegiatan"])

with tab1:
    st.header("Tentang Kunjungan LDK Nasional")
    st.write("#### JS gass ke Unair dan UB besok :rocket::rocket:")
    st.write("Kunjungan LDKN merupakan salah satu kegiatan Departemen Jaringan dan Kerjasama yang di mana dilakukan dalam rangka mempererat silaturahmi antar Lembaga dengan berkunjung ke Lembaga lain untuk saling bertukar informasi seputar strategi yang dilakukan lembaga, metode, kaderisasi dan lain-lain yang bermanfaat untuk kemajuan lembaga serta memahami bagaimana struktur atau kondisi umum lembaga yang bisa diambil dan diterapkan di lembaganya.")  
    st.write("Kunjungan LDK Nasional akan dilaksanakan pada hari Jumat (8 Nov 2024) malam sampai dengan hari Senin (11 Nov 2024) pagi. Kunjungan akan dilaksanakan ke LDK UKMKI Unair terlebih dahulu pada Sabtu (9 Nov 2024) dilanjutkan berkunjung ke LDK UAKI UB pada Minggu (10 Nov 2024).")

with tab2:
    st.header("Panitia Kunjungan LDK Nasional")
    data_diri = [
        ["Penanggung Jawab","Muchammad Udin Mustofa"],
        ['Ketua Pelaksana',"Ahmad Haidar Rasyid"],
        ["Sekbend","Yesyailla Abzani Alfath"],
        ["Perlengkapan", "Auva Bima Ahada"],
        ['Media','Arif Taufik'],
        ["Konsumsi","Nauval Ghaniya"],
        ['Acara', 'Fathiya Al-Khansa'],
        ['Acara', 'Eka Setiawan'],
        ['Acara', 'Diva Aisya'],
        
    ]
    dd = pd.DataFrame(data_diri)
    st.write(dd)

with tab3:
    st.header("Pendaftaran")
    st.write("Silahkan daftar untuk menjadi peserta LDK Nasional melalui tautan dibawah")
    # Menambahkan hyperlink
    st.markdown(
        """
        [Daftar Sekarang](https://docs.google.com/forms/d/e/1FAIpQLSdrODYr9QwUqe2_a5o0o6Jd1oem8ktC1j7oY1UGTGwu9PYVhA/viewform?usp=sf_link)
        """
    )

    st.write("Berikut merupakan daftar pendaftar yang sudah mendaftar")
    # Tombol refresh data tanpa st.experimental_rerun
    if st.button("Refresh Data"):
        st.cache_data.clear()  # Menghapus cache agar data terbaru dimuat
    st.dataframe(data)

with tab4:
    st.header("Pembayaran")
    st.write("Silahkan bagi pendaftar yang sudah menjadi peserta bisa melakukan pembayarak ke rekening Mandiri dengan nomor rekening 1370021364068 atas nama YESYAILLA ABZANI ALFATH.")
    st.header("Pendaftar yang diterima menjadi peserta")
    st.write("Berikut merupakan daftar pendaftar yang diterima menjadi peserta (kuota peserta 50 mahasiswa)")
    # Tombol refresh data tanpa st.experimental_rerun
    if st.button("Refresh  Data"):
        st.cache_data.clear()  # Menghapus cache agar data terbaru dimuat
     # Tombol refresh data tanpa st.experimental_rerun
    st.dataframe(data2)


with tab5:
    st.header("Gambaran Kegiatan")
    st.write("Kegiatan diawali dengan memperkenalkan masing-masing LDK, dilanjutkan dengan sharing-sharing antar LDK. Rundown kegiatan adalah sebagai berikut:")
    rd = [
            ['19.00-20.00', 1, 'kumpul peserta', 'Sekre'],
            ['20.00-04.00', 8, 'Perjalanan menuju Surabaya', 'Jalan'],
            ['04.00-07.00', 3, 'Solat subuh, mandi, dan persiapan', 'Masjid Unair'],
            ['07.00-08.00', 1, 'Perjalanan ke Lokasi Kunjungan', 'Jalan'],
            ['08.00-09.00', 1, 'Sarapan pagi', 'Unair'],
            ['09.00-15.00', 6, 'Acara Kunjungan dg LDK UKMKI Unair', 'Unair'],
            ['15.00-17.30', 2.5, 'Jalan-jalan Tour Kampus Unair', 'Unair'],
            ['17.30-19.00', 1.5, 'Salat Magrib dan Isya', 'Unair'],
            ['19.00-20.00', 1, 'Perjalanan ke Wisata Kota Lama', 'Jalan'],
            ['20.00-23.59', 4, 'Main-main di Kotalama', 'Kotalama'],
            ['00.00-04.00', 4, 'Perjalanan ke Kota Malang', 'Jalan'],
            ['04.00-07.00', 3, 'Solat subuh, mandi, dan persiapan', 'Masjid UB'],
            ['07.00-08.00', 1, 'Perjalanan ke Lokasi Kunjungan', 'Jalan'],
            ['08.00-14.00', 6, 'Acara Kunjungan dg LDK UAKI UB + makan siang', 'UB'],
            ['14.00-15.00', 1, 'Jalan-jalan Tour Kampus UB', 'UB'],
            ['15.00-16.00', 1, 'Perjalanan ke wisata & oleh', 'Jalan'],
            ['16.00-21.00', 5, 'Main-main di Wisata dan Oleh-oleh', 'Wisata'],
            ['21.00-03.00', 6, 'Perjalanan ke Yogyakarta', 'Jalan'],
        ]
    # Menambahkan nama kolom saat membuat DataFrame
    rundown = pd.DataFrame(rd, columns=['Waktu', 'Durasi (jam)', 'Kegiatan', 'Lokasi'])
    st.write(rundown)

