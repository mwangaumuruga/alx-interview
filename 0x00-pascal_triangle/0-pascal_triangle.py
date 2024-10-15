#!/usr/bin/python3
def pascal_triangle(n):
    """Returns a list of lists of integers representing Pascal's triangle of n."""
    if n <= 0:
        return []

    # Initialize the triangle with the first row
    triangle = [[1]]

    # Generate rows 1 through n-1
    for i in range(1, n):
        row = [1]  # Start the row with a 1
        # Fill the middle values
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)  # End the row with a 1
        triangle.append(row)

    return triangle

