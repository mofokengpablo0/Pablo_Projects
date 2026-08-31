# --- Data: Advice Dictionary ---
# Storing all gardening advice in a dictionary for easy maintenance
# and extensibility. Each season maps to advice and recommended plants.
ADVICE_BY_SEASON = {
    "spring": {
        "advice": "Plant new seeds and prepare your garden beds.\n",
        "recommended_plants": ["lettuce", "peas", "radishes", "carrots"],
    },
    "summer": {
        "advice": "Water your plants regularly and provide some shade.\n",
        "recommended_plants": ["tomatoes", "peppers", "cucumbers", "sunflowers"],
    },
    "autumn": {
        "advice": "Harvest your crops and prepare the soil for winter.\n",
        "recommended_plants": ["kale", "spinach", "garlic", "pumpkins"],
    },
    "winter": {
        "advice": "Protect your plants from frost with covers.\n",
        "recommended_plants": ["winter cabbage", "broccoli", "brussels sprouts"],
    },
}

# Mapping of plant types to specific care advice
ADVICE_BY_PLANT = {
    "flower": "Use fertiliser to encourage blooms.",
    "vegetable": "Keep an eye out for pests!",
    "herb": "Trim regularly to encourage bushy growth.",
    "tree": "Mulch around the base to retain moisture.",
    "succulent": "Water sparingly and ensure good drainage.",
}


def get_season():
    """Prompt the user for a season and normalise the input."""
    season = (
        input("Enter the current season (spring/summer/autumn/winter): ")
        .strip()
        .lower()
    )
    return season


def get_plant_type():
    """Prompt the user for a plant type and normalise the input."""
    plant_type = (
        input("Enter the plant type (flower/vegetable/herb/tree/succulent): ")
        .strip()
        .lower()
    )
    return plant_type


def get_seasonal_advice(season):
    """
    Return seasonal advice and recommended plants.
    Falls back to a default message when the season is unknown.
    """
    if season in ADVICE_BY_SEASON:
        data = ADVICE_BY_SEASON[season]
        advice = data["advice"]
        plants = data["recommended_plants"]
        plant_list = ", ".join(plants)
        advice += f"Recommended plants for {season}: {plant_list}.\n"
        return advice
    return "No advice for this season.\n"


def get_plant_advice(plant_type):
    """
    Return care advice for a specific plant type.
    Falls back to a default message when the plant type is unknown.
    """
    return ADVICE_BY_PLANT.get(plant_type, "No advice for this type of plant.")


def main():
    """Main entry point: gathers user input and prints the combined advice."""
    print("=== Garden Advisor ===\n")

    season = get_season()
    plant_type = get_plant_type()

    # Combine the seasonal and plant-type advice
    advice = get_seasonal_advice(season) + get_plant_advice(plant_type)

    print("\n--- Your Gardening Advice ---")
    print(advice)


# Run the program only when this file is executed directly
if __name__ == "__main__":
    main()


# TODO: Examples of possible features to add:
# - Add detailed comments explaining each block of code.
# - Refactor the code into functions for better readability and modularity.
# - Store advice in a dictionary for multiple plants and seasons.
# - Recommend plants based on the entered season.
