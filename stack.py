class Stack:
    ''' Simple Stack based on lists
    '''
    def __init__(self):
        self.ls = []
    
    def __len__(self):
        return len(self.ls)
    
    def __str__(self):
        return str(self.ls)
    
    def append(self,number):
        self.ls.append(number)
    
    def pop(self):
        top = self.ls[-1]
        self.ls = self.ls[:-1]
        return top

    