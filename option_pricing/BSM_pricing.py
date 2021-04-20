'''
BSM Pricing model
'''

class BSM():
    def __init__(self,r,sigma,k,S,q,t,PorC):
        '''
        input parameter:
        interest rate: r
        volatility: sigma
        strike price: k
        spot price: S
        dividend rate: q
        maturity: t
        Put or Call: PorC
        '''
        self.r=r
        self.sigma=sigma
        self.k=k
        self.S=S
        self.q=q
        self.t=t  
        self.PorC=PorC
    
    def BSM_pricing(self):
        from scipy.stats import norm
        import numpy as np
        d1=(np.log(self.S/self.k)+(self.r-self.q+(self.sigma**2)/2)*self.t)/(self.sigma*self.t**0.5)
        d2=d1-self.sigma*self.t**0.5
        if self.PorC=='C' :
            self.c=self.S*np.exp(-self.q*self.t)*norm.cdf(d1)-self.k*np.exp(-self.r*self.t)*norm.cdf(d2)
            return self.c
        elif self.PorC=='P' :
            self.p=-self.S*np.exp(-self.q*self.t)*norm.cdf(-d1)+self.k*np.exp(-self.r*self.t)*norm.cdf(-d2)
            return self.p
    
    def delta(self):
        '''
        Greeks: delta
        delta=d_option/d_S
        '''
        from scipy.stats import norm
        import numpy as np
        d1=(np.log(self.S/self.k)+(self.r-self.q+(self.sigma**2)/2)*self.t)/(self.sigma*self.t**0.5)
        if self.PorC=='C'  :
            delta=np.exp(-self.q*self.t)*norm.cdf(d1)
            return delta
        elif self.PorC=='P'  :
            delta=np.exp(-self.q*self.t)*(norm.cdf(d1)-1)
            return delta
    
    def gamma(self):
        '''
        Greeks: gamma
        gamma=d^2_option/d_S^2
        '''
        from scipy.stats import norm
        import numpy as np
        
        d1=(np.log(self.S/self.k)+(self.r-self.q+(self.sigma**2)/2)*self.t)/(self.sigma*self.t**0.5)
        gamma=norm.pdf(d1)/(self.S*self.sigma*self.t**0.5)*np.exp(-self.q*self.t)
        return gamma
    
    def theta(self):
        '''
        Greeks: theta
        theta=d_option/d_t
        '''
        from scipy.stats import norm
        import numpy as np
        
        d1=(np.log(self.S/self.k)+(self.r-self.q+(self.sigma**2)/2)*self.t)/(self.sigma*self.t**0.5)
        d2=d1-self.sigma*self.t**0.5
        if self.PorC=='C'  :
            theta=-self.S*norm.pdf(d1)*self.sigma*np.exp(-self.q*self.t)/(2*self.t**0.5)+self.q*self.S*norm.cdf(d1)*np.exp(-self.q*self.t)-self.r*self.k*np.exp(-self.r*self.t)*norm.cdf(d2)
            return theta
        elif self.PorC=='P'  :
            theta=-self.S*norm.pdf(d1)*self.sigma*np.exp(-self.q*self.t)/(2*self.t**0.5)-self.q*self.S*norm.cdf(-d1)*np.exp(-self.q*self.t)+self.r*self.k*np.exp(-self.r*self.t)*norm.cdf(-d2)
            return theta
        
    def vega(self):
        '''
        Greeks: vega
        vega=d_option/d_sigma
        '''
        
        from scipy.stats import norm
        import numpy as np
        
        d1=(np.log(self.S/self.k)+(self.r-self.q+(self.sigma**2)/2)*self.t)/(self.sigma*self.t**0.5)
        vega=self.S*self.t**0.5*norm.pdf(d1)*np.exp(-self.q*self.t)
        return vega
    
    def rho(self):
        '''
        Greeks: rho
        rho=d_option/d_r
        '''
        
        from scipy.stats import norm
        import numpy as np
        
        d1=(np.log(self.S/self.k)+(self.r-self.q+(self.sigma**2)/2)*self.t)/(self.sigma*self.t**0.5)
        d2=d1-self.sigma*self.t**0.5
        if self.PorC=='C'  :
            rho=self.k*self.t*np.exp(-self.r*self.t)*norm.cdf(d2)
            return rho
        elif self.PorC=='P'  :
            rho=-self.k*self.t*np.exp(-self.r*self.t)*norm.cdf(-d2)
            return rho
        
        
            
        
        
        
    
        
        