from ball_control import BallControl
from ball_control_sim import BallControlSim
from v1_update_reporter import V1UpdateReporter

def get_control_sim() -> BallControl:
    reporter = V1UpdateReporter()
    return BallControlSim(reporter)
