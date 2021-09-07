"""Switch platform for Dragino."""
from homeassistant.components.switch import SwitchEntity
from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry

from .const import DEFAULT_NAME, DOMAIN, ICON_SERVER, SWITCH, DEVICE_NAME
from .entity import IntegrationDraginoEntity
from .server import DraginoTCPServer

async def async_setup_entry(hass: HomeAssistant, config_entry: ConfigEntry, async_add_devices):
    """Setup sensor platform."""
    server = hass.data[DOMAIN][config_entry.entry_id]
    async_add_devices([IntegrationDraginoBinarySwitch(server, config_entry)])


class IntegrationDraginoBinarySwitch(IntegrationDraginoEntity, SwitchEntity):
    """Dragino event server switch class."""
    def __init__(self, server: DraginoTCPServer, config_entry: ConfigEntry):
        super().__init__(config_entry)
        self._server = server

    async def async_turn_on(self, **kwargs):  # pylint: disable=unused-argument
        """Turn on the switch."""
        self._server.start()

    async def async_turn_off(self, **kwargs):  # pylint: disable=unused-argument
        """Turn off the switch."""
        self._server.stop()

    @property
    def name(self):
        """Return the name of the switch."""
        return f"{DEVICE_NAME} Event Server"

    @property
    def icon(self):
        """Return the icon of this switch."""
        return ICON_SERVER

    @property
    def is_on(self):
        """Return true if the switch is on."""
        return self._server.is_start_initiated() or self._server.is_running()
