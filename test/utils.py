#%%
'''
Test Utils Package
'''

from Options.utils import interest_rate

def test_rate_transform():
    '''
    test function: rate_transform
    input parameters:
        if m=2 and Rm=0.1
        then Rc=0.09758
    '''
    print('Rc:',interest_rate.rate_transform(Rm=0.1,m=2))
    '''
    input parameters:
        if m=4 and Rc=0.08
        then Rm=0.0808
    '''
    print('Rm:',interest_rate.rate_transform(Rc=0.08,m=4))
    '''
    input parameters:
        if Rc=None and Rm=None
        then IOError
    '''
    print('Error:',interest_rate.rate_transform(m=1))

def test_to_forward_rate():
    '''
    test function: to_forward_rate
    input parameters:
        Maturity(years)     Rate(%)
        1                   2.0
        2                   3.0
        3                   3.7
        4                   4.2
        5                   4.5
    
    output parameters:
        Maturity(years)     Rate(%)
        1-2                 4.0
        2-3                 5.1
        3-4                 5.7
        4-5                 5.7
    '''
    from Options.rate import rate
    print(interest_rate.to_forward_rate(rate(2.0,1),rate(3.0,2)))
    print(interest_rate.to_forward_rate(rate(3.0,2),rate(3.7,3)))
    print(interest_rate.to_forward_rate(rate(3.7,3),rate(4.2,4)))
    print(interest_rate.to_forward_rate(rate(4.2,4),rate(4.5,5)))
    
    




