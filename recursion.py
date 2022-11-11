# Prime Factorization
import sys
sys.setrecursionlimit(1000000)
#def factorize(n,i):
    #if i<=n:
       # if n%i==0:
           ## n=n//i
       # else:
          #  i+=1
    #factorize(n,i)
#num=int(input())
#factorize(num,2)

# sum of digits of a no.
#def rsum(num):
#    if num!=0:
#        digit= num%10
#        num=int(num/10)
#       sum= digit + rsum(num)
#    else:
#        return 0
#    return sum
#x=rsum(10005)
#print(x)

#In every iteration paper cuts in half lengthwise
#def papercut(i,n,l,b):
 #   if n!=0:
  #      print(f'A{i}: length={float(l)},Breadth={float(b)}')
   #     newb=l/2
    #    newl=b
     #   n-=1
      #  i+=1
       # papercut(i,n,newl,newb)
#papercut(0,20,1500,800)


#Fibonacci series.
#def fibo(old,current,terms):
 #   if terms >= 1:
  #      new = old + current
#
 #       print(f'{new}',end='\t')
  #      terms -= 1
   #     fibo(current,new,terms)
#old=1
#current=1
#print(f'{old}', end='\t')
#print(f'{current}', end='\t')
#fibo(old,current,13)

#number to binary.
#def bin(num):
#    r=num%2
#    num=int(num/2)
#    if num!=0:
#        bin(num)
#    print(r,end='')
#num=int(input('Enter the number: '))
#bin(num)


#Running sum

#def runningsum(num):
 #   if num==0:
#        return 0
 #   if num>0:
#        s=num+runningsum(num-1)
#        return s
#max=int(input("Enter the n natural numbers: "))
#t=runningsum(max)
#print(f'The sum is {t:.2f}')













