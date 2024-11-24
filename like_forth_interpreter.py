from forth_virtual_machine import ForthVirtualMachine
import math

class LikeForthInterpreter(object):
    '''
        Simple forth interpreter. The interpreter
        includes some additional Forth words:

        : keyword <body> ; -> Done
        if <then-clause> [ else <else-clause> ] then
        begin <body> until
        do <body> loop
        (...)
        i ( a -- a i )
        . ( a -- ) -> Done
        .s ( [s] -- [s] ) -> Done
        .d ( [s] -- [s] ) -> Done
        ." -> Done
        cr -> Done
        acceptn -> Done
        bye -> Done

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
            ("swap",self.swap), ("rot",self.rot), ("over",self.over), ("pick",self.pick),
            (">",self.is_greater_than), ("<",self.is_less_than), (">=",self.is_greater_than_or_equal),
            ("<=",self.is_less_than_or_equal), ("and",self.and_forth), ("or",self.or_forth),
            ("eq",self.equal),("neq",self.different), ("clear",self.clear),
            (">r",self.push_to_return_stack),("r>",self.pop_from_return_stack),
            ("r@",self.copy_from_return_stack),
            ('."',self.forth_print), ("cr",self.print_n),
            ("acceptn", self.acceptn)
        ])

    def has_decimal_places(self,value):
        fractional_part, _ = math.modf(value)
        return fractional_part != 0

    def acceptn(self):
        try:
            value = float(input('Enter a number: '))
            self.fvm.push(value)
            return True
        except ValueError:
            print('Invalid input')
            return False

    def print_n(self):
        print("\n")
        return True

    def forth_print(self,char):
        try:
            if self.has_decimal_places(char):
                print(char,end=" ")
            else:
                print(int(char),end=" ")

            return True
        except:
            return False

    def copy_from_return_stack(self):
        D,_ = self.fvm.stacks()
        if len(D) == 0:
            return False
        else:
            return self.fvm.copy_from_return_stack()

    def pop_from_return_stack(self):
        D,_ = self.fvm.stacks()
        if len(D) == 0:
            return False
        else:
            return self.fvm.pop_from_return_stack()

    def push_to_return_stack(self):
        D,_ = self.fvm.stacks()
        if len(D) == 0:
            return False
        else:
            return self.fvm.push_to_return_stack()

    def clear(self):
        return self.fvm.clear()

    def equal(self):
        D, _ = self.fvm.stacks()
        if len(D) < 2:
            return False
        else:
            return self.fvm.equal()

    def different(self):
        D, _ = self.fvm.stacks()
        if len(D) < 2:
            return False
        else:
            return self.fvm.different()

    def and_forth(self):
        D, _ = self.fvm.stacks()
        if len(D) < 2:
            return False
        else:
            return self.fvm.and_forth()

    def or_forth(self):
        D, _ = self.fvm.stacks()
        if len(D) < 2:
            return False
        else:
            return self.fvm.or_forth()

    def is_greater_than(self):
        D, _ = self.fvm.stacks()
        if len(D) < 2:
            return False
        else:
            return self.fvm.is_greater_than()

    def is_less_than(self):
        D, _ = self.fvm.stacks()
        if len(D) < 2:
            return False
        else:
            return self.fvm.is_greater_than()

    def is_greater_than_or_equal(self):
        D, _ = self.fvm.stacks()
        if len(D) < 2:
            return False
        else:
            return self.fvm.is_greater_than_or_equal()

    def is_less_than_or_equal(self):
        D, _ = self.fvm.stacks()
        if len(D) < 2:
            return False
        else:
            return self.fvm.is_less_than_or_equal()

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

    def swap(self):
        D, _ = self.fvm.stacks()
        if len(D) < 2:
            return False
        else:
            return self.fvm.swap()

    def rot(self):
        D, _ = self.fvm.stacks()

        if len(D) < 3:
            return False

        else:
            return self.fvm.rot()

    def over(self):
        D, _ = self.fvm.stacks()
        if len(D) < 2:
            return False

        else:
            return self.fvm.over()

    def pick(self):
        return self.fvm.pick()

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
                if fun.__name__ == "forth_print":
                    fun(tokens[1])
                    if len(tokens[2:]) > 0:
                        if not '"' in str(tokens[2]):
                            return self.interpret(['."']+tokens[2:])
                        else:
                            print(tokens[2].split('"')[0],end=" ")
                            return self.interpret(tokens[3:])
                    else:
                        return True
                elif fun():
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
            ok = self.interpret(self.tokenize(input_str))
            if '."' in input_str:
                print("")
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