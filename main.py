import io
import os
import requests

import streamlit as st
import replicate
from PIL import Image
import imagehash
from streamlit_image_comparison import image_comparison

CHALLEGNGES = ["giraffe.png","surf.png"]
HASHES = {}

# Precompute hashes for all challenges
for challenge in CHALLEGNGES:
    HASHES[challenge] = imagehash.dhash(Image.open(os.path.join("challenges",challenge)))

# Set up the favicon and title
st.set_page_config(
    page_title="Prompt Artistry",
    page_icon="🎨"
)

st.title("Prompt Artistry")

# Challenge Picker
challenge = st.selectbox("Select a challenge", CHALLEGNGES)
with st.expander("Challenge"):
    st.image(os.path.join("challenges",challenge),use_column_width=True,width=500)

prompt = st.text_area("Prompt")
submit = st.button("Submit")

if submit:
    with st.spinner("Generating your prompt"):
        output = replicate.run(
            "ai-forever/kandinsky-2.2:ea1addaab376f4dc227f5368bbd8eff901820fd1cc14ed8cad63b29249e9d463",
            input={
                "width": 1024,
                "height": 1024,
                "prompt": prompt,
                "num_outputs": 1,
                "num_inference_steps": 60,
                "num_inference_steps_prior": 25,
                "seed": 69420
            }
        )

    response = requests.get(output[0])
    image = Image.open(io.BytesIO(response.content))
    h = imagehash.dhash(image)
    diff = HASHES[challenge] - h
    st.metric("DIFFERENCE", diff)
    image_comparison(
        img1=image,
        img2=os.path.join("challenges", challenge),
        width=500,
        label1="Yours",
        label2="Challenge",
        starting_position=50,
        show_labels=True,
        make_responsive=True,
        in_memory=True
    )
