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
    data_diri = [["Penanggung Jawab","Muchammad Udin Mustofa"], ['Ketua Pelaksana',"Ahmad Haidar Rasyid"],["Sekretaris","Yesyailla Abzani Alfath"],["Perlengkapan", "Auva Bima Ahada"],["Konsumsi","Siapa ya"]]
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
            [str(19.00-20.00),str(1),str(kumpul peserta),str(Sekre)],
            [str(20.00-04.00),str(8),str(Perjalanan menuju Surabaya),str(Jalan)],
            [str(04.00-07.00),str(3),str(Solat subuh, mandi, dan persiapan),str(Masjid Unair)],
            [str(07.00-08.00),str(1),str(Perjalanan ke Lokasi Kunjungan),str(Jalan)],
            [str(08.00-09.00),str(1),str(Sarapan pagi),str(Unair)],
            [str(09.00-15.00),str(6),str(Acara Kunjungan dg LDK UKMKI Unair),str(Unair)],
            [str(15.00-17.30),str(2,5),str(Jalan-jalan Tour Kampus Unair),str(Unair)],
            [str(17.30-19.00),str(1,5),str(Salat Magrib dan Isya),str(Unair)],
            [str(19.00-20.00),str(1),str(Perjalanan ke Wisata Kota Lama),str(Jalan)],
            [str(20.00-23.59),str(4),str(Main-main di Kotalama),str(Kotalama)],
            [str(00.00-04.00),str(4),str(Perjalanan ke Kota Malang),str(Jalan)],
            [str(04.00-07.00),str(3),str(Solat subuh, mandi, dan persiapan),str(Masjid UB)],
            [str(07.00-08.00),str(1),str(Perjalanan ke Lokasi Kunjungan),str(Jalan)],
            [str(08.00-14.00),str(6),str(Acara Kunjungan dg LDK UAKI UB + makan siang),str(UB)],
            [str(14.00-15.00),str(1),str(Jalan-jalan Tour Kampus UB),str(UB)],
            [str(15.00-16.00),str(1),str(Perjalanan ke wisata & oleh),str(Jalan)],
            [str(16.00-21.00),str(5),str(Main-main di Wisata dan Oleh-oleh),str(Wisata)],
            [str(21.00-03.00),str(6),str(Perjalanan ke Yogyakarta),str(Jalan)],
         ]
    rundown = pd.DataFrame(rd)
    st.write(rundown)

