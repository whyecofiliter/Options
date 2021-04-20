# option Class
# Call and Put

class Call():
    '''
    The standard Call option is divided into European Call and American Call
    The input parameters are 
    call prices : p
    strike prices: k
    maturitys : t
    European or American: EorA
    '''
    def __init__(self,p,k,t,EorA) :
        self.p=p
        self.k=k
        self.t=t
        self.EorA=EorA

class real_Call(Call):
    '''
    father class: Call
    son class: real_Call
    add two attributions: ask price: ask, bid price: bid
    '''
    def __init__(self,p,k,t,EorA,ask,bid):
        super(real_Call,self).__init__(p,k,t,EorA)
        self.ask=ask
        self.bid=bid

class Put():
    '''
    The standard Put option is divided into European Call and American Call
    The input parameters are 
    call prices : p
    strike prices: k
    maturitys : t
    European or American: EorA
    '''
    def __init__(self,p,k,t,EorA):
        self.p=p
        self.k=k
        self.t=t
        self.EorA=EorA
    
class real_Put(Put):
    '''
    father class: Put
    son class: real_Put
    add two attributions: ask price: ask, bid price: bid
    '''
    def __init__(self,p,k,t,EorA,ask,bid):
        super(real_Put,self).__init__(p,k,t,EorA)
        self.ask=ask
        self.bid=bid
        