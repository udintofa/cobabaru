import streamlit as st
from streamlit_gsheets import GSheetsConnection
import time
import pandas as pd
import numpy as np
import datetime
import time

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

# Membuat DataFrame dengan data yang telah didefinisikan
kegiatan_df = pd.DataFrame(data_kegiatan, columns=["Kegiatan", "Waktu", "Keperluan"])


tab1, tab2, tab4, tab5 = st.tabs(["Informasi", "Pengumuman Peserta", "Keperluan", "About"])

with tab5:
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


with tab2:
    st.header("Pembayaran")
    st.write("Silahkan bagi pendaftar yang sudah menjadi peserta bisa melakukan pembayaran sebesar Rp225.ooo ke rekening Mandiri dengan nomor rekening 1370021364068 atas nama YESYAILLA ABZANI ALFATH."+
            " Pembayaran dilakukan paling lambat pada 25 Oktober 2024 pukul 23.59. Bagi yang ada kendala bisa hubungi cp yang ada.")
    st.write("Jika setelah tgl 25 Oktober 2024 peserta tidak melakukan pembayaran tanpa konfirmasi ke CP yang ada, maka peserta akan digantikan oleh waiting list yang ingin juga mengikuti kegiatan ini.")
    
    # from datetime import datetime
    # deadline = datetime(2024, 10, 25, 23, 59, 0)
    # while True:
    #     # Tanggal saat ini
    #     sekarang = datetime.now()
        
    #     # Menghitung selisih waktu
    #     selisih = deadline - sekarang
        
    #     # Jika deadline sudah tercapai atau lewat
    #     if selisih.total_seconds() <= 0:
    #         print("Deadline sudah tercapai!")
    #         break
        
    #     # Mendapatkan jumlah hari, jam, menit, dan detik dari selisih
    #     hari = selisih.days
    #     detik_sisa = selisih.seconds
    #     jam = detik_sisa // 3600
    #     menit = (detik_sisa % 3600) // 60
    #     detik = detik_sisa % 60
    
    #     # Membersihkan output terminal
    #     st.write(f"Waktu sisa pembayaran: {hari} hari, {jam} jam, {menit} menit, {detik} detik")
    
    #     # Menunggu 1 detik sebelum update lagi
    #     time.sleep(1)

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
    # st.write("Silahkan daftar untuk menjadi peserta LDK Nasional melalui tautan dibawah")
    # Menambahkan hyperlink
    # st.markdown(
    #     """
    #     [Daftar Sekarang](https://docs.google.com/forms/d/e/1FAIpQLSdrODYr9QwUqe2_a5o0o6Jd1oem8ktC1j7oY1UGTGwu9PYVhA/viewform?usp=sf_link)
    #     """
    # )
    st.header("Waiting List")
    if st.button("Refresh Data"):
        st.cache_data.clear()  # Menghapus cache agar data terbaru dimuat
    st.dataframe(data3)

# with tab3:
#     st.header("Pendaftaran")
#     st.write("Silahkan daftar untuk menjadi peserta LDK Nasional melalui tautan dibawah")
#     # Menambahkan hyperlink
#     st.markdown(
#         """
#         [Daftar Sekarang](https://docs.google.com/forms/d/e/1FAIpQLSdrODYr9QwUqe2_a5o0o6Jd1oem8ktC1j7oY1UGTGwu9PYVhA/viewform?usp=sf_link)
#         """
#     )

#     st.write("Berikut merupakan daftar pendaftar yang sudah mendaftar")
#     # Tombol refresh data tanpa st.experimental_rerun
#     if st.button("Refresh Data"):
#         st.cache_data.clear()  # Menghapus cache agar data terbaru dimuat
#     st.dataframe(data)

