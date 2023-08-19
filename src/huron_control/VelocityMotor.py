import mumei
from huron_control import config


def VelocityMotor(**kwargs) -> mumei.Motor:
    return config.driver.VelocityMotor(**kwargs)
