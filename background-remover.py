import streamlit as st
from rembg import remove
from PIL import Image
import io

def main():
    st.set_page_config(page_title="Image Background Remover", page_icon="🖼️")
    st.title("🖼️ Image Background Remover")
    st.write("Upload an image to remove its background instantly.")

    # File uploader for the image
    uploaded_file = st.file_uploader("Choose an image file", type=["png", "jpg", "jpeg", "bmp", "tiff"])

    if uploaded_file is not None:
        # Open the uploaded image
        image = Image.open(uploaded_file)
        st.subheader("Original Image")
        st.image(image, use_column_width=True)

        with st.spinner("Removing background..."):
            # Remove the background
            output = remove(image)
            st.subheader("Image without Background")
            st.image(output, use_column_width=True)

        # Prepare the image for download
        buf = io.BytesIO()
        output.save(buf, format="PNG")
        byte_im = buf.getvalue()

        # Download button for the processed image
        st.download_button(
            label="Download Image without Background",
            data=byte_im,
            file_name="no_background.png",
            mime="image/png"
        )

if __name__ == "__main__":
    main()
 
