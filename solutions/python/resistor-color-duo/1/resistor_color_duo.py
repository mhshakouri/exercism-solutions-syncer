COLOR_MAP = [
    "black",
    "brown",
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "violet",
    "grey",
    "white",
]

def value(colors):
    if len(colors) < 2:
        raise ValueError("At least two colors are required")

    first, second = colors[0], colors[1]
    return COLOR_MAP.index(first) * 10 + COLOR_MAP.index(second)
