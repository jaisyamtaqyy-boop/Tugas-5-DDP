import streamlit as st
st.title("Form Data Diri")
st.write("Silakan isi data diri Anda di bawah ini:")
st.write("made by jai")

with st.form("form_data_diri"):
    nama = st.text_input("Nama Lengkap")
    alamat = st.text_input("Alamat")
    usia = st.number_input("Usia")
    submit = st.form_submit_button("Submit")
    
    if submit:
        st.success(f"terima kasih, {nama}, mengisi data diri Anda!")
        st.write(f"Nama : {nama}")
        st.write(f"Alamat : {alamat}")
        st.write(f"Usia : {usia} tahun")