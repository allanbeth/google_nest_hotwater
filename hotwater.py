import requests


def activate_hot_water_boost(token: str, project_id: str, device_id: str, duration: int):
    """Activates the hot water boost for the specified duration."""
    base_url = f"https://smartdevicemanagement.googleapis.com/v1"
    url = f"{base_url}/enterprises/{project_id}/devices/{device_id}:executeCommand"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }
    payload = {
        "command": "sdm.devices.commands.HotWater.ActivateBoost",
        "params": {"duration": duration},
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code != 200:
        raise Exception(
            f"Failed to activate hot water boost. "
            f"Status code: {response.status_code}, Response: {response.text}"
        )

    return response.json()
