#%%
from Options import option
from Options.portfolio_strategy import bull
from Options.portfolio_strategy import bear
from Options.portfolio_strategy import butterfly
from Options.portfolio_strategy import calendar_option
from Options.portfolio_strategy import diagonal_spreads
from Options.portfolio_strategy import straddle
from Options.portfolio_strategy import option_compound

def bull_test():
    '''
    test the vaild of bull test: the class bull
    input paramter:
        short_Call： p=5.39 k=45 maturity=30 European
        long_Call: p=10.08 k=40 maturity=30 European
    output parameter:
        if S=35 
        then portfolio.value_at_maturity()=-4.69
        if S=65
        then portfolio.value_at_maturity()=0.31
    '''
    import matplotlib.pyplot as plt
    
    short=option.Call(5.39,45,1/12,'E')
    long=option.Call(10.08,40,1/12,'E')
    portfolio=bull.bull(short,long,'C')
    print('S=35:',portfolio.value_at_maturity(35))
    print('S=65:',portfolio.value_at_maturity(65))
    plt.figure('Call Bull')
    portfolio.plot_value_at_maturity()
    '''
    test the vaild of bull test: the class bull
    input paramter:
        short_Put： p=9.96 k=60 maturity=30 European
        long_Put: p=0.02 k=40 maturity=30 European
    output parameter:
        if S=35 
        then portfolio.value_at_maturity()=-10.06
        if S=65
        then portfolio.value_at_maturity()=9.94
    '''
    short=option.Put(9.96,60,1/12,'E')
    long=option.Put(0.02,40,1/12,'E')
    portfolio=bull.bull(short,long,'P')
    print('S=35:',portfolio.value_at_maturity(35))
    print('S=65:',portfolio.value_at_maturity(65))
    plt.figure('Put Bull')
    portfolio.plot_value_at_maturity()
    '''
    plot the probability of spot price at maturity 
    Y axis: pdf(normed(log(ST/S0)))
    X axis: S
    '''
    plt.figure('probability')
    plt.plot(portfolio.S,portfolio.prob_value_at_maturity(50,0.1,0.3))
    '''
    Calculate the expected return follow the formula
    sum{return(i)*prob(i)*interval(i)}
    test validity
    if S0=65
    then expected return is around 9.90
    if S0=35
    then expected return is around -10.00
    '''
    print('expected_profit S0=35:',portfolio.expectated_profit(35,0.1,0.3))
    print('expected_profit S0=65:',portfolio.expectated_profit(65,0.1,0.3))

def bear_test():
    '''
    test the vaild of bull test: the class bull
    input paramter:
        short_Call： p=5.39 k=45 maturity=30 European
        long_Call: p=0.45 k=55 maturity=30 European
    output parameter:
        if S=35 
        then portfolio.value_at_maturity()=4.69
        if S=65
        then portfolio.value_at_maturity()=-0.31
    '''
    import matplotlib.pyplot as plt
    
    short=option.Call(5.39,45,30,'E')
    long=option.Call(0.45,55,30,'E')
    portfolio=bear.bear(short,long,'C')
    print('S=35:',portfolio.value_at_maturity(35))
    print('S=65:',portfolio.value_at_maturity(65))
    plt.figure('Call Bear')
    portfolio.plot_value_at_maturity()
    '''
    test the vaild of bull test: the class bull
    input paramter:
        short_Put： p=0.02 k=40 maturity=30 European
        long_Put: p=9.96 k=60 maturity=30 European
    output parameter:
        if S=35 
        then portfolio.value_at_maturity()=10.06
        if S=65
        then portfolio.value_at_maturity()=-9.94
    '''
    short=option.Put(0.02,40,1/12,'E')
    long=option.Put(9.96,60,1/12,'E')
    portfolio=bear.bear(short,long,'P')
    print('S=35:',portfolio.value_at_maturity(35))
    print('S=65:',portfolio.value_at_maturity(65))
    plt.figure('Put Bear')
    portfolio.plot_value_at_maturity()
    '''
    plot the probability of spot price at maturity 
    Y axis: pdf(normed(log(ST/S0)))
    X axis: S
    '''
    plt.figure('probability')
    plt.plot(portfolio.S,portfolio.prob_value_at_maturity(50,0.1,0.3))
    '''
    Calculate the expected return follow the formula
    sum{return(i)*prob(i)*interval(i)}
    test validity
    if S0=80
    then expected return is around -9.90
    if S0=35
    then expected return is around 10.00
    '''
    print('expected_profit:',portfolio.expectated_profit(35,0.1,0.3))
    print('expected_profit:',portfolio.expectated_profit(80,0.1,0.3))
    
