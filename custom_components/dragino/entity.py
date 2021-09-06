"""DraginoEntity class"""
from homeassistant.helpers.update_coordinator import CoordinatorEntity
import re

from .const import DOMAIN, DEVICE_NAME, ATTRIBUTION, MANUFACTURER, CONF_DEVICE_MODEL, VERSION


class IntegrationDraginoEntity(CoordinatorEntity):
    def __init__(self, coordinator, config_entry):
        super().__init__(coordinator)
        self.config_entry = config_entry

    @property
    def unique_id(self):
        """Return a unique ID to use for this entity."""
        pattern = re.compile('[\W_]+')
        model = re.sub(
            r'\W+', '',
            self.config_entry.data.get(CONF_DEVICE_MODEL).lower()
        )
        entry_id = self.config_entry.entry_id
        return f"{DOMAIN}_{model}_{entry_id}"

    @property
    def device_info(self):
        return {
            "identifiers": {(DOMAIN, self.unique_id)},
            "name": DEVICE_NAME,
            "model": self.config_entry.data.get(CONF_DEVICE_MODEL),
            "manufacturer": MANUFACTURER,
        }

    @property
    def device_state_attributes(self):
        """Return the state attributes."""
        return {
            "attribution": ATTRIBUTION,
            "id": str(self.coordinator.data.get("id")),
            "integration": DOMAIN,
        }
