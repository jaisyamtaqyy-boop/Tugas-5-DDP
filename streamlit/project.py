import streamlit as st
import random

# ==================================================
# KONFIGURASI HALAMAN
# ==================================================
st.set_page_config(
    page_title="Laptop Recommender",
    layout="centered"
)

# ==================================================
# INIT SESSION STATE
# ==================================================
default_state = {
    "status": None,
    "mobilitas": None,
    "os": None,
    "kebutuhan": None,
    "durasi": 8,
    "aplikasi": "",
    "budget": None,
    "ram": None,
    "storage": None,
    "prioritas": None,
    "merek": "Bebas",
    "baterai": "4000–5000 mAh"
}

for key, val in default_state.items():
    if key not in st.session_state:
        st.session_state[key] = val

# ==================================================
# DATA CONTOH LAPTOP
# ==================================================
contoh_laptop = {
    "Entry": {
        "ASUS": ["ASUS VivoBook 14", "ASUS X441"],
        "Lenovo": ["Lenovo IdeaPad 3", "Lenovo V14"],
        "Acer": ["Acer Aspire 3", "Acer Extensa"],
        "HP": ["HP 14s", "HP 240 G8"]
    },
    "Menengah": {
        "ASUS": ["ASUS ZenBook 14", "ASUS VivoBook S14"],
        "Lenovo": ["Lenovo IdeaPad Slim 5", "Lenovo ThinkBook"],
        "Acer": ["Acer Swift 3", "Acer Aspire 5"],
        "HP": ["HP Pavilion", "HP Envy"]
    },
    "Tinggi": {
        "ASUS": ["ASUS TUF Gaming", "ASUS ROG Strix"],
        "Lenovo": ["Lenovo Legion", "Lenovo LOQ"],
        "Acer": ["Acer Nitro 5", "Acer Predator"],
        "HP": ["HP Omen", "HP Victus"]
    }
}

# ==================================================
# SIDEBAR
# ==================================================
st.sidebar.title("💻 Laptop Recommender")
menu = st.sidebar.selectbox(
    "📂 Navigasi Menu",
    ["👤 Profil", "📌 Kebutuhan", "💰 Budget", "🏆 Rekomendasi"]
)
st.sidebar.caption("📊 website rekomendasi laptop")

# ==================================================
# HALAMAN PROFIL
# ==================================================
if menu == "👤 Profil":
    st.title("👤 Profil Pengguna")

    st.session_state.status = st.selectbox(
        "Status",
        ["Pelajar", "Mahasiswa", "Pekerja"],
        index=0 if st.session_state.status is None else
        ["Pelajar", "Mahasiswa", "Pekerja"].index(st.session_state.status)
    )

    st.session_state.mobilitas = st.selectbox(
        "Mobilitas",
        ["Rendah", "Sedang", "Tinggi"],
        index=0 if st.session_state.mobilitas is None else
        ["Rendah", "Sedang", "Tinggi"].index(st.session_state.mobilitas)
    )

    st.session_state.os = st.selectbox(
        "Sistem Operasi",
        ["Windows", "Linux", "MacOS"],
        index=0 if st.session_state.os is None else
        ["Windows", "Linux", "MacOS"].index(st.session_state.os)
    )

# ==================================================
# HALAMAN KEBUTUHAN
# ==================================================
elif menu == "📌 Kebutuhan":
    st.title("📌 Kebutuhan Penggunaan")

    st.session_state.kebutuhan = st.selectbox(
        "Kebutuhan Utama",
        ["Kuliah", "Kerja", "Desain", "Gaming"],
        index=0 if st.session_state.kebutuhan is None else
        ["Kuliah", "Kerja", "Desain", "Gaming"].index(st.session_state.kebutuhan)
    )

    st.session_state.durasi = st.slider(
        "Durasi penggunaan per hari (jam)",
        1, 16,
        st.session_state.durasi
    )

    st.session_state.aplikasi = st.text_input(
        "Aplikasi utama",
        st.session_state.aplikasi
    )

# ==================================================
# HALAMAN BUDGET
# ==================================================
elif menu == "💰 Budget":
    st.title("💰 Budget & Preferensi")

    st.session_state.budget = st.selectbox(
        "Budget",
        ["< 5 Juta", "5–10 Juta", "10–15 Juta", "> 15 Juta"],
        index=0 if st.session_state.budget is None else
        ["< 5 Juta", "5–10 Juta", "10–15 Juta", "> 15 Juta"].index(st.session_state.budget)
    )

    st.session_state.ram = st.selectbox(
        "RAM minimal",
        ["8 GB", "16 GB", "32 GB", "64 GB"],
        index=0 if st.session_state.ram is None else
        ["8 GB", "16 GB", "32 GB", "64 GB"].index(st.session_state.ram)
    )

    st.session_state.storage = st.selectbox(
        "Penyimpanan",
        ["SSD 256 GB", "SSD 512 GB", "SSD 1 TB"],
        index=0 if st.session_state.storage is None else
        ["SSD 256 GB", "SSD 512 GB", "SSD 1 TB"].index(st.session_state.storage)
    )

    st.session_state.prioritas = st.selectbox(
        "Prioritas",
        ["Harga", "Performa", "Baterai"],
        index=0 if st.session_state.prioritas is None else
        ["Harga", "Performa", "Baterai"].index(st.session_state.prioritas)
    )

# ==================================================
# HALAMAN REKOMENDASI
# ==================================================
elif menu == "🏆 Rekomendasi":
    st.title("🏆 Rekomendasi Laptop")

    st.session_state.merek = st.selectbox(
        "Merek Favorit",
        ["Bebas", "ASUS", "Lenovo", "Acer", "HP"]
    )

    # ======================
    # OPSI BATERAI
    # ======================
    opsi_baterai = [
        "< 4000 mAh",
        "4000–5000 mAh",
        "5000–6000 mAh",
        "> 6000 mAh"
    ]

    if st.session_state.baterai not in opsi_baterai:
        st.session_state.baterai = "4000–5000 mAh"

    st.session_state.baterai = st.selectbox(
        "Kapasitas baterai laptop",
        opsi_baterai,
        index=opsi_baterai.index(st.session_state.baterai)
    )

    # ======================
    # TOMBOL REKOMENDASI
    # ======================
    if st.button("🔍 Tampilkan Rekomendasi"):
        if not all([
            st.session_state.kebutuhan,
            st.session_state.budget,
            st.session_state.prioritas
        ]):
            st.warning("⚠ Lengkapi data di menu sebelumnya")
            st.stop()

        kebutuhan = st.session_state.kebutuhan
        budget = st.session_state.budget
        prioritas = st.session_state.prioritas

        # LOGIKA KATEGORI
        if budget == "< 5 Juta":
            kategori = "Entry"
            harga = "Rp 4 – 6 Juta"
        elif kebutuhan in ["Gaming", "Desain"] or prioritas == "Performa":
            kategori = "Tinggi"
            harga = "Rp 15 – 25 Juta"
        else:
            kategori = "Menengah"
            harga = "Rp 8 – 12 Juta"

        st.success(f"Laptop {kategori}")

        st.markdown("### ⭐ Contoh Produk")
        merek = st.session_state.merek

        if merek == "Bebas":
            for m in contoh_laptop[kategori]:
                st.write("-", random.choice(contoh_laptop[kategori][m]))
        else:
            for item in contoh_laptop[kategori][merek]:
                st.write("-", item)

        st.markdown("### 💰 Estimasi Harga")
        st.write(harga)

        st.caption("Rekomendasi berbasis rule-based system")
