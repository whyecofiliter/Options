'''
Interpolation Package
MAINLY USING FOR TERM STRUCTURE
'''

def linear(R1,t1,R2,t2,t) :
    '''
    input : 
       R1,R2: the interest rate of two terminals of the interval
       t1,t2: the time point of the two terminals and t1<t2
       t: the time point of the interpolated interest rate
    output :
        R: the interpolated interest rate 
    '''
    R=R1+(R2-R1)*(t-t1)/(t2-t1)
    return R

def linear_spline(Rate,t):
    
    def take(elem) :
        return elem.maturity
    Rate.sort(key=take)
    
    # judge which interval the maturity belongs
    def judge_maturity(Rate,t):
        for i in range(len(Rate)):
            if t<=Rate[i].maturity  :
                return i
        return len(Rate)
    
    num=judge_maturity(Rate,t)
    return linear(Rate[num-1].value,Rate[num-1].maturity,Rate[num].value,Rate[num].maturity,t)
    
    
def cubic_polynomial(Rate,t):
    '''
    The cubic polynomial is of the form
    r(s)=a*(s^3)+b*(s^2)+c*s+d
    A=B.dot(C)
    
    input :
        Rate: list of the rate
        t: the time point of the interpolated interest rate
    output:
        R: the interpolated interest rate
    '''
    import numpy as np
    # select 4 different rate
    rate_list=np.random.choice(Rate,size=4,replace=False)
    A=list()
    B=list()
    for i in rate_list :
        A.append(i.value)
        B.append([i.maturity**3,i.maturity**2,i.maturity,1])
    A=np.array(A)
    B=np.array(B)
    C=np.linalg.inv(B).dot(A)
    b=np.array([t**3,t**2,t,1])
    R=b.dot(C)
    return R
    
def polydyne(Rate,t,n):
    '''
    The polydyne is of the form
    r(s)=a*(s^n)+b*(s^(n-1))+c*(s^(n-2))+...+d
    A=B.dot(C)
    
    input :
        Rate: list of the rate
        t: the time point of the interpolated interest rate
        n: the degree of the polynomial
    output:
        R: the interpolated interest rate
    '''
    import numpy as np
    
    # select 4 different rate
    if len(Rate)<n+1 :
        return IOError
    
    rate_list=np.random.choice(Rate,size=n+1,replace=False)
    A=list()
    B=list()
    for i in rate_list :
        A.append(i.value)
        for j in range(n) :
            B.append(i.maturity**(n-j))
        B.append(1)
    A=np.array(A)
    B=np.array(B)
    B=B.reshape((n+1,n+1))
    C=np.linalg.inv(B).dot(A)
    b=list()
    for j in range(n) :
        b.append(t**(n-j))
    b.append(1)
    b=np.array(b)
    R=b.dot(C)
    return R

def difference(rate1,rate,rate2,startpoint=False,endpoint=False) :
    '''
    Calculate the difference at point i 
    '''
    sb=rate1.maturity
    sa=rate2.maturity
    si=rate.maturity
    rb=rate1.value
    ra=rate2.value
    ri=rate.value
    
    if startpoint==False and endpoint==False  :
        dri=1/(sa-sb)*((sa-si)*(ri-rb)/(si-sb)+(si-sb)*(ra-ri)/(sa-si))
        return dri
    elif startpoint==True and endpoint==False  :
        dri=1/(sa-sb)*((sa+si-2*sb)*(ri-rb)/(si-sb)-(si-sb)*(ra-ri)/(sa-si))
        return dri
    elif startpoint==False and endpoint==True  :
        dri=1/(sa-sb)*((sa-si)*(ri-rb)/(si-sb)-(2*sa-si-sb)*(ra-ri)/(sa-si))
        return dri

