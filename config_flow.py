from homeassistant import config_entries
from homeassistant.core import callback
from .const import DOMAIN, CONF_TOKEN, CONF_PROJECT_ID, CONF_DEVICE_ID


class GoogleNestHotWaterConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Google Nest Hot Water."""

    async def async_step_user(self, user_input=None):
        """Handle the initial step."""
        if user_input is not None:
            return self.async_create_entry(title="Google Nest Hot Water", data=user_input)

        return self.async_show_form(
            step_id="user",
            data_schema=self._get_form_schema(),
        )

    @callback
    def _get_form_schema(self):
        """Return the schema for the form."""
        import voluptuous as vol

        return vol.Schema(
            {
                vol.Required(CONF_TOKEN): str,
                vol.Required(CONF_PROJECT_ID): str,
                vol.Required(CONF_DEVICE_ID): str,
            }
        )
