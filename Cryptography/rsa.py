def run_rsa():
    # Step 0: Take user inputs for p, q, e, and plaintext
    p = int(input("Enter a prime number p: "))
    q = int(input("Enter a prime number q: "))
    e = int(input("Enter a public key exponent e (must be coprime with φ(n)): "))
    plaintext = int(input("Enter the plaintext (an integer less than n): "))

    # Step 1: Calculate n and φ(n)
    n = p * q
    phi_n = (p - 1) * (q - 1)
    print(f"\nStep 1: Calculate n and φ(n)")
    print(f"n = p * q = {p} * {q} = {n}")
    print(f"φ(n) = (p - 1) * (q - 1) = ({p} - 1) * ({q} - 1) = {phi_n}")

    # Step 2: Find D using the formula (phi_n * i + 1) / e until D is an integer
    D = None
    attempts = []
    for i in range(1, 100):  # Try values of i up to 100
        potential_d = (phi_n * i + 1) / e
        attempts.append((i, round(potential_d, 2)))  # Store with 2 decimal places
        if potential_d == int(potential_d):  # Check if it is an integer
            D = int(potential_d)
            break

    # Display the step-by-step process of finding D
    print("\nStep 2: Finding D with each i value:")
    for attempt in attempts:
        i_val, d_val = attempt
        print(f"i = {i_val}, D = (φ(n) * i + 1) / e = ({phi_n} * {i_val} + 1) / {e} = {d_val}")
    print(f"\nFound D = {D} when i = {i}\n")

    # Step 3: Encrypt the plaintext
    ciphertext = pow(plaintext, e, n)  # Calculate (plaintext^e) % n
    print(f"Step 3: Encrypting the plaintext")
    print(f"Ciphertext = plaintext^e mod n = {plaintext}^{e} mod {n} = {ciphertext}")

    # Step 4: Decrypt the ciphertext
    decrypted_text = pow(ciphertext, D, n)  # Calculate (ciphertext^D) % n
    print(f"\nStep 4: Decrypting the ciphertext")
    print(f"Recovered plaintext = ciphertext^D mod n = {ciphertext}^{D} mod {n} = {decrypted_text}")

    return {
        "n": n,
        "phi_n": phi_n,
        "public_key": (e, n),
        "private_key": (D, n),
        "ciphertext": ciphertext,
        "decrypted_text": decrypted_text
    }

# Run the RSA encryption and decryption process with user inputs


if __name__ == "__main__":
   run_rsa()


# -----------------------------------------------------------
# OUTPUT :
# Enter a prime number p: 13
# Enter a prime number q: 17
# Enter a public key exponent e (must be coprime with φ(n)): 19
# Enter the plaintext (an integer less than n): 12

# Step 1: Calculate n and φ(n)
# n = p * q = 13 * 17 = 221
# φ(n) = (p - 1) * (q - 1) = (13 - 1) * (17 - 1) = 192

# Step 2: Finding D with each i value:
# i = 1, D = (φ(n) * i + 1) / e = (192 * 1 + 1) / 19 = 10.16
# i = 2, D = (φ(n) * i + 1) / e = (192 * 2 + 1) / 19 = 20.26
# i = 3, D = (φ(n) * i + 1) / e = (192 * 3 + 1) / 19 = 30.37
# i = 4, D = (φ(n) * i + 1) / e = (192 * 4 + 1) / 19 = 40.47
# i = 5, D = (φ(n) * i + 1) / e = (192 * 5 + 1) / 19 = 50.58
# i = 6, D = (φ(n) * i + 1) / e = (192 * 6 + 1) / 19 = 60.68
# i = 7, D = (φ(n) * i + 1) / e = (192 * 7 + 1) / 19 = 70.79
# i = 8, D = (φ(n) * i + 1) / e = (192 * 8 + 1) / 19 = 80.89
# i = 9, D = (φ(n) * i + 1) / e = (192 * 9 + 1) / 19 = 91.0

# Found D = 91 when i = 9

# Step 3: Encrypting the plaintext
# Ciphertext = plaintext^e mod n = 12^19 mod 221 = 181

# Step 4: Decrypting the ciphertext
# Recovered plaintext = ciphertext^D mod n = 181^91 mod 221 = 12

