import streamlit as st
import numpy as np
import keras
from keras.preprocessing import image
from PIL import Image



def main():
	st.set_option('deprecation.showfileUploaderEncoding', False)
	hide_menu_style = """
        	<style>
        	#MainMenu {visibility: hidden;}
 		footer {visibility: hidden;}       
		</style>
        	"""
	st.markdown(hide_menu_style, unsafe_allow_html=True)
	image_file = st.file_uploader("", type=['jpeg', 'png', 'jpg'])
	if image_file is not None:
		if st.button("Process"):
			model = keras.models.load_model('modelofhands.h5')
			test_image = image.img_to_array(Image.open(image_file).convert("RGB"))
			test_image = np.expand_dims(test_image, axis = 0)
			result = model.predict(test_image)
			answer = ""
			if int(result[0][0]) == 1:
				answer = "Backward"
			elif int(result[0][1]) == 1:
				answer = "Forward"
			elif int(result[0][2]) == 1:
				answer = "Plays"
			elif int(result[0][3]) == 1:
				answer = "Stops"
			elif int(result[0][4]) == 1:
				answer = "VolumeDown"
			elif int(result[0][5]) == 1:
				answer = "VolumeUp"
			else:
				answer = "None"
			st.success(f"{answer}")
	else:
		pass

if __name__ == "__main__":
	main()
