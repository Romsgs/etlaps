import streamlit as st
from app.api.services.services import services
from fetch_data_functions.fetch_data import fetch_functions
import os
import pandas as pd
import json
from urllib.parse import urlparse
from fetch_data_functions.paths import paths
csv_folder_path = paths['csv_folder_path']

def get_files():
  
  list_of_files = []
  list_of_dfs = []
  
  for file in os.listdir(path=csv_folder_path):
    if file.startswith('item_metadata_version_'):
      list_of_files.append(file)
      df = pd.read_csv(f'{csv_folder_path}/{file}')
      list_of_dfs.append(df)
  if len(list_of_dfs) < 1 or list_of_dfs == []:
      return pd.DataFrame()
  if len(list_of_dfs) == 1:      
      return pd.DataFrame(list_of_dfs[0], index=False)
  else:
    return pd.concat(list_of_dfs)


def safe_parse_json(x):
    try:
        json_data = json.loads(x.replace("'", "\""))
        return json_data['data']['id'] if 'data' in json_data else None
    except json.JSONDecodeError as e:
        print(f"Failed to decode JSON: {x} - Error: {e}")
        return pd.DataFrame()
    except KeyError as e:
        print(f"Missing key in JSON: {x} - Error: {e}")
        return pd.DataFrame()



def versions(project_list_of_names, projects_df_normalized):
  selected_name = st.selectbox("Project Name", project_list_of_names)
  selected_project = projects_df_normalized[projects_df_normalized['attributes_name'] == selected_name].iloc[0]
  st.write("selected Project: ", selected_project['attributes_name'])
  items_df = get_files()
  st.write("items_df")
  st.write(items_df)
  
  if not items_df.empty:
    
    selected_item_name = st.selectbox("Choose the item", items_df['attributes_name'])
    st.write("Selected Item", selected_item_name)
    
    derivatives_data = items_df[items_df['attributes_name'] == selected_item_name]
    st.write('Derivatives Data')
    st.write(derivatives_data)

    if 'relationships_derivatives' in derivatives_data.columns:
      # Apply the function
      derivatives_data['guid'] = derivatives_data['relationships_derivatives'].apply(safe_parse_json)
      items_version_derivative_id = derivatives_data['guid'].dropna().unique().tolist()[0]
      # items_version_derivative_id = derivatives_data.loc['guid']

      if items_version_derivative_id:
        st.write('current file derivative id')
        st.write(items_version_derivative_id)        
        print(items_version_derivative_id)
        derivative_metadata_df = fetch_functions['fetch_and_normalize_derivative_metadata'](items_version_derivative_id)
        # item_guid = derivative_metadata_df.loc[0, 'metadata_guid']
        # item_guid = items_version_derivative_id
        item_guid = derivative_metadata_df.loc[0,'metadata_guid']
        st.write("derivative_metadata_df")
        st.write(derivative_metadata_df)
        st.write("item_guid")
        st.write(item_guid)
        
        derivative_hierarchy_df = fetch_functions['fetch_and_normalize_derivative_obj_hierarchy'](items_version_derivative_id, item_guid)
        st.write("derivative hierarchy")
        
        new_derivative_hierarchy=pd.DataFrame(derivative_hierarchy_df)
        st.write(new_derivative_hierarchy)
        derivativeproperties_df = fetch_functions['fetch_and_normalize_derivative_items_properties'](items_version_derivative_id, item_guid)
        st.write("derivative properties")
        derivativeproperties_df = pd.DataFrame(derivativeproperties_df)
        derivativeproperties_df.to_json(f"{csv_folder_path}/json_properties_{selected_item_name}.json")
        st.write(derivativeproperties_df)
#       # versions_df = fetch_functions['fetch_and_normalize_versions'](selected_project['id'], versionId) # pegar do file
      else:
            st.write("No derivative data available for the selected items.")
    else:
      items_version_derivative_id = derivatives_data['guid']

      if items_version_derivative_id:
        # Assume you are fetching data based on this ID
        st.write(items_version_derivative_id)
        # You can add more functionality here that depends on these IDs
        #     # derivatives_data = items_df.loc[0, 'relationships_derivatives']
        # items_version_derivative_id = derivatives_data['data']['id']
        # Extracting the 'id' from the nested dictionary
        # derivatives_data['guid'] = derivatives_data['relationships_derivatives'].apply(lambda x: x['data']['id'])

        # items_version_derivative_id = derivatives_data.loc['relationships_derivatives']['data']['id']
        
        st.write(items_version_derivative_id)
        print(items_version_derivative_id)
        derivative_metadata_df = fetch_functions['fetch_and_normalize_derivative_metadata'](items_version_derivative_id)
        # item_guid = derivative_metadata_df.loc[0, 'metadata_guid']
        item_guid = items_version_derivative_id[0]
        st.write(derivative_metadata_df)
        st.write(item_guid)
        derivative_hierarchy_df = fetch_functions['fetch_and_normalize_derivative_obj_hierarchy'](items_version_derivative_id, item_guid)
        st.write("derivative hierarchy")
        st.write(derivative_hierarchy_df)
        derivativeproperties_df = fetch_functions['fetch_and_normalize_derivative_items_properties'](items_version_derivative_id, item_guid)
        st.write("derivative properties")
        st.write(derivativeproperties_df)
#       # versions_df = fetch_functions['fetch_and_normal
        st.write("No 'relationships_derivatives' found in the data.")
  else:
      st.write('Try another file.')
