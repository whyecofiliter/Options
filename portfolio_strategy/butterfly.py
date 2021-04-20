
class butterfly():
    '''
    construct bull spread portfolio
    inupt parameters:
        short option: short_1
                      short_2
        long option: long_1
                     long_2
        Put or Call: PorC
    '''
    def __init__(self,short_1,short_2,long_1,long_2,PorC):
        import numpy as np
        self.short_1=short_1
        self.short_2=short_2
        self.long_1=long_1
        self.long_2=long_2
        self.PorC=PorC
        self.S=np.linspace(int(0.8*min([self.short_1.k,self.long_1.k,self.short_2.k,self.long_2.k])),int(1.2*max([self.short_1.k,self.long_1.k,self.short_2.k,self.long_2.k])),1000)
            
    def value_at_maturity(self,S) :
        '''
        calculate the value of the bull at the maturity at the certain spot price
        '''
        if self.PorC =='C' :
            return max(S-self.long_1.k,0)+max(S-self.long_2.k,0)-max(S-self.short_1.k,0)\
                   -max(S-self.short_2.k,0)+(self.short_1.p+self.short_2.p-self.long_1.p-self.long_2.p)
        elif self.PorC =='P' :
            return max(self.long_1.k-S,0)+max(self.long_2.k-S,0)-max(self.short_1.k-S,0)\
                   -max(self.short_2.k-S,0)+(self.short_1.p+self.short_2.p-self.long_1.p-self.long_2.p)
        
    def plot_value_at_maturity(self):
        '''
        plot the profit at the maturity with a spectrum of spot price
        '''
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
        
        T=self.long_1.t
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
        