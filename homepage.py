import streamlit as st
from streamlit_option_menu import option_menu

from Home import home_page
from News import news_page
from Publications import publication_page
from Team import team_page
from Teaching import teaching_page
from Research import research_page

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
	home_page()

if select_sidebar=="课题组新闻 | News":
	news_page()

if select_sidebar=="课题组成员 | Team":
	team_page()

if select_sidebar=="科研成果 | Publication":
	publication_page()

if select_sidebar=="教学成果 | Teaching":
	teaching_page()

if select_sidebar=="科研项目 | Projects":
	research_page()


