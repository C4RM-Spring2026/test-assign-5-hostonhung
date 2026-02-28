import numpy as np

def getBondPrice(y, face, couponRate, m, ppy=1):
    
    n = m * ppy          
    rate = y / ppy          
    coupon = face * couponRate / ppy  
    
    i = np.arange(1, n + 1)           
    df = (1 + rate) ** (-i)           

    pvcf   = coupon * df                   
    pvcf[-1] += face * df[-1]
    
    return np.sum(pvcf) 
    
