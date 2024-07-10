# import the necessary libraries
import streamlit as st
import pandas as pd
import base64
# import the main controller function
from main import controller
from powerwall import display_results

st.set_page_config(page_title="Job Recommendation System", page_icon=":briefcase:", layout="wide", )

# Function to convert image to Base64 for HTML embedding
def get_image_base64(path):
    with open(path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()

# Path to your image and getting Base64 encoding
zhaw_logo = "images/zhaw_logo.png"
logo_base64 = get_image_base64(zhaw_logo)

# Load the data
jobs_df = pd.read_json('../data_acquisition/finalized_data/finalized_data.json')
study_programs = pd.read_json('../data_acquisition/finalized_data/bachelor_degree_information.json')

# HTML for displaying logo inline with text
html = f"""
<div style="display: flex; align-items: center; justify-content: center; gap: 10px; margin-bottom: 5%; margin-top: 0;">
    <h1 style="margin: 0;">From <img src="data:image/png;base64,{logo_base64}" alt="ZHAW Logo" style="width: 60px; vertical-align: middle;"> to the perfect job!</h1>
</div>
"""

# Display HTML in a markdown cell in Streamlit
st.markdown(html, unsafe_allow_html=True)


# Initialize session state for salary and workload
if 'workload' not in st.session_state:
    st.session_state['workload'] = 80
if 'salary' not in st.session_state:
    st.session_state['salary'] = 50000

# Using columns to layout dropdowns and corresponding sliders/inputs
col1, col2 = st.columns(2)

with col1:
    st.header('Study Program')
    selected_title = st.selectbox('Select your study program', study_programs['title'].unique())
    selected_program = study_programs[study_programs['title'] == selected_title]
    st.header('Workload')
    workload = st.slider('Select the minimum workload percentage', 0, 100, st.session_state['workload'], step=5, key='workload')
    st.number_input('Or enter the minimum percentage', min_value=0, max_value=100, value=workload, step=5, key='input_workload', on_change=lambda: st.session_state.update({'workload': st.session_state.input_workload}))

with col2:
    st.header('Contract Type')
    selected_contract_type = st.selectbox('Select contract type', ['any'] + list(jobs_df['contract_type'].unique()))
    st.header('Salary')
    salary = st.slider('Select your minimum expected salary', 0, 400000, st.session_state['salary'], step=1000, key='salary')
    st.number_input('Or enter your desired minimum salary', min_value=0, max_value=400000, value=salary, step=1000, key='input_salary', on_change=lambda: st.session_state.update({'salary': st.session_state.input_salary}))

# Button to find jobs at the end
if st.button('Find Jobs'):
    result_df = controller(df=jobs_df, ms=salary, wl=workload, ct=selected_contract_type, sp=selected_program)

    # Check if the result DataFrame has the special message
    if 'Message' in result_df.columns:
        st.warning(result_df.at[0, 'Message'])
    else:
        display_results(result_df)
