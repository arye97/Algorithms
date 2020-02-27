	
from pprint import pprint

# undirected graph in the textbook example
"""
   Builds an Adjacency List from input in format shown below
   D (Node) 3 (Number of Nodes in Graph) W (Weighting of Edge)
   
   eg take first line
   D 3 W
   0 1 7
   Node 0 connects to Node 1 with a weighted edge of weight 7
"""
	
graph_string = """\
D 3 W
0 1 7
1 0 -2
0 2 0
"""


def adjacency_list(graph_str):
   graph_str = graph_str.split()
   isDir = graph_str.pop(0)
   numNodes = int(graph_str.pop(0))
   adj_list = []
   for i in range(numNodes):
      adj_list.append([])
   isWeighted = 'N'
   if graph_str[0].upper() == 'W':
      isWeighted = graph_str.pop(0)
   preList = [] #list contains prefinished items
   if isWeighted == 'W':
      distance = 3
   else:
      distance = 2
      weighting = None
      
   for i in range(0, len(graph_str), distance):
      if isWeighted == 'W':
         weighting = int(graph_str[i + 2])
      node = int(graph_str[i])
      connectionNode = int(graph_str[i + 1])
      if isDir == 'U':
         preList.append([connectionNode, node, weighting])
      preList.append([node, connectionNode, weighting])
         
   
   for edge in preList:
      node = edge[0]
      connectionNode = edge[1]
      weighting = edge[2]
      adj_list[node].append((connectionNode, weighting))
   
   return adj_list

print(adjacency_list(graph_string))