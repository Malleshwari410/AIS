# Addition of two values

def add(a,b):
    c=a+b
    return(c)
add(1,3)
    
******************************************************************************** 

#create User define fun star(3)
def star(a):
    for i in range(0,a):
        for j in range(0,i+1):
            print("* ",end=" ")
        print("\r")
        
star(3)



******************************************************************************** 


# Multiplication of three values

def mult(a,b,c):
    d=a*b*c
    return(d)
mult(2,3,4)



******************************************************************************** 


# power fuction eg. 2 raised to 3, 5raised to 4, base raised to power

def power(a):
    b=a*a*a
    return(b)
power(3)
    





# n raised to 4

def power(a):
    b=a*a*a*a
    return(b)
power(3)




def power(a):
    if a!=a:
        b=a*a
        return(b)
power(3)


******************************************************************************** 


# variance of 5 values

import statistics as s
a=[]
for i in range(10,15):
    a.append(i)
var=(s.variance(a))
print("The variance of above the numbers are :",var)

******************************************************************************** 



# variance of given numbers

import statistics as s
a=[1,2455,65,45,12,5]
print(s.variance(a))

******************************************************************************** 


#cube of any value

def cube(num):
    result=num*3
    return result

******************************************************************************** 


# factorial

def fact(n):
    if n==0 | n==1:
        return 1
    else:
        return(n* fact(n-1))
    print(fact(n))
fact(3)
    


******************************************************************************** 



# addition of even number

def even_add(number):
    a=0
    for i in number:
        if i % 2 ==0:
           a=a+i
    return a
number=[1,2,3,4,5,6,7,8,9,1,2,3,4,5,6]
even_add(number)
            


******************************************************************************** 



#print name

def name():
    for i in range(1,36):
        print(i,"Sumit")
name()


******************************************************************************** 



#list of specific range
def create_list(a,b):
    i=1
    c=[]
    for i in range(a,b):
        c.append(i)
        i+i+1
    print(c)
create_list(20,56)

******************************************************************************** 

