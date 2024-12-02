import streamlit as st
import pandas as pd
import numpy as np

# Fungsi untuk melakukan prediksi sederhana
def predict(data):
    # Contoh sederhana: misalnya jika nilai di kolom 'value' lebih besar dari 50, maka True, jika tidak maka False
    data['Deteksi'] = data['value'] > 50
    return data

# Judul utama aplikasi
st.title("Aplikasi Prediksi Hasil Deteksi Data")

# Sidebar untuk navigasi menu
menu = st.sidebar.selectbox("Pilih Menu", ["Prediksi"])

# Jika menu 'Prediksi' dipilih
if menu == "Prediksi":
    st.header("Prediksi Hasil Deteksi Data")

    # Upload file CSV
    uploaded_file = st.file_uploader("Upload file CSV", type="csv")
    
    if uploaded_file is not None:
        # Membaca file CSV
        data = pd.read_csv(uploaded_file)
        
        # Menampilkan data yang diupload
        st.write("Data yang diupload:")
        st.dataframe(data)
        
        # Menjalankan fungsi prediksi
        hasil_prediksi = predict(data.copy())
        
        # Menampilkan hasil prediksi
        st.write("Hasil Prediksi (True/False):")
        st.dataframe(hasil_prediksi)
        
        # Tombol untuk download hasil prediksi sebagai CSV
        csv = hasil_prediksi.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Download hasil prediksi sebagai CSV",
            data=csv,
            file_name='hasil_prediksi.csv',
            mime='text/csv'
        )
    else:
        st.warning("Silakan upload file CSV terlebih dahulu.")
