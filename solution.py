import numpy as np
def count_occurrences(array):
    unique_values, counts = np.unique(array, return_counts=True)
    return unique_values, counts