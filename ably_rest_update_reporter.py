import asyncio
import aiohttp
import base64
from update_reporter import UpdateReporter
from state_update_model import StateUpdateModel
from dataclasses import asdict, dataclass

@dataclass
class AblyMessageBody:
    name: str
    data: StateUpdateModel

class AblyRestUpdateReporter(UpdateReporter):
    """UpdateReporter using Ably REST API to push updates"""

    #backend = 'http://localhost:5167/'
    ably_host = 'https://rest.ably.io'
    client_session = None
    client_lock = asyncio.Lock()
    apiKey = base64.b64encode('ymu-SQ.ku-nlw:2yCDZJjeVuUB5a2ieEYw9E-7RbZWFdkcmjRVbVwhHsk'.encode("ascii")).decode("ascii")

    def get_session(self):
        if (self.client_session is None):
            self.client_session = aiohttp.ClientSession(base_url=self.ably_host, headers={'Authorization': f'Basic {self.apiKey}'})
        return self.client_session
    
    async def send_update(self, stateUpdate: StateUpdateModel):
        session = self.get_session()
        async with self.client_lock:
            url_path = f'/channels/{stateUpdate.userId}/messages'
            body = asdict(AblyMessageBody("dc", stateUpdate))
            resp = await session.post(url_path, json=body)
            print(resp.status)
            print(await resp.text())

    async def shutdown(self):
        if (self.client_session is not None):
            await self.client_session.close()
            await asyncio.sleep(0.5)
