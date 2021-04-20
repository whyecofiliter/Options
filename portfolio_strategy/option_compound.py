'''
calculate the parameters of the option_list 
'''
class option_compound():
    def __init__(self,option_list_short,option_list_long):
        import numpy as np
        
        self.option_list_short=option_list_short
        self.option_list_long=option_list_long
        k=list()
        for i in self.option_list_short  :
            k.append(i.k)
        for j in self.option_list_long  :
            k.append(j.k)
        self.S=np.linspace(min(k)*0.6,max(k)*1.4,1000)
            
    def value_at_maturity(self,S,r,sigma,q):
        '''
        calculate the option_list value at the minumun maturity of the option list 
        '''
        from Options.option_pricing.BSM_pricing import BSM
        from Options.option import Call,Put
        T=list()
        for i in self.option_list_short  :
            T.append(i.t)
        for j in self.option_list_long  :
            T.append(j.t)
        self.T=min(T)
        value=list()
        for i in self.option_list_short :
            if i.__class__==Call  :
                if i.t==self.T  :
                    value.append(-max(S-i.k,0)+i.p)
                else:
                    value.append(-BSM(r,sigma,i.k,S,q,i.t-self.T,'C').BSM_pricing()+i.p)
            elif i.__class__==Put  :
                if i.t==self.T  :
                    value.append(-max(i.k-S,0)+i.p)
                else:
                    value.append(-BSM(r,sigma,i.k,S,q,i.t-self.T,'P').BSM_pricing()+i.p)
        
        for i in self.option_list_long  :
            if i.__class__==Call  :
                if i.t==self.T   :
                    value.append(max(S-i.k,0)-i.p)
                else:
                    value.append(BSM(r,sigma,i.k,S,q,i.t-self.T,'C').BSM_pricing()-i.p)
            elif i.__class__==Put  :
                if i.t==self.T   :
                    value.append(max(i.k-S,0)-i.p)
                else:
                    value.append(BSM(r,sigma,i.k,S,q,i.t-self.T,'P').BSM_pricing()-i.p)
        value=sum(value)
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
        
        prob=stats.lognorm.pdf(self.S,s=sigma*self.T**0.5,scale=np.exp(np.log(S0)+(mu-0.5*sigma**2)*self.T))
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
    
            
        
        
    
    



