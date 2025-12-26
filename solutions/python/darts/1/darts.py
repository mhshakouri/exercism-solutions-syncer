def score(x, y):
    # Calculate distance from center (0, 0)
    distance = (x**2 + y**2)**0.5
    
    # Determine score based on distance
    if distance <= 1:
        return 10
    elif distance <= 5:
        return 5
    elif distance <= 10:
        return 1
    else:
        return 0