def butterfly_test():
    '''
    test the vaild of bull test: the class bull
    input paramter:
        short_Call_1： p=1.98 k=50 maturity=30 European
        short_Call_2:  p=1.98 k=50 maturity=30 European
        long_Call_1: p=0.45 k=55 maturity=30 European
        long_Call_2: p=5.39 k=45 maturity=30 European
    output parameter:
        if S=40 
        then portfolio.value_at_maturity()=-1.88
        if S=60
        then portfolio.value_at_maturity()=-1.88
        if S=50
        then portfolio.value_at_maturity()=3.12
        if S=46.88
        then portfolio.value_at_maturity()=0
        if S=53.12
        then portfolio.value_at_maturity()=0
    '''
    import matplotlib.pyplot as plt
    
    short_1=option.Call(1.98,50,30,'E')
    short_2=option.Call(1.98,50,30,'E')
    long_1=option.Call(0.45,55,30,'E')
    long_2=option.Call(5.39,45,30,'E')
    portfolio=butterfly.butterfly(short_1,short_2,long_1,long_2,'C')
    print('S=40:',portfolio.value_at_maturity(40))
    print('S=60:',portfolio.value_at_maturity(60))
    print('S=50:',portfolio.value_at_maturity(50))
    print('S=46.88:',portfolio.value_at_maturity(46.88))
    print('S=53.12:',portfolio.value_at_maturity(53.12))
    plt.figure('Call Butterfly')
    portfolio.plot_value_at_maturity()
    '''
    test the vaild of bull test: the class bull
    input paramter:
        short_Put： p=0.02 k=40 maturity=30 European
        long_Put: p=9.96 k=60 maturity=30 European
    output parameter:
        if S=40 
        then portfolio.value_at_maturity()=-18.9
        if S=60
        then portfolio.value_at_maturity()=-18.9
        if S=50
        then portfolio_value_at_maturity()=3.11
        if S=46.89
        then portfolio_value_at_maturity()=0
        if S=53.11
        then portfolio_value_at_maturity()=0
    '''
    short_1=option.Put(1.89,50,1/12,'E')
    short_2=option.Put(1.89,50,1/12,'E')
    long_1=option.Put(5.36,55,1/12,'E')
    long_2=option.Put(0.31,45,1/12,'E')
    portfolio=butterfly.butterfly(short_1,short_2,long_1,long_2,'P')
    print('S=40:',portfolio.value_at_maturity(40))
    print('S=60:',portfolio.value_at_maturity(60))
    print('S=50:',portfolio.value_at_maturity(50))
    print('S=46.89:',portfolio.value_at_maturity(46.89))
    print('S=53.11:',portfolio.value_at_maturity(53.11))
    plt.figure('Put Butterfly')
    portfolio.plot_value_at_maturity()
    '''
    plot the probability of spot price at maturity 
    Y axis: pdf(normed(log(ST/S0)))
    X axis: S
    '''
    plt.figure('probability')
    plt.plot(portfolio.S,portfolio.prob_value_at_maturity(50,0.1,0.3))
    '''
    Calculate the expected return follow the formula
    sum{return(i)*prob(i)*interval(i)}
    test validity
    if S0=80
    then expected return is around -9.90
    if S0=35
    then expected return is around 10.00
    '''
    print('expected_profit:',portfolio.expectated_profit(40,0.1,0.3))
    print('expected_profit:',portfolio.expectated_profit(50,0.1,0.3))
    print('expected_profit:',portfolio.expectated_profit(60,0.1,0.3))  
    
