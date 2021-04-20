
'''
Diagonal Spreads 对角组合
'''

class diagonal_spreads():
    '''
    construct diagonal spreads
    input parameters:
        the first option with strike k1:option1
        the second option with strike k2: option2
        the type of the option Put or Call: PorC
        the type of the portfolio Positive or Negative : PorN
        the judgement of the portfolio Bear or Bull: BearorBull
        k1<k2
        T<Tstar
    '''
    def __init__(self,option1,option2,PorC,PorN,BearorBull):
        import numpy as np
        
        self.option1=option1
        self.option2=option2
        self.PorC=PorC
        self.PorN=PorN
        self.BearorBull=BearorBull
        self.S=np.linspace(min(self.option1.k,self.option2.k)*0.6,max(self.option1.k,self.option2.k)*1.4,1000)
    
    def value_at_maturity(self,S,r,sigma,q):
        from Options.option_pricing.BSM_pricing import BSM
        if self.PorC=='C' and self.PorN=='P' and self.BearorBull=='bull'  :
            '''
            Call Positive Bull portfolio
            long: call(k1,Tstar)
            short: call(k2,T)
            '''
            value=-max(S-self.option2.k,0)+BSM(r,sigma,self.option1.k,S,q,self.option1.t-self.option2.t,'C').BSM_pricing()\
                  -self.option1.p+self.option2.p
            return value
        if self.PorC=='C' and self.PorN=='N' and self.BearorBull=='bear'  :
            '''
            Call Negative Bear portfolio
            long: call(k2,T)
            short: call(k1,Tstar)
            '''
            value=max(S-self.option2.k,0)-BSM(r,sigma,self.option1.k,S,q,self.option1.t-self.option2.t,'C').BSM_pricing()\
                  -self.option2.p+self.option1.p
            return value
        if self.PorC=='C' and self.PorN=='P' and self.BearorBull=='bear'  :
            '''
            Call Positivve Bear portfolio
            long: call(k2,Tstar)
            short: call(k1,T)
            '''
            value=-max(S-self.option1.k,0)+BSM(r,sigma,self.option2.k,S,q,self.option2.t-self.option1.t,'C').BSM_pricing()\
                  -self.option2.p+self.option1.p
            return value
        if self.PorC=='C' and self.PorN=='N' and self.BearorBull=='bull'  :
            '''
            Call Negative Bull portfolio
            long: call(k1,T)
            short: call(k2,Tstar)
            '''
            value=max(S-self.option1.k,0)-BSM(r,sigma,self.option2.k,S,q,self.option2.t-self.option1.t,'C').BSM_pricing()\
                  -self.option1.p+self.option2.p
            return value
        if self.PorC=='P' and self.PorN=='P' and self.BearorBull=='bull'  :
            '''
            Put Positive Bull portfolio
            long: put(k1,Tstar)
            short: put(k2,T)
            '''
            value=-max(self.option2.k-S,0)+BSM(r,sigma,self.option1.k,S,q,self.option1.t-self.option2.t,'P').BSM_pricing()\
                  -self.option1.p+self.option2.p
            return value
        if self.PorC=='P' and self.PorN=='N' and self.BearorBull=='bear'  :
            '''
            Put Negative Bear portfolio
            long: put(k2,T)
            short: put(k1,Tstar)
            '''
            value=max(self.option2.k-S,0)-BSM(r,sigma,self.option1.k,S,q,self.option1.t-self.option2.t,'P').BSM_pricing()\
                  -self.option2.p+self.option1.p
            return value
        if self.PorC=='P' and self.PorN=='P' and self.BearorBull=='bear'  :
            '''
            Put Positive Bear
            long: put(k2,Tstar)
            short: put(k1,T)
            '''
            value=-max(self.option1.k-S,0)+BSM(r,sigma,self.option2.k,S,q,self.option2.t-self.option1.t,'P').BSM_pricing()\
                  -self.option2.p+self.option1.p
            return value
        if self.PorC=='P' and self.PorN=='N' and self.BearorBull=='bull'  :
            '''
            Put Negative Bull
            long: put(k1,T)
            short: put(k2,Tstar)
            '''
            value=max(self.option1.k-S,0)-BSM(r,sigma,self.option2.k,S,q,self.option2.t-self.option1.t,'P').BSM_pricing()\
                  -self.option1.p+self.option2.p
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
        
        T=min(self.option1.t,self.option2.t)
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
    
'''
double diagonal portfolio 双对角组合
'''
class double_diagonal():
    '''
    The portfolio have two diagonal spreads
    init parameters: 
        diagonal spread1: spread1 (class diagnoal_spreads)
        diagonal spread2: spread2 (class diagonal_spreads)
    '''
    
    def __init__(self,spread1,spread2):
        import numpy as np
        self.spread1=spread1
        self.spread2=spread2
        self.S=np.linspace(min(self.spread1.S[0],self.spread2.S[0]),max(self.spread1.S[-1],self.spread2.S[-1]),1000)
    
    def value_at_maturity(self,S,r,sigma,q):
        value=self.spread1.value_at_maturity(S,r,sigma,q)+self.spread2.value_at_maturity(S,r,sigma,q)
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
        
        T=min(self.spread1.option1.t,self.spread1.option2.t,self.spread2.option1.t,self.spread2.option2.t)
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
 
    
    
    
    
    
        
        
        



