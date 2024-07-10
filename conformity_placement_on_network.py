# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 14:33:59 2024

@author: dmittal
"""

import numpy as np
from numba import njit

@njit(fastmath=True)
def conformity_placement_on_network(hipsters_on_hubs,N,frac_w,corr,A,conformity):
    
    degree=np.sum(A,axis=1)
    w = np.ones(N, dtype=np.int64)*conformity[1]
    num_w=int(N*frac_w)
    
    # anticonformists on hubs
    if hipsters_on_hubs==1:
        
        w = np.ones(N, dtype=np.int64)*0
        rank_list=np.argsort(degree)
        w[rank_list[-num_w:]]=1
        corr1=np.corrcoef(w,degree)[0,1]
        
        while corr1>corr:
            
            ii=np.random.choice(int(N), 2,replace=False)
            temp=w[ii[0]]
            w[ii[0]]=w[ii[1]]
            w[ii[1]]=temp

            corr1=np.corrcoef(w,degree)[0,1]
        
        for iii in range(N):
            
             if w[iii]==0:
                 w[iii]=conformity[1]
             else:
                 w[iii]=conformity[0]
    else:
        
        initial_w = np.random.choice(N,num_w,replace=False)
        w[initial_w]=conformity[0]
        
        
    return w