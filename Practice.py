import streamlit as st
from PIL import Image

st.title("Do you want to convert your image into grayscale?")
st.write("What is your name?")
user_name = st.text_input(label="", key= "name")

with st.expander("Start Camera"):

    camera_image = st.camera_input("Camera")

if camera_image:

    img = Image.open(camera_image)
    gray_img = img.convert("L")
    st.write("Hey", user_name,"this is your grayscale image :)")
    st.image(gray_img)








