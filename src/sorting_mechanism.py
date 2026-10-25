def sort_waste(category):
    """Map a recognized e-waste category to its planned compartment."""

    compartments = {
        "battery": "Battery compartment",
        "charger_cable": "Cables and chargers compartment",
        "earphones": "Small electronics compartment",
        "led_bulb": "LED bulb compartment",
    }

    if category not in compartments:
        return {
            "success": False,
            "message": "Unknown category. Manual inspection required."
        }

    return {
        "success": True,
        "compartment": compartments[category]
    }


if _name_ == "_main_":
    for item in ["battery", "charger_cable", "unknown"]:
        print(item, "->", sort_waste(item))
