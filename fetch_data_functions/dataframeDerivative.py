import pandas as pd
import asyncio
from app.api.services.retrieve_metadata_derivative_service import RetrieveMetadataDerivativeService
async def get_metadata(urnOfSouce, derivativeService: RetrieveMetadataDerivativeService):
  try:
    metadata_df = pd.DataFrame(await derivativeService.get_list_of_viewables(urnOfSouce))
    return metadata_df
  except Exception as e:
    print('erro no dataframeDerivative.py', e)

async def get_hierarchy(urnOfSouce, guid, derivativeService: RetrieveMetadataDerivativeService):
  print("urnofsource",urnOfSouce,"guid", guid)
  try:
    hierarchy_df = pd.DataFrame(await derivativeService.get_object_hierarchy(urnOfSouce, guid))
    return hierarchy_df
  except Exception as e:
    print('erro no dataframeDerivative.py', e)

async def get_properties(urnOfSouce, guid, derivativeService: RetrieveMetadataDerivativeService):
  print(f"Usando urn: {urnOfSouce}, guid: {guid}")
  try:
    properties_df = pd.DataFrame(await derivativeService.get_properties(urnOfSouce, guid))
    return properties_df
  except Exception as e:
    print('erro no dataframeDerivative.py', e)