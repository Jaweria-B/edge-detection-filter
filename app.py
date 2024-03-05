import sys
import streamlit as st
from PIL import Image, ImageFilter

# Define function to apply edge detection filter
def apply_edge_detection(image):
    filtered_image = image.filter(ImageFilter.Kernel(
        size=(3, 3),
        kernel=[-1, -1, -1, -1, 8, -1, -1, -1, -1],
        scale=1
    ))
    return filtered_image

# Main function to run the Streamlit app
def main():
    st.title("Edge Detection Filter ✨")
    st.write("This app applies an edge detection filter to your images. 🖼️")

    # Upload multiple images
    uploaded_files = st.file_uploader("Choose multiple images... 📷", type=["jpg", "png", "jpeg"], accept_multiple_files=True)

    if uploaded_files:
        for uploaded_file in uploaded_files:
            image = Image.open(uploaded_file).convert("RGB")
            
            # Display original image
            st.subheader("Original Image 🌟")
            st.image(image, caption="Original Image", use_column_width=True)
            
            # Apply edge detection filter
            filtered_image = apply_edge_detection(image)
            
            # Display filtered image
            st.subheader("Filtered Image ✨")
            st.image(filtered_image, caption="Filtered Image", use_column_width=True)
        
        st.write(
        """
        ---
        Made By **_Jaweria Batool_**
        """
        )

        # link to GitHub README file
        st.write("For more information about how the app works, please check out the [GitHub README](https://github.com/Jaweria-B/edge-detection-filter) file.")

# Run the app
if __name__ == "__main__":
    main()
