
def sum(a,b): 
    gr = a+b
    return gr

def sub(a,b): 
    gr = a-b
    return gr 

def mul(a,b): 
    gr = a*b
    return gr 

def div(a,b): 
    gr = a/b
    return gr 
 

a =  int (input (" enter the value of a:" ) )
b =  int(input ( "enter the value of b: ") )


a1 = sum(a,b) 

print ("addition is", a1)


b1= sub(a,b) 

print ("substraction is", b1)


c1 = mul(a,b) 

 
print ("mulplication is", c1)


d1= div(a,b) 

print ("division", d1)

