
def unsigned_generalized(Multiplicand, Product, N, M):
    """
    One step of unsigned shift-add multiplication for arbitrary bit lengths.

    Product: (N + M)-bit binary string = [upper N bits] + [lower M bits]
    Multiplicand: N-bit binary string
    """
    upper = Product[:N]    # Accumulator (partial sum)
    lower = Product[N:]    # Current multiplier bits

    # Step 1a: Add multiplicand if LSB is 1
    if lower[-1] == '1':
        acc_val = int(upper, 2)
        m_val = int(Multiplicand, 2)
        new_acc = acc_val + m_val
        upper = format(new_acc % (1 << N), f'0{N}b')  # Wrap to N bits

    # Step 1b: Right shift entire product logically
    combined = upper + lower
    shifted = '0' + combined[:-1]

    return shifted
def run_unsigned_mult(multiplicand, multiplier):
    N = len(multiplicand)
    M = len(multiplier)
    Product = '0' * N + multiplier  # Initial product (N+M bits)

    print(f"Initial State:")
    print(f"  Multiplicand: {multiplicand} (dec {int(multiplicand, 2)})")
    print(f"  Multiplier:   {multiplier}   (dec {int(multiplier, 2)})")
    print(f"  Product:      {Product}      (dec {int(Product, 2)})\n")

    for step in range(1, M + 1):
        print(f"Step {step}:")
        print(f"  Multiplicand: {multiplicand}")
        print(f"  Multiplier:   {Product[N:]}")
        print(f"  Product:      {Product} (before)\n")

        Product = unsigned_generalized(multiplicand, Product, N, M)

        print(f"  Product:      {Product} (after)\n{'-'*40}")

    return Product
def main():
    multiplicand = input("Enter the multiplicand (binary): ").strip()
    multiplier   = input("Enter the multiplier   (binary): ").strip()

    # Pad to same lengths if needed
    N = len(multiplicand)
    M = len(multiplier)
    multiplicand = multiplicand.zfill(N)
    multiplier = multiplier.zfill(M)

    final_product = run_unsigned_mult(multiplicand, multiplier)

    print(f"\nFinal {N+M}-bit Product: {final_product}")
    print(f"Decimal Value: {int(final_product, 2)}")
if __name__ == "__main__":
    main()
