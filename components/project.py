import streamlit as st
from src.utils import load_text

filename = "./to_costum.txt"
text = load_text(filename)
about = text.get("about1")

left, right = st.columns([3, 1], vertical_alignment="center")

img = right.image("./assets/vorg.png", use_column_width="always")
texta = left.markdown(about)
textb = left.markdown(about)

