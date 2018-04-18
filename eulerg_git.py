# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 13:47:14 2018

@author: taculin
"""

# =============================================================================
# The main function of this file returns the set of edges to be added to a non-eulerian graph to make it eulerian
# main function: toEulerian (adjacencyMatrix)
# =============================================================================



import numpy as np

# =============================================================================
# adjacency matrix to adjacency graph
# =============================================================================
def am2ag(M):
    G = dict()
    for [x,y] in np.transpose(np.nonzero(M)):
        if x not in G:
            G[x] = [y]
        else:
            G[x].append(y)
    return G

# =============================================================================
# adjacency graph to incidence graph
# =============================================================================
def ag2ig(G):
    H = dict()
    for v in G:
        for u in G[v]:
            if u not in H:
                H[u] = [v]
            else:
                H[u].append(v)
    return H


# =============================================================================
# X = {v such that indeg(v)>outdeg(v)}
# Y = {v such that indeg(v)<outdeg(v)}    
# =============================================================================
def getXY(G):
    H = ag2ig(G)
    X = [item for sublist in [[x]*(len(G[x])-len(H[x])) for x in G if x in H and len(G[x])>len(H[x])] for item in sublist]
    X.extend([x for x in G if not x in H])
    Y = [item for sublist in [[y]*(len(H[y])-len(G[y])) for y in G if y in H and len(G[y])<len(H[y])] for item in sublist]
    Y.extend([y for y in H if not y in G])    
    return Y, X

# =============================================================================
# checks if edge e is in graph G or in set of vertices E
# =============================================================================
def isIn(G,E,e):
    x,y=e
    return (x in G and y in G[x]) or (e in E)

# =============================================================================
# moves valid edges from F to E
# =============================================================================
def updateE(G,E,F):
    NK=[]
    for e in F:
        if isIn(G,E,e):
            NK.append(e)
        else:
            E.append(e)
    return E,NK

# =============================================================================
# since (u,w) [u in X and w in Y] is not a valid edge, then find a v such that (u,v) is valid
# =============================================================================
def findV(G,E,u):
    for v in G:
        if v!=u and not isIn(G,E,(u,v)) and (v,u) not in E:
            return v
    return u

# =============================================================================
# facilitates the recursive loop
# G is the original graph (which is not mutated in this loop)
# E is the set of edges that forms the partial solution
# X and Y are set of vertices v such that indeg(v)>outdege(v) or < respectively
# i is a dummy value that increments as the recursion goes further    
# =============================================================================
import itertools
def recr(G, E, X, Y, i):
    for F in itertools.permutations(zip(X,Y)):
        OK,NK = updateE(G,E,F)
        
        if NK:
            Q,V = zip(*NK)
            
            u = Q[:1][0]
            v = findV(G,OK,u)
            if u==v:
                continue
            return recr(G,[(u,v)]+OK,(v,)+Q[1:],V,i+1)
        else:
            return OK
#no solution
    return 'No solution'

# =============================================================================
# The main function
# input: M is the adjacency matrix of a simple, strongly connected graph
# output: a) is a set of tuple the represents the edges to be added to make G eulerian
#         b) 'no solution' if none exists
# =============================================================================
def toEulerian(M):
    G = am2ag(M)
    X,Y=getXY(G)
    return recr(G,[],X,Y,0)


# =============================================================================
#
#   SAMPLE RUNS
#
# >> M =
# [[0, 1, 1, 1, 1],
#  [0, 0, 1, 1, 1],
#  [0, 1, 0, 1, 1],
#  [1, 0, 0, 0, 1],
#  [0, 0, 0, 1, 0]]
# 
# >> main(M)
# Output: [(3, 2), (3, 1), (4, 0), (4, 1), (4, 2), (1, 0), (2, 0)]
# 
# 
# >> N =
# [[0, 0, 0, 0, 1, 0, 0, 0],
#  [1, 0, 0, 0, 0, 1, 0, 0],
#  [1, 1, 0, 0, 0, 0, 0, 0],
#  [0, 0, 1, 0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0, 1, 0, 0],
#  [0, 0, 0, 0, 0, 0, 1, 0],
#  [0, 1, 0, 0, 0, 0, 0, 1],
#  [0, 0, 1, 1, 0, 0, 0, 0]]
# 
# >> main(N)
# Output: [(0, 6), (5, 7)]
# 
# >> O = 
# [[0, 1, 1, 0, 0],
#  [0, 0, 1, 0, 1],
#  [0, 0, 0, 1, 0],
#  [0, 0, 0, 0, 1],
#  [1, 0, 0, 0, 0]]
# 
# >> main(M2)
# Output: [(2, 0), (4, 1)]
# =============================================================================
