
def rate_transform(m,Rc=None,Rm=None):
    '''
    continuously compounding transforms into discrete compounding or vice versa.
    following the formula below
    Rc=mln(1+Rm/m)
    Rm=m[exp(Rc/m)-1]
    '''
    import numpy as np
    
    if Rm==None and Rc!= None  :
        Rm=m*(np.exp(Rc/m)-1)
        return Rm
    elif Rc== None and Rm!= None  :
        Rc=m*np.log(1+Rm/m)
        return Rc
    elif Rm==None and Rc==None  :
        return IOError
    
def to_forward_rate(R1,R2,compounding='c'):
    '''
    transform the spot rate into forward rate
    input parameters:
        R1: the spot rate with maturity T1
        R2: the spot rate with maturity T2
        T1<T2
        componding: way of compounding:
            'c' for continuously
            'd' for discretely
        
    output parameters:
        the forward rate: RF
        if continuously compounding, then exp[RF(T2-T1)]=exp(-R1T1)*exp(R2T2)
        if discretely compounding, then [(1+RF)**(T2-T1)]*[(1+R1)**T1]=[(1+R2)**T2]
    '''
    if compounding=='c'  :
        RF=(-R1.value*R1.maturity+R2.value*R2.maturity)/(R2.maturity-R1.maturity)
        return RF
    elif compounding=='d'  :
        RF=(((1+R2.value)**R2.maturity)/((1+R1.value)**R1.maturity))**(1/(R2.maturity-R1.maturity))-1
        return RF
    
        
    
    
    
    
    
    
    