def Hermit(Rate,t):
    '''
    The Rate are interpolated by Hermit interpolate
    USING Hermit interpolation
    '''

    def take(elem) :
        return elem.maturity
    Rate.sort(key=take)
    
    pb=0
    pa=0
    for i in range(len(Rate)) :
        if t>Rate[i].maturity :
            pb=i
            pa=pb+1
    
    h=Rate[pa].maturity-Rate[pb].maturity
    ta=Rate[pa].maturity
    tb=Rate[pb].maturity
    ra=Rate[pa].value
    rb=Rate[pb].value
    if pb==0 :
        dyb=difference(Rate[pb],Rate[pb+1],Rate[pb+2],startpoint=True)
        dya=difference(Rate[pa-1],Rate[pa],Rate[pa+1])
    elif pb>0 and pa<len(Rate)-1 :
        dyb=difference(Rate[pb-1],Rate[pb],Rate[pb+1])
        dya=difference(Rate[pa-1],Rate[pa],Rate[pa+1])
    elif pa==len(Rate)-1 :
        dyb=difference(Rate[pb-1],Rate[pb],Rate[pb+1])
        dya=difference(Rate[pa-2],Rate[pa-1],Rate[pa],endpoint=True)
        
    alpha_b=((h+2*(t-tb))*(t-ta)**2)/(h**3)*rb
    alpha_a=((h+2*(t-ta))*(t-tb)**2)/(h**3)*ra
    beta_b=((t-tb)*(t-ta)**2)/(h**2)*dyb
    beta_a=((t-tb)**2*(t-ta))/(h**2)*dya
    H=alpha_a+alpha_b+beta_a+beta_b
    
    return H

def Rate_to_Discount(Rate):
    import numpy as np
    from Options.rate import rate
    
    def take(elem) :
        return elem.maturity
    Rate.sort(key=take)
    
    def value(x):
        return x.value
    def maturity(x):
        return x.maturity    
    
    value=list(map(value,Rate))
    matur=list(map(maturity,Rate))
    
    Discount=list()
    for i in range(len(value)):
        Discount.append(rate(np.exp(-value[i]*matur[i]),matur[i]))
        
    return Discount

def Discount_to_Rate(Discount):
    import numpy as np
    from Options.rate import rate
    
    def take(elem) :
        return elem.maturity
    Discount.sort(key=take)
    
    def value(x):
        return x.value
    def maturity(x):
        return x.maturity    
    
    value=list(map(value,Discount))
    matur=list(map(maturity,Discount))
    
    Rate=list()
    for i in range(len(value)):
        Rate.append(rate(-np.log(value[i])/matur[i],matur[i]))
        
    return Rate
       
