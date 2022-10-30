import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(layout="wide")

def define_sidebar():
	with st.sidebar:
		select_sidebar = option_menu(None, ["首页 | Home", "课题组新闻 | News", "课题组成员 | Team", '科研成果 | Publication', '教学成果 | Teaching', "科研项目 | Projects"], 
		    icons=['house', 'newspaper', 'people', 'list-task', 'book','diagram-2-fill'], 
		    menu_icon="cast", default_index=0, orientation="vertical",
		    styles={
		        "container": {"padding": "0!important", "background-color": "#fafafa"},
		        "icon": {"color": "orange", "font-size": "20px"}, 
		        "nav-link": {"font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
		        "nav-link-selected": {"background-color": "green"},
		    }
		)
	return select_sidebar

select_sidebar = define_sidebar()

if select_sidebar=="首页 | Home":
	from Home import home_page
	home_page()

if select_sidebar=="课题组新闻 | News":
	from News import news_page
	news_page()

if select_sidebar=="课题组成员 | Team":
	from Team import team_page
	team_page()

if select_sidebar=="科研成果 | Publication":
	from Publications import publication_page
	publication_page()

if select_sidebar=="教学成果 | Teaching":
	from Teaching import teaching_page
	teaching_page()

if select_sidebar=="科研项目 | Projects":
	from Research import research_page
	research_page()


