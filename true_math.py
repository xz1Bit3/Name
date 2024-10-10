import fake_math

def true_divide(first, second):
    if second == 0:
        return 'inf'
    return first / second
result3 = true_divide(49, 7)
result4 = true_divide(15, 0)
print(result3)
print(result4)