#numberclass

#class Number:
 #   def setnumber(self,n):
#        self.__num=int(n)
 #   def getnumber(self):
#   def printnumber(self):
#        print(self.__num)
#    def isnegative(self,n):
#        if self.__num<0:
#            return True
#        else:
#            pass
 #   def isdivisible(self,n):
#        if n==0:
#            return False
#        if self.__num%n == 0:
#            return True
#        else:
#            return False
#    def isabsolute(self):
#        if self.__num>=0:
#            return self.__num
#        else:
#            return -1*self.__num
#x=Number()
#x.setnumber(-48)
#x.printnumber()
#if x.isdivisible(4) == True:
#    print('4 divides ', x.getnumber())
#else:
 #   print('4 doesnot divide ', x.getnumber())
#print('absolute value of ', x.getnumber(),' is', x.isabsolute())

#class fruit.
    #class Fruit:
    #count=0
    #ef __init__(self,name='',size=0,colour=''):
        #self.__name=name
        #self.__size=size
        #self.__colour=colour
       # Fruit.count+=1
    #def display():
        #print(Fruit.count)
#f1 = Fruit('Banana', 5, 'Yellow')
#f2 = Fruit('Orange', 4, 'Orange')
#f3 = Fruit('Apple', 3, 'Red')
#Fruit.display( )
#print(Fruit.count)


#a program that determines whether two objects are of same type,whether their attributes are same and whether they are pointing tosame object.

#class Complex:
   # def __init__(self,r=0.0,i=0.0):
        #self.__real = r
        #self.__imag = i
    #def __eq__(self,other):
        #if self.__real==other.__real and self.__imag==other.__imag:
           # return True
        #else:
           # return False
#c1 = Complex(1.1,2.3)
#c2 = Complex(7.8,8.9)
#c3 = c1
#if c1==c2:
    #print('attributes of c1 and c2 are same')
#else:
#    print('attributes of c1 and c2 are not same')
#if type(c1) == type(c2):
#    print('types of c1 and c2 are  same')
#else:
#    print('types of c1 and c2 are not same')
#if c1 is c3:
#    print('c1 and c3 are pointing to same same object')
#else:
#     print('c1 and c3 are not pointing to same object')


#Write a program to get a list of built-in functions.
import builtins
print(vars(builtins))
print()
print(dir(builtins))