def cubic_spline(Rate,t,bc='natural',para=None):
    '''
    The Rate are interpolated by cubic spline
    '''
    import numpy as np
    
    n=len(Rate)-1
    X=np.zeros((4*n,4*n))
    B=np.ndarray((4*n,1))
    
    '''
    Arrange the Rate on maturity
    '''
    
    def take(elem) :
        return elem.maturity
    Rate.sort(key=take)
    
    '''
    judge the interval of the interpolated t
    '''
    pb=0
    for i in range(len(Rate)) :
        if t>Rate[i].maturity :
            pb=i
    
    '''
    interpolation condition
    '''
    j=0
    for i in range(n-1):
        X[i,j]=Rate[i+1].maturity**3
        X[i,j+1]=Rate[i+1].maturity**2
        X[i,j+2]=Rate[i+1].maturity
        X[i,j+3]=1
        B[i]=Rate[i+1].value
        j=j+4
    
    '''
    Connnection Condition
    '''
    j=0
    for i in range(n-1):
        X[n-1+i,j]=-3*Rate[i+1].maturity**2
        X[n-1+i,j+1]=-2*Rate[i+1].maturity
        X[n-1+i,j+2]=-1
        X[n-1+i,j+4]=3*Rate[i+1].maturity**2
        X[n-1+i,j+5]=2*Rate[i+1].maturity
        X[n-1+i,j+6]=1
        B[n-1+i]=0
        j=j+4
    
    j=0
    for i in range(n-1) :
        X[2*n-2+i,j]=-6*Rate[i+1].maturity
        X[2*n-2+i,j+1]=-2
        X[2*n-2+i,j+4]=6*Rate[i+1].maturity
        X[2*n-2+i,j+5]=2
        B[2*n-2+i]=0
        j=j+4
        
    j=0
    for i in range(n-1):
        X[3*n-3+i,j]=-Rate[i+1].maturity**3
        X[3*n-3+i,j+1]=-Rate[i+1].maturity**2
        X[3*n-3+i,j+2]=-Rate[i+1].maturity
        X[3*n-3+i,j+3]=-1
        X[3*n-3+i,j+4]=Rate[i+1].maturity**3
        X[3*n-3+i,j+5]=Rate[i+1].maturity**2
        X[3*n-3+i,j+6]=Rate[i+1].maturity
        X[3*n-3+i,j+7]=1
        B[3*n-3+i]=0
        j=j+4
    
    '''
    Boundary Condition
    '''
    
    X[4*n-4,0]=Rate[0].maturity**3
    X[4*n-4,1]=Rate[0].maturity**2
    X[4*n-4,2]=Rate[0].maturity
    X[4*n-4,3]=1
    B[4*n-4]=Rate[0].value
    
    X[4*n-3,4*n-4]=Rate[-1].maturity**3
    X[4*n-3,4*n-3]=Rate[-1].maturity**2
    X[4*n-3,4*n-2]=Rate[-1].maturity
    X[4*n-3,4*n-1]=1
    B[4*n-3]=Rate[-1].value
    
    if bc=='natural'  :
        '''
        the natural is the second boundary condition
        '''
        X[4*n-2,0]=6*Rate[0].maturity
        X[4*n-2,1]=2
        B[4*n-2]=0
    
        X[4*n-1,4*n-4]=6*Rate[-1].maturity
        X[4*n-1,4*n-3]=2
        B[4*n-1]=0
    elif bc=='continue'  :
        '''
        the continue is the first boundary condition
        '''
        X[4*n-2,0]=3*Rate[0].maturity**2
        X[4*n-2,1]=2*Rate[0].maturity
        X[4*n-2,2]=1
        B[4*n-2]=0
        
        X[4*n-1,4*n-4]=3*Rate[-1].maturity**2
        X[4*n-1,4*n-3]=2*Rate[-1].maturity
        X[4*n-1,4*n-2]=1
        B[4*n-1]=0
        
    elif bc=='setting_natural'  :
        '''
        the setting is that the boundary condition is setted with certain condition
        '''
        X[4*n-2,0]=6*Rate[0].maturity
        X[4*n-2,1]=2
        B[4*n-2]=para[0]
    
        X[4*n-1,4*n-4]=6*Rate[-1].maturity
        X[4*n-1,4*n-3]=2
        B[4*n-1]=para[1]
    
    elif bc=='setting_continue'  :
        X[4*n-2,0]=3*Rate[0].maturity**2
        X[4*n-2,1]=2*Rate[0].maturity
        X[4*n-2,2]=1
        B[4*n-2]=para[0]
        
        X[4*n-1,4*n-4]=3*Rate[-1].maturity**2
        X[4*n-1,4*n-3]=2*Rate[-1].maturity
        X[4*n-1,4*n-2]=1
        B[4*n-1]=para[1]        
    
    else:
        return IOError
        
    A=np.linalg.inv(X).dot(B)
    R=A[4*pb]*t**3+A[4*pb+1]*t**2+A[4*pb+2]*t+A[4*pb+3]
    
    return R[0]
#    return np.linalg.inv(X).dot(B)
#    return X,B

