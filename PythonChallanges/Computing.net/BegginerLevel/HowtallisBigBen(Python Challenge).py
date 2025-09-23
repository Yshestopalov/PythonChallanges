#How tall is Big Ben? - www.101computing.net/how-tall-is-big-ben-python-challenge/

# Input

# l: The length of the telephone box shadow.
# h: The height of the telephone box.
# L: The length of the Elizabeth Tower shadow.
l, h, L = 1.74, 2.51, 66.55 # meters

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


# Output

print(round(elizabeth_tower_height(l, h, L), 1))


