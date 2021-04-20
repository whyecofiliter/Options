#%%
from Options.interest_rate_pricing import coupon_pricing
from Options.bond import coupon

def test_coupon_pricing():
    
    '''
    input parameters:
        principle : 100
        coupon_rate : 8% or 0.08 
        maturity : 1.5 years 
        compounding : 2 per year
        yield_rate : 10.4% or 0.104
    output parameters:
        present_value=96.74
    '''
    coupon_pricing.discount_pricing(coupon(principle=100,coupon_rate=0.08,maturity=1.5,compounding=2,yield_rate=0.104),compounding=2)

    '''
    input parameters:
        principle : 100
        coupon_rate : 8% or 0.08 
        maturity : 1.5 years 
        compounding : 2 per year
        yield_rate : 10.4% or 0.104
        term_struc: [10% 10% 10.42%] or [0.1 0.1 0.1042]

    output parameters:
        present_value=96.74
    '''
    coupon_pricing.discount_pricing(coupon(principle=100,coupon_rate=0.08,maturity=1.5,compounding=2,yield_rate=0.104),compounding=2,term_struc=[0.1,0.1,0.1042])

    '''
    input parameters:
        principle : 100
        coupon_rate : 8% or 0.08 
        maturity : 5 years 
        compounding : 1 per year
        yield_rate : 7.0% or 0.07
        contimuously compounding

    output parameters:
        present_value=103.0512
    '''
    coupon_pricing.discount_pricing(coupon(principle=100,coupon_rate=0.08,\
                                           maturity=5,compounding=1,yield_rate=0.07),compounding='c')

    '''
    input parameters:
        principle : 100
        coupon_rate : 8% or 0.08 
        maturity : 5 years 
        compounding : 1 per year
        yield_rate : 11.0% or 0.11
        contimuously compounding

    output parameters:
        present_value=103.0512
    '''

    coupon_pricing.discount_pricing(coupon(principle=100,coupon_rate=0.08,\
                                           maturity=5,compounding=1,yield_rate=0.11),compounding='c')


from Options.interest_rate_pricing import fra_pricing
from Options.bond import fra

def test_fra_pricing():
    '''
    input parameters:
        principle : 1,000,000
        foward_rate : 5% or 0.05
        start: 1 year
        end : 1+3/12=1.25 years
        foward_rate_at_time_start : 4.5% or 0.045
        discount_rate : 3.6% or 0.036
    '''
    fra_agreement=fra(principle=1000000,forward_rate=0.05,start=1,end=1.25)
    print('FRA1:',fra_pricing.pricing(fra_agreement,0.045,0.036))

    '''
    input parameters:
        principle : 1,000,000
        foward_rate : 9.5% or 0.09
        start: 1 year
        end : 1+3/12=1.25 years
        foward_rate_at_time_start : 9.102% or 0.09102
        discount_rate : 8.6% or 0.086
    
    output parameters:
        value=893.56
    '''
    fra_agreement=fra(principle=1000000,forward_rate=0.095,start=1,end=1.25)
    print('FRA2:',fra_pricing.pricing(fra_agreement,0.09102,0.086))

    '''
    input parameters:
        principle : 1,000,000
        foward_rate : 5.5% or 0.055
        start: 2 year
        end : 3 years
        foward_rate_at_time_start : 5% or 0.05
        discount_rate : 3.7% or 0.037
    
    output parameters:
        value=893.56
    '''
    fra_agreement=fra(principle=1000000,forward_rate=0.055,start=2,end=3)
    print('FRA3:',fra_pricing.pricing(fra_agreement,0.05,0.037))

from Options.interest_rate_pricing.coupon_pricing import duration

def test_duration():
    '''
    input parameters:
        coupon: 5-year bond 
                11% coontinuously compounding yield
                8% coupon rate
        compounding: 'c'
        delta=0.01
    output parameters:
        dura: Duration = 4.245
    '''
    bond=coupon(100,0.08,5,1,yield_rate=0.11)
    print('bond price:',coupon_pricing.discount_pricing(bond,'c'))
    print('Duration:',duration(bond,compounding='c'))
    
#def test_convexity():
    '''
    input 
    '''
    
    
    
    
    
    
    
    
    
    
    
    

