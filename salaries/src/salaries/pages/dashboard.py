import streamlit as st
from salaries.utils.helpers import read_textfile, get_salaries_df, read_css
from salaries.utils.constants import MARKDOWN_PATH, STYLES_PATH
from salaries.components.kpi import avg_salary_usd_kpi
from salaries.components.charts import top_avg_salaries_chart, filtered_table
from salaries.components.filters import job_title_filter, experience_level_filter


st.markdown("# Dashboard")


def dashboard_layout():

    st.markdown("# Salaries Dashboard")
    st.markdown(read_textfile(MARKDOWN_PATH / "salaries_dashboard_description.md"))
    st.dataframe(get_salaries_df())

    st.markdown("**Yearly Salaries in USD for different roles**")
    # kpis
    roles = [
        "Data Scientist",
        "Data Analyst",
        "Data Engineer",
        "Machine Learning Engineer",
        "AI Engineer",
    ]

    cols = st.columns(len(roles))
    for column, role in zip(cols, roles):
        with column:
            avg_salary_usd_kpi(role, role)

    # ======================
    top_avg_salaries_chart()
    cols = st.columns(2)
    with cols[0]:
        job_title = job_title_filter()
    with cols[1]:
        experience_level = experience_level_filter()

    st.markdown(job_title)
    filtered_table(job_title, experience_level)

    read_css(STYLES_PATH / "dashboard.css")


if __name__ == "__main__":
    dashboard_layout()
