# How tall is Big Ben? - www.101computing.net/how-tall-is-big-ben-python-challenge/

# --- Input Data ---

# Case 1: Elizabeth Tower
PHONE_BOOTH_HEIGHT = 2.51
PHONE_BOOTH_SHADOW_LENGTH = 1.74
ELIZABETH_TOWER_SHADOW_LENGTH = 66.55

# Case 2: Eiffel Tower
PERSON_HEIGHT = 1.85
PERSON_SHADOW_LENGTH = 1.04
EIFFEL_TOWER_SHADOW_LENGTH = 185.5

# --- Process ---
def height_from_shadows(reference_height, reference_shadow_length, target_shadow_length):
    """Calculates an object's height based on its shadow length and a reference object.

    Args:
        reference_height (float): The height of the known reference object.
        reference_shadow_length (float): The length of the reference object's shadow.
        target_shadow_length (float): The length of the target object's shadow.

    Returns:
        float: The estimated height of the target object.
    """
    return (reference_height * target_shadow_length) / reference_shadow_length

# --- Calculations and Output ---

# Elizabeth Tower
elizabeth_tower_height = height_from_shadows(
    PHONE_BOOTH_HEIGHT,
    PHONE_BOOTH_SHADOW_LENGTH,
    ELIZABETH_TOWER_SHADOW_LENGTH
)
print(f"The Elizabeth Tower is {round(elizabeth_tower_height, 1)} meters tall.")

# Eiffel Tower
eiffel_tower_height = height_from_shadows(
    PERSON_HEIGHT,
    PERSON_SHADOW_LENGTH,
    EIFFEL_TOWER_SHADOW_LENGTH
)
print(f"The Eiffel Tower is {round(elizabeth_tower_height, 1)} meters tall.")

