def twos_comp_to_int(bin_str):
    """
    Convert a two's-complement binary string to a signed integer.
    """
    width = len(bin_str)
    val = int(bin_str, 2)
    if bin_str[0] == '1':
        val -= (1 << width)
    return val

def int_to_twos_comp(val, width):
    """
    Convert a signed integer to a two's-complement binary string of given width.
    """
    if val < 0:
        val = (1 << width) + val
    return format(val & ((1 << width) - 1), f'0{width}b')
def signed_step(Multiplier, Multiplicand, Product, mplier_len, mplcnd_len, prod_len):
    """
    Perform one signed multiplication step:
    - If LSB of multiplier is 1, add multiplicand to product
    - Arithmetic shift right on product
    - Left shift multiplicand
    - Right shift multiplier
    """
    # Convert to integers
    mplier = twos_comp_to_int(Multiplier)
    mplcnd = twos_comp_to_int(Multiplicand)
    prod = twos_comp_to_int(Product)

    # Step 1a: Add if LSB of multiplier is 1
    if mplier & 1 == 1:
        prod += mplcnd

    # Step 1b: Arithmetic right shift of product
    # prod_sign = (prod >> (prod_len - 1)) & 1
    # prod >>= 1
    # if prod_sign:
    #     prod |= (1 << (prod_len - 1))  # preserve sign bit

    # Step 1c: Arithmetic right shift of multiplier
    mplier_sign = (mplier >> (mplier_len - 1)) & 1
    mplier >>= 1
    if mplier_sign:
        mplier |= (1 << (mplier_len - 1))

    # Step 1d: Arithmetic left shift of multiplicand
    mplcnd <<= 1
    # Keep it in bounds
    mplcnd &= (1 << mplcnd_len) - 1

    # Format back to binary strings
    Multiplier = int_to_twos_comp(mplier, mplier_len)
    Multiplicand = int_to_twos_comp(mplcnd, mplcnd_len)
    Product = int_to_twos_comp(prod, prod_len)

    print(f"Multiplicand: {Multiplicand}, Multiplier: {Multiplier}, Product: {Product}")
    return Multiplier, Multiplicand, Product
def main():
    Product = "00000000"  # Will get updated to correct length

    Multiplicand = input("Please input the Multiplicand (binary): ").strip()
    Multiplier = input("Please input the Multiplier (binary): ").strip()
    number_of_loops = int(input("Please input how many iterations to run: "))

    mplier_len = len(Multiplier)
    initial_mplcnd_len = len(Multiplicand)
    prod_len = mplier_len + initial_mplcnd_len
    mplcnd_len = prod_len  # Extend multiplicand to match product width

    # Sign-extend the multiplicand
    sign_bit = Multiplicand[0]
    Multiplicand = sign_bit * (prod_len - initial_mplcnd_len) + Multiplicand

    # Zero-extend the product to the correct length
    Product = '0' * prod_len

    print(f"Initial Values:")
    print(f"Multiplicand: {Multiplicand}, Multiplier: {Multiplier}, Product: {Product}\n")

    # Perform iterations
    result = signed_step(Multiplier, Multiplicand, Product, mplier_len, mplcnd_len, prod_len)
    for step_count in range(1, number_of_loops):
        result = signed_step(result[0], result[1], result[2], mplier_len, mplcnd_len, prod_len)

    print(f"\nFinal Result =>")
    print(f"Multiplicand: {result[1]}")
    print(f"Multiplier:   {result[0]}")
    print(f"Product:      {result[2]}")
    print(f"Decimal Product: {twos_comp_to_int(result[2])}")
if __name__ == "__main__":
    main()
