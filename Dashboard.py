import streamlit as st

st.set_page_config(
    page_title="PROHI Dashboard",
    page_icon="👋",
)

# Sidebar configuration
st.sidebar.image("./assets/project-logo.jpg",)
st.sidebar.success("Select a tab above.")

# # Page information

st.write("# Welcome to PROHI Dashboard! 👋")

st.markdown(
"""
    ## Aims

    After completing the course the student should be able to:
    - explain basic project management methods
    - be able to account for success factors in Health Informatics projects
    - understand basic methods and tools in the field of data science and machine learning
    - explain process models for data mining projects
    - explain the difference between rule-based methods and machine learning methods
    - apply basic project management methods
    - work in an international multidisciplinary project group
    - independently lead and implement a limited project in health informatics - document the steps in the design of a prototype for a health informatics project
    - apply the steps in a process model for data mining projects
    - apply methods from the field of text mining on different types of health informatics problems
    - explain and argue for their positions regarding the implementation of a health informatics project
    - explain how to work with sensitive health information in a safe and ethical way.

"""
)

# You can also add text right into the web as long comments (""")
"""
The final project aims to apply data science concepts and skills on a 
medical case study that you and your team select from a public data source.
The project assumes that you bring the technical Python skills from 
previous courses (*DSHI*: Data Science for Health Informatics), as well as 
the analytical skills to argue how and why specific techniques could
enhance the problem domain related to the selected dataset.
"""

### UNCOMMENT THE CODE BELOW TO SEE EXAMPLE OF INPUT WIDGETS

# # DATAFRAME MANAGEMENT
# import numpy as np

# dataframe = np.random.randn(10, 20)
# st.dataframe(dataframe)

# # Add a slider to the sidebar:
# add_slider = st.slider(
#     'Select a range of values',
#     0.0, 100.0, (25.0, 75.0)
# )

import numpy as np
import pandas as pd

#Adding sidebar input widgets:
with st.sidebar.expander("Participant Info", expanded=True):
    gender = st.selectbox(
        "Gender",
        ["Male", "Female", "Other"]
    )

    conditions = st.multiselect(
        "Health conditions",
        ["Diabetes", "Hypertension", "Asthma", "Depression", "None"],
        default=["None"]
    )

    other_condition = st.text_input("Other condition (if not listed)")

    # Append free-text to list if user writes something
    if other_condition:
        conditions.append(other_condition)

    mental_score = st.slider(
        "Mental health score (self-rated)",
        min_value=0,
        max_value=100,
        value=50,
        step=5
    )
       
#Adding one element for Data
st.divider()
st.subheader("Participant Data Table")


# Generate synthetic demo data
rng = np.random.default_rng(42)
n = 10
df = pd.DataFrame({
    "ID": np.arange(1, n + 1),
    "Age": rng.integers(18, 70, size=n),
    "Gender": rng.choice(["Male", "Female", "Other"], size=n),
    "Mental Health Score": rng.integers(30, 95, size=n)
})

# Display the table
st.dataframe(df, use_container_width=True)

#Adding a chart

st.subheader("Mental Health Score by Gender (example chart)")

# Group by gender and calculate average score
chart_data = df.groupby("Gender")["Mental Health Score"].mean().reset_index()

# Display as a bar chart
st.bar_chart(chart_data.set_index("Gender"))