def calendar_option_test():
    '''
    test the vaild of calendar_option : the class calendar_option 
    input paramter:
        short_early_Call：p=1.98 k=50 maturity=30/360 European
        long_late_Call: p=2.91 k=50 maturity=65/360 European
        mu=0.1
        sigma=33.33%
        q=0
        r=0.015
        
    output parameter:
        if S=50
        then portfolio.value_at_maturity()=1.17
        if S=40
        then portfolio.value_at_maturity()=-0.90
        if S=47.19
        then portfolio.value_at_maturity()=0
        if S=53.35
        then portfolio.value_at_maturity()=0
        if S=60
        then portfolio.value_at_maturity()=around -0.5
    '''
    import matplotlib.pyplot as plt
    
    short_early_Call=option.Call(1.98,50,30/360,'E')
    long_late_Call=option.Call(2.91,50,65/360,'E')
    portfolio=calendar_option.calendar_option(short_early_Call,long_late_Call,'P')
    print('S=50:',portfolio.value_at_maturity(50,0.015,0.3333,0))
    print('S=40:',portfolio.value_at_maturity(40,0.015,0.3333,0))
    print('S=47.19:',portfolio.value_at_maturity(47.19,0.015,0.3333,0))
    print('S=53.35:',portfolio.value_at_maturity(53.35,0.015,0.3333,0))
    print('S=60:',portfolio.value_at_maturity(60,0.015,0.3333,0))
    plt.figure('Profit')
    portfolio.plot_value_at_maturity(0.015,0.3333,0)
    plt.figure('probability')
    plt.plot(portfolio.S,portfolio.prob_value_at_maturity(50,0.1,0.3333))
    plt.grid()
    print('expected_profit:',portfolio.expectated_profit(40,0.1,0.3333,0.015,0))
    print('expected_profit:',portfolio.expectated_profit(50,0.1,0.3333,0.015,0))
    print('expected_profit:',portfolio.expectated_profit(60,0.1,0.3333,0.015,0)) 
    '''
    input parameter
    '''
    
def diagonal_spreads_test():
    '''
    test the validity of diagonal_spreads.
    input parameter:
        short_early_Call_k1: p=0.34 k=50 maturity=30/360 European
        long_late_Call_k2：p=0.51 k=55 maturity=93/360 European
        mu=0.1
        sigma=33.33%
        q=0
        r=0.015
        
    output parameters:
        if S=50
        then portfolio.value_at_maturity()=0.93
        if S=60
        then portfolio.value_at_maturity()=-3.76
        if S=35
        then portfolio.value_at_maturity()=around -0.20
        if S=51.35
        then portfolio.value_at_maturity()=0
        if S=44.04
        then portfolio.value_at_maturity()=0
    '''
    import matplotlib.pyplot as plt
    
    short_early_Call_k1=option.Call(0.34,50,30/360,'E')
    long_late_Call_k2=option.Call(0.51,55,93/360,'E')
    portfolio=diagonal_spreads.diagonal_spreads(short_early_Call_k1,long_late_Call_k2,'C','P','bear')
    print('S=50:',portfolio.value_at_maturity(50,0.015,0.3333,0))
    print('S=60:',portfolio.value_at_maturity(60,0.015,0.3333,0))
    print('S=35:',portfolio.value_at_maturity(35,0.015,0.3333,0))
    print('S=51.35:',portfolio.value_at_maturity(51.35,0.015,0.3333,0))
    print('S=44.04:',portfolio.value_at_maturity(44.04,0.015,0.3333,0))
    plt.figure('Profit_diagonal_spreads')
    portfolio.plot_value_at_maturity(0.015,0.3333,0)
    plt.grid()
    plt.figure('probability_diagonal_spreads')
    plt.plot(portfolio.S,portfolio.prob_value_at_maturity(50,0.1,0.3333))
    plt.grid()
    print('expected_profit:',portfolio.expectated_profit(40,0.1,0.3333,0.015,0))
    print('expected_profit:',portfolio.expectated_profit(50,0.1,0.3333,0.015,0))
    print('expected_profit:',portfolio.expectated_profit(60,0.1,0.3333,0.015,0)) 


