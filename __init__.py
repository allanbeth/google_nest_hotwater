from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry
from .const import DOMAIN


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Google Nest Hot Water from a config entry."""
    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN][entry.entry_id] = entry.data

    # Register services
    await hass.async_add_executor_job(register_services, hass)
    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    if entry.entry_id in hass.data[DOMAIN]:
        hass.data[DOMAIN].pop(entry.entry_id)
    return True


def register_services(hass: HomeAssistant):
    """Register the hot water boost service."""

    async def handle_hot_water_boost_service(call):
        """Handle the service call to boost hot water."""
        data = hass.data[DOMAIN][call.data["entry_id"]]
        token = data["token"]
        project_id = data["project_id"]
        device_id = data["device_id"]
        duration = call.data["duration"]

        # Call the API to boost hot water
        try:
            from .hotwater import activate_hot_water_boost

            activate_hot_water_boost(token, project_id, device_id, duration)
        except Exception as e:
            raise Exception(f"Failed to activate hot water boost: {e}")

    hass.services.async_register(
        DOMAIN,
        "activate_hot_water_boost",
        handle_hot_water_boost_service,
    )
