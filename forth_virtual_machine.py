from stack import Stack
from random import randint
import math

class ForthVirtualMachine:
    ''' Forth Virtual Machine
    ======================================
    + ( a b -- a+b ) -> Done
    - ( a b -- a-b ) -> Done
    * ( a b -- a*b ) -> Done
    / ( a b -- a/b ) -> Done
    % ( a b -- a%b ) -> Done
    and ( a b -- -1 if a and b else 0 )
    or ( a b -- -1 if a or b else 0 )
    eq ( a b -- -1 if a = b else 0 )
    neq ( a b -- 0 if a = b else -1 )
    > ( a b -- -1 if a > b else 0 )
    < ( a b -- -1 if a < b else 0 )
    >= ( a b -- -1 if a >= b else 0 )
    <= ( a b -- -1 if a <= b else 0 )
    sqrt ( a -- sqrt(a) ) -> Done
    true ( a -- a -1 ) -> Done
    false ( a -- a 0 ) -> Done
    ======================================
    pick ( a0 .. an n -- a0 .. an a0 )
    dup ( a -- a a ) -> Done
    over ( a b -- a b a )
    swap ( a b -- b a )
    rot ( a b c -- c a b )
    drop ( a -- ) -> Done
    ======================================
    >r ( a -- R: a )
    r> ( R: a -- a )
    r@ ( R: a -- a R: a )
    ======================================
    rand -> Done
    clear ( [s] -- )
    stacks ( [s] -- [s] )
    pop ( a b -- a ) -> Done
    push b ( a -- a b ) -> Done
    '''
    def __init__(self):
        self.d_stack = Stack()
        self.r_stack = Stack()
  
    def stacks(self):
        return self.d_stack, self.r_stack 
    
    def rand(self):
        try:
            old_top = self.pop()
            new_top = float(randint(0,int(old_top)))
            self.push(new_top)
            return True
        except Exception as e:
            print("Stack empty")
            return False
        
    def pop(self):
        top = self.d_stack.pop()
        return top

    def drop(self):
        self.d_stack.drop()
    
    def dup(self):
        self.push(self.d_stack.ls[-1])

    def push(self,number):
        try:
            self.d_stack.append(number)
            return True
        except Exception as e:
            print("Error: ",e)
            return False
    
    def plus(self):
        try:
            n1 = self.d_stack.ls.pop()
            n2 = self.d_stack.ls.pop()
            self.d_stack.append(n1+n2)
            return True
        except:
            return False
    
    def minus(self):
        try:
            n1 = self.d_stack.ls.pop()
            n2 = self.d_stack.ls.pop()
            self.d_stack.append(n2-n1)
            return True
        except:
            return False
        
    def multiplication(self):
        try:
            n1 = self.d_stack.ls.pop()
            n2 = self.d_stack.ls.pop()
            self.d_stack.append(n2*n1)
            return True
        except:
            return False
        
    def division(self):
        try:
            denominator = self.d_stack.ls.pop()
            numerator = self.d_stack.ls.pop()
            self.d_stack.append(round( numerator// denominator,0))
            return True
        except:
            return False
        
    def modulus(self):
        try:
            denominator = self.d_stack.ls.pop()
            numerator = self.d_stack.ls.pop()
            self.d_stack.append(round( numerator % denominator,0))
            return True
        except:
            return False
    
    def square_root(self):

        try:
            number_ = self.d_stack.ls.pop()
            self.d_stack.append(round(math.sqrt(number_),0))
            return True
        except:
            return False
        
    def true(self):
        return self.push(-1)
    
    def false(self):
        return self.push(0)