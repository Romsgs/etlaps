import pandas as pd
import asyncio
async def get_hub_id(hubService) -> str:
    hubsResponse = await hubService.get_all_hubs()
    return hubsResponse[0]


# hubInfo = pd.DataFrame(asyncio.run(hubService.get_specific_hub( hub_id=blossom_360_hub_ID)))
# for hub in get_hub_id(hubService):
#   print(hub)
#   st.write(hub)
# # dataFrame = pd.DataFrame(hubInfo)
# st.write("hub Info")
# st.write(hubInfo)

