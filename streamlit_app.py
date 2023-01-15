import streamlit as st
from PIL import Image
import requests

st.title("Virtual Room Staging")

uploaded_file = st.file_uploader("Choose an image file")

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Original Image", use_column_width=True)

    # Send the image to the Stable Diffusion API
    api_key = ""
    api_url = "https://stablediffusionapi.com/api/v3/img2img"
    headers = {
        "Content-Type": "application/json"
    }
    body = {
        "key": "76XgHJI9sRqRf24mQIVe6KySJZyDV6wcJbhzVVkYamRW2yie9UMTovBnyvu7",
        "prompt": "high resolution photography interior design, wooden floor, bedroom cozy atmosphere",
        "negative_prompt": "null",
        "init_image": "https://d12mivgeuoigbq.cloudfront.net/assets/blog/Great%20American%20Home%20Store/greatamericanhomestore-seotool-56745-essentialbedroomfurniture-blogbanner1.jpg",
        "width": "512",
        "height": "512",
        "samples": "1",
        "num_inference_steps": "30",
        "guidance_scale": 7.5,
        "strength": 0.7,
        "seed": "null",
        "webhook": "null",
        "track_id": "null"
    }
    response = requests.post(api_url, headers=headers, json=body)

    # Display the staged image
    if response.status_code == 200:
        st.write(response.json())
        # staged_image_url = response.json()["output"][0]
        # staged_image = Image.open(requests.get(staged_image_url, stream=True).raw)
        # st.image(staged_image, caption="Staged Image", use_column_width=True)
    else:
        st.error("There was an error processing the image")
