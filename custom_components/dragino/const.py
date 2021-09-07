"""Constants for Dragino."""
# Base component constants
DEVICE_NAME = "Dragino"
MANUFACTURER = "Dragino Technology Co., LTD."
NAME = "Dragino Integration"
DOMAIN = "dragino"
DOMAIN_DATA = f"{DOMAIN}_data"
VERSION = "0.0.1"
ATTRIBUTION = "Data provided by Dragino gateway"
ISSUE_URL = "https://github.com/ezand/dragino/issues"

# Icons
ICON = "mdi:format-quote-close"
ICON_SERVER = "mdi:earth"

# Device classes
BINARY_SENSOR_DEVICE_CLASS = "connectivity"

# Platforms
BINARY_SENSOR = "binary_sensor"
SENSOR = "sensor"
SWITCH = "switch"
PLATFORMS = [BINARY_SENSOR, SENSOR, SWITCH]


# Configuration and options
CONF_ENABLED = "enabled"
CONF_BIND_HOST = "host"
CONF_LISTEN_PORT = "port"
CONF_DEVICE_MODEL = "model"

# Defaults
DEFAULT_NAME = DOMAIN
DEFAULT_BIND_HOST = "localhost"
DEFAULT_LISTEN_PORT = 9999
DEFAULT_DEVICE_MODEL = "LPS8"

STARTUP_MESSAGE = f"""
-------------------------------------------------------------------
{NAME}
Version: {VERSION}
This is a custom integration!
If you have any issues with this you need to open an issue here:
{ISSUE_URL}
-------------------------------------------------------------------
"""
