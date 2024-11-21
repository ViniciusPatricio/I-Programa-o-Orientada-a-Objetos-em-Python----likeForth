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
    and ( a b -- -1 if a and b else 0 ) -> Done
    or ( a b -- -1 if a or b else 0 ) -> Done
    eq ( a b -- -1 if a = b else 0 ) -> Done
    neq ( a b -- 0 if a = b else -1 ) -> Done
    > ( a b -- -1 if a > b else 0 ) -> Done
    < ( a b -- -1 if a < b else 0 ) -> Done
    >= ( a b -- -1 if a >= b else 0 ) -> Done
    <= ( a b -- -1 if a <= b else 0 ) -> Done
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
    >r ( a -- R: a ) -> Done
    r> ( R: a -- a ) -> Done
    r@ ( R: a -- a R: a ) -> Done
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

    def greater_than(self):
        n1 = self.d_stack.pop()
        n2 = self.d_stack.pop()
        self.d_stack.append(-1 if n2 > n1 else 0)

    def greater_than_or_equal(self):
        n1 = self.d_stack.pop()
        n2 = self.d_stack.pop()
        self.d_stack.append(-1 if n2 >= n1 else 0)

    def less_than(self):
        n1 = self.d_stack.pop()
        n2 = self.d_stack.pop()
        self.d_stack.append(-1 if n2 < n1 else 0)

    def less_than_or_equal(self):
        n1 = self.d_stack.pop()
        n2 = self.d_stack.pop()
        self.d_stack.append(-1 if n2 <= n1 else 0)

    def equal(self):
        n1 = self.d_stack.pop()
        n2 = self.d_stack.pop()
        self.d_stack.append(-1 if n2 == n1 else 0)

    def not_equal(self):
        n1 = self.d_stack.pop()
        n2 = self.d_stack.pop()
        self.d_stack.append(-1 if n2 != n1 else 0)

    def logical_or(self):
        n1 = self.d_stack.pop()
        n2 = self.d_stack.pop()
        self.d_stack.append(-1 if n2 != 0 or n1 != 0 else 0)

    def logical_and(self):
        n1 = self.d_stack.pop()
        n2 = self.d_stack.pop()
        self.d_stack.append(-1 if n2 != 0 and n1 != 0 else 0)

    def push_to_r(self):
        top = self.d_stack.pop()
        self.r_stack.append(top)

    def pop_from_r(self):
        top = self.r_stack.pop()
        self.d_stack.append(top)

    def peek_r(self):
        top = self.r_stack.ls[-1]
        self.d_stack.append(top)