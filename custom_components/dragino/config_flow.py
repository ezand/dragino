"""Adds config flow for Dragino."""
from homeassistant import config_entries
from homeassistant.core import callback
from homeassistant.helpers.aiohttp_client import async_create_clientsession
import voluptuous as vol

from .const import (
    CONF_BIND_HOST,
    CONF_LISTEN_PORT,
    CONF_DEVICE_MODEL,
    DEFAULT_BIND_HOST,
    DEFAULT_LISTEN_PORT,
    DEFAULT_DEVICE_MODEL,
    DOMAIN,
    PLATFORMS,
)


class DraginoFlowHandler(config_entries.ConfigFlow, domain=DOMAIN):
    """Config flow for Dragino."""

    VERSION = 1
    CONNECTION_CLASS = config_entries.CONN_CLASS_CLOUD_POLL

    def __init__(self):
        """Initialize."""
        self._errors = {}

    async def async_step_user(self, user_input=None):
        """Handle a flow initialized by the user."""
        self._errors = {}

        # Uncomment the next 2 lines if only a single instance of the integration is allowed:
        # if self._async_current_entries():
        #     return self.async_abort(reason="single_instance_allowed")

        if user_input is not None:
            valid = await self._test_credentials(
                user_input[CONF_LISTEN_PORT], user_input[CONF_DEVICE_MODEL]
            )
            if valid:
                return self.async_create_entry(
                    title=user_input[CONF_DEVICE_MODEL], data=user_input
                )
            else:
                self._errors["base"] = "auth"

            return await self._show_config_form(user_input)

        user_input = {}
        # Provide defaults for form
        user_input[CONF_BIND_HOST] = ""
        user_input[CONF_LISTEN_PORT] = ""
        user_input[CONF_DEVICE_MODEL] = ""

        return await self._show_config_form(user_input)

    @staticmethod
    @callback
    def async_get_options_flow(config_entry):
        return DraginoOptionsFlowHandler(config_entry)

    async def _show_config_form(self, user_input):  # pylint: disable=unused-argument
        """Show the configuration form to edit location data."""
        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema(
                {
                    vol.Required(CONF_BIND_HOST, default=DEFAULT_BIND_HOST): str,
                    vol.Required(CONF_LISTEN_PORT, default=DEFAULT_LISTEN_PORT): int,
                    vol.Required(CONF_DEVICE_MODEL, default=DEFAULT_DEVICE_MODEL): vol.In( ["LPS8", "LG308", "DLOS8", "Other"]),
                }
            ),
            errors=self._errors,
        )

    async def _test_credentials(self, username, password):
        """Return true if credentials is valid."""
        try:
            # TODO
            return True
        except Exception:  # pylint: disable=broad-except
            pass
        return False


class DraginoOptionsFlowHandler(config_entries.OptionsFlow):
    """Dragino config flow options handler."""

    def __init__(self, config_entry):
        """Initialize HACS options flow."""
        self.config_entry = config_entry
        self.options = dict(config_entry.options)

    async def async_step_init(self, user_input=None):  # pylint: disable=unused-argument
        """Manage the options."""
        return await self.async_step_user()

    async def async_step_user(self, user_input=None):
        """Handle a flow initialized by the user."""
        if user_input is not None:
            self.options.update(user_input)
            return await self._update_options()

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema(
                {
                    vol.Required(x, default=self.options.get(x, True)): bool
                    for x in sorted(PLATFORMS)
                }
            ),
        )

    async def _update_options(self):
        """Update config entry options."""
        return self.async_create_entry(
            title=self.config_entry.data.get(CONF_DEVICE_MODEL), data=self.options
        )
