from fetch_data_functions.fetch_data import fetch_functions
import streamlit as st
import pandas as pd
def explore_folders(project_id, folder_id):

    """Recursive function to explore folders and retrieve their contents.
    Args:
        project_id (str): The project identifier.
        folder_id (str): The starting folder identifier.

    Returns:
        pd.DataFrame: A DataFrame containing all folder contents recursively.
    """
    all_folders = []
    content_df = fetch_functions['fetch_and_normalize_folder_content'](project_id, folder_id)
    
    # Check if the column exists before accessing it
    if 'attributes_objectCount' in content_df.columns:
        folder_ids_with_multiple_objects = content_df[(content_df['attributes_objectCount'] > 0) & (content_df['type'] == 'folders')]['id'].tolist()

        # Recurse into each folder found
        for sub_folder_id in folder_ids_with_multiple_objects:
            sub_folder_content = explore_folders(project_id, sub_folder_id)
            all_folders.append(sub_folder_content)
    else:
        # print("Column 'attributes_objectCount' does not exist in the DataFrame.")
        # print(content_df.columns)
        pass 
    # Append content_df only if it's not empty
    if not content_df.empty:
        all_folders.append(content_df)
    if len(all_folders) == 0:
        print("Sem conteudo para concatenar (função explore_folders)")
        return pd.DataFrame()
    concated_dfs = pd.concat(all_folders, ignore_index=True)
    # Concatenate all results once outside the loop
    return concated_dfs


