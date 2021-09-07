"""DraginoEntity class"""
from homeassistant.helpers.entity import Entity, DeviceInfo
from homeassistant.config_entries import ConfigEntry

import re

from .const import DOMAIN, DEVICE_NAME, ATTRIBUTION, MANUFACTURER, CONF_DEVICE_MODEL, VERSION


class DraginoDevice:
    """Represents a single Dragino device."""
    def __init__(self, config_entry):
        """Initialize device."""
        self._config_entry = config_entry
        self._name = DEVICE_NAME
        self._model = config_entry.data.get(CONF_DEVICE_MODEL)
        self._manufacturer = MANUFACTURER
        self._attribution = ATTRIBUTION

    @property
    def name(self):
        """Return the name of the device if any."""
        return self._name

    @property
    def model(self):
        """Return the model of the device if any."""
        return self._model

    @property
    def manufacturer(self):
        """Return the manufacturer of the device if any."""
        return self._manufacturer

    @property
    def attribution(self):
        """Return the attribution of the device if any."""
        return self._attribution

    async def async_setup(self):
        """TODO Fetch info from device"""


class IntegrationDraginoEntity(Entity):
    def __init__(self, config_entry: ConfigEntry):
        self._device = DraginoDevice(config_entry)
        self._config_entry = config_entry

    @property
    def unique_id(self):
        """Return a unique ID to use for this entity."""
        pattern = re.compile('[\W_]+')
        model = re.sub(
            r'\W+', '',
            self._config_entry.data.get(CONF_DEVICE_MODEL).lower()
        )
        entry_id = self._config_entry.entry_id
        return f"{DOMAIN}_{model}_{entry_id}"

    @property
    def device_info(self) -> DeviceInfo:
        """Return the device info."""
        return {
            "identifiers": {(DOMAIN, self.unique_id)},
            "name": self._device.name,
            "model": self._device.model,
            "manufacturer": self._device.manufacturer,
        }

    @property
    def device_state_attributes(self):
        """Return the state attributes."""
        return {
            "attribution": self._device.attribution,
        }
