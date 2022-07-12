# Solve the problem from the third set here
#problem 2 (13)
def prime_div (u): #this function count the different prime divisors for a number
    x=u
    k=int(0)
    if(x==1):
        return 1
    for i in range(2,x+1):
         if(x%i==0):
             k=k+1
             while(x%i==0):
                 x=x//i
    return k


def rezult(n,l):
        j=int(1)
        while j:
            if(n-prime_div(j)<=0): #if the n - the number of different prime divisors
                p=j               #is 0 or lower that means that position n is a part of the
                for r in range(2,p+1): # prime divisors for that number so we do the decomposition
                    if(p%r==0):        #into prime factors for that number to find our position exactly
                        l.append(r)
                        while(p%r==0):
                            p=p//r

                print(l[n-1]) #we print l[n-1] bcs it beggins w poz 0
                break
            else:
                p=int(prime_div(j))
                n=n-p
            j=j+1

def function():
    l=[]
    n=int(input())
    if n==1:
        print(1)
    else:
        rezult(n,l)
function()