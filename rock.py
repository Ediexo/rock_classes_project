'''
Meredith and Namitha
'''

class Rock:
    '''the characteristics and traits of rocks'''
    
    def __init__(self, rockType = 'unknown' , age=None):
        '''assumming user inputs either igneous, metamorphic or sedimentary'''
        self.type = rockType
        self.age = age
        self.eon = "unknown'

    def mayContainFossils(self):
        if self.type.casefold() == 'sedimentary':
            return True
        
        return False

    def eon(self):
        if self.age != None:
            if self.age > 4,000,000,000:
                self.eon = 'Hadean'
            elif self.age > 2,500,000,000:
                self.eon = 'Archean'
            elif self.age > 514,000,000:
                self.eon = 'Proterozoic'
            else:
                self.eon = 'Phanerozoic'
    '''
    def subType(self):
        if self.type.casefold() == 'igneous':
            print("Extrusive or Intrusive rocks")
                
        elif self.type.casefold() == 'sedimentary':
            print('Organic, Clastic, Chemical')
            
        elif self.type.casefold() == 'metamorphic':
            print('Foliated and Unfoliated')
        else:
            print('Unfortunately, there is no subtype found')
    '''
class Igneous(Rock):
    def __init__(self, age=None):
        super.__init__('igneous', age)
        self.subTypes = ['Extrusive', 'Intrusive']
        
    self.eon = super.eon(self)
        
        
class Sedimentary(Rock):
    def __init__(self, age=None):
        super.__init__('sedimentary', age)
        self.subTypes = ['Organic', 'Clastic', 'Chemical']
        
    self.eon = super.eon(self)
        
class Metamorphic(Rock):
    def __init__(self, age=None):
        super.__init__('metamorphic', age)
        self.subTypes = ['Foliated', 'Unfoliated']
        
    self.eon = super.eon(self)
