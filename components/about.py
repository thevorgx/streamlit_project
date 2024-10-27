import streamlit as st
from src.utils import load_text

filename = "./to_costum.txt"
text = load_text(filename)
about = text.get("about1")

left, right = st.columns([1, 3], vertical_alignment="center")

img = left.image("./assets/vorg.png", use_column_width="always")
texta = right.container(height= 200, key="A", border=False)
textb = right.container(height= 200, key="B", border=False)
with texta:
    st.markdown(about)
with textb:
    st.markdown(about)