class cubic_constraint_regress():
    '''
    Cubic constraint regress class
    instead of analyzing Rate, analyse the discount factor: Discount
    The relation formula is 
        Discount(0,s)=exp(Rate(0,s)*s)
    The regress funtion is 
    Discount(0,s)=a1*s**3+b1*s**2+c1*s+d1   if s in interval 1
                  a2*s**3+b2*s**2+c2*s+d2   if s in interval 2
                  ...
                  an*s**3+bn*s**2+cn*s+dn   if s in interval n
    WITH n-1 continuous constraint : 
    a1*s**3+b1*s**2+c1*s+d1=a2*s**3+b2*s**2+c2*s+d2  at the joint point between interval 1 and 2
    ...
    a[n-1]*s**3+b[n-1]*s**2+c[n-1]*s+d[n-1]=an*s**3+bn*s**2+cn*s+dn at the joint point between interval n-1 and n
    WITH boundary condition
    Discount(0,0)=1
    '''
    def __init__(self,Rate):
        '''
        initial parameters:
            Rate: the analyzed Term Structure
        initial function:
            judge_maturity
        '''
        self.rate=Rate
        self.judge_maturity
    
    def judge_maturity(self,interval,maturity):
        '''
        judge which interval the maturity belongs
        input: interval: the interval for the whole term structure
               maturity: the maturity of the rate i
        output: len(interval): which interval the maturity belongs
        '''
        for i in range(len(interval)):
            if maturity<=interval[i]  :
                return i
        return len(interval)
    
    def cubic_constraint_regress(self,number=2,interval=None,constraint=None,constraint_or_not=True,omga=None):
        '''
        The Rate are constructed by constraint regress
        input:
            Rate:  the interpolated yield curve
            t:  the interpoalted rate at time point t
            number:  the number of interval 
            interval:  the interval point of cut points
            constraint:  the constraint of the regression
            constraint_or_not : having or having not constraint 
                                if True, then having constraint
                                if False, then having not constraint
        if number is given, then the interval are cutted into equal length
        output: regress parameter
        '''
        import numpy as np
        Rate=self.rate
    
        def take(elem) :
            return elem.maturity
        Rate.sort(key=take)
    
        # the numbers of parameters    
        if interval!=None  :
            number=len(interval)+1
            b=4*number
        else:
            interval=list()
            b=4*number
            mlength=Rate[-1].maturity-Rate[0].maturity
            for i in range(number-1):
                interval.append(mlength/number*(i+1))
        
        self.interval=interval
    
        # the number of the samples
        n=len(Rate)
        # the parameters
        self.beta=np.zeros((b,1))
        # the variable Y
        f=np.zeros((n,1))
        ''' the constraint matrix satisfies
            A*beta=0
        '''
        if constraint != None and constraint_or_not==True  :
            A=constraint[0]
            d=constraint[1]
        elif constraint==None and constraint_or_not==True  :
            m=len(interval)+1
            A=np.zeros((m,b))
            d=np.zeros((m,1))
            
            ''' boundary condition
                B[0,0]=1
            '''
            A[0,3]=1
            d[0,0]=1
            
            '''
            continue condition 
            B[i]-=B[i-1]+
            '''
            for i in range(1,len(interval)+1):
                A[i,4*(i-1)]=interval[i-1]**3
                A[i,4*(i-1)+1]=interval[i-1]**2
                A[i,4*(i-1)+2]=interval[i-1]
                A[i,4*(i-1)+3]=1
                A[i,4*i]=-interval[i-1]**3
                A[i,4*i+1]=-interval[i-1]**2
                A[i,4*i+2]=-interval[i-1]
                A[i,4*i+3]=-1
          
        X=np.zeros((b,n))
        for j in range(n)  :
            mjudge=self.judge_maturity(interval,Rate[j].maturity)
            X[4*mjudge,j]=Rate[j].maturity**3
            X[4*mjudge+1,j]=Rate[j].maturity**2
            X[4*mjudge+2,j]=Rate[j].maturity
            X[4*mjudge+3,j]=1
            f[j]=Rate[j].value
        
        from numpy.linalg import inv
            
        if constraint_or_not==None and omga==None  :
            self.beta=inv(X.dot(X.T)).dot(X).dot(f)
            return self.beta
        elif constraint_or_not==None and omga!=None  :
            self.beta=inv(X.dot(inv(omga)).dot(X.T)).dot(X).dot(inv(omga)).dot(f)
            return self.beta
        elif constraint_or_not!=None and omga==None :
            self.beta=inv(X.dot(X.T)).dot(X).dot(f)+inv(X.dot(X.T)).dot(A.T).dot(inv(A.dot(inv(X.dot(X.T))).dot(A.T))).dot(d-A.dot(inv(X.dot(X.T)).dot(X).dot(f)))
            return self.beta
        elif constraint_or_not!=None and omga!=None  :
            self.beta=inv(X.dot(inv(omga)).dot(X.T)).dot(X).dot(inv(omga)).dot(f)+inv(X.dot(inv(omga)).dot(X.T)).dot(A.T).dot(inv(A.dot(inv(X.dot(inv(omga)).dot(X.T))).dot(A.T))).dot(d-A.dot(inv(X.dot(X.T)).dot(X).dot(f)))
            return self.beta
        
    def fit(self,t):
        '''
        fit the regressed model
        input: t: the fitted maturity
        output: the rate for the fitted maturity
        '''
        import numpy as np
        X=np.zeros((len(self.beta),1))
        mjudge=self.judge_maturity(self.interval,t)
        X[4*mjudge,0]=t**3
        X[4*mjudge+1,0]=t**2
        X[4*mjudge+2,0]=t
        X[4*mjudge+3,0]=1
        
        return self.beta.T.dot(X)[0,0]
        
