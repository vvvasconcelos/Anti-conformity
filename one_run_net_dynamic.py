# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 14:49:42 2024

@author: dmittal
"""
import numpy as np
from numba import njit


#this code is for populations with evolving preferences on networks 


# N :population size
# num_of_iter : maximum number of iterations
# x0A : intial fraction of population with choice A
# frac_w : fration of anti-conformists
# frac_oA : fraction of population preferring A
# beta : inverse temperature of fermi update function 
# A : adjacency matrix of the network of the population
# freq: rate of change of preference in case of linearly changing prefernce or frequency of sinusoidal preference
# linear: 1 for linearly changing prefernce and 0 for sinusoidal preference 
# w : list of conformities of agents 

@njit(fastmath=True)
def one_run_network_dynamic(N,num_of_iter,x0A,frac_w,beta,A,w,o):
    
    
    
    
    
    
    initial_num_A=int(np.round(N*x0A))
    initial_num_B=N-initial_num_A
    num_w=int(np.round(frac_w*N))
    
    
    
    neighbours=[] 
    degree=np.empty(N)
    for i in range(N):
        values=A[:][i]
        temp=[i for i, x in enumerate(values) if x == 1]
        neighbours.append(temp)
        degree[i]=len(temp)
    
    
    #stores time series of fraction of As in the population
    x1 = np.ones(num_of_iter, dtype=np.float32)
    
    #stores time series of fraction of As in the conforming subpopulation
    x1_c = np.ones(num_of_iter, dtype=np.float32)
    
    #stores  time series of fraction of As in the anti-conforming subpopulation
    x1_a = np.ones(num_of_iter, dtype=np.float32)
    

    
    
    
    # stores alignment of choice and preference for conforming subpopulation
    align_c=np.ones(num_of_iter, dtype=np.float32)
    
    
    # stores alignment of choice and preference for anti-conforming subpopulation
    align_a=np.ones(num_of_iter, dtype=np.float32)
        
    
    
    
    
    xa=x0A*N
    
    initial_choice_A=np.random.choice(int(N), initial_num_A,replace=False)
    temp = np.array([x for x in range(0, N) if x not in initial_choice_A])
    initial_choice_B=np.random.choice(temp, initial_num_B,replace=False)
    
          
    
    choices = np.zeros(N, dtype=np.int64)
           
    choices[initial_choice_A] = 1
    choices[initial_choice_B] = -1
    
            
    
    
    conformists=np.ones(int(N*(1-frac_w)),dtype=np.int64)
    c=0
    for iii in range(N):
        if w[iii]==1:
           conformists[c]=iii
           c=c+1

    
    
    sequence = np.random.choice(int(N), size=num_of_iter, replace=True)
    
    
    
    
    xa_conformist=0
    for agent in conformists:
        
        xa_conformist = xa_conformist + np.ceil(choices[agent]/2)

            
    
    
    for i in range(num_of_iter):
        agent=sequence[i]
        
        initial_choice = choices[agent]
        final_choice = initial_choice
        
        
        c = sum([choices[i] for i in neighbours[agent]])
        
                        
        marginal_payoff= o[i] + w[agent]*c
        
        
              

        p1 = (1 + np.exp(-marginal_payoff * beta))**(-1)
        if p1 >= np.random.random():
            final_choice = 1
        else: 
            final_choice = -1
        
        
        choices[agent] = final_choice
        
        
        xa += np.ceil((final_choice - initial_choice)/2)
        if agent in conformists:
            xa_conformist += np.ceil((final_choice - initial_choice)/2)
            
        
        x1[i] = xa / N
        x1_c[i]=xa_conformist/int(N-num_w)
        x1_a[i]=(xa-xa_conformist)/num_w
        
        if o[i]>=0:
            
            align_c[i]=x1_c[i]
            align_a[i]=x1_a[i]
        else:
            
            align_c[i]=1-x1_c[i]
            align_a[i]=1-x1_a[i]

            
        
        
    
    return np.mean(align_a),np.mean(align_c),x1_a,x1_c,x1
    
