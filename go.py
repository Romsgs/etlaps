import streamlit as st
from fetch_data_functions.fetch_data import fetch_functions
from selected_functions.explore_folders import explore_folders
import pandas as pd
import json
import time
from datetime import datetime, timedelta
csv_folder_path = "./CSVs"
inicio = time.time()

# def safe_parse_json(x):
#     try:
#         json_data = json.loads(x.replace("'", "\""))
#         return json_data['data']['id'] if 'data' in json_data else None
#     except json.JSONDecodeError as e:
#         print(f"Failed to decode JSON: {x} - Error: {e}")
#         return None
#     except KeyError as e:
#         print(f"Missing key in JSON: {x} - Error: {e}")
#         return None



def go(hub_id, project_df, project_list_names):
  print('######################################################')
  print('###########################inicio#####################')
  print('######################################################')
  # project_list_names_macetated_list = ['VAL-BL1069-Adequacao Circuito Hidrico','GER-BL1075-Aditivo Cerrado','BLS-BL3001- Piloto Fluxograma BIM','GER-BL1075-Cerrado','BLS-BL0000-Controle Verificação Interdisciplinar','CBM-BL1063-Engenharia Detalhada Arcelor Mittal','BLS-BL0000-Template BIM360','BLS-BL1069-Piloto Design Generativo','HYD-BL1033-Gerenciamento Projetos B&A','BLS-BL0001-POC','ACT-BL1074-CCM 520 Petrobas','VAL-BL1030','HYD-BL1010-AS-BUILT-02','BLS-BL1000-Treinamento','ALC-BL1067','ALB-BL1059-Engenharia Multidisciplinar','GER-BL1058-Plantas de Carbonização','ALB-BL1090-Adequacao Area 49-412','NEX-BL1034-Bonsucesso','ECH-BL1036-Technical Diligence','USI-BL1018-RAF3','Temporario','BLS-BL0000-Propostas Blossom','AAB-BL1082-Plataforma Acesso Valvulas','BHA-BL1066-BH Airport','AAB-BL1038-Engenharia CMD','AAB-BL1072-Peer Review','AAB-BL1081-Realocacao Caixa Geminada','AAB-BL1084-Flotacao Recleaner','AMG-BL1064','HYD-BL1011','IZA-BL3001-Izabel Souki','HYD-BL1039-As Built Hydro Alunorte','ACT-BL1057-Modelagem 3D','BLS-BL0000-Treinamento','HYD-BL1021-PGM','BLS-BL0000-Sistema de Despoeiramento Filtro Manga','BL0000-Projetos Blossom','HYD-BL1065-Metal Loss','HYD-BL1061-Interstage Cooler - ISC','BLS-BL0000-Piloto Autodesk 2024','GER-BL1086-Peneiramento de Pelotas','BLS-BL0000-Estudos','MNR-BL0000-Piloto Minery','BLS-BL1012-IPOS','BLS-BL0000-Template ACC','BLS-BL0000-Engenharia-de-Dados','ALC-BL0000-GED','BLS-BL0000-Biblioteca Blossom','BLS-BL0001-Engenharia-de-Dados']
  # project_list_names_macetated_list = ['BLS-BL3001- Piloto Fluxograma BIM','GER-BL1075-Cerrado','BLS-BL0000-Controle Verificação Interdisciplinar','CBM-BL1063-Engenharia Detalhada Arcelor Mittal','BLS-BL0000-Template BIM360','BLS-BL1069-Piloto Design Generativo','HYD-BL1033-Gerenciamento Projetos B&A','BLS-BL0001-POC','ACT-BL1074-CCM 520 Petrobas','VAL-BL1030','HYD-BL1010-AS-BUILT-02','BLS-BL1000-Treinamento','ALC-BL1067','ALB-BL1059-Engenharia Multidisciplinar','GER-BL1058-Plantas de Carbonização','ALB-BL1090-Adequacao Area 49-412','NEX-BL1034-Bonsucesso','ECH-BL1036-Technical Diligence','USI-BL1018-RAF3','Temporario','BLS-BL0000-Propostas Blossom','AAB-BL1082-Plataforma Acesso Valvulas','BHA-BL1066-BH Airport','AAB-BL1038-Engenharia CMD','AAB-BL1072-Peer Review','AAB-BL1081-Realocacao Caixa Geminada','AAB-BL1084-Flotacao Recleaner','AMG-BL1064','HYD-BL1011','IZA-BL3001-Izabel Souki','HYD-BL1039-As Built Hydro Alunorte','ACT-BL1057-Modelagem 3D','BLS-BL0000-Treinamento','HYD-BL1021-PGM','BLS-BL0000-Sistema de Despoeiramento Filtro Manga','BL0000-Projetos Blossom','HYD-BL1065-Metal Loss','HYD-BL1061-Interstage Cooler - ISC','BLS-BL0000-Piloto Autodesk 2024','GER-BL1086-Peneiramento de Pelotas','BLS-BL0000-Estudos','MNR-BL0000-Piloto Minery','BLS-BL1012-IPOS','BLS-BL0000-Template ACC','BLS-BL0000-Engenharia-de-Dados','ALC-BL0000-GED','BLS-BL0000-Biblioteca Blossom','BLS-BL0001-Engenharia-de-Dados']
  project_list_names_macetated_list = ['BLS-BL0001-Engenharia-de-Dados']
  # st.write("Fetching from this project list")
  # list_of_project_names = ["BLS-BL0000-Engenharia-de-Dados"] #####  >>>>>> So esta buscando em UM projeto apenas
  list_of_project_names = project_list_names
  # list_of_project_names = ["AAB-BL1072-Peer Review"] #####  >>>>>> So esta buscando em UM projeto apenas
  # st.write(list_of_project_names)
  selected_projects_df = project_df[project_df['attributes_name'].isin(list_of_project_names)]
  list_of_project_id = []
  # for project in list_of_project_names:
  for project in project_list_names_macetated_list:
    selected_project = selected_projects_df[selected_projects_df['attributes_name'] == project].iloc[0]
    list_of_project_id.append(selected_project['id'])
  
  
  # Top folders
  # projects_id_and_Top_folder = {}
  for project_id in list_of_project_id:
    top_folders_df= fetch_functions['fetch_and_normalize_top_folders'](hub_id, project_id)
    top_folder_regex = r'\bBL\d{4}\b'
    top_project_folder = top_folders_df[top_folders_df['attributes_name'].str.contains(top_folder_regex, na=False, regex=True)]
    if top_project_folder.empty:
      top_project_folder = top_folders_df[top_folders_df['attributes_name'] == "Project Files"]
    if top_folders_df is None:
      continue
    if top_folders_df.empty:
      continue
    # populating dict
    # st.write(project_id)
    # try:
    #   # projects_id_and_Top_folder[f"{project_id}"] = {f"Top Folder - {top_project_folder['attributes_name'].iloc[0]}" : top_project_folder['id'].iloc[0]}
    # except Exception as e:
    #   print('-------------------------------------- foi aqui')
    #   st.error(f"id do projeto: {project_id}")
    #   st.write(top_folders_df)
    #   st.write(folder_content_df)
    #   st.write("Aconteceu este erro: " + e)
    # st.text(f"{top_project_folder['attributes_name'].iloc[0]} - {top_project_folder['id'].iloc[0]}")
  
  # Folder Content
  
    # st.write(projects_id_and_Top_folder)
    try:
      st.write(f"folder_content_df try:")
      folder_content_df = fetch_functions['fetch_and_normalize_folder_content'](project_id, top_project_folder['id'].iloc[0])
      st.write(folder_content_df)
      st.text("rolou o fetch")
      st.write(folder_content_df)
      if folder_content_df is None:
        st.write(f"folder_content_df if1: {folder_content_df}")
        continue
      if folder_content_df.empty:
        st.write(f"folder_content_df if2: {folder_content_df}")
        continue
    except Exception as e:
      st.error(f"error on folder contend df: {e}")
      print(e)
    folder_content_regex = r'.ENG$'
    selected_folders_df = folder_content_df[folder_content_df['attributes_name'].str.contains(folder_content_regex, na=False, regex=True) ]
    # projects_id_and_Top_folder[f"{project_id}"][f"Folder content- {top_project_folder['attributes_name'].iloc[0]}"] = selected_folders_df['attributes_name'].iloc[0]
    # st.write(projects_id_and_Top_folder)
    folder_content_files_df = explore_folders(project_id, selected_folders_df['id'].iloc[0])
    folder_content_regex = r'\.nwd$|\.nwc$'
    only_federated_files = folder_content_files_df[folder_content_files_df['attributes_displayName'].str.contains(folder_content_regex, na=False, regex=True)]
    list_of_files_id = []
    for index, row in only_federated_files.iterrows():
      list_of_files_id.append(row['id'])
      # file operations
      items_metadata = fetch_functions['fetch_and_normalize_item_metadata'](project_id, row['id'])
      if items_metadata is None:
        continue
      if items_metadata.empty:
        continue
      item_metadata_id = items_metadata['id'].iloc[0]
      # st.write("item_metadata_id")
      # st.text(item_metadata_id)
      items_metadata_version = fetch_functions['fetch_and_normalize_item_metadata_version'](project_id, item_metadata_id)
      if items_metadata_version is None:
        continue
      if items_metadata_version.empty:
        continue
      # items_metadata_version_id = items_metadata_version['id'].iloc[0]
      # items_metadata_version_id = items_metadata_version_id['id'].loc[0]
      
      # st.write(f"Inicio: {inicio}. final: {final}. total = {final - inicio}")
      # st.write("items_metadata")
      # st.write(items_metadata)
      # st.write("items_metadata_version")
      # st.text(items_metadata_version_id)
      # st.write("items_metadata version")
      # st.write(items_metadata_version)
      # derivatives_data = items_metadata_version['relationships_derivatives'].apply(safe_parse_json)
      derivatives_data = items_metadata_version['relationships_derivatives'].iloc[0]
      # st.write(" derivative_data")
      # st.write(derivatives_data)
      items_version_derivative_id = derivatives_data['data']['id']
      # st.text(items_version_derivative_id)
      derivative_metadata_df = fetch_functions['fetch_and_normalize_derivative_metadata'](items_version_derivative_id)
      if derivative_metadata_df is None:
        continue
      if derivative_metadata_df.empty:
        continue
      item_guid = derivative_metadata_df.loc[0,'metadata_guid']
      # st.write("item_guid")
      # st.text(item_guid)
      # st.write("derivative metadata")
      # st.write(derivative_metadata_df)
      
      item_guid = derivative_metadata_df['metadata_guid'].iloc[0]
      # st.write("item_guid")
      # st.text(item_guid)
      
      
      # derivative_hierarchy_df = fetch_functions['fetch_and_normalize_derivative_obj_hierarchy'](items_metadata_version_id, item_guid)
      try:
        derivativeproperties_df = fetch_functions['fetch_and_normalize_derivative_items_properties'](items_version_derivative_id, item_guid)
        st.success(f"using this item version{items_version_derivative_id} and this itme guid {item_guid}")
        st.write(derivativeproperties_df)
        if derivativeproperties_df is None:
          st.write(" Caiu no IF NONE")
          continue
        elif not derivativeproperties_df.empty:
          file_path = f"{csv_folder_path}/properties_{derivative_metadata_df['metadata_name'].iloc[0]}.json"
          st.write(f"escrevendo para o arquivo: {file_path}")
          derivativeproperties_df.to_json(file_path)
        else:
          
          st.error("No data found for ID: " + items_version_derivative_id)
      except Exception as e:
        st.error("No data found for ID: " + items_version_derivative_id)
        st.error("An error occurred: " + str(e))
  final = time.time()
  duracao = final - inicio
  duracao_timedelta = timedelta(seconds=duracao)
  duracao_formatada = str(duracao_timedelta)
  print(f"Acabou inicio {(duracao_formatada)} ")
  st.success(f"duração: {duracao_formatada}")
  