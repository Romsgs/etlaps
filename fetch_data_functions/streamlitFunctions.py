from fetch_data_functions.dataframeHubs import get_hub_id
from fetch_data_functions.dataframeProjects import get_projects, get_specific_project
from fetch_data_functions.dataframeFolder import get_folder_content, get_top_folders
from fetch_data_functions.dataframeItems import get_items_metadata
from fetch_data_functions.dataframeVersions import get_items_version

streamlitFunctions = {
  "get_items_metadata":get_items_metadata,
  "get_folder_content":get_folder_content,
  "get_top_folders":get_top_folders,
  "get_projects":get_projects,
  "get_specific_project":get_specific_project,
  'get_hub_id':get_hub_id
  }