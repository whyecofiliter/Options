def moving_average(sequence,win):
    '''
    Calculate the sequence moving average with window: win.
    input: sequence, window: win
    output: moving average sequence (maq)
    '''
    import numpy as np
    
    length=len(sequence)
    maq=np.zeros((length-win,1))
    for i in range(length-win):
        maq[i]=np.mean(sequence[i:i+win])
        
    return maq
        
    
    
    
    
 