from src.utils import import_module, load_text
import streamlit as st

st.set_page_config(layout="wide")

st.markdown(
    """
    <div style='display: flex; align-items: center; justify-content: center;'>
        <hr style='width: 40%; margin: 0; border: 2px solid #ccc;'>
        <h1 style='text-align: center; margin: 0 50px;'>About</h1>
        <hr style='width: 40%; margin: 0; border: 2px solid #ccc;'>
    </div>
    """,
    unsafe_allow_html=True
)
about_module = import_module("./components/about.py", "about_module")

st.markdown(
    """
    <div style='display: flex; align-items: center; justify-content: center;'>
        <hr style='width: 40%; margin: 0; border: 2px solid #ccc;'>
        <h1 style='text-align: center; margin: 0 50px;'>About</h1>
        <hr style='width: 40%; margin: 0; border: 2px solid #ccc;'>
    </div>
    """,
    unsafe_allow_html=True
)
main_module = import_module("./components/project.py", "main_module")