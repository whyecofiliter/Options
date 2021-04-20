
def discount_pricing(coupon,compounding,term_struc=None):
    '''
    calculate the discount price of the coupon
    input parameters:
        coupon: coupon class
        compounding: the way of compounding using to discount the coupon
                     'c': continuously compound
                     =coupon.compounding: follow the same compounding way as the coupon
        term struc: if term_structure is giving, the coupon discount rate is term structure not yield rate 
    output parameters:
        sum(present_value): sum the discount value of the whole before maturity.
    '''
    import numpy as np
    
    present_value=list()
    for i in range(int(coupon.maturity*coupon.compounding)):
        if term_struc==None and coupon.yield_rate!=None  :
            if i<int(coupon.maturity*coupon.compounding)-1 and compounding!='c'  :
                present_value.append((coupon.coupon_rate/coupon.compounding*coupon.principle)/((1+coupon.yield_rate/coupon.compounding)**(i+1)))
            elif i<int(coupon.maturity*coupon.compounding)-1 and compounding =='c'  :
                present_value.append(coupon.coupon_rate*coupon.principle*np.exp(-coupon.yield_rate*(i+1)/coupon.compounding))
            elif i == int(coupon.maturity*coupon.compounding)-1 and compounding!='c'  :
                present_value.append((coupon.principle+coupon.coupon_rate/coupon.compounding*coupon.principle)/((1+coupon.yield_rate/coupon.compounding)**(i+1)))
            elif i == int(coupon.maturity*coupon.compounding)-1 and compounding =='c'  :
                present_value.append((coupon.principle+coupon.coupon_rate*coupon.principle)*np.exp(-coupon.yield_rate*(i+1)/coupon.compounding))
        if term_struc!=None  :
            if i<int(coupon.maturity*coupon.compounding)-1 and compounding!='c'  :
                present_value.append((coupon.coupon_rate/coupon.compounding*coupon.principle)/((1+term_struc[i]/coupon.compounding)**(i+1)))
            elif i<int(coupon.maturity*coupon.compounding)-1 and compounding =='c'  :
                present_value.append(coupon.coupon_rate*coupon.principle*np.exp(-term_struc[i]*(i+1)/coupon.compounding))
            elif i == int(coupon.maturity*coupon.compounding)-1 and compounding!='c'  :
                present_value.append((coupon.principle+coupon.coupon_rate/coupon.compounding*coupon.principle)/((1+term_struc[i]/coupon.compounding)**(i+1)))
            elif i == int(coupon.maturity*coupon.compounding)-1 and compounding =='c'  :
                present_value.append((coupon.principle+coupon.coupon_rate*coupon.principle)*np.exp(-term_struc[i]*(i+1)/coupon.compounding))
    
    return sum(present_value)

def duration(coupon,compounding,delta=0.01):
    '''
    calculate the duration of the coupon
    input parameters:
        coupon: coupon class
        compounding: the way of compounding using to discount the coupon
                     'c': continuously compound
                     =coupon.compounding: follow the same compounding way as the coupon
        delta: the change of the yield
               delta_yield=delta*yield
    output parameters:
        dura: the coupon duration
    '''
    
    if coupon.yield_rate==None  :
        return IOError
    delta_yield=coupon.yield_rate*delta
    yield_rate_plus=delta_yield+coupon.yield_rate
    price=discount_pricing(coupon,compounding)
    coupon_plus=coupon
    coupon_plus.yield_rate=yield_rate_plus
    price_plus=discount_pricing(coupon_plus,compounding)
    dura=-(price_plus-price)/(price*delta_yield)
    return dura
    
#def convexity(coupon,compounding,delta=0.01):
    

