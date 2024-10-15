#!/usr/bin/python3
def pascals_triangle(n):
    # Initialize the triangle with the first row
    triangle = [[1]]
    
    # Generate rows 1 through n
    for i in range(1, n):
        # Start the row with a 1
        row = [1]
        # Calculate the middle elements
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        # End the row with a 1
        row.append(1)
        # Add the row to the triangle
        triangle.append(row)
    
    return triangle

# Example of generating Pascal's Triangle with 5 rows
n = 5
triangle = pascals_triangle(n)

# Print the triangle
for row in triangle:
    print(row)
