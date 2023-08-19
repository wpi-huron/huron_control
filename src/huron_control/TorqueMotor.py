import mumei
from huron_control import config


def TorqueMotor(**kwargs) -> mumei.Motor:
    return config.driver.TorqueMotor(**kwargs)