#     st.header("Pembayaran")
#     st.write("Silahkan bagi pendaftar yang sudah menjadi peserta bisa melakukan pembayaran sebesar Rp225.ooo ke rekening Mandiri dengan nomor rekening 1370021364068 atas nama YESYAILLA ABZANI ALFATH."+
#             " Bagi peserta yang dalam 1 pekan setelah ditetapkan menjadi peserta belum membayar akan dibatalkan menjadi peserta dan akan digantikan oleh pendaftar lain. Bagi yang ada kendala bisa hubungi cp yang ada.")
#     st.write("Dana iuran akan digunakan untuk membayar administrasi seperti sewa bus, bayar tol, serta konsumsi peserta.")
#     st.write("Bagi yang telah membayar, silahkan konfirmasi ke:")
#     st.markdown("[Ihwan](http://wa.me/+6285727318940)")
#     st.markdown("[Akhwat](http://wa.me/+6287732661779)")
#     st.write("Berikut merupakan daftar pendaftar yang diterima menjadi peserta. Kuota peserta 50 mahasiswa dengan masing-masing unit selain Departemen Jaksa diberi kuota 4 peserta yang akan diseleksi setelah penutupan pendaftaran")
#     # Tombol refresh data tanpa st.experimental_rerun
#     if st.button("Refresh_Data"):
#         st.cache_data.clear()  # Menghapus cache agar data terbaru dimuat
#      # Tombol refresh data tanpa st.experimental_rerun
#     st.dataframe(data2)

# with tab4:
#     st.header("Pembayaran")
#     st.write("Silahkan bagi pendaftar yang sudah menjadi peserta bisa melakukan pembayaran sebesar Rp225.ooo ke rekening Mandiri dengan nomor rekening 1370021364068 atas nama YESYAILLA ABZANI ALFATH."+
#             " Bagi peserta yang dalam 1 pekan setelah ditetapkan menjadi peserta belum membayar akan dibatalkan menjadi peserta dan akan digantikan oleh pendaftar lain. Bagi yang ada kendala bisa hubungi cp yang ada.")
#     st.write("Dana iuran akan digunakan untuk membayar administrasi seperti sewa bus, bayar tol, serta konsumsi peserta.")
#     st.write("Bagi yang telah membayar, silahkan konfirmasi ke:")
#     st.markdown("[Ihwan](http://wa.me/+6285727318940)")
#     st.markdown("[Akhwat](http://wa.me/+6287732661779)")
#     st.write("Berikut merupakan daftar pendaftar yang diterima menjadi peserta (kuota peserta 50 mahasiswa)")
#     # Tombol refresh data tanpa st.experimental_rerun
#     if st.button("Refresh  Data"):
#         st.cache_data.clear()  # Menghapus cache agar data terbaru dimuat
#      # Tombol refresh data tanpa st.experimental_rerun
#     st.dataframe(data2)


# with tab3:
#     st.header("Kegiatan")
#     st.write("Kegiatan diawali dengan memperkenalkan masing-masing LDK, dilanjutkan dengan sharing-sharing antar LDK. Rundown kegiatan adalah sebagai berikut:")
#     rd = [
#             ['19.00-20.00', 1, 'kumpul peserta', 'Sekre'],
#             ['20.00-04.00', 8, 'Perjalanan menuju Surabaya', 'Jalan'],
#             ['04.00-07.00', 3, 'Solat subuh, mandi, dan persiapan', 'Masjid Unair'],
#             ['07.00-08.00', 1, 'Perjalanan ke Lokasi Kunjungan', 'Jalan'],
#             ['08.00-09.00', 1, 'Sarapan pagi', 'Unair'],
#             ['09.00-15.00', 6, 'Acara Kunjungan dg LDK UKMKI Unair', 'Unair'],
#             ['15.00-17.30', 2.5, 'Jalan-jalan Tour Kampus Unair', 'Unair'],
#             ['17.30-19.00', 1.5, 'Salat Magrib dan Isya', 'Unair'],
#             ['19.00-20.00', 1, 'Perjalanan ke Wisata Kota Lama', 'Jalan'],
#             ['20.00-23.59', 4, 'Main-main di Kotalama', 'Kotalama'],
#             ['00.00-04.00', 4, 'Perjalanan ke Kota Malang', 'Jalan'],
#             ['04.00-07.00', 3, 'Solat subuh, mandi, dan persiapan', 'Masjid UB'],
#             ['07.00-08.00', 1, 'Perjalanan ke Lokasi Kunjungan', 'Jalan'],
#             ['08.00-14.00', 6, 'Acara Kunjungan dg LDK UAKI UB + makan siang', 'UB'],
#             ['14.00-15.00', 1, 'Jalan-jalan Tour Kampus UB', 'UB'],
#             ['15.00-16.00', 1, 'Perjalanan ke Kota Batu', 'Jalan'],
#             ['16.00-21.00', 5, 'Main-main di Kota Batu dan beli Oleh-oleh', 'Wisata'],
#             ['21.00-03.00', 6, 'Perjalanan ke Yogyakarta', 'Jalan'],
#         ]
#     # Menambahkan nama kolom saat membuat DataFrame
#     rundown = pd.DataFrame(rd, columns=['Waktu', 'Durasi (jam)', 'Kegiatan', 'Lokasi'])
#     st.write(rundown)


