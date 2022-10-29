"""
This code designs the Home Page
"""
import streamlit as st

def news_page():
	tab1, = st.tabs(["2022"])

	with tab1:
		st.info('**2022-05: Undergraduate student Kaihao Zheng won the First Prize in the Challenging Cup competition for his research work on levee detection advised by Dr. Lin**. This competition consists of mostly masters or PhD students (can be in teams or single player), with less than 10% undergrads participating. Kaihao completed the competition on his own and won the award. **Big congratulations!** ')
		st.info('**2022-04-25: Co-authored paper published in Nature Sustainability!** Another work examining our rivers using an earth system science view, and a collaborative effort with the DryRiverRCN team, led by Corey Krabbenhoft. See article link here: https://www.nature.com/articles/s41893-022-00873-0. ')
		st.info('**2022-04: Water Resources Research Editors has recommended that I receive the 2021 Editors’ Citation for Excellence in Refereeing for Water Resources Research! Honored to receive such positive feedbacks as a reviewer.**')
		st.info('**2022-01: Peirong is joining Journal of Remote Sensing as a Young Editorial Board Member.**')
	