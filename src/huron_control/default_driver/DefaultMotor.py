"""Placeholder for huron_control API when huron_control.config.driver has not
been set. PackageConfigurationError will be raised."""

from overrides import override
from typing import Union, List
import mumei
from ..PackageConfigurationError import PackageConfigurationError


class DefaultMotor(mumei.Motor):

    def __init__(self, *args, **kwargs):
        raise PackageConfigurationError("huron_control not configured.")

    @override
    def configure(self, *arg, **kwargs) -> None:
        raise PackageConfigurationError("huron_control not configured.")

    @override
    def initialize(self, *args, **kwargs) -> None:
        raise PackageConfigurationError("huron_control not configured.")

    @override
    def set_up(self, *args, **kwargs) -> None:
        raise PackageConfigurationError("huron_control not configured.")

    @override
    def move(self, val: Union[float, List[float]], *args, **kwargs) -> bool:
        raise PackageConfigurationError("huron_control not configured.")

    @override
    def stop(self, *args, **kwargs) -> bool:
        raise PackageConfigurationError("huron_control not configured.")

    @override
    def terminate(self, *args, **kwargs) -> None:
        raise PackageConfigurationError("huron_control not configured.")

    @override
    def reach_goal(self) -> bool:
        raise PackageConfigurationError("huron_control not configured.")


class PositionMotor(DefaultMotor):
    pass


class VelocityMotor(DefaultMotor):
    pass


class TorqueMotor(DefaultMotor):
    pass
