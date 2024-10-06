#!/usr/bin/python3
"""
0. Pascal's Triangle
"""
def pascal_triangle(n):
    """
    Returns a list of lists representing the first N rows of Pascal's Triangle.
    """
    
    if n <= 0:
        return []
    
    triangle = []
        
    for i in range(n):
        row = [1]  # Every row starts with 1
        if i > 0:
            last_row = triangle[i - 1]
            row.extend([sum(pair) for pair in zip(last_row, last_row[1:])])
            row.append(1)  # Only append 1 if it's not the first row
        triangle.append(row)
    
    return triangle