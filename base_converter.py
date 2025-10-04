# Constants for defining the range and mapping
DIGITS = "0123456789ABCDEF"
MIN_BASE = 2
MAX_BASE = 16

def get_digit_value(char):
    """
    Returns the numerical value (0-15) of a single character digit (0-9, A-F).
    Returns -1 if the character is not a valid digit.
    """
    try:
        return DIGITS.index(char)
    except ValueError:
        return -1

def str_to_base10(number_str, base_in):
    """
    Step 1: Converts a number string from base_in to a Base 10 integer value.
    Uses the Polynomial Method: Value = sum(digit * base^position)
    """
    decimal_value = 0
    power = 0
    
    # Iterate through the number string from right to left (least significant digit first)
    for i in range(len(number_str) - 1, -1, -1):
        char = number_str[i]
        digit_value = get_digit_value(char)
        
        # 1. Validate the digit against the input base
        if digit_value == -1 or digit_value >= base_in:
            # -1 means the character is not a valid base digit (e.g., 'G')
            # digit_value >= base_in means the digit is too large for the base (e.g., '2' in Base 2)
            return None, f"Error: '{char}' is not a valid digit for Base {base_in}."

        # 2. Calculate the decimal contribution: digit_value * base^power 
        # Manually calculate base^power (since ** is allowed, but will use a loop)
        power_of_base = 1
        for _ in range(power):
            power_of_base *= base_in
            
        decimal_value += digit_value * power_of_base
        power += 1
        
    return decimal_value, None # Return the integer value and no error

def base10_to_str(decimal_num, base_out):
    """
    Step 2: Converts a Base 10 integer to a number string in the target base_out.
    Uses the Repeated Division and Remainder Method.
    """
    if decimal_num == 0:
        return "0"

    result = ""
    
    # The loop continues as long as the quotient (decimal_num) is greater than 0
    while decimal_num > 0:
        # 1. Calculate the remainder (the next digit)
        remainder = decimal_num % base_out
        
        # 2. Map the remainder value (0-15) to its character (0-F)
        digit_char = DIGITS[remainder]
        
        # 3. Prepend the digit to the result string (since we find LSB first)
        result = digit_char + result
        
        # 4. Update the number to the new quotient (integer division)
        decimal_num //= base_out
        
    return result

def safe_int_input(prompt):
    """Safely reads input and attempts to convert it to an integer."""
    try:
        return int(input(prompt).strip()), None
    except ValueError:
        return None, "Invalid input. Please enter a whole number."

def main():
    """Main function to handle user interface and coordinate conversion."""
    print("-" * 40)
    print("Manual Numerical Base Converter (Base 2 to 16)")
    print("-" * 40)

    while True:  # Repeatable UI for multiple conversions
        # --- 1. Get Input Number String ---
        while True:
            original_number_str = input("Enter the number to convert: ").strip().upper()

            if original_number_str == "":
                print("Error: please enter a non-empty number.\n")
                continue

            if original_number_str.startswith('-'):
                print("Error: only positive integers are allowed.\n")
                continue

            if '.' in original_number_str:
                print("Error: only integer values are allowed.\n")
                continue

            # Validate that all characters are valid hex digits (max base 16)
            if any(get_digit_value(c) == -1 for c in original_number_str):
                print("Error: invalid character(s) detected in number.\n")
                continue

            break  # input is valid

        # --- 2. Get Input Base and Validate ---
        while True:
            base_in, error = safe_int_input(f"Enter the original base ({MIN_BASE}-{MAX_BASE}): ")
            if error:
                print(error)
                continue
            if not (MIN_BASE <= base_in <= MAX_BASE):
                print(f"Error: Original base must be between {MIN_BASE} and {MAX_BASE}.")
                continue
            break

        # --- 3. Get Target Base and Validate ---
        while True:
            base_out, error = safe_int_input(f"Enter the target base ({MIN_BASE}-{MAX_BASE}): ")
            if error:
                print(error)
                continue
            if not (MIN_BASE <= base_out <= MAX_BASE):
                print(f"Error: Target base must be between {MIN_BASE} and {MAX_BASE}.")
                continue
            break

        # --- 4. Conversion Step 1: B_in to Decimal (Base 10) ---
        decimal_value, error = str_to_base10(original_number_str, base_in)
        if error:
            print(error)
            continue

        # --- 5. Conversion Step 2: Decimal (Base 10) to Target Base ---
        converted_number_str = base10_to_str(decimal_value, base_out)

        # --- 6. Output Result ---
        print("\n" + "=" * 40)
        print(f"Original Number: {original_number_str} (Base {base_in})")
        print(f"Converted Number: {converted_number_str} (Base {base_out})")
        print("=" * 40)

        # --- 7. Ask user if they want to continue ---
        again = input("\nConvert another number? (y/n): ").strip().lower()
        if again != "y":
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
