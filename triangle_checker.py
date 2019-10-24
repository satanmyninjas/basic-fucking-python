def is_triangle(a, b, c):

    ordered_sides = [a, b, c]
    ordered_sides.sort()

    a = ordered_sides[0]
    b = ordered_sides[1]
    c = ordered_sides[2]

    if (a + b) > c:  # excludes possibility of degenerate triangles
        return True
    else:
        return False
        