def double_diagonal_test():
    import matplotlib.pyplot as plt
    '''
    input parameters:
        spread1:
            Call_Positive_bear spread
            short_early_call_k1: p=0.45, k1=55, t=30/360
            long_late_call_k2: p=0.38, k2=60, t=65/360
        spread2:
            Put_Positive_bull spread
            long_late_Put_k1: p=0.15, k1=40, t=65/360
            short_early_Put_k2: p=0.31, k2=45, t=30/360
    output parameters:
        if S=45
        then portfolio.value_at_maturity()=around 0.50
        if S=55
        then portfolio.value_at_maturity()=0.91
        if S=44.43
        then portfolio.value_at_maturity()=0
        if S=56.22
        then portfolio.value_at_maturity()=0
        if S=40
        then portfolio.value_at_maturity()=-3.16
        if S=60
        then portfolio.value_at_maturity()=around -2.10
    '''
    short_early_Call_k1=option.Call(0.45,55,30/360,'E')
    long_late_Call_k2=option.Call(0.38,60,65/360,'E')
    long_late_Put_k1=option.Put(0.15,40,65/360,'E')
    short_early_Put_k2=option.Put(0.31,45,30/360,'E')
    spread1=diagonal_spreads.diagonal_spreads(short_early_Call_k1,long_late_Call_k2,'C','P','bear')
    spread2=diagonal_spreads.diagonal_spreads(long_late_Put_k1,short_early_Put_k2,'P','P','bull')
    portfolio=diagonal_spreads.double_diagonal(spread1,spread2)
    print('S=45:',portfolio.value_at_maturity(45,0.015,0.3333,0))
    print('S=55:',portfolio.value_at_maturity(55,0.015,0.3333,0))
    print('S=44.43:',portfolio.value_at_maturity(44.43,0.015,0.3333,0))
    print('S=56.22:',portfolio.value_at_maturity(56.22,0.015,0.3333,0))
    print('S=40:',portfolio.value_at_maturity(40,0.015,0.3333,0))
    print('S=60:',portfolio.value_at_maturity(60,0.015,0.3333,0))
    plt.figure('Profit_double_spreads')
    portfolio.plot_value_at_maturity(0.015,0.3333,0)
    plt.grid()
    plt.figure('probability_double_spreads')
    plt.plot(portfolio.S,portfolio.prob_value_at_maturity(50,0.1,0.3333))
    plt.grid()
    print('expected_profit:',portfolio.expectated_profit(40,0.1,0.3333,0.015,0))
    print('expected_profit:',portfolio.expectated_profit(50,0.1,0.3333,0.015,0))
    print('expected_profit:',portfolio.expectated_profit(60,0.1,0.3333,0.015,0)) 
    
    '''
    input parameters:
        spread1:
            Call_Positive_bear spread
            short_early_call_k1: p=0.45, k1=55, t=30/360
            long_late_call_k2: p=0.38, k2=60, t=65/360
        spread2:
            Put_Positive_bull spread
            long_late_Put_k1: p=0.15, k1=40, t=65/360
            short_early_Put_k2: p=0.31, k2=45, t=30/360
            
    output parameters:
        if S=50
        then portfolio.value_at_maturity()=2.77
        if S=40
        then portfolio.value_at_maturity()=-2.94
        if S=60
        then portfolio.value_at_maturity()=-2.25
        if S=46.95
        then portfolio.value_at_maturity()=0
        if S=53.59
        then portfolio.value_at_maturity()=0
    '''
    short_early_Call_k1=option.Call(1.98,50,30/360,'E')
    long_late_Call_k2=option.Call(1.16,55,65/360,'E')
    long_late_Put_k1=option.Put(0.85,45,65/360,'E')
    short_early_Put_k2=option.Put(1.89,50,30/360,'E')
    spread1=diagonal_spreads.diagonal_spreads(short_early_Call_k1,long_late_Call_k2,'C','P','bear')
    spread2=diagonal_spreads.diagonal_spreads(long_late_Put_k1,short_early_Put_k2,'P','P','bull')
    portfolio=diagonal_spreads.double_diagonal(spread1,spread2)
    print('S=50:',portfolio.value_at_maturity(50,0.015,0.3333,0))
    print('S=40:',portfolio.value_at_maturity(40,0.015,0.3333,0))
    print('S=60:',portfolio.value_at_maturity(60,0.015,0.3333,0))
    print('S=46.95:',portfolio.value_at_maturity(46.95,0.015,0.3333,0))
    print('S=53.59:',portfolio.value_at_maturity(53.59,0.015,0.3333,0))
    plt.figure('Profit_double_spreads with same strikes')
    portfolio.plot_value_at_maturity(0.015,0.3333,0)
    plt.grid()
    plt.figure('probability_double_spreads with same strikes')
    plt.plot(portfolio.S,portfolio.prob_value_at_maturity(50,0.1,0.3333))
    plt.grid()
    print('expected_profit:',portfolio.expectated_profit(40,0.1,0.3333,0.015,0))
    print('expected_profit:',portfolio.expectated_profit(50,0.1,0.3333,0.015,0))
    print('expected_profit:',portfolio.expectated_profit(60,0.1,0.3333,0.015,0))     
 
    '''
    input parameters:
        spread1:
            Call_Positive bear spread
            short_early_call_k1: p=0.45, k1=55, t=30/360
            long_late_call_k2: p=0.38, k2=60, t=65/360
        spread2: 
            Put_Positive bull spread
            long_late_put_k1: p=0.85, k1=45, t=65/360
            short_early_put_k2: p=1.89, k2=50, t=30/360
    
    output parameters:
        if S=55 
        then portfolio.value_at_maturity()=1.84
        if S=40
        then portfolio.value_at_maturity()=-3.69
        if S=48.14
        then portfolio.value_at_maturity()=0
        if S=57.55
        then portfolio.value_at_maturity()=0
    '''
    short_early_Call_k1=option.Call(0.45,55,30/360,'E')
    long_late_Call_k2=option.Call(0.38,60,65/360,'E')
    long_late_put_k1=option.Put(0.85,45,65/360,'E')
    short_early_put_k2=option.Put(1.89,50,30/360,'E')
    spread1=diagonal_spreads.diagonal_spreads(short_early_Call_k1,long_late_Call_k2,'C','P','bear')
    spread2=diagonal_spreads.diagonal_spreads(long_late_put_k1,short_early_put_k2,'P','P','bull')
    portfolio=diagonal_spreads.double_diagonal(spread1,spread2)
    print('S=55:',portfolio.value_at_maturity(55,0.015,0.3333,0))
    print('S=40:',portfolio.value_at_maturity(40,0.015,0.3333,0))
    print('S=48.14:',portfolio.value_at_maturity(48.14,0.015,0.3333,0))
    print('S=57.55:',portfolio.value_at_maturity(57.55,0.015,0.3333,0))
    plt.figure('Profit_double_spreads with positive bull')
    portfolio.plot_value_at_maturity(0.015,0.3333,0)
    plt.grid()
    plt.figure('probability_double_spreads with positive bull')
    plt.plot(portfolio.S,portfolio.prob_value_at_maturity(50,0.1,0.3333))
    plt.grid()
    print('expected_profit:',portfolio.expectated_profit(40,0.1,0.3333,0.015,0))
    print('expected_profit:',portfolio.expectated_profit(50,0.1,0.3333,0.015,0))
    print('expected_profit:',portfolio.expectated_profit(60,0.1,0.3333,0.015,0))        
 
    '''
    input parameters:
        spread1:
            Call_Positive bear spread
            short_early_call_k1: p=0.45, k1=55, t=30/360
            long_late_call_k2: p=0.38, k2=60, t=65/360
        spread2: 
            Put_Positive bull spread
            long_late_put_k1: p=0.85, k1=45, t=65/360
            short_early_put_k2: p=1.89, k2=50, t=30/360
    
    output parameters:
        if S=50 
        then portfolio.value_at_maturity()=1.54
        if S=60
        then portfolio.value_at_maturity()=-3.28
        if S=43.51
        then portfolio.value_at_maturity()=0
        if S=52.06
        then portfolio.value_at_maturity()=0
    '''
    short_early_Call_k1=option.Call(1.98,50,30/360,'E')
    long_late_Call_k2=option.Call(1.16,55,65/360,'E')
    long_late_put_k1=option.Put(0.15,40,65/360,'E')
    short_early_put_k2=option.Put(0.31,45,30/360,'E')
    spread1=diagonal_spreads.diagonal_spreads(short_early_Call_k1,long_late_Call_k2,'C','P','bear')
    spread2=diagonal_spreads.diagonal_spreads(long_late_put_k1,short_early_put_k2,'P','P','bull')
    portfolio=diagonal_spreads.double_diagonal(spread1,spread2)
    print('S=50:',portfolio.value_at_maturity(50,0.015,0.3333,0))
    print('S=60:',portfolio.value_at_maturity(60,0.015,0.3333,0))
    print('S=43.51:',portfolio.value_at_maturity(43.51,0.015,0.3333,0))
    print('S=52.06:',portfolio.value_at_maturity(52.06,0.015,0.3333,0))
    plt.figure('Profit_double_spreads with positive bear')
    portfolio.plot_value_at_maturity(0.015,0.3333,0)
    plt.grid()
    plt.figure('probability_double_spreads with positive bear')
    plt.plot(portfolio.S,portfolio.prob_value_at_maturity(50,0.1,0.3333))
    plt.grid()
    print('expected_profit:',portfolio.expectated_profit(40,0.1,0.3333,0.015,0))
    print('expected_profit:',portfolio.expectated_profit(50,0.1,0.3333,0.015,0))
    print('expected_profit:',portfolio.expectated_profit(60,0.1,0.3333,0.015,0))     
    
