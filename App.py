import streamlit as st
import os
from fetch_data_functions.fetch_data import fetch_functions
os.makedirs('./CSVs', exist_ok=True)
from fetch_data_functions.paths import paths
csv_folder_path = paths['csv_folder_path']
from go import go


def fetch_and_display_projects():
    hub_id = fetch_functions['fetch_hub_id']()
    projects_df = fetch_functions['fetch_and_normalize_projects'](hub_id)
    return hub_id, projects_df 
  
  
def main  ():
  hub_id, projects_df = fetch_and_display_projects()
  project_list_names = projects_df['attributes_name']
  # st.text(hub_id)
  # st.text(project_list_names)
  go(hub_id, projects_df, project_list_names)

if __name__ == "__main__":
    main()
