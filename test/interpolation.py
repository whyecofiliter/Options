'''
Testing the interpolation Package 
'''

from Options import interpolation as inpl

def test_linear():
    '''
    test:
        when R1=0.1047
             t1=0.5
             R2=0.1054
             t2=1
             t=0.75
        then R=0.10505
    '''
    R1=0.1047
    t1=0.5
    R2=0.1054
    t2=1
    t=0.75
    print('The interpolated rate:',inpl.linear(R1,t1,R2,t2,t))
    

def test_cubic_polynomial():
    '''
    test cubic_polynomial    
    '''
    from Options.rate import rate
    # time stamp
    tt=0.5
    # Rate list using for interpolation
    Rate=list()
    for i in range(6):
        '''
        Generate the Rate list for testing the function
        
        r=a*tt^3+b*tt^2+c*tt+d
        a=0.2
        b=0.5
        c=-0.1
        d=0.1
        '''
        Rate.append(rate(0.2*tt**3+0.5*tt**2-0.1*tt+0.1,tt))
        tt=tt+0.5
    
    # the time point of the interpolated rate
    ttt=2.25
    
    print('The Real Rate:',0.2*ttt**3+0.5*ttt**2-0.1*ttt+0.1)
    print('The Interpolated Rate',inpl.cubic_polynomial(Rate,t=ttt))

def test_polydyne() :
    '''
    test polydyne
    '''
    
    from Options.rate import rate
    # time stamp
    tt=0.5
    # Rate list using for interpolation
    Rate=list()
    for i in range(8):
        '''
        Generate the Rate list for testing the function
        
        r=e*tt^5+f*tt^4+a*tt^3+b*tt^2+c*tt+d
        e=0.1
        f=0.4
        a=0.2
        b=0.5
        c=-0.1
        d=0.1
        '''
        Rate.append(rate(0.1*tt**5+0.4*tt**4+0.2*tt**3+0.5*tt**2-0.1*tt+0.1,tt))
        tt=tt+0.5
    
    # the time point of the interpolated rate
    ttt=2.25
    
    print('The Real Rate:',0.1*ttt**5+0.4*ttt**4+0.2*ttt**3+0.5*ttt**2-0.1*ttt+0.1)
    print('The Interpolated Rate',inpl.polydyne(Rate,t=ttt,n=5))
    
def test_Hermit():
    '''
    test Hermit    
    '''
    from Options.rate import rate
    # time stamp
    tt=0.5
    # Rate list using for interpolation
    Rate=list()
    for i in range(6):
        '''
        Generate the Rate list for testing the function
        
        r=a*tt^3+b*tt^2+c*tt+d
        a=0.2
        b=0.5
        c=-0.1
        d=0.1
        '''
        Rate.append(rate(0.2*tt**3+0.5*tt**2-0.1*tt+0.1,tt))
        tt=tt+0.5
    
    # the time point of the interpolated rate
    ttt=2.25
    
    print('The Real Rate:',0.2*ttt**3+0.5*ttt**2-0.1*ttt+0.1)
    print('The Interpolated Rate',inpl.Hermit(Rate,t=ttt))    
    
    import numpy as np
    a=np.linspace(0.5,3,num=100)
    b=list()
    for j in a:
        b.append(inpl.Hermit(Rate,t=j))
    import matplotlib.pyplot as plt
    plt.plot(a,b)
    
    '''
    Another Example
    '''
    Rate=[rate(0.1047,0.5),rate(0.1054,1),rate(0.1068,1.5),rate(0.1081,2)]
    print(inpl.difference(Rate[0],Rate[1],Rate[2],startpoint=True))
    
