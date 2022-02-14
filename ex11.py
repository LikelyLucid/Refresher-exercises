"""
Write a function that calculates overdue fines for books at a library.
"""
base_fine = 0.5
per_day_fine = 0.8
max_fine = 30

def calc_fine(days_late):
    fine = base_fine
    if days_late > 0:
        fine = fine + (per_day_fine * days_late)
        if fine > max_fine:
            fine = max_fine
    return fine

