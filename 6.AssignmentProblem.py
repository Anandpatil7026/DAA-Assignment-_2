import numpy as np
from scipy.optimize import linear_sum_assignment

def solve_assignment(cost_matrix):
    max_cost = np.max(cost_matrix)
    max_cost_matrix = max_cost - cost_matrix

    row_indices, col_indices = linear_sum_assignment(max_cost_matrix)

    
    total_cost = np.sum(cost_matrix[row_indices, col_indices])

    
    return row_indices, col_indices, total_cost

cost_matrix = np.array([[4, 2, 8], 
                        [3, 5, 6], 
                        [7, 1, 9]])
row_indices, col_indices, total_cost = solve_assignment(cost_matrix)

print("Assignment:")
for i in range(len(row_indices)):
    print("Task", row_indices[i], "-> Worker", col_indices[i])

print("Total Cost:", total_cost)
