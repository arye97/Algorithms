import copy
"""
Floyd's Algorithm
Graph is always weighted

pseudocode -->

let dist be a |V|x|V| array of minimum distances initialized to int('inf')

for each edge (u,v):
  dist[u][v] <- w(u,v) // the weight of the edge (u,v)

for k from 1 to |V|:
  for i from 1 to |V|:
     for j from 1 to |V|:
        if dist[i][j] > dist[i][k] + dist[k][j]:
           dist[i][j] <- dist[i][k] + dist[k][j]
        end if

"""


def undirected_graph(graph_str, numNodes):
   matrix = []
   for i in range(0, numNodes):
      new_list = []
      for j in range(0, numNodes):
         new_list.append(float('inf'))
      matrix.append(new_list)
   for i in range(0, len(graph_str), 3):
      node = int(graph_str[i])
      connection = int(graph_str[i + 1])
      weight = int(graph_str[i + 2])
      matrix[node][connection] = weight
      matrix[connection][node] = weight
   for i in range(0, numNodes):
      matrix[i][i] = 0
   return matrix

def directed_graph(graph_str, numNodes):
   matrix = []
   for i in range(0, numNodes):
      new_list = []
      for j in range(0, numNodes):
         new_list.append(float('inf'))
      matrix.append(new_list)
   for i in range(0, len(graph_str), 3):
      node = int(graph_str[i])
      connection = int(graph_str[i + 1])
      weight = int(graph_str[i + 2])
      matrix[node][connection] = weight
   for i in range(0, numNodes):
      matrix[i][i] = 0   
   return matrix
      

def adjacency_matrix(graph_str):
   graph_str = graph_str.split()
   direction = graph_str.pop(0)
   numNodes = int(graph_str.pop(0))
   isWeighted = graph_str.pop(0)
   if direction == 'D':
      return directed_graph(graph_str, numNodes)
   else:
      return undirected_graph(graph_str, numNodes)

def floyd(adj_matrix): #dist is matrix
   dist = copy.deepcopy(adj_matrix)
   numNodes = len(dist[0])
   for k in range(0, numNodes):
      for i in range(0, numNodes):
         for j in range(0, numNodes):
            if dist[i][j] > dist[i][k] + dist[k][j]:
               dist[i][j] = dist[i][k] + dist[k][j]
   return dist   
   
graph_str = """\
D 3 W
0 1 1
1 2 2
2 0 4
"""

adj_matrix = adjacency_matrix(graph_str)
dist_matrix = floyd(adj_matrix)

print("Adjacency matrix:", adj_matrix)
print("Distance matrix:", dist_matrix)