def straddle_test():
    '''
    test the validity of diagonal_spreads.
    input parameter:
        call: p=1.98 k=50 maturity=30/360 European
        put：p=1.89 k=50 maturity=30/360 European
        mu=0.1
        sigma=33.33%
        q=0
        r=0.015
        
    output parameters:
        if S=50
        then portfolio.value_at_maturity()=-3.87
        if S=60
        then portfolio.value_at_maturity()=6.32
        if S=46.13
        then portfolio.value_at_maturity()=0
        if S=53.87
        then portfolio.value_at_maturity()=0
    '''
    import matplotlib.pyplot as plt
    
    call=option.Call(1.98,50,30/360,'E')
    put=option.Put(1.89,50,30/360,'E')
    portfolio=straddle.straddle(call,put)
    print('S=50:',portfolio.value_at_maturity(50))
    print('S=60:',portfolio.value_at_maturity(60))
    print('S=46.13:',portfolio.value_at_maturity(46.13))
    print('S=53.87:',portfolio.value_at_maturity(53.87))
    plt.figure('Profit')
    portfolio.plot_value_at_maturity()
    plt.grid()
    plt.figure('probability')
    plt.plot(portfolio.S,portfolio.prob_value_at_maturity(50,0.1,0.3333))
    plt.grid()
    print('expected_profit:',portfolio.expectated_profit(40,0.1,0.3333))
    print('expected_profit:',portfolio.expectated_profit(50,0.1,0.3333))
    print('expected_profit:',portfolio.expectated_profit(60,0.1,0.3333))  
    
    '''
    input parameter:
        call: p=0.45 k=55 maturity=30/360 European
        put：p=0.31 k=45 maturity=30/360 European
        mu=0.1
        sigma=33.33%
        q=0
        r=0.015
        
    output parameters:
        if S=50
        then portfolio.value_at_maturity()=-0.76
        if S=65
        then portfolio.value_at_maturity()=9.42
        if S=44.24
        then portfolio.value_at_maturity()=0
        if S=55.76
        then portfolio.value_at_maturity()=0
    '''
    call=option.Call(0.45,55,30/360,'E')
    put=option.Put(0.31,45,30/360,'E')
    portfolio=straddle.straddle(call,put)
    print('S=50:',portfolio.value_at_maturity(50))
    print('S=65:',portfolio.value_at_maturity(65))
    print('S=44.24:',portfolio.value_at_maturity(44.24))
    print('S=55.76:',portfolio.value_at_maturity(55.76))
    plt.figure('Profit_strangle')
    portfolio.plot_value_at_maturity()
    plt.grid()
    plt.figure('probability_strangle')
    plt.plot(portfolio.S,portfolio.prob_value_at_maturity(50,0.1,0.3333))
    plt.grid()
    print('expected_profit:',portfolio.expectated_profit(40,0.1,0.3333))
    print('expected_profit:',portfolio.expectated_profit(50,0.1,0.3333))
    print('expected_profit:',portfolio.expectated_profit(60,0.1,0.3333)) 
    
