
def pricing(fra,forward_rate_at_time_start,discount_rate):
    import numpy as np
    
    value=fra.principle*(fra.forward_rate-forward_rate_at_time_start)*(fra.end-fra.start)*np.exp(-discount_rate*fra.end)
    return value