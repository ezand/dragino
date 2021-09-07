"""Binary sensor platform for Dragino."""
from homeassistant.components.binary_sensor import BinarySensorEntity
from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry

from .const import (
    BINARY_SENSOR,
    BINARY_SENSOR_DEVICE_CLASS,
    DEFAULT_NAME,
    DOMAIN,
)
from .entity import IntegrationDraginoEntity, DraginoDevice


async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_devices):
    """Setup binary_sensor platform."""
    async_add_devices([IntegrationDraginoBinarySensor(config_entry)])


class IntegrationDraginoBinarySensor(IntegrationDraginoEntity, BinarySensorEntity):
    """Dragino binary_sensor class."""

    @property
    def name(self):
        """Return the name of the binary_sensor."""
        return f"{DEFAULT_NAME}_{BINARY_SENSOR}"

    @property
    def device_class(self):
        """Return the class of this binary_sensor."""
        return BINARY_SENSOR_DEVICE_CLASS

    @property
    def is_on(self):
        """Return true if the binary_sensor is on."""
        return True #self.coordinator.data.get("title", "") == "foo"
