import asyncio
import aiohttp
from update_reporter import UpdateReporter
from state_update_model import StateUpdateModel

class V1UpdateReporter(UpdateReporter):
    """UpdateReporter using custom backend API to push updates"""

    backend = 'http://localhost:5167/'
    client_session = None
    client_lock = None

    def get_session(self):
        if (self.client_session is None):
            self.client_lock = asyncio.Lock()
            self.client_session = aiohttp.ClientSession(self.backend)
        return self.client_session
    
    async def send_update(self, state: StateUpdateModel):
        session = self.get_session()
        async with self.client_lock:
            resp = await session.post('/api/update', json=state)
            print(resp.status)
            print(await resp.text())

    async def shutdown(self):
        await self.client_session.close()
        await asyncio.sleep(0.5)