# Idea borrowed from https://github.com/fsmosca/sample-streamlit-authenticator

import streamlit as st

#### ------------------------ General ------------------------
def HomeNav():
    st.sidebar.page_link("Home.py", label="Home", icon='🏠')

def AboutPageNav():
    st.sidebar.page_link("pages/30_About.py", label="About", icon="🧠")

#### ------------------------ Student Interface ------------------------
def StudentHomeNav():
    st.sidebar.page_link("pages/00_Pol_Strat_Home.py", label="Student Home", icon='👤')

def FormNav():
    st.sidebar.page_link("pages/01_World_Bank_Viz.py", label="Fill Out Preference Form", icon='📋')

def GroupNav():
    st.sidebar.page_link("pages/02_Map_Demo.py", label="Join A Group", icon='👥')
def SchedulingTaskNav():
    st.sidebar.page_link("pages/Scheduler_Tracker.py", label="Tasks + Scheduling", icon='🗓')

## ------------------------ Examples for Role of TA ------------------------
def SpecialTaNav():
    st.sidebar.page_link("pages/12_Special_Ta.py", label="Specialty", icon='🌟')

def AvailabilityTaNav():
    st.sidebar.page_link("pages/11_Availability_Ta.py", label="Availability", icon='🗓')

def UpdateTANav():
    st.sidebar.page_link("pages/13_Update_Ta.py", label="Update availability", icon='📝')

#### ------------------------ Professor (ADMIN) Role ------------------------
def AdminPageNav():
    st.sidebar.page_link("pages/20_Admin_Home.py", label="Update Groups", icon='💻')
    st.sidebar.page_link("pages/21_ML_Model_Mgmt.py", label='My Students', icon='📕')


# --------------------------------Links Function -----------------------------------------------
def SideBarLinks(show_home=False):
    """
    This function handles adding links to the sidebar of the app based upon the logged-in user's role, which was put in the streamlit session_state object when logging in. 
    """    

    # add a logo to the sidebar always
    st.sidebar.image("assets/logo.png", width = 200)

    # If there is no logged in user, redirect to the Home (Landing) page
    if 'authenticated' not in st.session_state:
        st.session_state.authenticated = False
        st.switch_page('Home.py')
        
    if show_home:
        # Show the Home page link (the landing page)
        HomeNav()

    # Show the other page navigators depending on the users' role.
    if st.session_state["authenticated"]:

        # Show World Bank Link and Map Demo Link if the user is a political strategy advisor role.
        if st.session_state['role'] == 'student':
            StudentHomeNav()
            FormNav()
            GroupNav()
            SchedulingTaskNav()

        # If the user role is usaid worker, show the Api Testing page
        if st.session_state['role'] == 'ta':
            AvailabilityTaNav()
            SpecialTaNav()
            UpdateTANav()
        
        # If the user is an administrator, give them access to the administrator pages
        if st.session_state['role'] == 'professor':
            AdminPageNav()

    # Always show the About page at the bottom of the list of links
    AboutPageNav()

    if st.session_state["authenticated"]:
        # Always show a logout button if there is a logged in user
        if st.sidebar.button("Logout"):
            del st.session_state['role']
            del st.session_state['authenticated']
            st.switch_page('Home.py')