def test_cubic_spline():
    '''
    test cubic spline    
    '''
    from Options.rate import rate
    # time stamp
    tt=0.5
    # Rate list using for interpolation
    Rate=list()
    for i in range(6):
        '''
        Generate the Rate list for testing the function
        
        r=a*tt^3+b*tt^2+c*tt+d
        a=0.2
        b=0.5
        c=-0.1
        d=0.1
        '''
        Rate.append(rate(0.2*tt**3+0.5*tt**2-0.1*tt+0.1,tt))
        tt=tt+0.5
    
    # the time point of the interpolated rate
    ttt=2.25
    
    print('The Real Rate:',0.2*ttt**3+0.5*ttt**2-0.1*ttt+0.1)
    print('The Interpolated Rate:',inpl.cubic_spline(Rate,t=ttt))    
    
    import numpy as np
    a=np.linspace(0.5,3,num=100)
    b=list()
    for j in a:
        b.append(inpl.cubic_spline(Rate,t=j))
    import matplotlib.pyplot as plt
    
    plt.figure('The Natural Condition')
    plt.plot(a,b,label='inter')
    
    from scipy.interpolate import CubicSpline 
    
    def value(x):
        return x.value
    def maturity(x):
        return x.maturity
    
    '''
    using scipy.interpolate.CubicSpline 
    parameters are setted
    bc_type='natural' : the second boudary condition
    extrapolate='bool' : the boudary point satisfies the inner interpolated function
    
    print and plot the result 
    '''
    cs=CubicSpline(list(map(maturity,Rate)),list(map(value,Rate)),bc_type='natural',extrapolate='bool')
    print('The scipy Rate:',cs(ttt))
    plt.plot(list(map(maturity,Rate)),list(map(value,Rate)),'o',label='data')
    plt.plot(a,cs(a),label='scipy')
    plt.legend()
    
    plt.figure('The Clamped Condition')
    c=list()
    for j in a:
        c.append(inpl.cubic_spline(Rate,t=j,bc='continue'))
    import matplotlib.pyplot as plt
    plt.plot(a,c,label='inter')    
    
    cs=CubicSpline(list(map(maturity,Rate)),list(map(value,Rate)),bc_type='clamped')
    print('The scipy Rate:',cs(ttt))
    plt.plot(list(map(maturity,Rate)),list(map(value,Rate)),'o',label='data')
    plt.plot(a,cs(a),label='scipy')
    plt.legend()    
    
def test_cubic_constraint_regress():
    '''
    Testing cubic constraint regress
    Construct the test sample
    B(0,s)= a1*s^3+b1*s^2+c1*s+d1  0<s<5
            a2*s^3+b2*s^2+c2*s+d2  5<s<15
            a3*s^3+b3*s^2+c3*s+d3  15<s<30
    
    generate the data
    a1= 0.1   b1= 0.2   c1=-0.5   d1=1
    a2= 0.2   b2=-0.5   c2= 0.3   d2=2    
    a3= 0.15  b3= 0.25  c3= 0.4   d3=0.5 
    
    interval 1 sample number: 10
    interval 2 sample number: 8
    interval 3 sample number: 3
    '''
    from Options.rate import rate
    import numpy as np
    
    # discounting factor
    Back=list()
    for i in range(10):
        s=np.random.uniform(low=0.0,high=5.0,size=1)
        a1=0.1
        b1=0.2
        c1=-0.5
        d1=1
        value=a1*s**3+b1*s**2+c1*s+d1+np.random.normal(scale=0.01)
        Back.append(rate(value,s))
    
    for i in range(8):
        s=np.random.uniform(low=5.0,high=15.0,size=1)
        a2=0.2
        b2=-0.5
        c2=0.3
        d2=2
        value=a2*s**3+b2*s**2+c2*s+d2+np.random.normal(scale=0.01)
        Back.append(rate(value,s))
        
    for i in range(10):
        s=np.random.uniform(low=15.0,high=30.0,size=1)
        a3=0.15
        b3=0.25
        c3=0.4
        d3=0.5
        value=a3*s**3+b3*s**2+c3*s+d3+np.random.normal(scale=0.01)
        Back.append(rate(value,s))   
    
    interval=list([5,15])
    
    # construct constraint
    A=np.zeros((3+len(Back),12))
    d=np.zeros((3+len(Back),1))
    A[0,0]=5**3
    A[0,1]=5**2
    A[0,2]=5
    A[0,3]=1
    A[0,4]=-5**3
    A[0,5]=-5**2
    A[0,6]=-5
    A[0,7]=-1
    d[0,0]=0
    
    A[1,4]=15**3
    A[1,5]=15**2 
    A[1,6]=15
    A[1,7]=1
    A[1,8]=-15**3
    A[1,9]=-15**2
    A[1,10]=-15
    A[1,11]=-1
    d[1,0]=0
    
    A[2,3]=1
    d[2,0]=1
    
    for i in range(10):
        A[3+i,0]=Back[i].maturity**3
        A[3+i,1]=Back[i].maturity**2
        A[3+i,2]=Back[i].maturity
        A[3+i,3]=1
        d[3+i,0]=Back[i].value
    
    for i in range(8):
        A[13+i,4]=Back[10+i].maturity**3
        A[13+i,5]=Back[10+i].maturity**2
        A[13+i,6]=Back[10+i].maturity
        A[13+i,7]=1
        d[13+i,0]=Back[10+i].value
    
    for i in range(3):
        A[21+i,8]=Back[18+i].maturity**3
        A[21+i,9]=Back[18+i].maturity**2
        A[21+i,10]=Back[18+i].maturity
        A[21+i,11]=1
        d[21+i,0]=Back[18+i].value
    
    
    constraint=list([A,d])
    
    result=inpl.cubic_constraint_regress(Back)
    result.cubic_constraint_regress(interval=interval,constraint_or_not=True)
    fit=result.fit(0.1)
