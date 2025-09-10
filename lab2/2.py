a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Sum:", a + b)
print("Diff", a - b)
print("Product", a * b)
print("Division:", a / b if b != 0 else "Cannot divide by zero")
print("Remainder:", a % b if b != 0 else "No remainder (division by zero)")