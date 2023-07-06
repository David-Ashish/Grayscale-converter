import streamlit as st
from PIL import Image

st.title("Do you want to convert your image into grayscale?")

#uploaded_image = st.file_uploader("Upload Image")
with st.expander("Start Camera"):

    camera_image = st.camera_input("Camera")

st.write("What is your name?", font="Helvetica")
user_name = st.text_input(label="", key="name")

if camera_image:

    img = Image.open(camera_image)
    gray_img = img.convert("L")
    st.write("Hey modala", user_name,", i will meet you very soon :)")
    st.image(gray_img)

#if uploaded_image:

    #img = Image.open(uploaded_image)
    #gray_uploaded_img = img.convert('L')
    #st.image(gray_uploaded_img)








