from pathlib import Path

SUPPORTED_CATEGORIES = [
    "battery",
    "charger_cable",
    "earphones",
    "led_bulb",
]


def classify_waste(image_path):
    """
    Placeholder for the future AI image-classification model.
    A trained model must be connected before real predictions.
    """
    path = Path(image_path)

    if not path.is_file():
        raise FileNotFoundError(f"Image not found: {image_path}")

    raise NotImplementedError(
        "AI model is not connected yet. "
        "Train or load a model before classifying images."
    )


if _name_ == "_main_":
    print("EcoSort waste classifier")
    print("Supported categories:", ", ".join(SUPPORTED_CATEGORIES))
    print("AI model integration is pending.")
