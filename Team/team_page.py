"""
This code designs the Team Page
"""
import streamlit as st
import pathlib
import os

def team_page():
	file_path = os.path.join(pathlib.Path(__file__).parent.resolve(),'files')

	tab1, tab2, tab3 = st.tabs(["PI", "Graduate Students","Undergraduates"])
	with tab1:
		st.header("Prof. Peirong Lin")
		col1, col2 = st.columns([1.5, 6])
		with col1:
			st.markdown("#####")
			st.image(os.path.join(file_path,"PeirongLin.jpeg"),width=150)
		with col2:
			tab_1,tab_2,tab_3 = st.tabs(["Current Position", "Professional Experiences","Academic Services"])
			with tab_1:
				col1, col2 = st.columns([6, 2])
				with col1:
					st.markdown("""<p style="background-color:#D7E4FE;color:#05286C;font-size:16px;border-radius:2%;padding: 15px 15px 15px 15px;">
						<b>Assistant Professor</b>, 2021-current
						<br>Institute of Remote Sensing and GIS, School of Earth and Space Sciences
						<br>Peking University
						<br><a href="https://scholar.google.com/citations?user=jCA3MkfZkRoC&hl=en">Google Scholar</a>
						</p>""", unsafe_allow_html=True)
				with col2:
					st.image(os.path.join(file_path,'Peking_University_logo.png'),width=100)
				st.markdown("""<p style="background-color:#D7E4FE;color:#05286C;font-size:16px;border-radius:2%;padding: 15px 15px 15px 15px;">
					contact: <a href="peironglinlin@pku.edu.cn">peironglinlin@pku.edu.cn</a>
					</p>""", unsafe_allow_html=True)
			with tab_2:
				col1, col2 = st.columns([6, 2])
				with col1:
					st.markdown("""<p style="background-color:#D7E4FE;color:#05286C;font-size:16px;border-radius:2%;padding: 15px 15px 15px 15px;">
						<b>Postdoc</b>, 2018-2021
						<br>Department of Civil and Environmental Engineering,
						<br>Princeton University
						</p>""", unsafe_allow_html=True)
				with col2:
					st.image(os.path.join(file_path,'Princeton_University_log.png'),width=200)
				col1, col2 = st.columns([6, 2])
				with col1:
					st.markdown("""<p style="background-color:#D7E4FE;color:#05286C;font-size:16px;border-radius:2%;padding: 15px 15px 15px 15px;">
						<b>Ph.D.</b>, 2012-2018
						<br>Water, Climate, and Environment (WCE) Program,
						<br>Jackson School of Geosciences,
						<br>The University of Texas at Austin
						</p>""", unsafe_allow_html=True)
				with col2:
					st.image(os.path.join(file_path,'ut_austin_logo.png'),width=200)
				col1, col2 = st.columns([6, 2])
				with col1:
					st.markdown("""<p style="background-color:#D7E4FE;color:#05286C;font-size:16px;border-radius:2%;padding: 15px 15px 15px 15px;">
						<b>B.S. (honors)</b>, 2008-2012
						<br>Remote Sensing and Geographic Information Science,
						<br>Peking University
						</p>""", unsafe_allow_html=True)
				with col2:
					st.image(os.path.join(file_path,'Peking_University_logo.png'),width=100)
			with tab_3:
				st.markdown("""<p style="background-color:#D7E4FE;color:#05286C;font-size:16px;border-radius:2%;padding: 15px 15px 15px 15px;">
						<b>NSF proposal reviewer</b>
						</p>""", unsafe_allow_html=True)
				st.markdown("""<p style="background-color:#D7E4FE;color:#05286C;font-size:16px;border-radius:2%;padding: 15px 15px 15px 15px;">
						<b>Journal Reviewer for</b> <a href="https://www.webofscience.com/wos/author/record/170368">(check publon)</a>
						<br> &bull; Geophysical Research Letters (4), 
						<br> &bull; Journal of Geophysical Research (2), 
						<br> &bull; Journal of Hydrology (2), 
						<br> &bull; Climatic Change (2), 
						<br> &bull; Journal of the American Water Resources Association (4), 
						<br> &bull; Weather and Forecasting (1), 
						<br> &bull; Advances in Meteorology (1), 
						<br> &bull; The Cryosphere (1), 
						<br> &bull; Environmental Modelling & Software (1), 
						<br> &bull; Hydrology and Earth System Sciences (1)
						</p>""", unsafe_allow_html=True)
	with tab2:
		pass