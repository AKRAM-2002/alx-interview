#!/usr/bin/python3
"""

"""
def pascal_triangle(n):
    list_of_lists = []
    if n <= 0:
        return list_of_lists
        
    for i in range(n):
        row = [1]  # Every row starts with 1
        if i > 0:
            last_row = list_of_lists[i - 1]
            row.extend([sum(pair) for pair in zip(last_row, last_row[1:])])
            row.append(1)  # Only append 1 if it's not the first row
        list_of_lists.append(row)
    
    return list_of_lists