
import numpy as np

grades = {"alice": 15, "bob": 12, "Clara": 18, "David": 14}

for name, grade in grades.items():
    print(f"{name} -> {grade}")

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

n = int(input("Enter a number to compute its factorial: "))
print(f"Factorial of {n} is {factorial(n)}")

t1 = np.linspace(0, 1, 100)
print("First 10 values of t1:", t1[:10])

t2 = np.arange(0, 1 + 0.01, 0.01)
print("Length of t2:", len(t2))
print("Last value of t2:", t2[-1])

t = np.linspace(0, 1, 11)
result = (t * 2 + 3) ** 2
print("Result of operations on t:", result)
