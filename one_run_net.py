# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 02:53:08 2021

@author: Dhruv
"""

#this code is for populations with heterogenous preferences on networks  

import numpy as np
from numba import njit


# N :population size
# num_of_iter : maximum number of iterations
# num_of_replicatres : number of replicates
# x0A : intial fraction of population with choice A
# O: strengths of the two preferences in the population e.g. [10,-10]; postive (negative) value indicating preference for A(B)  
# frac_w : fration of anti-conformists
# frac_oA : fraction of population preferring A
# beta : inverse temperature of fermi update function 
# A : adjacency matrix of the network of the population
# w : list of conformities of agents 

@njit(fastmath=True)
def one_run_network(N,num_of_iter,num_of_replicates,x0A,O,frac_w,frac_oA,beta,A,w):

    
    initial_num_A=int(np.round(N*x0A))
    
    num_oA=int(np.round(frac_oA*N))
    

    neighbours=[]
    degree=np.empty(N)
    for i in range(N):
        values=A[:][i]

        temp=[i for i, x in enumerate(values) if x == 1]
        neighbours.append(temp)
        degree[i]=len(temp)



    
    
    #assigning preference randomly 
    oA=np.random.choice( N,num_oA,replace=False)    
    o = np.ones(N, dtype=np.int32)*O[1]
    o[oA]=O[0]
   

               
    #stores alignment of choice and preference of entire population
    final_align=np.ones(num_of_replicates, dtype=np.float32)
    
    
    
    volatility=np.ones(num_of_replicates, dtype=np.float32)
    
        
    #stores equilibrium value of xA
    final_xa=np.zeros(num_of_replicates,dtype=np.float32)
    
    
    
    sequence = np.random.choice(int(N), size=num_of_iter, replace=True)
    x1=np.zeros(N,dtype=np.float64)
    
    for r in range(num_of_replicates):
        xa=x0A*N


        # assigning choice randomly (1 for A and -1 for B)
        choices = np.zeros(N, dtype=np.int32)*(-1)
        initial_choice_A=np.random.choice(int(N), initial_num_A,replace=False)
        choices[initial_choice_A] = 1
        

        cc=0


        for i in range(int(num_of_iter/N)):
            change=0
            for ii in range(N):
                agent=sequence[cc]

                initial_choice = choices[agent]
                final_choice = initial_choice

                
                a_b = sum([choices[iii] for iii in neighbours[agent]])
                marginal_payoff= o[agent] + w[agent]*a_b

                # fermi update rule of choice 
                p1 = (1 + np.exp(-marginal_payoff * beta))**(-1)
                if p1 >= np.random.random():
                    final_choice = 1
                else:
                    final_choice = -1

                choices[agent] = final_choice
                xa += (final_choice - initial_choice)/2
                
                
                change +=abs(np.ceil((final_choice-initial_choice)/2))
                cc+=1

                x1[ii] = xa/ N

            if (np.std(x1) < 0.0001) or i == int(num_of_iter/N)-1  :

                final_align[r]=(len([j for j in range(N) if (o[j]*choices[j]>0)]))/N
                final_xa[r]=xa/N
                volatility[r]=change/N
                break
            
                
                


    return np.mean(final_xa),np.mean(volatility),np.mean(final_align)



