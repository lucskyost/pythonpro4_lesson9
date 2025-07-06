import streamlit as st

st.title("🐾 THẾ GIỚI ĐỘNG VẬT 🦁")
st.subheader("Nhấn vào từng con vật để xem ảnh, video và nghe tiếng kêu!")

# Định nghĩa các cột
col1, col2, col3, col4, col5 = st.columns(5)  # Chia 5 cột có độ rộng bằng nhau
col6, col7 = st.columns([2, 1])  # Chia 2 cột với cột trái có độ rộng gấp đôi cột phải

# Nút bấm trong các cột từ 1 đến 5
with col1:
    b1 = st.button("Con mèo")  # Mỗi cột sẽ chứa một nút bấm
with col2:
    b2 = st.button("Con chó")
with col3:
    b3 = st.button("Con khỉ")
with col4:
    b4 = st.button("Đại bàng")
with col5:
    b5 = st.button("Con gà")

# Các khối điều kiện cho từng nút bấm
if b1:
    with col6:  # Nếu nút bấm được nhấn, sẽ hiển thị các cột bên trái
        st.write("Âm thanh")
        audio = open("sound/cat.wav", "rb")
        st.audio(audio, format="audio/wav")
    
    st.write("Video")
    video = "https://www.youtube.com/watch?v=retoWhUMs_s"
    st.video(video, format="video/mp4")
    
    with col7:  # Mở file ảnh ở cột bên phải
        image = "img/cat.jpg"
        st.image(image, caption="Con mèo")

if b2:
    with col6:
        st.write("Âm thanh")
        audio = open("sound/dog.wav", "rb")
        st.audio(audio, format="audio/wav")
    
    st.write("Video")
    video = "https://www.youtube.com/shorts/ERZlMCH99tg"
    st.video(video, format="video/mp4")
    
    with col7:
        image = "img/dog.jpg"
        st.image(image, caption="Con chó")

if b3:
    with col6:
        st.write("Âm thanh")
        audio = open("sound/monkey.wav", "rb")
        st.audio(audio, format="audio/wav")
    
    st.write("Video")
    video = "https://www.youtube.com/shorts/dvYypoec4e0"
    st.video(video, format="video/mp4")
    
    with col7:
        image = "img/monkey.jpg"
        st.image(image, caption="Con khỉ")

if b4:
    with col6:
        st.write("Âm thanh")
        audio = open("sound/eagle.wav", "rb")
        st.audio(audio, format="audio/wav")
    
    st.write("Video")
    video = "https://www.youtube.com/watch?v=hecXupPpE9o"
    st.video(video, format="video/mp4")
    
    with col7:
        image = "img/eagle.jpg"
        st.image(image, caption="Đại bàng")

if b5:
    with col6:
        st.write("Âm thanh")
        audio = open("sound/chicken.wav", "rb")
        st.audio(audio, format="audio/wav")
    
    st.write("Video")
    video = "https://www.youtube.com/shorts/nVdvFuR9aQo"
    st.video(video, format="video/mp4")
    
    with col7:
        image = "img/chicken.jpg"
        st.image(image, caption="Con gà")