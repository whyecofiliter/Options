'''
Volatility and GRACH
'''


def log_return(St_before,St_now)  :
    import numpy as np
        
    if St_before!=0  :
        return np.log(St_now/St_before)
    else:
        return IOError
        
def unbiased_variance(sequence)  :
    '''
    Calculate the sequence unbiased variance
    计算序列无偏方差
    input: sequence
    return: unbiased variance
    '''
    import numpy as np
        
    return np.sum(np.square(sequence-np.mean(sequence)))/(len(sequence)-1)

def unbiased_std(sequence)  :
    '''
    Calculate the sequence unbiased standard error
    计算序列无偏标准差
    input: sequence
    return: unbiased sequence
    '''
    
    return unbiased_variance(sequence)**0.5 
    
def ordinary_return(St_before,St_now):
    if St_before !=0  :
        return (St_now-St_before)/St_before
    else:
        return IOError
        
def simplified_variance(sequence) :
    import numpy as np
        
    return np.sum(np.square(sequence))/(len(sequence))
    
def weighted_variance(sequence,weight) :
    import numpy as np
        
    return weight.T.dot(np.square(sequence))
        
def EWMA(sigma,mu,lamda) :
    import numpy as np
        
    sigma_estimated=lamda*np.square(sigma)+(1-lamda)*np.square(mu)
        
    return sigma_estimated

def moving_average_variance(sequence,win)  :
    '''
    Calculate the sequence moving average with window: win
    input: sequence  序列
           win : window 窗口
    output: ma: moving average sequence 移动平均方差序列
    '''
    import numpy as np
    
    ma=np.zeros((len(sequence)-win,1))
    for i in range(len(sequence)-win):
        ma[i]=unbiased_variance(sequence[i:i+win])
    return ma
        
def moving_average_std(sequence,win)  :
    '''
    Calculate the sequence moving average with window: win
    input: sequence  序列
           win : window 窗口
    output: ma: moving average sequence 移动平均方差序列
    '''
    import numpy as np
    
    ma=np.zeros((len(sequence)-win,1))
    for i in range(len(sequence)-win):
        ma[i]=unbiased_std(sequence[i:i+win])
    return ma    

def implied_volatility(r,k,S,q,t,PorC,price)  :
    from Options.option_pricing.BSM_pricing import BSM
    
    
    step_length=0.0001
    implied_vol=1.0
    implied_price=BSM(r,implied_vol,k,S,q,t,PorC).BSM_pricing()
    while abs(implied_price-price) >= 0.01  :
        implied_price=BSM(r,implied_vol,k,S,q,t,PorC).BSM_pricing()
        implied_vol=implied_vol-(implied_price-price)/abs(implied_price-price)*step_length
        if implied_vol<0:
            return ('Error: Implied Volatility is below zero')
        print(implied_price,price)
    
    return implied_vol
    
    
    

"""   
class GARCH():
    def ___init___(self,sequence,p,q):
        '''
        input: sequence: return sequence mu
               p: the level of recent realized volatility mu[t-1]**2
               q: the level of estimated volatility sigma[t-1]**2
        '''
        
        self.seq=sequence
        self.p=p
        self.q=q
    
    def optimization(step,precise) :
        
        
        
        
        
    def fit() :
        import numpy as np
        
        seq=self.seq
        n=len(seq)
        mu=np.zeros((n,p))
        sigma=np.zeros((n,q))
        for i in range(n):
            for j in range(p):
                if i<=p :
                    continue
                elif i>p :
                    mu[i,j]=seq[i-1-j]**2
        
        for i in range(n):
            for j in range(q):
                if i<=q :
                    continue
                elif i>q :
                    sigma[i,j]=seq[]
                    
                
        
        
        alpha_init=np.full((p,1),0.1)
        beta_init=np.full((p,1),0.1)
        omga_init=0.0000001
        estimate(omga_init,mu,sigma,alpha_init,beta_init)
        
        
        
    
    def estiamte(omga,mu,sigma,alpha,beta):
        '''
        ESTIMATE present volatility following the formula:
            sigma_estimate[t]**2=omga+alpha*mu[t-1]**2+beta*sigma[t-1]**2
        
        input:
            omga: the long average volatility
            mu: the recent realized volatility
            sigma: the estimated volatility at time t-1
            alpha: the parameter of mu
            beta: the parameter of sigma
        constraint: alpha+beta<1
        output: estimated volatility at time t
        '''
        import numpy as np
        
        sigma_estimate=omga+np.square(mu).dot(alpha)+np.square(sigma).dot(beta)
        return sigma_estimate
        
"""     
        
        
        
        
        
    
    