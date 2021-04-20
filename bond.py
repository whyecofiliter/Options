
'''
Bond Class
'''
class coupon():
    def __init__(self,principle,coupon_rate,maturity,compounding,yield_rate=None):
        self.principle=principle
        self.coupon_rate=coupon_rate
        self.maturity=maturity
        self.compounding=compounding
        self.yield_rate=yield_rate

class fra():
    def __init__(self,principle,forward_rate,start,end):
        self.principle=principle
        self.forward_rate=forward_rate
        self.start=start
        self.end=end

    
        