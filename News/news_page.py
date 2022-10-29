"""
This code designs the Home Page
"""
import streamlit as st

def news_page():
	tab1,tab2 = st.tabs(["2022","2021"])

	with tab1:
		st.info('**2022-05: Undergraduate student Kaihao Zheng won the First Prize in the Challenging Cup competition for his research work on levee detection advised by Dr. Lin**. This competition consists of mostly masters or PhD students (can be in teams or single player), with less than 10% undergrads participating. Kaihao completed the competition on his own and won the award. **Big congratulations!** ')
		st.info('**2022-04-25: Co-authored paper published in Nature Sustainability!** Another work examining our rivers using an earth system science view, and a collaborative effort with the DryRiverRCN team, led by Corey Krabbenhoft. See article link here: https://www.nature.com/articles/s41893-022-00873-0. ')
		st.info('**2022-04: Water Resources Research Editors has recommended that I receive the 2021 Editors’ Citation for Excellence in Refereeing for Water Resources Research! Honored to receive such positive feedbacks as a reviewer.**')
		st.info('**2022-01: Peirong is joining Journal of Remote Sensing as a Young Editorial Board Member.**')
		st.info("""**2022-1-17: The prestigious Boya Postdoc Fellowship application is open this year!** 
			Check out the application notice here: https://postdocs.pku.edu.cn/tzgg/134996.htm. 
			If you are interested in working at PKU as a postdoc and expand your research topics on using remote sensing/GIS to addressing water-energy-food-ecology nexus problems, you may have the opportunity to work collaboratively with several faculty members in our department (Institute of Remote Sensing and GIS @ PKU), with myself being the major advisor. Note two deadlines are in March and September, respectively. Interested candidates may email peironglinlin@pku.edu.cn and a brief research statement and CV would be helpful.""")
	with tab2:
		st.info("""**2021-12/18-19: I chaired the 3rd International Graduate Workshop on Geoinformatics (IGWG) for a two-day event.** 
			This workshop is co-organized by Peking University, Wuhan University, and the Hong Kong Polytechnic University. This year PKU is the leading organizer. 59 students from 14 universities presented their work orally, judged by 10 faculty advisors we invited from PKU, WHU, PolyU, and U Minnesota.  """)
		st.info("""**2021-07-31 to 08-01: I convened a session named "New methods in hydrologic monitoring and modeling" at the 9th summer meeting for CYWater!**
			 (together with Hui Lu from Tsinghua University, Xiaogang He from National University of Singapore, and Yanhong Gao from CAS).""")
		st.info("""**2021-07-27: I gave an invited talk at the "Quantitative Remote Sensing Summer School"**, 
			 one of the most influential summer programs at Peking University for the past 20 years. The topic is on the "Role of geospatial information techniques on the global high-resolution river discharge modeling".""")
		st.info("""**2021-06-30: I gave an invited talk at Hydro90.**
			 200+ audience showed up, with a lot of great questions. See more about Hydro90 on Twitter (https://twitter.com/hydro90er?lang=en).""")
		st.info("""**2021 Summer: I will join Peking University as a tenure-track Assistant Professor! Please contact peironglinlin@pku.edu.cn for further correspondence**, 
			 or if you are interested in joining us at PKU! (PKU is located in Beijing, China, and the program is from Institute of Remote Sensing and GIS at School of Earth and Space Sciences. We will use an Earth System Science approach to study global water problems @ GeoWater lab)""")
		st.info("""**2021-01-28: I published three first-author papers since joining Princeton as a postdoc in June 2018.**
			 Check out Lin et al. (2019; WRR), Lin et al. (2020; GRL) and Lin et al (2021; Scientific Data). These three papers all focused on global rivers (e.g., discharge, bankfull width, and drainage density) and would lay the foundation for many ensuing global river studies!""")