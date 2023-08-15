from update_reporter import UpdateReporter
from state_update_model import StateUpdateModel

class AblyUpdateReporter(UpdateReporter):
    """UpdateReporter using Ably API to push updates"""

    async def send_update(self, state: StateUpdateModel):
        pass #temp!!

