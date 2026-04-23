import streamlit as st
from salaries.utils.constants import IMAGE_PATH, MARKDOWN_PATH

st.markdown("# Home")


def home():
    st.markdown("## Money raining down on us")
    st.image(IMAGE_PATH / "salaries_data_engineers.png")
    st.markdown(MARKDOWN_PATH / "intro_salaries.md")


if __name__ == "__main__":
    home()
