import streamlit as st
from streamlit_gsheets import GSheetsConnection
import time
import pandas as pd
import numpy as np
from datetime import datetime
import time
import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from google.oauth2.service_account import Credentials
import json
import pytz

#title page
st.set_page_config(
    page_title="Kunjungan LDKN",
    page_icon=":rocket:",
    layout="centered",
    initial_sidebar_state="auto",
    menu_items=None)

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            <style>            
"""


# Fungsi untuk membaca data dari Google Sheets
def load_data(url):
    conn = st.connection("gsheets", type=GSheetsConnection)
    data = conn.read(spreadsheet=url, usecols=[1, 2, 3, 5, 9])
    return data

# Fungsi untuk membaca data dari Google Sheets
def load_data2(url):
    conn = st.connection("gsheets", type=GSheetsConnection)
    data = conn.read(spreadsheet=url, usecols=[1, 2, 5, 9, 11])
    return data

# URL Google Sheets
url = 'https://docs.google.com/spreadsheets/d/1tU0OByLfC0ISXWk2OAhknPnrpSeOX2GtaZFG0DWjwvc/edit?usp=sharing'
url2 = 'https://docs.google.com/spreadsheets/d/1gC_9B9rcl5F9Cx12AMyD-HPeXmyPrYk8o-ey6RxSbMg/edit?usp=sharing'
url3 = 'https://docs.google.com/spreadsheets/d/1IG6p-mV0beuyKncItIqwnJ57zD42R9-kHKXGsXxcDQQ/edit?usp=sharing'
    
# Memuat dan menampilkan data

data = load_data(url)
data2 = load_data2(url2)
data3 = load_data(url3)
data["Angkatan masuk JS"] = data["Angkatan masuk JS"].astype(str)
data2["Angkatan masuk JS"] = data2["Angkatan masuk JS"].astype(str)
data3["Angkatan masuk JS"] = data3["Angkatan masuk JS"].astype(str)

# Menggunakan reset_index dan mulai indeks dari 1
data = data.reset_index(drop=True)  # Reset index terlebih dahulu
data.index = data.index + 1         # Mengubah index menjadi mulai dari 1

# Menggunakan reset_index dan mulai indeks dari 1
data2 = data2.reset_index(drop=True)  # Reset index terlebih dahulu
data2.index = data2.index + 1         # Mengubah index menjadi mulai dari 1

# Menggunakan reset_index dan mulai indeks dari 1
data3 = data3.reset_index(drop=True)  # Reset index terlebih dahulu
data3.index = data3.index + 1         # Mengubah index menjadi mulai dari 1

st.write('''
# :raised_hand_with_fingers_splayed: Selamat Datang :raised_hand_with_fingers_splayed:
### di Laman Departemen Jaksa :blush::pray:
mari bermuhasabah diri, meluruskan niat, ikhlaskan pikiran, dan berusaha menjadi hamba yang baik untuk Allah SWT
''')

#dataframe kegiatan
data_kegiatan = [
    ["Perjalanan dari UGM ke Surabaya", "19.30-04.00", "Perjalanan"],
    ["Singgah di Masjid Nasional Al Akbar", "04.00-07.00", "Subuh, mandi, persiapan"],
    ["Perjalanan menuju Kampus A Unair", "07.00-08.00", "Perjalanan"],
    ["Kegiatan Kunjungan bersama LDK UKMKI Unair", "08.00-12.00", "Makan (disediakan), Kegiatan kunjungan"],
    ["Isama", "12.00-13.00", "Dzuhur, Ashar, Makan (disediakan)"],
    ["Kampus Tour Unair", "13.00-16.00", "Kampus Tour"],
    ["Isa", "16.00-18.00", "Ashar (bagi yg belum jamak sm zuhur), magrib (sekalian isya)"],
    ["Perjalanan ke Wisata Kota Lama Surabaya", "18.00-19.00", "Perjalanan"],
    ["Main di Kota Lama Surabaya", "18.30-23.00", "Isya (bagi yg belum), makan mandiri, main"],
    ["Perjalanan dari Surabaya ke Malang", "23.00-04.00", "Perjalanan"],
    ["Singgah di Masjid Kampus Raden Patah UB", "04.00-07.00", "Subuh, mandi, persiapan"],
    ["Perjalanan menuju lokasi Kegiatan Kunjungan", "07.00-08.00", "Perjalanan"],
    ["Kegiatan Kunjungan bersama LDK UAKI UB", "08.00-12.00", "Makan (disediakan), Kegiatan Kunjungan"],
    ["Isama", "12.00-13.00", "Dzuhur sekalian Ashar, makan (disediakan)"],
    ["Kampus Tour UB", "13.00-15.00", "Kampus Tour"],
    ["Perjalanan ke Kota Batu", "15.00-16.00", "Perjalanan"],
    ["Main dan beli oleh-oleh ke Kota Batu Malang", "16.00-21.00", "Magrib, Isya, Main, Beli Oleh-oleh"],
    ["Perjalanan pulang ke UGM", "21.00-04.00", "Perjalanan"]
]

#Menyambung sheet form
# Fungsi untuk autentikasi ke Google Sheets menggunakan Streamlit Secrets
def authenticate_google_sheets():
    # Mengambil kredensial JSON dari Streamlit Secrets (sudah berbentuk dictionary)
    creds_data = st.secrets["gcp_service_account"]
    
    # Tentukan scope API yang dibutuhkan
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    
    # Membuat kredensial dari dictionary JSON
    creds = Credentials.from_service_account_info(creds_data, scopes=scope)
    
    # Otentikasi dan membuat client Google Sheets
    client = gspread.authorize(creds)
    return client

# Fungsi untuk menyimpan data ke Google Sheets Versi War
def save_to_google_sheets(data):
    client = authenticate_google_sheets()
    # Membuka Google Sheet berdasarkan nama file
    sheet = client.open("FormSeatBus").sheet1  # Ganti dengan nama sheet Anda
    # Menambahkan data ke Google Sheets
    sheet.append_row(data)

# Fungsi untuk menyimpan data ke Google Sheets Playlist
def save_to_google_sheets2(data):
    client = authenticate_google_sheets()
    # Membuka Google Sheet berdasarkan nama file
    sheet = client.open("Playlist").sheet1  # Ganti dengan nama sheet Anda
    # Menambahkan data ke Google Sheets
    sheet.append_row(data)

# Membuat DataFrame dengan data yang telah didefinisikan
kegiatan_df = pd.DataFrame(data_kegiatan, columns=["Kegiatan", "Waktu", "Keperluan"])


tab1, tab2, tab3, tab4 = st.tabs(["Informasi", "Pengumuman Peserta", "Keperluan", "About"])

with tab4:
    st.header("Tentang Kunjungan LDK Nasional")
    st.write("#### JS gass ke Unair dan UB besok :bus::rocket::bus::rocket:")
    st.image("poster kunjungan.jpg", caption="Poster Kunjungan LDK Nasional")
    st.write("Kunjungan LDKN merupakan salah satu kegiatan Departemen Jaringan dan Kerjasama yang di mana dilakukan dalam rangka mempererat silaturahmi antar Lembaga dengan berkunjung ke Lembaga lain untuk saling bertukar informasi seputar strategi yang dilakukan lembaga, metode, kaderisasi dan lain-lain yang bermanfaat untuk kemajuan lembaga serta memahami bagaimana struktur atau kondisi umum lembaga yang bisa diambil dan diterapkan di lembaganya.")  
    st.write("Kunjungan LDK Nasional akan dilaksanakan pada hari Jumat (8 Nov 2024) malam sampai dengan hari Senin (11 Nov 2024) pagi. Kunjungan akan dilaksanakan ke LDK UKMKI Unair terlebih dahulu pada Sabtu (9 Nov 2024) dilanjutkan berkunjung ke LDK UAKI UB pada Minggu (10 Nov 2024).")
    
    st.header("Panitia Kunjungan LDK Nasional")
    data_diri = [
        ["Penanggung Jawab","Muchammad Udin Mustofa"],
        ['Ketua Pelaksana',"Ahmad Haidar Rasyid"],
        ["Sekbend","Yesyailla Abzani Alfath"],
        ["Perlengkapan", "Auva Bima Ahada"],
        ['Perlengkapan', 'Diva Aisya'],
        ['Media','Arif Taufik'],
        ['Acara', 'Fathiya Al-Khansa'],
        ['Konsumsi', 'Anisa Nurliana']
        
    ]
    dd = pd.DataFrame(data_diri, columns=["Nama Panita", "Jabatan"])
    # Menggunakan reset_index dan mulai indeks dari 1
    dd = dd.reset_index(drop=True)  # Reset index terlebih dahulu
    dd.index = dd.index + 1         # Mengubah index menjadi mulai dari 1
    st.write(dd)
    
    st.subheader("Playlist Perjalanan")
    with st.expander("Berikut Usulan Playlist Sementara"):
        st.write('coming soon')

        # Input Nama
        judul_lagu = st.text_input("Judul Lagu (wajib diisi):")
        penyanyi = st.text_input("Penyanyi (wajib diisi):")
        pengusul = st.text_input("Siapa pengusulnya ini?")
        
        # Tombol untuk menyimpan data
        if st.button("Simpan"):
            if judul_lagu and penyanyi and pengusul:
                # Zona waktu Indonesia (WIB)
                tz = pytz.timezone("Asia/Jakarta")
                # Ambil timestamp saat ini
                timestamp = datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")
                new_data = [timestamp, judul_lagu, penyanyi, pengusul]
                save_to_google_sheets2(new_data)
                st.success("Data berhasil disimpan. Ingat!! ada yg bilang kalau musik itu haram, maka pilihlah murotal")
            else:
                st.error("Semua wajib diisi")
        


with tab2:
    st.header("Pembayaran")
    st.write("Silahkan bagi pendaftar yang sudah menjadi peserta bisa melakukan pembayaran sebesar Rp225.ooo ke rekening Mandiri dengan nomor rekening 1370021364068 atas nama YESYAILLA ABZANI ALFATH."+
            " Pembayaran dilakukan paling lambat pada 25 Oktober 2024 pukul 23.59. Bagi yang ada kendala bisa hubungi cp yang ada.")
    st.write("Jika setelah tgl 25 Oktober 2024 peserta tidak melakukan pembayaran tanpa konfirmasi ke CP yang ada, maka peserta akan digantikan oleh waiting list yang ingin juga mengikuti kegiatan ini.")
    st.write("Dana iuran akan digunakan untuk membayar administrasi seperti sewa bus, bayar tol, serta konsumsi peserta.")
    st.write("Bagi yang telah membayar, silahkan konfirmasi ke:")
    st.markdown("[Ihwan](http://wa.me/+6285727318940)")
    st.markdown("[Akhwat](http://wa.me/+6287732661779)")
    st.header("Peserta")
    st.write("Berikut daftar peserta kunjungan LDK Nasional")
    # Tombol refresh data tanpa st.experimental_rerun
    if st.button("Refresh  Data"):
        st.cache_data.clear()  # Menghapus cache agar data terbaru dimuat
    st.dataframe(data2)

with tab3:
    st.header("Keperluan Peserta")
    st.write("Berikut merupakan keperluan peserta yang wajib atau diutamakan untuk dibawa:")
    st.write('''
                1. DC hari pertama yaitu kemeja putih
                2. DC hari kedua yaitu kemeja batik (ihwan) dan berkain (akhwat)
                3. Jas Almamater UGM
                4. Baju ganti
                5. Alat Solat
                6. Tumbler
                7. Sepatu
                8. Obat-obatan pribadi
                9. Bantal  (opsional)
                10. Selimut (opsional)
                11. Jaket (opsional)
                12. Peralatan pribadi (opsional)
            ''')

with tab1:
    st.header("Informasi Untuk Peserta")
    
    st.subheader(":page_facing_up: Rangkaian Kegiatan Kunjungan")
    with st.expander("Lihat Rangkaian"):
        st.write("Berikut rangkaian kegiatan selama kunjungan LDK Nasional")
        st.dataframe(kegiatan_df)
        
    st.subheader(":warning: Petunjuk Teknis Peserta")
    # Membaca file PDF sebagai binary
    with open("Juknis LDK Nasional.pdf", "rb") as pdf_file:
        pdf_data = pdf_file.read()
    
    # Tombol untuk mengunduh file PDF
    st.download_button(
        label="Unduh File PDF",
        data=pdf_data,
        file_name="Juknis LDK Nasional.pdf",
        mime="application/pdf"
    )

    st.subheader(":bus: Penomoran Kursi Bus")
    with st.expander("Penomoran Kursi"):
        st.image("SeatBus.png", caption="Penomoran Kursi Bus")

    
    st.subheader(":fire: War Seat Bus:fire:")
    # Judul dan form input
    st.write("Form Pemilihan Kursi Duduk")
    with st.expander("WAR SEKARANGGG:fire::fire::fire:"):
        sm_siapa = ""
        kenapa = ""

        # Input Nama
        nama = st.text_input("Nama (wajib diisi):")
        # Input Pilihan Kursi Duduk
        kursi_1 = st.selectbox("Kursi Duduk Pilihan 1 (wajib diisi)", [i for i in range(50)])
        kursi_2 = st.selectbox("Kursi Duduk Pilihan 2 (wajib diisi)", [i for i in range(50)])
        kursi_3 = st.selectbox("Kursi Duduk Pilihan 3 (wajib diisi)", [i for i in range(50)])
        kursi_4 = st.selectbox("Kursi Duduk Pilihan 4 (wajib diisi)", [i for i in range(50)])
        kursi_5 = st.selectbox("Kursi Duduk Pilihan 5 (wajib diisi)", [i for i in range(50)])
        jejer = st.radio("Apakah kamu harus bersebelahan sm temenmu? (wajib diisi)", ["Iya", "Sama siapa aja juga gapapa"])
        sm_siapa = st.text_input("Sama siapa? (Jika pilih Iya di pertanyaan sebelumnya):")
        kenapa = st.text_input("Kenapa harus sm dia? (Jika pilih Iya di pertanyaan sebelumnya)")
        
        # Tombol untuk menyimpan data
        if st.button("Simpan"):
            if nama and kursi_1 and kursi_2 and kursi_3 and kursi_4 and kursi_5 and jejer:
                # Zona waktu Indonesia (WIB)
                tz = pytz.timezone("Asia/Jakarta")
                # Ambil timestamp saat ini
                timestamp = datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")
                new_data = [timestamp, nama, kursi_1, kursi_2, kursi_3, kursi_4, kursi_5, jejer, sm_siapa, kenapa]
                save_to_google_sheets(new_data)
                st.success("Data berhasil disimpan, Semoga mendapatkan tempat duduk terbaik yaa. Maaf kalau panitia banyak salah!")
            else:
                st.error("Kolom wajib harus diisi!")

    
