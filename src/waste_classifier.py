from pathlib import Path

SUPPORTED_CATEGORIES = [
    "battery",
    "charger_cable",
    "earphones",
    "led_bulb",
]


def classify_waste(image_path):
    """Placeholder until a trained AI model is connected."""
    path = Path(image_path)

    if not path.is_file():
        raise FileNotFoundError(f"Image not found: {image_path}")

    raise NotImplementedError(
        "AI model integration is still pending."
    )


if _name_ == "_main_":
    print("EcoSort Waste Classifier")
    print("Categories:", ", ".join(SUPPORTED_CATEGORIES))
    print("AI model integration is pending.")
