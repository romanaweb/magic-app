import streamlit as st
import google.generativeai as genai

# --- Konfigurasi Halaman ---
st.set_page_config(
    page_title="Magic App",
    page_icon="🌱",
    layout="centered"
)

# --- Judul dan Deskripsi ---
st.title("🌱 Aplikasi Magic")
st.write("Masukkan ide singkat, dan lihatlah ia tumbuh menjadi sesuatu yang menakjubkan!")

# --- Mengambil Kunci Rahasia ---
# Kita akan mengatur kunci ini di Langkah 4, jangan ditulis langsung di sini!
try:
    api_key = st.secrets["GOOGLE_API_KEY"]
    genai.configure(api_key=api_key)
except FileNotFoundError:
    st.error("Kunci API belum diatur. Silakan atur di Streamlit Secrets.")
    st.stop()

# --- Memilih Model AI ---
# Kita menggunakan model Gemini Pro yang bagus untuk teks
model = genai.GenerativeModel('gemini-pro')

# --- Area Input Pengguna ---
user_input = st.text_area("Tulis bibit idemu di sini (contoh: 'Seekor kucing yang ingin terbang'):", height=100)
tombol_grow = st.button("✨ Tumbuhkan Ide Ajaib! ✨")

# --- Logika "Magic App" ---
if tombol_grow and user_input:
    with st.spinner("Sedang menyiram ide dengan keajaiban..."):
        try:
            # Ini adalah "mantra" yang kita kirim ke AI
            # Kita meminta AI untuk bertindak sebagai penulis kreatif.
            prompt_rahasia = f"""
            Bertindaklah sebagai penulis kreatif dan imajinatif.
            Tugasmu adalah mengambil input singkat berikut dan mengembangkannya ("menumbuhkannya") 
            menjadi paragraf yang kaya, detail, dan menarik. Gunakan bahasa Indonesia yang ekspresif.
            
            Input Singkat: "{user_input}"
            
            Hasil Pengembangan:
            """
            
            # Meminta AI membuat respons
            response = model.generate_content(prompt_rahasia)
            
            # Menampilkan Hasil
            st.success("Ide berhasil tumbuh!")
            st.markdown("### Hasil Panen Imajinasimu:")
            st.write(response.text)
            
        except Exception as e:
            st.error(f"Terjadi kesalahan saat menumbuhkan ide: {e}")

elif tombol_grow and not user_input:
    st.warning("Tolong masukkan bibit ide dulu ya!")

# --- Footer ---
st.markdown("---")
st.caption("Dibuat dengan ❤️ menggunakan Streamlit dan Google Gemini AI")
