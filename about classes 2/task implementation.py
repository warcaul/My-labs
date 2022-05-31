class task1:
    def __init__ (self, x, y):
        self.x = x
        self.y = y
    def func1 (self):
        if self.y > self.x: return (self.x+self.x*self.y+ self.y**2)
        if self.x > self.y: return (self.x**2+self.y**0.5)
        if self.x== self.y: return (self.x+2*self.y)
x =int (input("x"))
y =int (input("y"))
obj1 = task1(x, y)
print(obj1.func1())



import math
class task2 :
    def __init__ (self, a, b, h):
            self.a = a
            self.b = b
            self.h = h
    pass        
    def func2(self):
         while self.a<=self.b:
          print  (math.log10(self.a))
          self.a += self.h
a = float(input("a="))
b = float(input("b="))
h = float(input("h="))
obj2 = task2(a, b, h)
obj2.func2()




import math
class task2bonus :
    def __init__ (self, a, b):
            self.a = a
            self.b = b
    pass        
    def func2b(self):
         self.a1=self.a
         while self.a<=self.b:
          print (math.log10(self.a))
          self.a += h1
         while self.a1<=self.b:
          print (math.log10(self.a1))
          self.a1 += h2
a = float(input("a="))
b = float(input("b="))
h1 = float(input("h1="))
h2 = float(input("h2="))
obj2b = task2bonus(a, b)
obj2b.func2b()



import math
class task3:
 def __init__(self, n):
     self.n = n
 def func3 (self):
      x=0
      for i in range(1, self.n + 1):
       term=2**0.5*math.factorial(i)
       x = x + term
      return(x) 

n = int(input())
obj3 = task3(n)
print (obj3.func3())