""""Implement a function that accepts 3 integer values a, b, c. The function should return true if a triangle can be built
...with the sides of given length and false in any other case.

(In this case, all triangles must have surface greater than 0 to be accepted)."""

def is_triangle(a, b, c):
    """Determine if three sides of given lengths can form a triangle.

            Args:
                a (int): First side length
                b (int): Second side length
                c (int): Third side lenght

            Returns:
                bool: True if the three sides given can form a triangle.
        """
    return a + b > c and b + c > a and a + c > b