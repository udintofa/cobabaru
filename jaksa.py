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

# URL Google Sheets
url = 'https://docs.google.com/spreadsheets/d/1tU0OByLfC0ISXWk2OAhknPnrpSeOX2GtaZFG0DWjwvc/edit?usp=sharing'
url2 = 'https://docs.google.com/spreadsheets/d/1gC_9B9rcl5F9Cx12AMyD-HPeXmyPrYk8o-ey6RxSbMg/edit?usp=sharing'
    
# Memuat dan menampilkan data

data = load_data(url)
data2 = load_data(url2)
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

tab1, tab2, tab3, tab4, tab5 = st.tabs(["Home", "Panitia", "Pendaftaran", "Pendaftar", "Peserta"])

with tab1:
    st.header("Tentang Kunjungan LDK Nasional")
    st.write("#### JS gass ke Unair dan UB besok :rocket::rocket:")
    st.write("Kunjungan LDKN merupakan salah satu kegiatan Departemen Jaringan dan Kerjasama yang di mana dilakukan dalam rangka mempererat silaturahmi antar Lembaga dengan berkunjung ke Lembaga lain untuk saling bertukar informasi seputar strategi yang dilakukan lembaga, metode, kaderisasi dan lain-lain yang bermanfaat untuk kemajuan lembaga serta memahami bagaimana struktur atau kondisi umum lembaga yang bisa diambil dan diterapkan di lembaganya.")
    st.write("Tujuan LDKN itu sendiri yaitu untuk memperluas relasi antar lembaga, mengetahui struktur dan mekanisme Lembaga serta mendiskusikan langkah-langkah yang dapat diambil untuk meningkatkan produktivitas dan efisiensi yang baik dan bisa diterapkan di internal Jama’ah Shalahuddin UGM.")
    st.write("Kunjungan LDK Nasional akan dilaksanakan pada hari Jumat (8 Nov 2024) malam sampai dengan hari Senin (10 Nov 2024) pagi.")

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
    
with tab4:
    st.header("Pendaftar")
    st.write("Berikut merupakan daftar pendaftar yang sudah mendaftar")
    # Tombol refresh data tanpa st.experimental_rerun
    if st.button("Refresh Data"):
        st.cache_data.clear()  # Menghapus cache agar data terbaru dimuat
    st.dataframe(data)
    
with tab5:
    st.header("Pendaftar yang diterima menjadi peserta")
    st.write("Berikut merupakan daftar pendaftar yang diterima menjadi peserta")
    # Tombol refresh data tanpa st.experimental_rerun
    if st.button("Refresh  Data"):
        st.cache_data.clear()  # Menghapus cache agar data terbaru dimuat
     # Tombol refresh data tanpa st.experimental_rerun
    st.dataframe(data2)
