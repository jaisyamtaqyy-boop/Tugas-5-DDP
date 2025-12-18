import streamlit as st

st.title("Komponen Dasar Streamlit")
st.header("Header Level 1")
st.subheader("Header Level 2")

st.markdown("# H1")
st.markdown("## H2")
st.markdown("### H3")
st.markdown("#### H4")
st.markdown("##### H5")
st.markdown("###### H6")

st.caption("Ini adalah teks caption.")

st.code("""def hello():
    print("Hello, Streamlit!")
""", language='python')

st.divider()

with st.echo():
    st.write("Kode ini akan ditampilkan dan dieksekusi!")

st.latex(r"E = mc^2")

st.text("Ini adalah teks biasa dalam Streamlit")

import pandas as pd
df = pd.DataFrame({"Nama": ["Ali", "Budi", "Citra"], "Usia": [25, 30, 22]})
st.dataframe(df)

st.json({"nama": "Ali", "usia": 25})

st.table(df)

st.image("Furina.jpg", caption="Contoh Gambar", use_column_width=True)

st.success("Operasi berhasil!")

st.info("Ini adalah informasi penting.")

st.warning("Hati-hati dengan tindakan ini!")

st.error("Terjadi kesalahan!")

st.help(st.button)

import streamlit as st

st.html(
    "<h1 style='color:red;'>Hello Streamlit!</h1>"
)

col1, col2 = st.columns(2)
col1.write("Ini adalah kolom pertama")
col2.write("Ini adalah kolom kedua")

with st.container():
    st.write("Ini adalah dalam container")

placeholder = st.empty()
placeholder.text("Teks sementara")

st.balloons()

st.snow()

with st.expander("Klik untuk melihat lebih banyak"):
    st.write("Ini adalah konten tersembunyi")

with st.form("form1"):
    name = st.text_input("Masukkan Nama")
    submit = st.form_submit_button("Kirim")

with st.popover("Klik di sini"):
    st.write("Ini adalah popover")

st.sidebar.title("Menu Samping")
pilihan = st.sidebar.selectbox("Pilih menu", ["Home", "Profil", "Kontak"])

tab1, tab2 = st.tabs(["Tab 1", "Tab 2"])
with tab1:
    st.write("Konten Tab 1")
with tab2:
    st.write("Konten Tab 2")