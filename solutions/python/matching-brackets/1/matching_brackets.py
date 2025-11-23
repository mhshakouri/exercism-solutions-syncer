def is_paired(input_string):
    stack = []
    bracket_map = {'(': ')', '[': ']', '{': '}'}
    
    for char in input_string:
        if char in bracket_map:
            # Opening bracket
            stack.append(char)
        elif char in bracket_map.values():
            # Closing bracket
            if not stack:
                return False
            opening = stack.pop()
            if bracket_map[opening] != char:
                return False
    
    return len(stack) == 0