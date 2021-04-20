
'''
Calendar option 日历期权
'''

class calendar_option():
    '''
    construct calendar option 
    input 
    early:  the option have short maturity
    late: the option have long maturity
    OorN: whether the portfolio is Positive or Negative 
    '''
    def __init__(self,early,late,OorN):
        import numpy as np
        self.early=early
        self.late=late
        self.OorN=OorN
        self.S=np.linspace(self.early.k*0.6*(1-self.early.t),self.early.k*1.4*(1+self.early.t),1000)
    
    def value_at_maturity(self,S,r,sigma,q):
        from Options.option_pricing.BSM_pricing import BSM
        from Options.option import Call
        from Options.option import Put
        if self.late.__class__==Call and self.OorN=='P' :
            value=-max(S-self.early.k,0)+BSM(r,sigma,self.late.k,S,q,self.late.t-self.early.t,'C').BSM_pricing()\
                  +(self.early.p-self.late.p)
            return value
        if self.late.__class__==Put and self.OorN=='P'  :
            value=-max(self.early.k-S,0)+BSM(r,sigma,self.late.k,S,q,self.late.t-self.early.t,'P').BSM_pricing()\
                  +self.early.p-self.late.p
            return value
        if self.late.__class__==Call and self.OorN=='N'  :
            value=max(S-self.early.k,0)-BSM(r,sigma,self.late.k,S,q,self.late.t-self.early.t,'C').BSM_pricing()\
                  +self.late.p-self.early.p
            return value
        if self.late.__class==Put and self.OorN=='N'  :
            value=max(self.early.k-S,0)-BSM(r,sigma,self.late.k,S,q,self.late.t-self.early.t,'P').BSM_pricing()\
                  +self.late.p-self.early.p
            return value
        
    def plot_value_at_maturity(self,r,sigma,q):
        '''
        plot the profit at the maturity with a spectrum of spot price
        '''
        import matplotlib.pyplot as plt
        
        value=list()
        for i in self.S :
            value.append(self.value_at_maturity(i,r,sigma,q))
        plt.plot(self.S,value)
        
    def prob_value_at_maturity(self,S0,mu,sigma):
        '''
        calculate the probability of the spot at the maturity
        Assuming the spot follows the geometric brownian motion
        log(ST/S0)=(mu-0.5*sigma^2)T+WT
        '''
        import scipy.stats as stats
        import numpy as np
        
        T=self.early.t
        prob=stats.lognorm.pdf(self.S,s=sigma*T**0.5,scale=np.exp(np.log(S0)+(mu-0.5*sigma**2)*T))
        return prob
        
    def expectated_profit(self,S0,mu,sigma,r,q):
        '''
        Using prob_vaue_at_maturity calculate the probability of spot price at maturity
        '''
        prob=self.prob_value_at_maturity(S0,mu,sigma)
        prob[prob<=0.0001]=0
        value1=list()
        for i in range(0,len(self.S)) :
            value1.append(self.value_at_maturity(self.S[i],r,sigma,q)*prob[i]*(self.S[2]-self.S[1]))
        return sum(value1)
    
        
        
        
        
    
