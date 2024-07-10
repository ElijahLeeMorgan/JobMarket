import streamlit as st


def display_results(df):
    max_score = df['matching_score'].max()
    min_score = df['matching_score'].min()

    def color_for_value(value):
        # Normalize the value between 0 and 1
        if max_score != min_score:
            normalized = (value - min_score) / (max_score - min_score)
        else:
            normalized = 1  # Default to max if all scores are the same

        # Convert to red (low) to green (high) gradient
        red = int(255 * (1 - normalized))
        green = int(255 * normalized)
        return f'rgb({red},{green},0)'

    for index, row in df.iterrows():
        with st.expander(f"{row['company']} - {row['title']} ({row['matching_score']}%)"):
            color = color_for_value(row['matching_score'])
            st.markdown(f"<span style='color: {color};'>Matching Score: {row['matching_score']}</span>", unsafe_allow_html=True)
            st.text(f"Salary Range: {row['combined_salary']}")
            st.text(f"Workload Range: {row['combined_workload']}")
            st.text(f"Contract Type: {row['contract_type']}")
            st.write(f"Description: {row['description']}")
