from stack import Stack
from random import randint
import math

TRUE = -1
FALSE = 0

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
    pick ( a0 .. an n -- a0 .. an a0 ) -> Done
    dup ( a -- a a ) -> Done
    over ( a b -- a b a ) -> Done
    swap ( a b -- b a ) -> Done
    rot ( a b c -- c a b ) -> Done
    drop ( a -- ) -> Done
    ======================================
    >r ( a -- R: a ) -> Done
    r> ( R: a -- a ) -> Done
    r@ ( R: a -- a R: a ) -> Done
    ======================================
    rand -> Done
    clear ( [s] -- ) -> Done
    stacks ( [s] -- [s] ) -> Done
    pop ( a b -- a ) -> Done
    push b ( a -- a b ) -> Done
    '''
    def __init__(self):
        self.d_stack = Stack()
        self.r_stack = Stack()
        self.loop_control_stack = Stack()

    def get_len_loop_control(self):
        return len(self.loop_control_stack)

    def clear_loop_control_stack(self):
        self.loop_control_stack.clear()

    # true -> execute the loop
    # false -> limit >= start, so no need to execute the loop
    def compare_loop_control_stack(self)->bool:

        if self.loop_control_stack.ls[-2] < self.loop_control_stack.ls[-1]:
            return True
        else:
            return False
    def att_top_loop_stack(self):
        self.loop_control_stack.ls[-2] = self.loop_control_stack.ls[-2] + 1
    
    def get_i(self):
        try:
            return self.push(self.loop_control_stack.ls[-2])
        except:
            return None 
        
    def push_loop_stack(self,number):
        self.loop_control_stack.append(number)
        return True

    def copy_from_return_stack(self):
        
        try:
            top = self.r_stack.ls[-1]
            self.d_stack.append(top)
            return True
        except:
            return False

    def push_to_return_stack(self):
        try:
            top = self.pop()
            self.r_stack.append(top)
            return True
        except:
            return False
    
    def pop_from_return_stack(self):
        try:
            top = self.r_stack.pop()
            print(top)
            self.d_stack.append(top)
            return True
        except:
            return False

    def clear(self):
        try:
            self.d_stack.ls = []
            return True
        except:
            return False
        
    def equal(self):
        try:
            n1 = self.pop()
            n2 = self.pop()
            if n1 == n2:
                self.push(TRUE)
            else:
                self.push(FALSE)
            return True
        except Exception as e:
            return False

    def different(self):
        try:
            n1 = self.pop()
            n2 = self.pop()
            if n1 != n2:
                self.push(TRUE)
            else:
                self.push(FALSE)
            return True
        except Exception as e:
            return False

    def and_forth(self):
        try:
            n1 = self.pop()
            n2 = self.pop()
            result = float(int(n1) & int(n2))
            self.push(result)
            return True
        except Exception as e:
            return False
        
    def or_forth(self):
        try:
            n1 = self.pop()
            n2 = self.pop()
            result = float(int(n1) | int(n2))
            self.push(result)
            return True
        except Exception as e:
            return False
        
    def is_greater_than(self):
        try:
            n1 = self.pop()
            n2 = self.pop()
            
            if n2 > n1:
                self.push(-1)
            else:
                self.push(0)

            return True
        except:
            return False

    def is_less_than(self):
        try:
            n1 = self.pop()
            n2 = self.pop()
            
            if n2 < n1:
                self.push(-1)
            else:
                self.push(0)

            return True
        except:
            return False

    def is_greater_than_or_equal(self):
        try:
            n1 = self.pop()
            n2 = self.pop()
            
            if n2 >= n1:
                self.push(-1)
            else:
                self.push(0)

            return True
        except:
            return False
    
    def is_less_than_or_equal(self):
        try:
            n1 = self.pop()
            n2 = self.pop()
            
            if n2 <= n1:
                self.push(-1)
            else:
                self.push(0)

            return True
        except:
            return False

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
        
    def pop(self)->float:
        top = self.d_stack.pop()
        return top

    def drop(self):
        self.d_stack.drop()
    
    def dup(self):
        self.push(self.d_stack.ls[-1])

    def swap(self):
        try:
            top = self.d_stack.pop()
            top_ = self.d_stack.pop()
            self.d_stack.append(top)
            self.d_stack.append(top_)
            return True
        except:
            return False

    def rot(self):
        try:
            n1 = self.d_stack.pop()
            n2 = self.d_stack.pop()
            n3 = self.d_stack.pop()
            self.push(n2)
            self.push(n1)
            self.push(n3)
            return True
        except:
            return False
    
    def over(self):
        try:
            self.push(self.d_stack.ls[-2])
            return True
        except:
            return False
    
    def pick(self):
        try:
            top = self.pop()
            num_ = self.d_stack.ls[int((-top-1))]
            self.push(num_)
            return True
        except Exception as e:
            print(e)
            self.push(top)
            return False

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
    """
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
    """