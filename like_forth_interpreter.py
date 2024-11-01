from forth_virtual_machine import ForthVirtualMachine

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
        ('true',self.true), ('false',self.false), ('drop',self.drop),
        ('rand',self.rand),
        ])
    
    def false(self):
        rem = self.fvm.push(0)
        return rem

    def true(self):
        rem = self.fvm.push(-1)
        return rem
    
    def rand(self):
        rem = self.fvm.rand()
        return rem
    
    def dot(self):
        D, _ = self.fvm.stacks()
        if  len(D) == 0:
            print("Stack empty")
        else:
            print(self.fvm.drop())
        return True
    
    def drop(self):
        D, _ = self.fvm.stacks()
        if  len(D) == 0:
            print("Stack empty")
        else:
            self.fvm.pop()
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
            print(self.tokenize(input_str)) # verificar comportamento
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