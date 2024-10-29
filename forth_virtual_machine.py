from stack import Stack
from random import randint

class ForthVirtualMachine:
    ''' Forth Virtual Machine
    ======================================
    + ( a b -- a+b )
    - ( a b -- a-b )
    * ( a b -- a*b )
    / ( a b -- a/b )
    % ( a b -- a%b )
    and ( a b -- -1 if a and b else 0 )
    or ( a b -- -1 if a or b else 0 )
    eq ( a b -- -1 if a = b else 0 )
    neq ( a b -- 0 if a = b else -1 )
    > ( a b -- -1 if a > b else 0 )
    < ( a b -- -1 if a < b else 0 )
    >= ( a b -- -1 if a >= b else 0 )
    <= ( a b -- -1 if a <= b else 0 )
    sqrt ( a -- sqrt(a) )
    true ( a -- a -1 )
    false ( a -- a 0 )
    ======================================
    pick ( a0 .. an n -- a0 .. an a0 )
    dup ( a -- a a )
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

    def push(self,number):
        try:
            self.d_stack.append(number)
            return True
        except Exception as e:
            print("Error: ",e)
            return False