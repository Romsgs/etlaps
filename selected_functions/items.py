import streamlit as st
from app.api.services.services import services
from fetch_data_functions.fetch_data import fetch_functions
import os
import pandas as pd
import json
from urllib.parse import urlparse
from fetch_data_functions.paths import paths
csv_folder_path = paths['csv_folder_path']

def get_df_from_files(prefix):

    list_of_files = []
    list_of_dfs = []
    listedDir = os.listdir(csv_folder_path)
    for file in listedDir:
        if file.startswith(prefix):
            print('-------------------------------------------------------------------')
            print(file)
            list_of_files.append(file)
            df = pd.read_csv(f'{csv_folder_path}/{file}')
            list_of_dfs.append(df)

    if len(list_of_dfs) < 1:
      st.error('no files')
      return pd.DataFrame()
    if len(list_of_dfs) == 1:
        return pd.DataFrame(list_of_dfs[0])
    else:
        return pd.concat(list_of_dfs)

def items(prefix):
        
    items_df = get_df_from_files(prefix)
    items_names = items_df['attributes_displayName']
    selected_item = st.selectbox('selecione o arquivo', items_names, placeholder="Choose")
    if not items_df.empty:
        
        item = items_df[items_df['attributes_displayName'] == selected_item].iloc[0]  
        item_url = json.loads(item['links_self'].replace("'", '"'))
        item_url = urlparse(item_url["href"])
        project_id = item_url.path.split('/')[4]  
        metadata = fetch_functions['fetch_and_normalize_item_metadata'](project_id, item['id'])

        metadata_transposed = metadata.T
        metadata.to_csv(f'{csv_folder_path}/item_metadata_{selected_item}.csv')
        metadata_transposed.to_csv(f'{csv_folder_path}/item_metadata_transposed{selected_item}.csv')
        # st.write(type(metadata))
        versions_id = metadata.loc['versions'].loc['id']
        st.write(metadata)
        st.write(metadata_transposed)
        st.write(metadata.loc['versions'])
        st.write(metadata.loc['versions'].loc['id']) 
        item_metadata_version = fetch_functions['fetch_and_normalize_item_metadata_version'](project_id, versions_id)
        st.write("salvando o arquivo para usar no versions")
        item_metadata_version.to_csv(f'{csv_folder_path}/item_metadata_version_{selected_item}.csv')
        st.write(item_metadata_version.T)
        # print(versions_id)
        # versions_df = fetch_and_normalize_versions(project_id, 'urn:adsk.wipprod:dm.lineage:6vo44vQ5QUyS3str8nGufw')
        # st.write(versions_df)
        
        # urn:adsk.wipprod:dm.lineage:6vo44vQ5QUyS3str8nGufw
        # urn:adsk.wipprod:dm.lineage:6vo44vQ5QUyS3str8nGufw
        # st.write(metadata['versions'])
        
        # sitem_metadata = get_items_metadata()
    else:
        st.warning('arquivo vazio')
    