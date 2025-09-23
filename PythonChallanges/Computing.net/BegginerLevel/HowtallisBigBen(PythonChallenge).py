#How tall is Big Ben? - www.101computing.net/how-tall-is-big-ben-python-challenge/

# Input

# l: The length of the telephone box shadow.
# h: The height of the telephone box.
# L: The length of the Elizabeth Tower shadow.
l_eliz, h_eliz, L_eliz = 1.74, 2.51, 66.55 # meters

l_eiff, h_eiff, L_eiff = 1.04, 1.85, 185.5 # meters

# Process

# Figures out the height of the Elizabeth Tower.
def elizabeth_tower_height(l, h, L):
    """
    Calculate the height of the Elizabeth Tower using shadow proportions.

    Parameters:
        l (float): Length of the shadow of the telephone booth.
        h (float): Height of the telephone booth.
        L (float): Length of the shadow of the Elizabeth Tower.

    Returns:
        float: Estimated height of the Elizabeth Tower.
    """
    return (h * L) / l

# Figures out the height of the Eiffel Tower.
def eiffel_tower_height(l, h, L):
    """
    Calculate the height of the Eiffel Tower using shadow proportions.

    Parameters:
        l (float): Length of the shadow of the person.
        h (float): Height of the person.
        L (float): Length of the shadow of the Eiffel Tower.

    Returns:
        float: Estimated height of the Eiffel Tower.
    """
    return (h * L) / l


# Output

tower_height = round(elizabeth_tower_height(l_eliz, h_eliz, L_eliz), 1)
print(tower_height)

tower_height = round(eiffel_tower_height(l_eiff, h_eiff, L_eiff), 1)
print(tower_height)


