import asyncio
from ably import AblyRest

from update_reporter import UpdateReporter
from state_update_model import StateUpdateModel

class AblyUpdateReporter(UpdateReporter):
    """UpdateReporter using Ably API to push updates"""

    apiKey = 'ymu-SQ.ku-nlw:2yCDZJjeVuUB5a2ieEYw9E-7RbZWFdkcmjRVbVwhHsk'
    client_lock = asyncio.Lock()
    client = AblyRest(apiKey)
    

    async def send_update(self, stateUpdate: StateUpdateModel):
        channel = self.client.channels.get(stateUpdate["userId"])    
        async with self.client_lock:
            await channel.publish('dontcareeventname', stateUpdate)
