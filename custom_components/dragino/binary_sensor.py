"""Binary sensor platform for Dragino."""
from homeassistant.components.binary_sensor import BinarySensorEntity
from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry

from .const import (
    BINARY_SENSOR,
    BINARY_SENSOR_DEVICE_CLASS,
    DEFAULT_NAME,
    DOMAIN,
    DEVICE_NAME
)
from .entity import IntegrationDraginoEntity, DraginoDevice
from .server import DraginoTCPServer


async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_devices):
    """Setup binary_sensor platform."""
    server = hass.data[DOMAIN][config_entry.entry_id]
    async_add_devices([IntegrationDraginoBinarySensor(server, config_entry)])


class IntegrationDraginoBinarySensor(IntegrationDraginoEntity, BinarySensorEntity):
    """Dragino binary_sensor class."""
    def __init__(self, server: DraginoTCPServer, config_entry: ConfigEntry):
        super().__init__(config_entry)
        self._server = server

    @property
    def name(self):
        """Return the name of the binary_sensor."""
        return f"{DEVICE_NAME} Event Server"

    @property
    def device_class(self):
        """Return the class of this binary_sensor."""
        return BINARY_SENSOR_DEVICE_CLASS

    @property
    def is_on(self):
        """Return true if the binary_sensor is on."""
        return self._server.is_start_initiated() or self._server.is_running()
