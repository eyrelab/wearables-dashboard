import streamlit as st
pg = st.navigation([st.Page('landing.py'),st.Page('dashboard.py')])
pg.run()