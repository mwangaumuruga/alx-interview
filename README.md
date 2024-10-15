# alx-interview
Pascal's Triangle Algorithm

Pascal's Triangle is a triangular array where the numbers at the ends of each row are always 1, and each number inside the triangle is the sum of the two numbers directly above it. Here's an explanation of how Pascal's Triangle is built:

    Row 0 starts with 1.
    Row 1 has two 1s.
    For each subsequent row, the first and last number are 1, and each number in between is the sum of the two numbers directly above it in the previous row.
    
Algorithm for Pascal’s Triangle

The algorithm to generate Pascal's Triangle up to n rows is as follows:

    Start by initializing an empty list to store all the rows.
    For each row:
        The first and last values are always 1.
        The values in between are the sum of two adjacent values from the previous row.
    Continue building the rows until you reach the desired number of rows.
