def diffie_hellman(p, g, a, b):
    A = pow(g, a, p)
    B = pow(g, b, p)
    shared_key_a = pow(B, a, p)
    shared_key_b = pow(A, b, p)
    return shared_key_a, shared_key_b

# Example usage:
p = int(input("Enter the value of p: "))
g = int(input("Enter the value of g: "))
a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

shared_key_a, shared_key_b = diffie_hellman(p, g, a, b)
print(f"Shared Key A: {shared_key_a}")
print(f"Shared Key B: {shared_key_b}")
