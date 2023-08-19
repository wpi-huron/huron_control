# read version from installed package
import importlib
from importlib.metadata import version
__version__ = version("huron_control")

from . import config


def configure_driver(drv_name):
    """
    Configures the low-level driver for huron_control.

    Parameters
    ----------
    drv_name: str
        Name of the driver package.
    """
    spec = importlib.util.find_spec(drv_name)
    if spec is not None:
        config.driver = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(config.driver)
        config.driver_name = drv_name
    else:
        raise PackageConfigurationError(
            f"Cannot set {drv_name} as the driver for huron_control." +
            f"Module {drv_name} not found.")

# Bring methods to package level
from .PackageConfigurationError import PackageConfigurationError
from .PositionMotor import PositionMotor
from .VelocityMotor import VelocityMotor
from .TorqueMotor import TorqueMotor
