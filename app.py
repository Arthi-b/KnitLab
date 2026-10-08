import streamlit as st
from PIL import Image

st.title("KnitLab")
st.write("Turn inspiration into a knitting chart.")

uploaded_file = st.file_uploader(
    "Upload an inspiration image",
    type=["png", "jpg", "jpeg"]
)

if uploaded_file is not None:
    image = Image.open(uploaded_file)

    st.image(
        image,
        caption="Your inspiration image"
    )