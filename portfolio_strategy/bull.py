#
'''
Bull Spread Portfolio
'''
#%
class bull():
    '''
    construct bull spread portfolio
    inupt parameters:
        short option: short
        long option: long
        Put or Call : PorC
    '''
    def __init__(self,short,long,PorC):
        import numpy as np
        self.short=short
        self.long=long
        self.PorC=PorC
        self.S=np.linspace(int(min(self.short.k,self.long.k)-2*abs(self.long.k-self.short.k)),int(max(self.short.k,self.long.k)+2*abs(self.long.k-self.short.k)),1000)
            
    def value_at_maturity(self,S) :
        '''
        calculate the value of the bull at the maturity at the certain spot price
        '''
        if self.PorC =='C' :
            return max(S-self.long.k,0)-max(S-self.short.k,0)+(self.short.p-self.long.p)
        elif self.PorC =='P' :
            return max(self.long.k-S,0)-max(self.short.k-S,0)+(self.short.p-self.long.p)
        
    def plot_value_at_maturity(self):
        import matplotlib.pyplot as plt
        
        value=list()
        for i in self.S :
            value.append(self.value_at_maturity(i))
        plt.plot(self.S,value)
        
        
    def prob_value_at_maturity(self,S0,mu,sigma):
        '''
        calculate the probability of the spot at the maturity
        Assuming the spot follows the geometric brownian motion
        log(ST/S0)=(mu-0.5*sigma^2)T+WT
        '''
        import scipy.stats as stats
        import numpy as np
        
        T=self.long.t
        prob=stats.lognorm.pdf(self.S,s=sigma*T**0.5,scale=np.exp(np.log(S0)+(mu-0.5*sigma**2)*T))
        return prob
        
    def expectated_profit(self,S0,mu,sigma):
        '''
        Using prob_vaue_at_maturity calculate the probability of spot price at maturity
        '''
        prob=self.prob_value_at_maturity(S0,mu,sigma)
        value=list()
        for i in range(0,len(self.S)) :
            if self.S[i]>0 :
                value.append(self.value_at_maturity(self.S[i])*prob[i]*(self.S[2]-self.S[1]))
        return sum(value)
        
                
        
        