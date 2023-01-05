import streamlit as st
from PIL import Image
import requests

st.title("Virtual Room Staging")

uploaded_file = st.file_uploader("Choose an image file")

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Original Image", use_column_width=True)

    # Send the image to the Dalle API
    api_key = "your-api-key"
    api_url = "https://api.dalle.io/v1/staging"
    headers = {"Authorization": f"Bearer {api_key}"}
    files = {"image": uploaded_file}
    response = requests.post(api_url, headers=headers, files=files)

    # Display the staged image
    if response.status_code == 200:
        staged_image_url = response.json()["data"]["url"]
        staged_image = Image.open(requests.get(staged_image_url, stream=True).raw)
        st.image(staged_image, caption="Staged Image", use_column_width=True)
    else:
        st.error("There was an error processing the image")
