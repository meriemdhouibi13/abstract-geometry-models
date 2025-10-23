def hamming_distance(x, y):
    """Calculates the Hamming distance between two 7-tuples x and y."""
    return sum(el1 != el2 for el1, el2 in zip(x, y))

# Verification of distance function properties
# Let D be the Hamming distance function
# Let X be the set of 7-tuples with coordinates 0 or 1

# 1. Non-negativity: D(x, y) >= 0
#    Hamming distance is non-negative since it counts differences.

# 2. Identity of indiscernibles: D(x, y) = 0 if and only if x = y
#    D(x, y) = 0 only when all corresponding coordinates are equal.

# 3. Symmetry: D(x, y) = D(y, x)
#    Hamming distance is symmetric since differences are counted in both directions.

# 4. Triangle inequality: D(x, z) <= D(x, y) + D(y, z)
#    For any x, y, z in X, this holds true for Hamming distance.

# Example usage:
if __name__ == '__main__':
    x = (0, 1, 0, 1, 0, 1, 0)
    y = (1, 0, 1, 0, 1, 0, 1)
    z = (0, 0, 0, 0, 0, 0, 0)
    print("D(x, y):", hamming_distance(x, y))  # Example distance
    print("D(x, z):", hamming_distance(x, z))
    print("D(y, z):", hamming_distance(y, z))
    
