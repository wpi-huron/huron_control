import mumei
from huron_control import config


def PositionMotor(**kwargs) -> mumei.Motor:
    return config.driver.PositionMotor(**kwargs)
