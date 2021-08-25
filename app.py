import streamlit as st
import tensorflow as tf

import tensorflow_datasets as tfds
from PIL import Image
from news import classes


model = tf.keras.models.load_model("my_model.h5")
encoder = tfds.deprecated.text.SubwordTextEncoder.load_from_file("encoder")

def pad_to_size(vec, size):
  zero = [0] * (size - len(vec))
  vec.extend(zero)
  return vec


def sample_predict(sample_pred_text, pad):
  encoded_sample_pred_text = encoder.encode(sample_pred_text)

  if pad:
    encoded_sample_pred_text = pad_to_size(encoded_sample_pred_text, 64)
  encoded_sample_pred_text = tf.cast(encoded_sample_pred_text, tf.float32)
  predictions = model.predict(tf.expand_dims(encoded_sample_pred_text, 0))

  return (predictions)
ttl="<center><h1>Fake News Detection</h1></center>"
st.markdown(ttl, unsafe_allow_html=True)
#st.set_page_config(layout="wide")
banner=Image.open("Fakeoff.png")
st.image(banner,use_column_width=True)



def about():
	st.write(
		'''
		**Haar Cascade** is an object detection algorithm.
		It can be used to detect objects in images or videos. 

		The algorithm has four stages:

			1. Haar Feature Selection 
			2. Creating  Integral Images
			3. Adaboost Training
			4. Cascading Classifiers



View Dev-k web :point_right: http://dev-k-copyright.herokuapp.com/
		''')
activities = ["Home", "About"]
choice = st.sidebar.selectbox("Pick something fun", activities)


def main():
    if choice=="Home":
        
        st.write("**Model:Here we used BERT as a pre-trained model**")
        text_inp = st.text_area("Enter any News here--")
        st.sidebar.info('© 2021 Copyright: Dev-k')  
        st.dataframe(classes,600,200) 

        if st.button("Process"):
            pred=sample_predict(text_inp, pad=False)
            res=''
            if pred>.5:
                    res='Real'
            else:
                    res='Fake'
        
            st.success("The news you typed is: {} ".format(res))
    elif choice == "About":
    	about()

if __name__ == "__main__":
    main()