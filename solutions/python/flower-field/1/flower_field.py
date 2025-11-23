def annotate(garden):
    if not garden:
        return []

    rows = len(garden)
    cols = len(garden[0])

    # Validate the board
    for row in garden:
        if len(row) != cols:
            raise ValueError("The board is invalid with current input.")
        if not all(c in ('*', ' ') for c in row):
            raise ValueError("The board is invalid with current input.")

    # Directions: 8 adjacent cells
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),          (0, 1),
        (1, -1),  (1, 0), (1, 1)
    ]

    result = []

    for r in range(rows):
        new_row = ""
        for c in range(cols):
            if garden[r][c] == '*':
                new_row += '*'
            else:
                count = 0
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and garden[nr][nc] == '*':
                        count += 1
                new_row += str(count) if count > 0 else ' '
        result.append(new_row)

    return result
