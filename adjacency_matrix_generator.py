# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 14:27:54 2024

@author: dmittal
"""
import networkx as nx

def adjacency_matrix_generator(network,N, z,rndseed):
    if network == 1:
        c = nx.erdos_renyi_graph(N, z/N,seed=rndseed)
    else:
        c=nx.barabasi_albert_graph(int(N), z,seed=rndseed)
        
    A= nx.adjacency_matrix(c)
    A=A.todense()
    A=A.astype('int8')
    return A