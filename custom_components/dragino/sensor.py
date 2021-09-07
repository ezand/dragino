"""Sensor platform for Dragino."""
from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry

from .const import DEFAULT_NAME, DOMAIN, ICON, SENSOR
from .entity import IntegrationDraginoEntity


async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_devices):
    """Setup sensor platform."""
    async_add_devices([IntegrationDraginoSensor(config_entry)])


class IntegrationDraginoSensor(IntegrationDraginoEntity):
    """Dragino Sensor class."""

    @property
    def name(self):
        """Return the name of the sensor."""
        return f"{DEFAULT_NAME}_{SENSOR}"

    @property
    def state(self):
        """Return the state of the sensor."""
        return {} #self.coordinator.data.get("body")

    @property
    def icon(self):
        """Return the icon of the sensor."""
        return ICON
