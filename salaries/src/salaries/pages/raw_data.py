import streamlit as st
import pandas as pd
from salaries.utils.constants import DATA_PATH

df = pd.read_csv(DATA_PATH / "salaries.csv")


def raw_data():
    st.markdown("# Raw Data utilized in my dashboard")
    st.dataframe(df)


if __name__ == "__main__":
    raw_data()
