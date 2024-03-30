import streamlit as st
from streamlit_option_menu import option_menu

import about, SQL, github 


st.set_page_config(
    page_title="SQL Case Study"
)

class MultiApp:
    def __init__(self):
        self.apps = []
    def add_app(self,title,function):
        self.apps.append({
            "title": title,
            "function": function
        })
    
    def run():

        with st.sidebar:
            st.markdown('<i class="fab fa-github"></i>', unsafe_allow_html=True)  # Display GitHub icon
            app = option_menu(
                menu_title= 'SQL Case Study',
                options= ["About", "SQL", "Github"],
                icons=['info-circle', 'database', ''],
                menu_icon='bar-chart-fill',
                default_index=1,
                styles={
                    "container": {"padding": "5!important","background-color":'black'},
        "icon": {"color": "white", "font-size": "23px"}, 
        "nav-link": {"color":"white","font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "blue"},
        "nav-link-selected": {"background-color": "#02ab21"},}
            )
        
        if app == 'About':
            about.app()
        if app == 'SQL':
            SQL.app()
        if app == 'Github':
            github.app()
    run()



