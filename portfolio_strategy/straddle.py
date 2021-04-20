'''
straddle portfolio
'''
class straddle():
    '''
    input: 
        call:call
        put:put
    '''
    def __init__(self,call,put):
        import numpy as np
        
        self.call=call
        self.put=put
        self.S=np.linspace(min(self.call.k,self.put.k)*0.6,max(self.call.k,self.put.k)*1.4,1000)
    
    def value_at_maturity(self,S):
        value=max(S-self.call.k,0)+max(self.put.k-S,0)-self.call.p-self.put.p
        return value
    
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
        
        T=min(self.call.t,self.put.t)
        prob=stats.lognorm.pdf(self.S,s=sigma*T**0.5,scale=np.exp(np.log(S0)+(mu-0.5*sigma**2)*T))
        return prob
        
    def expectated_profit(self,S0,mu,sigma):
        '''
        Using prob_vaue_at_maturity calculate the probability of spot price at maturity
        '''
        prob=self.prob_value_at_maturity(S0,mu,sigma)
        prob[prob<=0.0001]=0
        value1=list()
        for i in range(0,len(self.S)) :
            value1.append(self.value_at_maturity(self.S[i])*prob[i]*(self.S[2]-self.S[1]))
        return sum(value1)
    
class inverse_straddle(straddle):
    '''
    input: 
        call: call
        put: put
    '''
    def __init__(self,call,put):
        super(inverse_straddle,self).__init__(call,put)
        
    def value_at_maturity(self,S):
        value=-(max(S-self.call.k,0)+max(self.put.k-S,0)-self.call.p-self.put.p)
        return value
        
        
        
        
        
        
        