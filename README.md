# Text-to-Image Generation with Ollama and Stable Diffusion


This project demonstrates how to create a simple **Streamlit app** that generates images from text input. It combines **Ollama** for text generation (using the Llama model) and **Stable Diffusion** for image generation


##  Features
- **Text Prompt Generation**: Enter a simple text, and the Llama model will refine it into a more creative and detailed prompt.
- **Image Generation**: Stable Diffusion takes the refined prompt and generates a unique image based on it.
- **Interactive**: Use the app directly in your browser, no complex setup required.

##  Requirements
Before running the app, make sure you have the following installed:

- **Python** 3.7 or higher
- **Streamlit**: For building the web interface.
- **diffusers**: To run the Stable Diffusion model.
- **torch**: Required for GPU acceleration (optional but recommended).
- **ollama**: To generate creative prompts using the Llama model.

## How It Works

- **User Input**:
The user provides a simple text input for image generation.
-  **Ollama Prompt Generation**:
The text input is passed to the Ollama Llama model, which generates a more creative or refined prompt.
-  **Image Generation with Stable Diffusion**:
The generated prompt is fed to Stable Diffusion, a powerful text-to-image generation model.
The image is then generated based on the prompt.
  - **Displaying the Image**:
The generated image is displayed in the app, ready for the user to view.

### Use Cases:
- **Concept Art**: Generate visualizations for new projects, games, or creative concepts.
- **Product Design**: Quickly mock up product ideas and design elements.
- **Illustrations**: Create custom illustrations for books, blogs, or marketing material.
- **Inspiration**: Explore various creative ideas and get visual inspiration for your work.



