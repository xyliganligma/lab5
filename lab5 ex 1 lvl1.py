import math
def combinations(n, k):
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))
n1, k1 = 8, 5
n2, k2 = 10, 5
n3, k3 = 11, 5
ways1 = combinations(n1, k1)
ways2 = combinations(n2, k2)
ways3 = combinations(n3, k3)
print(f"Ways to select 5 people from 8 candidates: {ways1}")
print(f"Ways to select 5 people from 10 candidates: {ways2}")
print(f"Ways to select 5 people from 11 candidates: {ways3}")