import streamlit as st
import ollama
from diffusers import StableDiffusionPipeline
import torch

# Initialize Stable Diffusion
pipe = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5")
pipe = pipe.to("cuda" if torch.cuda.is_available() else "cpu")

# Streamlit app
st.title("Text-to-Image Generation with Ollama")

# User input
user_input = st.text_input("Enter a simple text for the Llama model to auto-generate")

if st.button("Generate Image"):
    if user_input:
        prompt = ollama.generate(model="llama3", prompt=user_input)
    else:
        prompt = ollama.generate(model="llama3", prompt="Generate a creative image de")

    st.write(f"Generated Prompt: {prompt}")

    # Generate and display the image
    with st.spinner("Generating image..."):
        image = pipe(prompt).images[0]
        image.save("temp_image.png")
        st.image("temp_image.png", caption="Generated Image")
