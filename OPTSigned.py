def twos_comp_to_int(bin_str):
    """
    Convert a two's-complement binary string to a signed integer.
    """
    width = len(bin_str)
    val = int(bin_str, 2)
    if bin_str[0] == '1':  # negative
        val -= (1 << width)
    return val

def int_to_twos_comp(val, width):
    """
    Convert an integer to a two's-complement binary string of given width.
    """
    if val < 0:
        val = (1 << width) + val
    return format(val & ((1 << width) - 1), f'0{width}b')
def signed_step(Multiplicand, Product, N, M):
    """
    Perform one step of signed shift-add multiplication:
    - Adds multiplicand to top N bits if LSB is 1
    - Then does an arithmetic right shift, replicating multiplicand's sign bit
    """
    upper = Product[:N]
    lower = Product[N:]

    # Step 1a: If LSB == 1, add multiplicand to upper bits (signed)
    if lower[-1] == '1':
        acc = twos_comp_to_int(upper)
        mval = twos_comp_to_int(Multiplicand)
        acc += mval
        upper = int_to_twos_comp(acc, N)

    # Step 1b: Arithmetic shift right using multiplicand's sign bit
    full = upper + lower
    sign_bit = Multiplicand[0]
    shifted = sign_bit + full[:-1]

    return shifted
def run_signed_mult(multiplicand, multiplier):
    N = len(multiplicand)
    M = len(multiplier)
    Product = '0' * N + multiplier

    print(f"Initial State:")
    print(f"  Multiplicand: {multiplicand} (dec {twos_comp_to_int(multiplicand)})")
    print(f"  Multiplier:   {multiplier}   (dec {twos_comp_to_int(multiplier)})")
    print(f"  Product:      {Product}      (dec {twos_comp_to_int(Product)})\n")

    for i in range(1, M + 1):
        print(f"Step {i}:")
        print(f"  Multiplicand: {multiplicand}")
        print(f"  Multiplier:   {Product[N:]}")
        print(f"  Product:      {Product} (before)")

        Product = signed_step(multiplicand, Product, N, M)

        print(f"  Product:      {Product} (after)  (dec {twos_comp_to_int(Product)})")
        print('-' * 40)

    return Product
def main():
    multiplicand = input("Enter the signed multiplicand (binary): ").strip()
    multiplier = input("Enter the signed multiplier   (binary): ").strip()

    N = len(multiplicand)
    M = len(multiplier)

    final_product = run_signed_mult(multiplicand, multiplier)

    print(f"\nFinal {N+M}-bit Product: {final_product}")
    print(f"Decimal Value: {twos_comp_to_int(final_product)}")
if __name__ == "__main__":
    main()
