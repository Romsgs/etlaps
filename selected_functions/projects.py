import streamlit as st
from app.api.services.services import services
from fetch_data_functions.fetch_data import fetch_functions


def projects(hub_id, project_list_of_names, projects_df_normalized):

  # try:
    #### Projects section

    selected_name = st.selectbox("Project Name", project_list_of_names)
    selected_project = projects_df_normalized[projects_df_normalized['attributes_name'] == selected_name].iloc[0]

    st.write("Selected project details:")
    st.write(selected_project)
    #### specific Project section
    st.write("Output of 'project_PROJECT_ID_CSV.csv'")
    specific_project = fetch_functions['fetch_and_normalize_specifyc_projects'](hub_id, selected_project['id'], selected_name)
    
    st.write(specific_project)

   
    #### items section
    print('items section')
    # items_metadata_normalized = fetch_and_normalize_items(selected_project['id'],)
