import streamlit as st
import cv2
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2,preprocess_input as mobilenet_v2_preprocess_input

# Deploy Model 
with st.spinner('Loading Model...'):
    model = tf.keras.models.load_model("model/animal.hdf5")


# Upload file
uploaded_file = st.file_uploader("Choose an image file", type=["jpg","png"])

# map image classes
animal_dict = {0: 'dog',
            1: 'horse',
            2: 'elephant',
            3: 'butterfly',
            4: 'chicken',
            5: 'cat',
            6: 'cow'}


if uploaded_file is not None:

    # Apply Imaging Techniques for uploaded image
    img_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    img = cv2.imdecode(img_bytes, 1)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_resize = cv2.resize(img,(224,224))
    
    # Display Image
    st.image(img, channels="RGB")

    img_resize = mobilenet_v2_preprocess_input(img_resize)
    img_reshape = img_resize[np.newaxis,...]

    # Button for Prediction
    predict_img = st.button("Predict Animal")    
    if predict_img:
        prediction = model.predict(img_reshape).argmax()
        st.title("Predicted Animal is {}".format(animal_dict [prediction]))