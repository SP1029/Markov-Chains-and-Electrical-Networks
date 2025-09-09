# Libraries
import random 
import numpy as np
import igraph as ig

# Depth First Search
def dfs(u, adj, visited):
    visited[u] = 1
    for v in adj[u]:
        if visited[v] == 0:
            dfs(v,adj,visited)


# Check if graph is connected
def is_connected(adj):
    n = len(adj)
    u = 0
    
    visited = [0] * n
    dfs(0,adj,visited)
    
    if sum(visited)!=n:
        return False
    else:
        return True

  
# Generate a random graph
def generate_graph(n):
    adj = {}
    for u in range(n):
        adj[u] = []
        
    for u in range(n):
        for v in range(u+1,n):
            p = random.random()**2
            if random.random() < p**2:
                adj[u].append(v)
                adj[v].append(u)
                
    return adj


# Take next step in random walk
def take_step(u, adj):
    return random.choice(adj[u])


# Calculate effecetive resitance between two nodes
# By injecting 1A current and calculating Voltage difference
def Ruv(u,v,adj):
    
    n = len(adj)
    M = np.zeros([n,n])
    I = np.zeros([n,1])

    # Create M
    for i in range(n):
        M[i][i] = len(adj[i])
        for j in adj[i]:
            M[i][j] = -1

    # Set V[v] = 0
    for i in range(n):
        M[v][i] = 0
    M[v][v] = 1

    # Add current=1 at u
    I[u] = 1

    # Ruv = V[u]
    V = np.linalg.inv(M) @ I
    return float(V[u])


