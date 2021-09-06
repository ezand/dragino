"""Constants for Dragino tests."""
from custom_components.dragino.const import CONF_BIND_HOST, CONF_LISTEN_PORT, CONF_DEVICE_MODEL

# Mock config data to be used across multiple tests
MOCK_CONFIG = {CONF_BIND_HOST: "localhost", CONF_LISTEN_PORT: 9999, CONF_DEVICE_MODEL: "LPS8"}