def plot_Rate(Rate):
    '''
    plot term structure:
    input: Rate: the term structure list
    output: plot the term structure
    '''
    import matplotlib.pyplot as plt
    def value(x):
        return x.value
    def maturity(x):
        return x.maturity

    value=list(map(value,Rate))
    matur=list(map(maturity,Rate))
    plt.plot(matur,value,label='Rate')  
    


class NS_Model():
    '''
    Nelson-Siegel Model
    the basic function form NS model:
    R(0,s)=beta0+beta1*(1-exp(-s/m))/(s/m)+beta2*{[1-exp(-s/m)]/(s/m)-exp(-s/m)}
    the advanced function form NSS model:
    R(0,s)=beta0+beta1*(1-exp(-s/m))/(s/m)+beta2*{[1-exp(-s/m1)]/(s/m1)-exp(-s/m1)}+beta3*{[1-exp(-s/m2)]/(s/m2)-exp(-s/m2)}
    WITH or WITHOUT boundary condition:
    R(0,0)=0
    '''
    def __init__(self,Rate,mtype,bc=False):
        '''
        initial parameters:
            input: Rate: term structure
                   mtype: if 'NS', then using NS model
                          if 'NSS', then using NSS model
                   bc: with or without boundary condition
                       if 'False', then without condition
                       if 'True', then with condition
        '''
        def take(elem) :
            '''
            take the elem's maturity
            '''
            return elem.maturity
        # sort on the maturity
        Rate.sort(key=take)
        self.Rate=Rate
        
        def value(x):
            return x.value
        def maturity(x):
            return x.maturity    

        self.matur=list(map(maturity,self.Rate))
        self.value=list(map(value,self.Rate))
        self.mtype=mtype
        self.bc=bc
        
        
    def NS_m_Setted(self,m):
        '''
        calibration the NS model with fixed m
        input:  
            the yield curve: Rate
            the interpolated time point: t
            the parameter m determined or not determined 
                if determined, then m != None
                if not determined, then m=None
            the model type: mtype
                if mtype='NS', then the model is NS model
                if mtype='NSS', then the model is NSS model
        output:
            the interpolated rate
        '''
        import numpy as np
        from numpy.linalg import inv
        
        Rate=self.Rate
        mtype=self.mtype
        
    
        n=len(Rate)
        f=np.zeros((n,1))
    
        if mtype=='NS'  :
            b=3
            self.b=b
            m=list([m])
        elif mtype=='NSS'  :
            b=4
            self.b=b
        else:
            return IOError
    
        X=np.zeros((b,n))
    
        A=np.zeros((1,b))
        d=np.zeros((1,1))
        A[0,0]=1
        A[0,1]=1
        
        for j in range(n):
            s=Rate[j].maturity
            X[0,j]=1
            if s==0  :
                X[1,j]=1
                X[2,j]=0
            elif s>0  :
                X[1,j]=(1-np.exp(-s/m[0]))/(s/m[0])
                X[2,j]=(1-np.exp(-s/m[0]))/(s/m[0])-np.exp(-s/m[0])
            f[j]=Rate[j].value
            if b==4  :
                if s==0  :
                    X[3,j]=0
                elif s>0  :
                    X[3,j]=(1-np.exp(-s/m[1]))/(s/m[1])-np.exp(-s/m[1])
        
        self.X=X
        self.f=f
        
        para=np.zeros((b,1))
        if self.bc==False:
            para=inv(X.dot(X.T)).dot(X).dot(f)
        elif self.bc==True :
            para=inv(X.dot(X.T)).dot(X).dot(f)+inv(X.dot(X.T)).dot(A.T).dot(inv(A.dot(inv(X.dot(X.T))).dot(A.T))).dot(d-A.dot(inv(X.dot(X.T)).dot(X).dot(f)))
        
        self.m_para=para
        self.m=m
        self.X=X
        
        return para
    
    def NS_m_setted_fit(self,t):
        '''
        fit the NS model with m fixed
        input : t: the fitted maturity
        output: f_hat: the rate on the fitted maturity
        '''
        import numpy as np
        
        b=self.b
        m=self.m
        m=list([m])
        para=self.m_para
        
        Xt=np.zeros((b,len(t)))
        for j in range(len(t)):
            Xt[0,j]=1
            Xt[1,j]=(1-np.exp(-t[j]/m[0]))/(t[j]/m[0])
            Xt[2,j]=(1-np.exp(-t[j]/m[0]))/(t[j]/m[0])-np.exp(-t[j]/m[0])
            if b==4  :
                Xt[3,j]=(1-np.exp(-t[j]/m[1]))/(t[j]/m[1])-np.exp(-t[j]/m[1])
        
        f_hat=Xt.T.dot(para)
        return f_hat

    
    def optimization(self,m_initial,step,precise) :
        '''
        optimize the loss fucntion using gradient descent
        input: m_initial: the setted initial value of m
              step: the step using for optimization
              precise: the step length for each iteration
        output: the optimized parameter: m 
        '''
        import numpy as np
        
        last_m=0.9*m_initial
        m=m_initial
        for i in range(step):
            e1=np.log(self.error(last_m))
            e2=np.log(self.error(m))
            temp=last_m
            last_m=m
            if self.mtype=='NS' and m==temp :
                return m
            elif self.mtype=='NSS' and (m==temp).all() :
                return m
            m=m-precise*(e2-e1)/(m-temp)
        return m
    
    def error(self,m):
        '''
        calculate the total squared error between the fit value and the real value
        input: the parameter m
        output: the total squared error
        '''
        import numpy as np
        
        estimate=np.array(self.value)-self.NS_m_Setted(m).T.dot(self.X)[0]
        return sum(estimate**2)
    
    
    def NS_m_unsetted(self,m_initial,step,precise):
        '''
        calibration the NS model with unfixed m
        input: m_initial: the initial value of m
               step: the iteration step for optimization
               precise: the step length for each iteration
        output: the parameter calibrated
        '''
        m=self.optimization(m_initial,step,precise)
        self.m=m
        return [self.NS_m_Setted(m),m]
    
    def NS_m_unsetted_fit(self,t):
        '''
        fit the NS model with unfixed m
        input: t: the fitted maturity
        output: the fitted rate at the maturity t
        '''
        import numpy as np
        
        b=self.b
        m=self.m
        m=list(m)
        para=self.m_para
        
        Xt=np.zeros((b,len(t)))
        for j in range(len(t)):
            Xt[0,j]=1
            Xt[1,j]=(1-np.exp(-t[j]/m[0]))/(t[j]/m[0])
            Xt[2,j]=(1-np.exp(-t[j]/m[0]))/(t[j]/m[0])-np.exp(-t[j]/m[0])
            if b==4  :
                Xt[3,j]=(1-np.exp(-t[j]/m[1]))/(t[j]/m[1])-np.exp(-t[j]/m[1])
        
        f_hat=Xt.T.dot(para)
        return f_hat[0,0]
        
    