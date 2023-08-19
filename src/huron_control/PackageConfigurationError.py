class PackageConfigurationError(Exception):
    """Exception raised for not (or incorrectly) configuring huron_control."""

    def __init__(self, message):
        self.message = message
        super().__init__(self.message)
