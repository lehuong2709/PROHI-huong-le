import streamlit as st

st.set_page_config(page_title="About", page_icon="📝")

# Title
st.markdown(
    "<h1 style='font-size: 36px;'>Huong Le — About</h1>",
    unsafe_allow_html=True
)

# Subtitle
st.markdown(
    "<h2 style='font-size: 24px;'>Project Summary (DSHI Course)</h2>",
    unsafe_allow_html=True
)

st.markdown(
"""
<div style="text-align: justify; font-size: 18px; line-height: 1.6;">

In my project last semester, I worked with a **Sleep Disorder dataset** to practice building
a classification model. The main idea was to predict whether a patient might have a sleep
disorder based on features like the **AHI score**, **oxygen saturation**, and the type of sleep disorder recorded.  

I started by checking how many patients with AHI > 5 were misdiagnosed, which shows the importance of accurate detection.
Then, i applied **cross-validation on the training set** and compared different classification models.  
Among the models I tried, a **Decision Tree (DT-3)** had the best performance matrix, nearly 1 for all parameters.

Since this dataset was synthetic, I decided not using the model directly in clinical practice.
For me, the results are more of a **proof of concept**. 
The model neeed to trained and validated on actual patient data. </div>""",
unsafe_allow_html=True
)