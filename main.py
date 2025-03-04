def int_to_roman(num):
    """
    Convert an integer to a Roman numeral.

    :param num: Integer value between 1 and 3999 inclusive.
    :return: A string representing the Roman numeral of the integer.
    """
        l=num//1000
    yuzler=num%1000

    
    print (l*"M",end='')
    

    k=yuzler//100
    u=k%5
    
    
    
    
    if k==9:
        print("CM",end='')
    elif k==8:
        print("DCCC",end='')
    elif k==7:
        print("DCC",end='')
    elif k==6:
        print("DC",end='')
    elif k==5:
        print("D",end='')
    elif k==4:
        print("CD",end='')

    else:
        print(u*'C',end='')

    onlar=yuzler%100

    e=onlar//10
    z=e%5
    if e==9:
        print("XC",end='')
    elif e==8:
        print("LXXX",end='')
    elif e==7:
        print("LXX",end='')
    elif e==6:
        print("LX",end='')
    elif e==5:
        print("L",end='')
    elif e==4:
        print("XL",end='')

    else:
        print(z*'X',end='')
    


    birler=onlar%10

    y=birler
    p=y%5
    if y==9:
        print("IX",end='')
    elif y==8:
        print("VIII",end='')
    elif y==7:
        print("VII",end='')
    elif y==6:
        print("VI",end='')
    elif y==5:
        print("V",end='')
    elif y==4:
        print("IV",end='')

    else:
        print(p*'I',end='')
    

    print()
    
    
