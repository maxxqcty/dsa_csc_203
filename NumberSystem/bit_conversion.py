def char_to_digit(ch):
    if '0' <= ch <= '9':
        return ord(ch) - ord('0')
    elif 'A' <= ch <= 'F':
        return ord(ch) - ord('A') + 10
    elif 'a' <= ch <= 'f':
        return ord(ch) - ord('a') + 10
    return 0

def string_to_decimal(num, base):
    decimal = 0.0
    point_pos = num.find('.')

    i = (len(num) - 1) if point_pos == -1 else point_pos - 1
    multiplier = 1
    while i >= 0:
        decimal += char_to_digit(num[i]) * multiplier
        multiplier *= base
        i -= 1

    if point_pos != -1:
        frac_multiplier = 1.0 / base
        for i in range(point_pos + 1, len(num)):
            decimal += char_to_digit(num[i]) * frac_multiplier
            frac_multiplier /= base

    return decimal

def decimal_to_base(dec, base):
    int_part = int(dec)
    frac_part = dec - int_part
    result = ""

    if int_part == 0:
        result = "0"
    else:
        result = print_integer_part(int_part, base)

    if frac_part > 0:
        result += "."
        result += print_fractional_part(frac_part, base)

    return result

def print_integer_part(int_part, base):
    result = ""
    while int_part > 0:
        remainder = int_part % base
        if remainder < 10:
            result = str(remainder) + result
        else:
            result = chr(ord('A') + (remainder - 10)) + result
        int_part //= base
    return result

def print_fractional_part(frac_part, base):
    result = ""
    precision = 10
    while frac_part > 0 and precision > 0:
        frac_part *= base
        frac_int = int(frac_part)
        if frac_int < 10:
            result += str(frac_int)
        else:
            result += chr(ord('A') + (frac_int - 10))
        frac_part -= frac_int
        precision -= 1
    return result

def convert_to_decimal(num, base):
    if base == 1:
        return string_to_decimal(num, 2)
    elif base == 2:
        return float(num)
    elif base == 3:
        return string_to_decimal(num, 8)
    elif base == 4:
        return string_to_decimal(num, 16)
    else:
        raise ValueError("Invalid choice.")

def convert_from_decimal(num, base):
    if base == 1:
        return decimal_to_base(num, 2)
    elif base == 2:
        return str(num)
    elif base == 3:
        return decimal_to_base(num, 8)
    elif base == 4:
        return decimal_to_base(num, 16)
    else:
        raise ValueError("Invalid choice.")

def main_conversions():
    from_base = int(input("Convert From: \n1. Binary\n2. Decimal\n3. Octal\n4. Hexadecimal\n\nEnter Choice: "))
    to_base = int(input("Convert To\n1. Binary\n2. Decimal\n3. Octal\n4. Hexadecimal\n\nEnter Choice: "))
    
    if from_base == 1:
        binary_inp = input("\nEnter Binary: ")
        if to_base == 2:
            print(convert_to_decimal(binary_inp, 1))
        elif to_base == 3:
            print(convert_from_decimal(convert_to_decimal(binary_inp, 1), 3))
        elif to_base == 4:
            print(convert_from_decimal(convert_to_decimal(binary_inp, 1), 4))

    elif from_base == 2:
        dec_inp = input("\nEnter Decimal: ")
        if to_base == 1:
            print(decimal_to_base(float(dec_inp), 2))
        elif to_base == 3:
            print(decimal_to_base(float(dec_inp), 8))
        elif to_base == 4:
            print(decimal_to_base(float(dec_inp), 16))

    elif from_base == 3:
        octal_inp = input("\nEnter Octal: ")
        if to_base == 1:
            print(decimal_to_base(string_to_decimal(octal_inp, 8), 2))
        elif to_base == 2:
            print(string_to_decimal(octal_inp, 8))
        elif to_base == 4:
            print(decimal_to_base(string_to_decimal(octal_inp, 8), 16))

    elif from_base == 4:
        hex_inp = input("\nEnter Hexadecimal: ")
        if to_base == 1:
            print(decimal_to_base(string_to_decimal(hex_inp, 16), 2))
        elif to_base == 2:
            print(string_to_decimal(hex_inp, 16))
        elif to_base == 3:
            print(decimal_to_base(string_to_decimal(hex_inp, 16), 8))

if __name__ == "__main__":
    main_conversions()

# -----------------------------------------------------------
# OUTPUT :

# Convert From:
# 1. Binary
# 2. Decimal
# 3. Octal
# 4. Hexadecimal

# Enter Choice: 1
# Convert To
# 1. Binary
# 2. Decimal
# 3. Octal
# 4. Hexadecimal

# Enter Choice: 3

# Enter Binary: 10111111.11011
# Result: 277.66

