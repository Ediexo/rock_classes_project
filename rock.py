'''
Meredith and Namitha
'''

class Rock:
    '''the characteristics and traits of rocks'''
    
    def __init__(self, rockType = 'unknown' , age=None):
        '''assumming user inputs either igneous, metamorphic or sedimentary'''
        self.type = rockType
        self.age = age

    def mayContainFossils(self):
        if self.type.casefold() == 'sedimentary':
            return True
        
        return False
    '''
    
class Igneous(Rock):
    def __init__(self, age=None):
        super.__init__('igneous', age)
        self.subTypes = ['Extrusive', 'Intrusive']
        
class Sedimentary(Rock):
    def __init__(self, age=None):
        super.__init__('sedimentary', age)
        self.subTypes = ['Organic', 'Clastic', 'Chemical']
        
class Metamorphic(Rock):
    def __init__(self, age=None):
        super.__init__('metamorphic', age)
        self.subTypes = ['Foliated', 'Unfoliated']
    
