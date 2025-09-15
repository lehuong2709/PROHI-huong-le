import streamlit as st

st.set_page_config(page_title="About", page_icon="📝")

st.title("Huong Le — About")

st.markdown(
"""
## Project Summary (DSHI Course)

In my project last semester, I worked with a **Sleep Disorder dataset** to practice building
a classification model. The main idea was to predict whether a patient might have a sleep
disorder based on features like the **AHI score**, **oxygen saturation**, and the type of sleep disorder recorded.  

I started by checking how many patients with AHI > 5 were misdiagnosed, which shows the importance of accurate detection.
Then, i applied **cross-validation on the training set** and compared different classification models.  
Among the models I tried, a **Decision Tree (DT-3)** had the best performance matrix, nearly 1 for all parameters.

Since this dataset was synthetic, I decided not using the model directly in clinical practice.
For me, the results are more of a **proof of concept**. 
The model neeed to trained and validated on actual patient data"""
)