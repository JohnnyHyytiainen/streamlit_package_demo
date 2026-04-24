import streamlit as st
import pandas as pd
from salaries.utils.constants import DATA_PATH


def read_textfile(path):
    with open(path) as file:
        return file.read()


@st.cache_data(ttl=3600)
def get_salaries_df():
    return pd.read_csv(DATA_PATH / "salaries.csv")


def read_css(path):
    css = read_textfile(path)
    st.write(f"<style>{css}</style>", unsafe_allow_html=True)
