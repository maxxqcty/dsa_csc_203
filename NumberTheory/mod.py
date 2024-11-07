class Modulars:
    def __init__(self, mod):
        self.mod = mod

    def modular_addition(self, a, b):
        return (a + b) % self.mod

    def modular_subtraction(self, a, b):
        return (a - b + self.mod) % self.mod

    def modular_multiplication(self, a, b):
        return (a * b) % self.mod

    def modular_exponential(self, a, b):
        result = 1
        a = a % self.mod
        while b > 0:
            if b % 2 == 1:
                result = (result * a) % self.mod
            b = b // 2
            a = (a * a) % self.mod
        return result

    def modular_congruence(self, a, b):
        if (a - b) % self.mod == 0:
            print(f"{a} is congruent to {b} mod {self.mod}")
        else:
            print(f"{a} is not congruent to {b} mod {self.mod}")

    def evaluate_expression(self, expression):
        tokens = self.tokenize(expression)
        postfix = self.infix_to_postfix(tokens)
        return self.evaluate_postfix(postfix)

    def tokenize(self, expression):
        tokens = []
        token = ""
        for ch in expression:
            if ch.isdigit():
                token += ch
            else:
                if token:
                    tokens.append(token)
                    token = ""
                if ch != ' ':
                    tokens.append(ch)
        if token:
            tokens.append(token)
        return tokens

    def infix_to_postfix(self, tokens):
        ops = []
        output = []

        for token in tokens:
            if token.isdigit():
                output.append(token)
            elif token == "(":
                ops.append(token)
            elif token == ")":
                while ops and ops[-1] != "(":
                    output.append(ops.pop())
                ops.pop()
            else:
                while ops and self.precedence(ops[-1]) >= self.precedence(token):
                    output.append(ops.pop())
                ops.append(token)

        while ops:
            output.append(ops.pop())

        return output

    def evaluate_postfix(self, postfix):
        values = []

        for token in postfix:
            if token.isdigit():
                values.append(int(token))
            else:
                b = values.pop()
                a = values.pop()
                result = self.perform_operation(a, b, token)
                values.append(result)

        return values[0]

    def perform_operation(self, a, b, op):
        if op == "+":
            return self.modular_addition(a, b)
        elif op == "-":
            return self.modular_subtraction(a, b)
        elif op == "*":
            return self.modular_multiplication(a, b)
        elif op == "^":
            return self.modular_exponential(a, b)
        return 0

    def precedence(self, op):
        if op == "^":
            return 3
        if op in ["*", "/"]:
            return 2
        if op in ["+", "-"]:
            return 1
        return 0

    def decision(self):
        print("\n\n| ======= MODULAR ARITHMETIC ======= |\n\n")
        expression = ""
        decision = ''
        run = True

        while run:
            print("\nChoices: \n")
            print("A.) Modular Addition (e.g., '5 + 3')")
            print("B.) Modular Subtraction (e.g., '5 - 3')")
            print("C.) Modular Multiplication (e.g., '5 * 3')")
            print("D.) Modular Exponentiation (e.g., '5 ^ 3')")
            print("E.) Modular Congruence")
            print("F.) Evaluate Expression (e.g., '(5 + 3) * 2 - (2 ^ 2)')")
            print("Q) Quit")
            decision = input("Your choice: ").strip().upper()

            if decision in ['A', 'B', 'C', 'D', 'F']:
                expression = input("\nEnter the expression you wish to calculate: ")
                result = self.evaluate_expression(expression)
                print(f"\nResult: {result} mod {self.mod} = {result % self.mod}\n")
            elif decision == 'E':
                a = int(input("Enter first number: "))
                b = int(input("Enter second number: "))
                self.modular_congruence(a, b)
            elif decision == 'Q':
                print("Exiting...")
                run = False
            else:
                print("\n\n|| ===== INVALID ====== ||\n\n")

# Usage

def mod_run():
    mod = int(input("Enter the modulus (mod): "))
    modulars = Modulars(mod)
    modulars.decision()

if __name__ == "__main__":
    mod_run()
# -----------------------------------------------------------
# OUTPUT :
# Enter the modulus (mod): 5


# | ======= MODULAR ARITHMETIC ======= |



# Choices: 

# A.) Modular Addition (e.g., '5 + 3')
# B.) Modular Subtraction (e.g., '5 - 3')
# C.) Modular Multiplication (e.g., '5 * 3')
# D.) Modular Exponentiation (e.g., '5 ^ 3')
# E.) Modular Congruence
# F.) Evaluate Expression (e.g., '(5 + 3) * 2 - (2 ^ 2)')
# Q) Quit
# Your choice: F

# Enter the expression you wish to calculate: (2 + 3) ^ 3 + 4 - 1 /3

# Result: 4 mod 5 = 4

