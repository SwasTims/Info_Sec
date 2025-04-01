def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

a = int(input("Enter the value for a: "))
b = int(input("Enter the value for b: "))
print(gcd(a, b))  # Output: 14
