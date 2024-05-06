import pandas as pd
import asyncio
from app.api.services.projects_service import ProjectsService

async def get_projects(hub_id, projectsService: ProjectsService):
    try:
        projects = pd.DataFrame(await projectsService.get_all_projects(hub_id))
        projects.to_csv('./CSVs/projects.csv', index=True)
        return projects
    except Exception as e:
        print(f"Failed to retrieve or save projects: {e}")
        return pd.DataFrame()

async def get_specific_project(hubId, projectId, projectName, projectService: ProjectsService):
    try:
        projects_df = pd.DataFrame(await projectService.get_specific_project(hubId, projectId))
        # Uncomment and adjust the following if 'attributes' contains JSON-like data
        attributes_expanded = projects_df['attributes'].apply(pd.Series)
        attributes_expanded.columns = ['attr_' + str(col) for col in attributes_expanded.columns]
        projects_df = pd.concat([projects_df.drop('attributes', axis=1), attributes_expanded], axis=1)
        projects_df.to_csv(f'./CSVs/{projectName}.csv', index=True)
        return projects_df
    except Exception as e:
        print(f"Failed to retrieve or save specific project: {e}")
        return pd.DataFrame()

# Assuming you call these functions from an async context, e.g.,
# asyncio.run(get_projects(123, ProjectsService()))
# asyncio.run(get_specific_project(123, 456, ProjectsService()))




# import pandas as pd
# import asyncio
# from app.api.services.projects_service import ProjectsService


# async def get_projects(hub_id, projectsService:ProjectsService):
#   projects = pd.DataFrame(await (projectsService.get_all_projects(hub_id)))
#   projects.to_csv('./CSVs/projects_CSV.csv',index=True)
#   return projects
  
  
# async def get_specific_project(hubId, projectId, projectService:ProjectsService):
#   projects_df = pd.DataFrame(await (projectService.get_specific_project(hubId, projectId)))
#   # attributes_expanded = projects_df['attributes'].apply(pd.Series)
#   # attributes_expanded.columns = ['attr_' + str(col) for col in attributes_expanded.columns]
#   # print(attributes_expanded.head())
#   # projects_df_attributes_expanded = projects_df['attributes'].apply(pd.Series)
#   # projects_df_with_Attributes = pd.concat([projects_df.drop('attributes', axis=1), projects_df_attributes_expanded], axis=1)
#   # projects_df = pd.concat([projects_df.drop('attributes', axis=1), attributes_expanded], axis=1)
#   projects_df.to_csv(f'./CSVs/specific_project_{projectId}_CSV.csv', index=True)
#   return projects_df

  
    


