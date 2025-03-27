import numpy


# Multiplicand = "00001010"
# Multiplier = "0011"
Product = "00000000"

#Lets create a script for the multiplication hardware shouldnt be too bad

def unsigned(Multiplier, Multiplicand, Product,mplier_len, mplcnd_len, prod_len ):
    
    mplier = int(Multiplier, 2)
    mplcnd = int(Multiplicand, 2)
    prod = int(Product, 2)
    
    
    
    if mplier & 1 == 1:
        prod = prod + mplcnd
    
    mplier >>= 1
    mplcnd <<= 1
    
    Multiplier = format(mplier, f'0{mplier_len}b')[-mplier_len:]
    Multiplicand = format(mplcnd, f'0{mplcnd_len}b')[-mplcnd_len:]
    Product = format(prod, f'0{prod_len}b')[-prod_len:]
    
    print(Multiplicand, Multiplier, Product)
    return Multiplier, Multiplicand, Product

def main():
    
    
    Multiplicand = input("Please input the Multiplicand: ")
    Multiplier = input("Please input the Multiplier: ")
    number_of_loops = int(input("Please input which step you would like to stop at: "))
    
    mplier_len = len(Multiplier)
    mplcnd_len = len(Multiplicand)
    prod_len = mplcnd_len + mplier_len
    mplcnd_len = prod_len
    
    result = unsigned(Multiplier, Multiplicand, Product, mplier_len, mplcnd_len, prod_len)
    for step_count in range(number_of_loops - 1):
        result = unsigned(result[0], result[1], result[2], mplier_len, mplcnd_len, prod_len)
    print(result[:3])
        
        

if __name__ == "__main__":
    main()
    