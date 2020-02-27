"""
Finds what adapters a charger plug needs to use to get to a
wall socket using Dijkstra's Algorithm
"""

from collections import deque

def adjacency_list(graph_str):
   graph_str = graph_str.split()
   isDir = graph_str.pop(0)
   numNodes = int(graph_str.pop(0))
   adj_list = []
   if len(graph_str) <= 1:
      for i in range(numNodes):
         adj_list.append([[i, None]])
         return adj_list
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
   


def adapter_chain(adapters_info, charger_plug, wall_socket):
   graph = adjacency_list(adapters_info)
   processed = []
   queue = [[charger_plug]]
   
   if charger_plug == wall_socket:
      return [charger_plug]
   
   while queue:
      path = queue.pop(0)
      node = path[-1]
      if node not in processed:
         neighbours = graph[node]
         for neighbour in neighbours:
            new_path = list(path)
            new_path.append(neighbour[0])
            queue.append(new_path)
            if new_path[-1] == wall_socket:
               return new_path
            
         processed.append(node)
   return "CS Unplugged!"
    


adapters_info_str = """\
D 5
0 1
0 2
1 2
2 3
1 3
3 0
"""

print(adapter_chain(adapters_info_str, 1, 0))
#[1, 3, 0]
print(adapter_chain(adapters_info_str, 0, 3) in [[0, 1, 3], [0, 2, 3]])
#True
print(adapter_chain(adapters_info_str, 4, 4))
#[4]
print(adapter_chain(adapters_info_str, 3, 3))
#[3]
print(adapter_chain(adapters_info_str, 3, 2))
#[3,0,2]
print(adapter_chain(adapters_info_str, 3, 4))
#CS Unplugged!