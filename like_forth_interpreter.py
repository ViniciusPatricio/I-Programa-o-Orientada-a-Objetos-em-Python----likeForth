from forth_virtual_machine import ForthVirtualMachine
import math

class LikeForthInterpreter(object):
    ''' 
        Simple forth interpreter. The interpreter
        includes some additional Forth words:
        : keyword <body> ;
        if <then-clause> [ else <else-clause> ] then
        begin <body> until
        do <body> loop
        (...)
        i ( a -- a i )
        . ( a -- )
        .s ( [s] -- [s] )
        .d ( [s] -- [s] )
        ."
        cr
        acceptn
        bye
    '''
    def __init__(self):
        self.fvm = ForthVirtualMachine()
        self.words = dict([
        ('.s', self.dots), ('.d', self.dotd), ('.',self.dot),
        ('true',self.true), ('false',self.false),
        ('drop',self.drop), ('dup',self.duplication),
        ('rand',self.rand),
        ('+',self.plus), ('-',self.minus), ("*",self.multiplication),
        ("/",self.division), ('%',self.modulus), ('sqrt',self.square_root),
        ('>', self.greater_than),
        ('>=', self.greater_than_or_equal),
        ('<', self.less_than),
        ('<=', self.less_than_or_equal),
        ('eq', self.equal),
        ('neq', self.not_equal),
        ('or', self.logical_or),
        ('and', self.logical_and),
        ('>r', self.push_to_r),
        ('r>', self.pop_from_r),
        ('r@', self.peek_r)
        ])
    
    def false(self):
        rem = self.fvm.false()
        return rem

    def true(self):
        rem = self.fvm.true()
        return rem
    
    def rand(self):
        rem = self.fvm.rand()
        return rem
    
    def dot(self):
        D, _ = self.fvm.stacks()
        if  len(D) == 0:
            print("Stack empty")
            return False
        else:
            print(self.fvm.pop())
        return True
    
    def drop(self):
        D, _ = self.fvm.stacks()
        if  len(D) == 0:
            print("Stack empty")
            return False
        else:
            self.fvm.drop()
        return True
    
    def duplication(self):
        D, _ =  self.fvm.stacks()
        if  len(D) == 0:
            print("Stack empty")
            return False
        else:
            self.fvm.dup()

        return True
    
    def dots(self):
        D, R = self.fvm.stacks()
        print(f"D <{len(D)}> {str(D)} ")
        print(f"R <{len(R)}> {str(R)} ")
        return True

    def dotd(self):
        for w in self.words:
            if not callable(self.words[w]):
                print('%s: %s'%(w, list(self.words[w])))
            return True

    def plus(self):
        D, _ = self.fvm.stacks()
        if len(D) >= 2 and type(D.ls[-1]) == float and type(D.ls[-2]) == float:
            return self.fvm.plus()
        else:
            return False

    def minus(self):
        D, _ = self.fvm.stacks()
        if len(D) >= 2 and type(D.ls[-1]) == float and type(D.ls[-2]) == float:
            return self.fvm.minus()
        else:
            return False  

    def multiplication(self):
        D, _ = self.fvm.stacks()
        if len(D) >= 2 and type(D.ls[-1]) == float and type(D.ls[-2]) == float:
            return self.fvm.multiplication()
        else:
            return False  
    
    def division(self):
        D, _ = self.fvm.stacks()
        if len(D) >= 2 and type(D.ls[-1]) == float and (D.ls[-1]) != 0 and type(D.ls[-2]) == float:
            return self.fvm.division()
        else:
            return False
    
    def modulus(self):
        D, _ = self.fvm.stacks()
        if len(D) >= 2 and type(D.ls[-1]) == float and (D.ls[-1]) != 0 and type(D.ls[-2]) == float:
            return self.fvm.modulus()
        else:
            return False

    def square_root(self):
        D, _ = self.fvm.stacks()
        if len(D) >= 1 and type(D.ls[-1]) == float:
            return self.fvm.square_root()
        else:
            return False

    def greater_than(self):
        D, _ = self.fvm.stacks()
        if len(D) >= 2:
            self.fvm.greater_than()
            return True
        else:
            print("Not enough elements in stack")
            return False

    def greater_than_or_equal(self):
        D, _ = self.fvm.stacks()
        if len(D) >= 2:
            self.fvm.greater_than_or_equal()
            return True
        else:
            print("Not enough elements in stack")
            return False

    def less_than(self):
        D, _ = self.fvm.stacks()
        if len(D) >= 2:
            self.fvm.less_than()
            return True
        else:
            print("Not enough elements in stack")
            return False

    def less_than_or_equal(self):
        D, _ = self.fvm.stacks()
        if len(D) >= 2:
            self.fvm.less_than_or_equal()
            return True
        else:
            print("Not enough elements in stack")
            return False

    def equal(self):
        D, _ = self.fvm.stacks()
        if len(D) >= 2:
            self.fvm.equal()
            return True
        else:
            print("Not enough elements in stack")
            return False

    def not_equal(self):
        D, _ = self.fvm.stacks()
        if len(D) >= 2:
            self.fvm.not_equal()
            return True
        else:
            print("Not enough elements in stack")
            return False

    def logical_or(self):
        D, _ = self.fvm.stacks()
        if len(D) >= 2:
            self.fvm.logical_or()
            return True
        else:
            print("Not enough elements in stack")
            return False

    def logical_and(self):
        D, _ = self.fvm.stacks()
        if len(D) >= 2:
            self.fvm.logical_and()
            return True
        else:
            print("Not enough elements in stack")
            return False

    def push_to_r(self):
        D, _ = self.fvm.stacks()
        if len(D) == 0:
            print("Stack empty")
            return False
        else:
            self.fvm.push_to_r()
        return True

    def pop_from_r(self):
        _, R = self.fvm.stacks()
        if len(R) == 0:
            print("Return stack empty")
            return False
        else:
            self.fvm.pop_from_r()
        return True

    def peek_r(self):
        _, R = self.fvm.stacks()
        if len(R) == 0:
            print("Return stack empty")
            return False
        else:
            self.fvm.peek_r()
        return True

    def fcompile(self, tokens):
        'Add keyword to words dictionary'
        keyword = tokens[0]
        try:
            semicolon_pos = tokens.index(';')
        except ValueError:
            return False
        body = tokens[1:semicolon_pos]
        self.words[keyword] = body
        return tokens[semicolon_pos + 1:]

    def interpret(self, tokens):
        if not tokens:
            return True

        if tokens[0] == ':':
            rem = self.fcompile(tokens[1:])
            if rem == False:
                return False
            else:
                return self.interpret(rem)
        
        if tokens[0] in self.words:
            fun = self.words[tokens[0]]
            if callable(fun):
                if fun():
                    return self.interpret(tokens[1:])
                else:
                    return False
            else:
                return self.interpret(list(fun) + tokens[1:])
        
        # inserindo numero na pilha
        if type(tokens[0]) == float:
            rem = self.fvm.push(tokens[0])
            if not rem: # caso a insercao falhe
                return False
            else:
                return self.interpret(tokens[1:]) 

        
        return False
    
    def tokenize(self, s):
        def string_to_num(s):
            try:
                return float(s)
            except ValueError:
                return s
        return [string_to_num(t) for t in s.split()]

    def REPL(self):
        input_str = input('?> ')
        if input_str != 'bye':
            #print(self.tokenize(input_str)) # verificar comportamento
            ok = self.interpret(self.tokenize(input_str))
            if not ok:
                print('?')
            else:
                print('<ok>')
            self.REPL()
    
    def run(self, txt = None):
        self.__init__()
        if txt is None:
            print('Micro Forth (September 2024)')
            self.REPL()
        else:
            self.interpret(self.tokenize(txt))

if __name__ == "__main__":
    interpreter = LikeForthInterpreter()  
    interpreter.run()