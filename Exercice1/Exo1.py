
a = 10
b = 5

print("Sum:", a + b)
print("Difference:", a - b)
print("Product:", a * b)
print("Quotient:", a / b)

text = "I love signal processing!"
print("Length:", len(text))
print("First 5 characters:", text[:5])
print("Reversed:", text[::-1])

numbers = [1, 2, 3, 4, 5]
numbers.append(6)
numbers[1] = 99  
print("Final list:", numbers)

num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")


print("Numbers 1 to 10:")
for i in range(1, 11):
    print(i, end=" ")


print("Even numbers from 1 to 20:")
for i in range(1, 21):
    if i % 2 == 0:
        print(i, end=" ")


def square(x):
    return x ** 2


grades = {"alice": 15, "bob": 12, "Clara": 18}
print("Clara's grade:", grades["Clara"])
grades["David"] = 14
print("Updated grades:", grades)
