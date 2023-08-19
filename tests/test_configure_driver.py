import pytest
import huron_control as hc
import importlib.util


@pytest.mark.parametrize(
    "default_motor_class",
    [
        hc.PositionMotor, hc.VelocityMotor, hc.TorqueMotor
    ]
)
def test_default_driver(default_motor_class):
    with pytest.raises(hc.PackageConfigurationError):
        motor = default_motor_class()


def test_phys_driver_torque():
    pkg_name = "huron_driver"
    # assert class
    spec = importlib.util.find_spec(pkg_name)
    if spec is not None:
        print("huron_driver is installed!")
        # Import huron_driver's TorqueMotor class
        hc.configure_driver(pkg_name)

        # Load the expected class
        expected_class = None
        exp_spec = importlib.util.find_spec(pkg_name)
        if exp_spec is not None:
            module = importlib.util.module_from_spec(exp_spec)
            exp_spec.loader.exec_module(module)
            expected_class = module.TorqueMotor

        # Instantiate a TorqueMotor object
        motor = hc.TorqueMotor(odrive_controller=None)

        assert type(motor) is expected_class
    else:
        print("huron_driver is not installed!")


def test_phys_driver_position():
    pkg_name = "huron_driver"
    # assert class
    spec = importlib.util.find_spec(pkg_name)
    if spec is not None:
        print("huron_driver is installed!")
        # Import huron_driver's TorqueMotor class
        hc.configure_driver(pkg_name)

        # Load the expected class
        expected_class = None
        exp_spec = importlib.util.find_spec(pkg_name)
        if exp_spec is not None:
            module = importlib.util.module_from_spec(exp_spec)
            exp_spec.loader.exec_module(module)
            expected_class = module.PositionMotor

        # Instantiate a TorqueMotor object
        motor = hc.PositionMotor(odrive_controller=None)

        assert type(motor) is expected_class
    else:
        print("huron_driver is not installed!")


def test_phys_driver_velocity():
    pkg_name = "huron_driver"
    # assert class
    spec = importlib.util.find_spec(pkg_name)
    if spec is not None:
        print("huron_driver is installed!")
        # Import huron_driver's TorqueMotor class
        hc.configure_driver(pkg_name)

        # Load the expected class
        expected_class = None
        exp_spec = importlib.util.find_spec(pkg_name)
        if exp_spec is not None:
            module = importlib.util.module_from_spec(exp_spec)
            exp_spec.loader.exec_module(module)
            expected_class = module.VelocityMotor

        # Instantiate a TorqueMotor object
        motor = hc.VelocityMotor(odrive_controller=None)

        assert type(motor) is expected_class
    else:
        print("huron_driver is not installed!")


def test_invalid_driver():
    with pytest.raises(hc.PackageConfigurationError):
        hc.configure_driver("inv4l1d")
