from app.api.services.services import services
import asyncio
import pandas as pd
import streamlit as st
from fetch_data_functions.dataframeHubs import get_hub_id
from fetch_data_functions.dataframeProjects import get_projects, get_specific_project
from fetch_data_functions.dataframeFolder import get_folder_content, get_top_folders
from fetch_data_functions.dataframeItems import get_items_metadata, get_items_metadata_version
from fetch_data_functions.dataframeVersions import get_items_version
from fetch_data_functions.dataframeDerivative import get_metadata, get_hierarchy, get_properties

async def make_arrow_compatible(data_frame):
    try:
        for column in data_frame.columns:
            if isinstance(data_frame[column].iloc[0], dict):
                expanded = data_frame[column].apply(pd.Series)
                expanded.columns = [f"{column}_{subcol}" for subcol in expanded.columns]
                data_frame = data_frame.drop(column, axis=1).join(expanded)
        return data_frame
    except Exception as e:
        st.error(e)
        return pd.DataFrame({})

async def fetch_hub_id():
    return await get_hub_id(services['hubService'])

async def fetch_and_normalize_projects(hub_Id):
    projects_df = await get_projects(hub_Id, services['projectsService'])
    return await make_arrow_compatible(projects_df)

async def fetch_and_normalize_specifyc_projects(hub_Id, project_id, project_name):
    projects_df = await get_specific_project(hub_Id, project_id, project_name, services['projectsService'])
    return await make_arrow_compatible(projects_df)

async def fetch_and_normalize_folder_content(project_id, folderId):
    top_folders_df = await get_folder_content(project_id, folderId, services['folderService'])
    return await make_arrow_compatible(top_folders_df)

async def fetch_and_normalize_top_folders(hub_Id, project_id):
    top_folders_df = await get_top_folders(hub_Id, project_id, services['folderService'])
    return await make_arrow_compatible(top_folders_df)

async def fetch_and_normalize_item_metadata(projectId, itemId):
    items_metadata_df = await get_items_metadata(projectId, itemId, services['itemService'])
    return await make_arrow_compatible(items_metadata_df)

async def fetch_and_normalize_item_metadata_version(projectId, itemId):
    items_metadata_version_df = await get_items_metadata_version(projectId, itemId, services['itemService'])
    return await make_arrow_compatible(items_metadata_version_df)

async def fetch_and_normalize_versions(projectId, versionId):
    return await get_items_version(projectId, versionId, services['versionService'])

async def fetch_and_normalize_derivative_metadata(urnOfSource):
    metadata_df = await get_metadata(urnOfSource, services['derivativeService'])
    return await make_arrow_compatible(metadata_df)

async def fetch_and_normalize_derivative_obj_hierarchy(urnOfSource, guid):
    metadata_df = await get_hierarchy(urnOfSource, guid, services['derivativeService'])
    return metadata_df

async def fetch_and_normalize_derivative_items_properties(urnOfSource, guid):
    metadata_df = await get_properties(urnOfSource, guid, services['derivativeService'])
    return metadata_df
fetch_functions = {
    'fetch_hub_id': lambda: asyncio.run(fetch_hub_id()),
    'fetch_and_normalize_projects': lambda hub_Id: asyncio.run(fetch_and_normalize_projects(hub_Id)),
    'fetch_and_normalize_specifyc_projects': lambda hub_Id, project_id, project_name: asyncio.run(fetch_and_normalize_specifyc_projects(hub_Id, project_id, project_name)),
    'fetch_and_normalize_folder_content': lambda project_id, folderId: asyncio.run(fetch_and_normalize_folder_content(project_id, folderId)),
    'fetch_and_normalize_top_folders': lambda hub_Id, project_id: asyncio.run(fetch_and_normalize_top_folders(hub_Id, project_id)),
    'fetch_and_normalize_item_metadata': lambda projectId, itemId: asyncio.run(fetch_and_normalize_item_metadata(projectId, itemId)),
    'fetch_and_normalize_item_metadata_version': lambda projectId, itemId: asyncio.run(fetch_and_normalize_item_metadata_version(projectId, itemId)),
    'fetch_and_normalize_versions': lambda projectId, versionId: asyncio.run(fetch_and_normalize_versions(projectId, versionId)),
    'fetch_and_normalize_derivative_metadata': lambda urnOfSource: asyncio.run(fetch_and_normalize_derivative_metadata(urnOfSource)),
    'fetch_and_normalize_derivative_obj_hierarchy': lambda urnOfSource, guid: asyncio.run(fetch_and_normalize_derivative_obj_hierarchy(urnOfSource, guid)),
    'fetch_and_normalize_derivative_items_properties': lambda urnOfSource, guid: asyncio.run(fetch_and_normalize_derivative_items_properties(urnOfSource, guid))
}
