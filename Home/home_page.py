"""
This code designs the Home Page
"""
import streamlit as st

def home_page():
	st.header("Welcome to GeoWater's Homepage")
	col1, col2 = st.columns([6, 6])
	with col1:
		st.image("https://github.com/geowaterpku/homepage/raw/main/animation.gif")

	with col2:
		st.markdown(f'<p style="background-color:#9FAAF8;color:#0C22BE;font-size:16px;border-radius:2%;padding: 15px 15px 15px 15px;">We study the geography of global inland waters, and we develop physically-based models, data-driven methods, and geographic information data infrastructures to improve our fundamental understanding of the river-climate and river-human relationships.</p>', unsafe_allow_html=True)
		st.error('I am always looking for highly motivated **PhD/master/undergraduate students** and **Postdoctoral Fellows** to work in my lab.')
		st.error('Please reach out to peironglinlin@pku.edu.cn if you are interested in working @ GeoWater lab @ PKU')
	