#    result=result.cubic_constraint_regress()   
    def value(x):
        return x.value
    def maturity(x):
        return x.maturity
    
    value=list(map(value,Back))
    matur=list(map(maturity,Back))
    import matplotlib.pyplot as plt
    plt.plot(matur,value)
    
    matur_simu=np.linspace(0,30,1000)
    value_simu=list()
    for i in matur_simu :
        value_simu.append(result.fit(i))
    
    plt.plot(matur_simu,value_simu)
    
    return fit    


def test_NS_model():
    '''
    Testing NS_model
    construct sample:
        R(0,s)=beta_0+beta_1*(1-exp(-s/m))/(s/m)+beta_2*((1-exp(-s/m))/(s/m)-exp(-s/m))
        n=15
        beta_0=1.5
        beta_1=-0.5
        beta_2=1.0
        m_0=1.0
    '''
    
    from Options.rate import rate
    import numpy as np
    
    n=15
    R=list()
    beta_0=1.5
    beta_1=-0.5
    beta_2=1.0
    m_0=5.0
    
    # Generate R
    for i in range(n):
        if i==0  :
            R.append(rate(beta_0+beta_1,i))
        elif i>0  :
            R.append(rate(beta_0+beta_1*(1-np.exp(-i/m_0))/(i/m_0)+beta_2*((1-np.exp(-i/m_0))/(i/m_0)-np.exp(-i/m_0)),i))
    
    def value(x):
        return x.value
    def maturity(x):
        return x.maturity
    
    value=list(map(value,R))
    matur=list(map(maturity,R))
    import matplotlib.pyplot as plt
    plt.figure('NS model')
    plt.plot(matur,value)         
    
    m=list([1.0])
    t=list([1.0])
    result=inpl.NS_model(R,t=t,m=m)
    print('R with m=1.0:',result)
    
    # m = None
    result=inpl.NS_model(R,t=t,step_length=0.1,step=100000)
    print('R with m=None:',result)
    
    '''
        n=15
        beta_0=1.5
        beta_1=-0.5
        beta_2=1.0
        beta_3=0.3
        m_0=1.0
        m_1=1.5
    '''
    
    # Generate R_plus
    R_plus=list()
    beta_3=0.3
    m_1=1.5
    for i in range(n):
        if i==0  :
            R_plus.append(rate(beta_0+beta_1,i))
        elif i>0  :
            R_plus.append(rate(beta_0+beta_1*(1-np.exp(-i/m_0))/(i/m_0)+beta_2*((1-np.exp(-i/m_0))/(i/m_0)-np.exp(-i/m_0))+beta_3*((1-np.exp(-i/m_1))/(i/m_1)-np.exp(-i/m_1)),i)) 
    
    def value(x):
        return x.value
    def maturity(x):
        return x.maturity    
    
    value_plus=list(map(value,R_plus))
    matur_plus=list(map(maturity,R_plus))
    import matplotlib.pyplot as plt
    plt.figure('NSS model')
    plt.plot(matur_plus,value_plus)
    
    t=list([1.0,5.0])
    result_plus=inpl.NS_model(R_plus,t=t,mtype='NSS',step_length=0.1,step=10000)
    print('R_plus:',result_plus)
    
    from Options import interpolation as inpl
    import numpy as np
    from Options.rate import rate
    
    n=15
    R=list()
    beta_0=1.5
    beta_1=-0.5
    beta_2=1.0
    m_0=5.0
    
    # Generate R
    for i in range(n):
        if i==0  :
            R.append(rate(beta_0+beta_1,i))
        elif i>0  :
            R.append(rate(beta_0+beta_1*(1-np.exp(-i/m_0))/(i/m_0)+beta_2*((1-np.exp(-i/m_0))/(i/m_0)-np.exp(-i/m_0)),i))

    result=inpl.NS_Model(R,'NS')
    a=result.NS_m_unsetted(10.0,1000,0.01)
    print(a)
    b=list()
    for i in np.linspace(0,30,1000):
        b.append(result.NS_m_unsetted_fit(list([i])))

    import matplotlib.pyplot as plt
    plt.plot(np.linspace(0,30,1000),b)        

    
    
    
    

    
    
    
    
    
    
    
    
    
    
    