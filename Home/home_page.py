"""
This code designs the Home Page
"""
import streamlit as st

def home_page():
	tab1, tab2 = st.tabs(["Welcome", "News"])
	with tab1:
		st.header("Welcome to GeoWater's Homepage")
		col1, col2 = st.columns([6, 6])
		with col1:
			st.image("https://github.com/geowaterpku/homepage/raw/main/animation.gif")

		with col2:
			st.markdown(f'<p style="background-color:#9FAAF8;color:#0C22BE;font-size:16px;border-radius:2%;padding: 15px 15px 15px 15px;">We study the geography of global inland waters, and we develop physically-based models, data-driven methods, and geographic information data infrastructures to improve our fundamental understanding of the river-climate and river-human relationships.</p>', unsafe_allow_html=True)
			st.error('I am always looking for highly motivated **PhD/master/undergraduate students** and **Postdoctoral Fellows** to work in my lab.')
			st.error('Please reach out to peironglinlin@pku.edu.cn if you are interested in working @ GeoWater lab @ PKU')
	with tab2:
		st.header("News")
		st.info('**2022-05: Undergraduate student Kaihao Zheng won the First Prize in the Challenging Cup competition for his research work on levee detection advised by Dr. Lin**. This competition consists of mostly masters or PhD students (can be in teams or single player), with less than 10% undergrads participating. Kaihao completed the competition on his own and won the award. **Big congratulations!** ')
		st.info('**2022-04-25: Co-authored paper published in Nature Sustainability!** Another work examining our rivers using an earth system science view, and a collaborative effort with the DryRiverRCN team, led by Corey Krabbenhoft. See article link here: https://www.nature.com/articles/s41893-022-00873-0. ')
		st.info('**2022-04: Water Resources Research Editors has recommended that I receive the 2021 Editors’ Citation for Excellence in Refereeing for Water Resources Research! Honored to receive such positive feedbacks as a reviewer.**')
		st.info('**2022-01: Peirong is joining Journal of Remote Sensing as a Young Editorial Board Member.**')
	