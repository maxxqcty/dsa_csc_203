# Diffie-Hellman key exchange with user input

def diffie_hellman(g, p, a, b):
    print(f"Given:")
    print(f"  Base (g) = {g}")
    print(f"  Prime modulus (p) = {p}")
    print(f"  Alice's private key (a) = {a}")
    print(f"  Bob's private key (b) = {b}")
    print("\nStep 1: Alice computes her public key:")
    A = pow(g, a, p)
    print(f"  A = g^a mod p = {g}^{a} mod {p} = {A}")

    print("\nStep 2: Bob computes his public key:")
    B = pow(g, b, p)
    print(f"  B = g^b mod p = {g}^{b} mod {p} = {B}")

    print("\nStep 3: Alice and Bob compute the shared key:")
    shared_key_alice = pow(B, a, p)
    shared_key_bob = pow(A, b, p)
    
    print(f"  Alice's shared key = B^a mod p = {B}^{a} mod {p} = {shared_key_alice}")
    print(f"  Bob's shared key = A^b mod p = {A}^{b} mod {p} = {shared_key_bob}")
    
    print(f"\nShared key (Both Alice and Bob have the same key): {shared_key_alice}")

# User input for the values
g = int(input("Enter the base (g): "))
p = int(input("Enter the prime modulus (p): "))
a = int(input("Enter Alice's private key (a): "))
b = int(input("Enter Bob's private key (b): "))

# Run the visualization
diffie_hellman(g, p, a, b)
# -----------------------------------------------------------

# # OUTPUT:

# # Enter the base (g): 5
# # Enter the prime modulus (p): 17
# # Enter Alice's private key (a): 4
# # Enter Bob's private key (b): 6
# # Given:
# #   Base (g) = 5
# #   Prime modulus (p) = 17
# #   Alice's private key (a) = 4
# #   Bob's private key (b) = 6

# # Step 1: Alice computes her public key:
# #   A = g^a mod p = 5^4 mod 17 = 13

# # Step 2: Bob computes his public key:
# #   B = g^b mod p = 5^6 mod 17 = 2

# # Step 3: Alice and Bob compute the shared key:
# #   Alice's shared key = B^a mod p = 2^4 mod 17 = 16
# #   Bob's shared key = A^b mod p = 13^6 mod 17 = 16

# # Shared key (Both Alice and Bob have the same key): 16