with tab4:
    st.header("Keperluan Peserta")
    st.write("Berikut merupakan keperluan peserta yang wajib atau diutamakan untuk dibawa:")
    st.write('''
                1. DC hari pertama yaitu kemeja putih
                2. DC hari kedua yaitu kemeja batik
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
    
    st.subheader("Rangkaian Kegiatan Kunjungan")
    with st.expander("Lihat Rangkaian"):
        st.write("Berikut rangkaian kegiatan selama kunjungan LDK Nasional")
        st.dataframe(kegiatan_df)
        
    st.subheader("Petunjuk Teknis Peserta")
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

    st.subheader("War Seat Bus")
    import os
    
    # Nama file CSV tempat data akan disimpan
    csv_file = 'data_kursi.csv'
    
    # Cek apakah file CSV sudah ada
    if not os.path.exists(csv_file):
        # Jika file belum ada, buat file baru dengan header
        df = pd.DataFrame(columns=["Nama", "Kursi Pilihan 1", "Kursi Pilihan 2", 
                                   "Kursi Pilihan 3", "Kursi Pilihan 4", "Kursi Pilihan 5"])
        df.to_csv(csv_file, index=False)
    
    # Fungsi untuk menambahkan data ke CSV (append)
    def save_to_csv(data):
        # Menambahkan data baru ke file CSV dengan mode append
        data.to_csv(csv_file, mode='a', header=False, index=False)
    
    # Judul dan form input
    st.subheader("Form Pemilihan Kursi Duduk")

    with st.expander("Isi form"):
        # Input nama
        nama = st.text_input("Nama:")
        
        # Pilihan kursi duduk
        kursi_1 = st.text_input("Kursi Duduk Pilihan 1:")
        kursi_2 = st.text_input("Kursi Duduk Pilihan 2:")
        kursi_3 = st.text_input("Kursi Duduk Pilihan 3:")
        kursi_4 = st.text_input("Kursi Duduk Pilihan 4:")
        kursi_5 = st.text_input("Kursi Duduk Pilihan 5:")
    
    # Tombol untuk menyimpan data
    if st.button("Simpan"):
        if nama and kursi_1 and kursi_2 and kursi_3 and kursi_4 and kursi_5:
            # Data yang akan disimpan dalam format DataFrame
            new_data = pd.DataFrame([{
                "Nama": nama,
                "Kursi Pilihan 1": kursi_1,
                "Kursi Pilihan 2": kursi_2,
                "Kursi Pilihan 3": kursi_3,
                "Kursi Pilihan 4": kursi_4,
                "Kursi Pilihan 5": kursi_5
            }])
    
            # Menyimpan data ke CSV
            save_to_csv(new_data)
            st.success("Data berhasil disimpan!")
        else:
            st.error("Semua kolom harus diisi!")
    
        
            
