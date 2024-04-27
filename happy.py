import streamlit as st
from PIL import Image
import numpy as np
import imutils
from streamlit_cropper import st_cropper

# Title and introduction
st.title('Dorsal Hand Vein-Based Authentication System')
st.write('Upload an image of your dorsal hand vein for authentication.')

# Upload image
uploaded_image = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

# Function to perform authentication
def perform_authentication(cropped_image):
    # Placeholder for authentication logic
    st.write("Authentication logic goes here...")

# Define session state variable for rotation angle
if 'rotation_angle' not in st.session_state:
    st.session_state.rotation_angle = 0

if uploaded_image is not None:
    # Display the uploaded image
    image = Image.open(uploaded_image)

    # Use st_cropper to enable cropping functionality
    cropped_image = st_cropper(image, aspect_ratio=(16, 9), box_color="red")

    # Display the cropped image
    st.image(cropped_image, caption='Cropped Image', use_column_width=True)

    # Button to rotate the image
    if st.button("Rotate Image"):
        # Increment rotation angle by 90 degrees
        st.session_state.rotation_angle += 90

    # Perform rotation
    rotated_image = imutils.rotate_bound(np.array(cropped_image), st.session_state.rotation_angle)

    # Convert the rotated NumPy array back to a PIL Image
    rotated_image_pil = Image.fromarray(rotated_image)

    # Display the rotated image
    st.image(rotated_image_pil, caption='Rotated Image', use_column_width=True)

    # Button to perform authentication
    if st.button('Authenticate'):
        perform_authentication(rotated_image_pil)
