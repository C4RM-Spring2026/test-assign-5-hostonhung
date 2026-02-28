import numpy as np
def getBondDuration(y, face, couponRate, m, ppy=1):
   
    n = m * ppy          
    rate = y / ppy          
    coupon = face * couponRate / ppy  
    
    i = np.arange(1, n + 1)           
    df = (1 + rate) ** (-i)  
    cf = np.full(n, coupon)       
    cf[-1] += face                     
    pvcf = cf * df                  
    duration = np.sum(pvcf * i) / np.sum(pvcf)  
    return duration / ppy




    