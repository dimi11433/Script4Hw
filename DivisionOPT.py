def division( Divisor, Remainder, divisor_len,remain_len, Helper):
   
    divisor = int(Divisor, 2)
    remainder = int(Remainder, 2)
    help_please = int(Helper, 2)
    print(remainder)
    remainder  <<= 1
    print(remainder)
    remainder = remainder - help_please
    
    
    print(remainder)
    #print(remainder)
    if remainder < 0:
        remainder = remainder + help_please
        q0 = '0'
        
    else:
        q0 = '1'
    #print(divisor)
    #print( divisor, remainder, quotient)  
    
  
    Divisor = format(divisor, f'0{divisor_len}b')[-divisor_len:]
    Remainder = format(remainder, f'0{remain_len}b')[-remain_len:]
    Remainder = Remainder[1:] + q0
    
    print( Divisor, Remainder)
 
    return  Divisor, Remainder


def main():
    Dividen = input("Please input the Dividen: ")
    Divisor = input("Please input the Divisor: ")
    no_steps = int(input("Please input the number of Steps: "))
    
    
    dividen_len = len(Dividen)
    divisor_len = len(Divisor)
   
    
    Helper = Divisor + "0" * divisor_len
    Remainder = "0" * dividen_len + Dividen
    divisor_len = len(Divisor)
    remain_len = len(Remainder)
    #divisor_len = len(Divisor)
    
    result = division(Divisor, Remainder, divisor_len, remain_len, Helper)
    for iterations in range(no_steps - 1):
        result = division(result[0], result[1], divisor_len, remain_len, Helper)
    

if __name__ == "__main__":
    main()