def option_compound_test():
    import matplotlib.pyplot as plt 
    '''
    input parameters:
        spread1:
            Call_Positive bear spread
            short_early_call_k1: p=0.45, k1=55, t=30/360
            long_late_call_k2: p=0.38, k2=60, t=65/360
        spread2: 
            Put_Positive bull spread
            long_late_put_k1: p=0.85, k1=45, t=65/360
            short_early_put_k2: p=1.89, k2=50, t=30/360
    
    output parameters:
        if S=50 
        then portfolio.value_at_maturity()=1.54
        if S=60
        then portfolio.value_at_maturity()=-3.28
        if S=43.51
        then portfolio.value_at_maturity()=0
        if S=52.06
        then portfolio.value_at_maturity()=0
    '''
    short_early_Call_k1=option.Call(1.98,50,30/360,'E')
    long_late_Call_k2=option.Call(1.16,55,65/360,'E')
    long_late_put_k1=option.Put(0.15,40,65/360,'E')
    short_early_put_k2=option.Put(0.31,45,30/360,'E')
    option_list_short=[short_early_Call_k1,short_early_put_k2]
    option_list_long=[long_late_Call_k2,long_late_put_k1]
    portfolio=option_compound.option_compound(option_list_short,option_list_long)
    print('S=50:',portfolio.value_at_maturity(50,0.015,0.3333,0))
    print('S=60:',portfolio.value_at_maturity(60,0.015,0.3333,0))
    print('S=43.51:',portfolio.value_at_maturity(43.51,0.015,0.3333,0))
    print('S=52.06:',portfolio.value_at_maturity(52.06,0.015,0.3333,0))
    plt.figure('Profit_double_spreads with positive bear')
    portfolio.plot_value_at_maturity(0.015,0.3333,0)
    plt.grid()
    plt.figure('probability_double_spreads with positive bear')
    plt.plot(portfolio.S,portfolio.prob_value_at_maturity(50,0.1,0.3333))
    plt.grid()
    print('expected_profit:',portfolio.expectated_profit(40,0.1,0.3333,0.015,0))  
    print('expected_profit:',portfolio.expectated_profit(50,0.1,0.3333,0.015,0))
    print('expected_profit:',portfolio.expectated_profit(60,0.1,0.3333,0.015,0)) 
    
    '''
    input parameter:
        call: p=0.45 k=55 maturity=30/360 European
        put：p=0.31 k=45 maturity=30/360 European
        mu=0.1
        sigma=33.33%
        q=0
        r=0.015
        
    output parameters:
        if S=50
        then portfolio.value_at_maturity()=-0.76
        if S=65
        then portfolio.value_at_maturity()=9.42
        if S=44.24
        then portfolio.value_at_maturity()=0
        if S=55.76
        then portfolio.value_at_maturity()=0
    '''
    call=option.Call(0.45,55,30/360,'E')
    put=option.Put(0.31,45,30/360,'E')
    option_list_short=[]
    option_list_long=[call,put]
    portfolio=option_compound.option_compound(option_list_short,option_list_long)
    print('S=50:',portfolio.value_at_maturity(50,0.015,0.3333,0))
    print('S=65:',portfolio.value_at_maturity(65,0.015,0.3333,0))
    print('S=44.24:',portfolio.value_at_maturity(44.24,0.015,0.3333,0))
    print('S=55.76:',portfolio.value_at_maturity(55.76,0.015,0.3333,0))
    plt.figure('Profit_strangle')
    portfolio.plot_value_at_maturity(0.015,0.3333,0)
    plt.grid()
    plt.figure('probability_strangle')
    plt.plot(portfolio.S,portfolio.prob_value_at_maturity(50,0.1,0.3333))
    plt.grid()
    print('expected_profit:',portfolio.expectated_profit(40,0.1,0.3333,0.015,0))
    print('expected_profit:',portfolio.expectated_profit(50,0.1,0.3333,0.015,0))
    print('expected_profit:',portfolio.expectated_profit(60,0.1,0.3333,0.015,0)) 
 









