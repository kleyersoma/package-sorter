
def sort(width, height, length, mass):
    """
    Sort packages based on their dimensions and mass.
    Args:
        width (float): Width of the package in cm
        height (float): Height of the package in cm
        length (float): Length of the package in cm
        mass (float): Mass of the package in kg
        
    Returns:
        str: The appropriate stack name - 'STANDARD', 'SPECIAL', or 'REJECTED'
    """
    # Calculate package volume
    volume = width * height * length
    
    # Determine if package is bulky
    is_bulky = False
    if volume >= 1000000:
        is_bulky = True
    if width >= 150 or height >= 150 or length >= 150:
        is_bulky = True
    
    # Determine if package is heavy
    is_heavy = False
    if mass >= 20:
        is_heavy = True
        
    # Sort package based on conditions
    if is_bulky and is_heavy:
        return "REJECTED"
    if is_bulky or is_heavy:
        return "SPECIAL"
    
    # Default case: neither bulky nor heavy
    return "STANDARD"


def test_sort():
    # Standard cases
    assert sort(50, 50, 50, 10) == "STANDARD"  # Small and light

    # Special cases (bulky only)
    assert sort(150, 50, 50, 10) == "SPECIAL"  # One dimension ≥ 150
    assert sort(100, 100, 100, 10) == "SPECIAL"  # Volume = 1,000,000
    
    # Special cases (heavy only)
    assert sort(50, 50, 50, 20) == "SPECIAL"  # Heavy but not bulky
    
    # Rejected cases
    assert sort(150, 50, 50, 20) == "REJECTED"  # Both bulky and heavy
    assert sort(100, 100, 100, 20) == "REJECTED"  # Both bulky and heavy
    
    # Edge cases
    assert sort(149, 149, 45, 19) == "STANDARD"  # Just under all thresholds
    assert sort(0, 0, 0, 0) == "STANDARD"  # Zero values

    print("All tests passed!")

# Run tests
test_sort()