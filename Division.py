    
def division( Divisor, Remainder, Quotient, divisor_len, quot_len):
    
    divisor = int(Divisor, 2)
    remainder = int(Remainder, 2)
    quotient = int(Quotient, 2)
    #print(remainder, divisor, quotient)
    remainder = remainder - divisor
    #print(remainder)
    if remainder < 0:
        remainder = remainder + divisor 
        quotient <<= 1
    else:
        quotient = (quotient << 1) | 1
    divisor >>= 1
    #print(divisor)
    #print( divisor, remainder, quotient)  
    
  
    Divisor = format(divisor, f'0{divisor_len}b')[-divisor_len:]
    Remainder = format(remainder, f'0{divisor_len}b')[-divisor_len:]
    Quotient = format(quotient, f'0{len(Quotient)}b')[-quot_len:]
    
    print( Divisor, Remainder, Quotient)
 
    return  Divisor, Remainder, Quotient  


def main():
    Dividen = input("Please input the Dividen: ")
    Divisor = input("Please input the Divisor: ")
    no_steps = int(input("Please input the number of Steps: "))
    
    
    dividen_len = len(Dividen)
    divisor_len = len(Divisor)
   
    Quotient = "0" * dividen_len
    Divisor = Divisor + "0" * divisor_len
    Remainder = "0" * dividen_len + Dividen
    quot_len = len(Quotient)
    divisor_len = len(Divisor)
    #divisor_len = len(Divisor)
    
    result = division(Divisor, Remainder, Quotient, divisor_len, quot_len)
    for iterations in range(no_steps - 1):
        result = division(result[0], result[1], result[2], divisor_len, quot_len)
    

if __name__ == "__main__":
    main()