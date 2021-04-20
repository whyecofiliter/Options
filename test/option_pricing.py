#%% test option prcing 

from Options.option_pricing import BSM_pricing

def test_BSM_pricing():
    print(BSM_pricing.BSM(0.1,0.3,50,50,0,0.5,'C').BSM_pricing())
    
def test_greeks():
    '''
    input parameters:
        call:
            S=49, K=50, r=0.05, T=0.3846, sigma=0.2
    output parameters:
        d1=0.0542
        delta=N(d1)=0.522
        theta=-4.31
        gamma=0.066
        vega=12.1
        rho=8.91
    '''
    r=0.05
    sigma=0.2
    k=50
    S=49
    q=0
    t=0.3846
    PorC='C'
    portfolio=BSM_pricing.BSM(r,sigma,k,S,q,t,PorC)
    print('Delta of the call:',portfolio.delta())
    print('Theta of the call:',portfolio.theta())
    print('Gamma of the call:',portfolio.gamma())
    print('Vega of the call:',portfolio.vega())
    print('Rho of the call:',portfolio.rho())
    
    
    