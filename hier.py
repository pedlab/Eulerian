# -*- coding: utf-8 -*-
"""
Created on Wed Apr 04 14:40:43 2018

@author: alquine
"""
# File E02



# =============================================================================
# Impelementation of Hierholzers Algorithm in extracting/
# finding eulerian circuit of a simple graph G.
# main function: heir (adjacencymatrix)
# output: the set of vertices the constitutes the closed tour
#          Throws error if there is none
# =============================================================================


from toEulerian import am2ag     # File E01

def hier(M):
    return hier_loop(am2ag(G), [])

# extracts a circuit (tour) from vertex cur
def hier_circuit(G, cur, tour):
    nxt = G[cur].pop()
    if not G[cur]:
        del G[cur]
    tour.append(nxt)
    if nxt == tour[0]:
        return tour
    else:
        return hier_circuit(G, nxt, tour)
        
# replaces the vertex cut in the tour with a subtour    
def hier_replace(tour, subtour):
    if tour:
        i = tour.index(subtour[0])
        return tour[:i]+subtour+tour[i+1:]
    else:
        return subtour

# facilitator loop    
def hier_loop(G, tour):
    if G:
        k = G.keys()[0]
        cycle = [k]
        circuit = hier_circuit(G, k, cycle)
        tour = hier_replace(tour, circuit)
        return hier_loop(G, tour)
    else:
        return tour


##############################################
# Sample run, matrices from File 01: toEulerian
#################################################

# hie(M)

# hier(N)


