import streamlit as st
from fetch_data_functions.fetch_data import fetch_functions
from selected_functions.explore_folders import explore_folders

from fetch_data_functions.paths import paths
csv_folder_path = paths['csv_folder_path']

def folders(hub_id, project_list_of_names, projects_df_normalized):
  st.write("fluxo de obtenção dos Dados:")
  st.write("essa pagina colhe dados das pastas e mostra. depois te pede para procurar uma pagina especifica. desse ponto, ela vai percorrer toda arvore das pastas que n'ao estejam vazias e criar um arquivo csv com o prefixo items_from. esse aqruqivo, será usado na pagina Items <-")
  
  selected_name = st.selectbox("Project Name", project_list_of_names)
  selected_project = projects_df_normalized[projects_df_normalized['attributes_name'] == selected_name].iloc[0]
  
   #### top folders section
  top_folders_df_normalized = fetch_functions['fetch_and_normalize_top_folders'](hub_id, selected_project['id'])
  st.write("Top Folders of this project:")
  st.write(top_folders_df_normalized)
  top_folders_df_normalized.to_csv(f'{csv_folder_path}/top_folders_from_project_{selected_project['attributes_name']}.csv')
  #### folder content section
  selected_folder_name = st.selectbox("Select Folder", top_folders_df_normalized['attributes_name'])
  selected_folder = top_folders_df_normalized[top_folders_df_normalized['attributes_name'] == selected_folder_name].iloc[0]
  folder_content_df_normalized  = fetch_functions['fetch_and_normalize_folder_content'](selected_project['id'], selected_folder['id'])
  if folder_content_df_normalized is not None and not folder_content_df_normalized.empty:
      print('executando a funcao folders dentro do if')
      st.write('folder content')
      st.write(folder_content_df_normalized)
      print(folder_content_df_normalized.dtypes)
      folder_content_df_normalized.to_csv(f'{csv_folder_path}/folder_content_{selected_folder_name}.csv')
      
      folders_with_multiple_objects = folder_content_df_normalized[folder_content_df_normalized['attributes_objectCount'] > 1]
      st.write('pastas com objetos dentro:')
      st.write(folders_with_multiple_objects)
      # folder_content_df_normalized2  = fetch_and_normalize_folder_content(selected_project['id'], 'urn:adsk.wipprod:fs.folder:co.oIdhx7YxTBy2RGfcEaAQxw')
      folder_content_df = explore_folders(selected_project['id'], selected_folder['id'])
      st.write('dataFrame concatenato com toda hieraquia encontrada:')
      st.write(folder_content_df)
      st.write(f"salvando em csv, {csv_folder_path}/hierarchy_{selected_name}_{selected_folder_name}.csv")
      folder_content_df.to_csv(f'{csv_folder_path}/hierarchy_{selected_name}_{selected_folder_name}.csv')
      folder_content_df['attributes_displayName'] = folder_content_df['attributes_displayName'].astype(str)
      only_items_df = folder_content_df[folder_content_df['attributes_displayName'].str.contains(r"\.nwc|\.nwd$", regex=True)]
      only_nwc = only_items_df[only_items_df['attributes_displayName'].str.contains(r"ED-MOD", regex=True)]
      print('only_items_df >>>>>>', type(only_items_df))
      print('only_items_df >>>>>>', only_items_df)
      st.write(f"salvando em csv o only_items_df, {csv_folder_path}/items_from_{selected_folder_name}.csv")
      only_items_df.to_csv(f"{csv_folder_path}/items_from_{selected_folder_name}.csv")
      st.write(f"Salvando em csv o only_nwc -> {csv_folder_path}/nwc_items{selected_folder_name}.csv")
      only_nwc.to_csv(f"{csv_folder_path}/nwc_items{selected_folder_name}.csv")
      st.write("apenas os Items")
      st.write(only_items_df)     
      # Print or use the folder IDs
      # print("Folder IDs with more than one object: >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>", folder_ids_with_multiple_objects)
      st.write("only_items_df")
      st.write(only_items_df)
      list_of_items_names_df = only_items_df['attributes_displayName'] if not only_items_df.empty else st.warning("no items")
      if not only_items_df.empty:
        selected_item_name = st.selectbox("selecione o nome do arquivo", list_of_items_names_df) 
        selected_item = only_items_df[only_items_df['attributes_displayName'] == selected_item_name].iloc[0]
        st.write(selected_item)
          
      else:
        st.warning("no items")
  elif folder_content_df_normalized is None:
      st.warning("No folder content data available.")
  else:
      st.warning("Folder content data is empty.")
  