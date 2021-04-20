
class rate():
    '''
    present rate
    '''
    def __init__(self,value,maturity):
        self.value=value
        self.maturity=maturity

class forward_rate():
    '''
    forward rate
    '''
    def __init__(self,value,start,end,maturity=None):
        self.value=start
        self.start=start
        self.end=end
        self.maturity=maturity

