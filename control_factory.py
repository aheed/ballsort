from ball_control_sim import BallControlSim
#from v1_update_reporter import V1UpdateReporter
from ably_update_reporter import AblyUpdateReporter

def get_control_sim() -> BallControlSim:
    #reporter = V1UpdateReporter()
    reporter = AblyUpdateReporter()
    return BallControlSim(reporter)
