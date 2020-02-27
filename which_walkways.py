"""
SuperQuiz1 Q4

Green Campus
Walkways between classes on Uni Campus
"""

def adjacency_list(graph_str):
   graph_str = graph_str.split()
   str_len = len(graph_str)
   #print(graph_str)
   isDir = graph_str.pop(0)
   numNodes = int(graph_str.pop(0))
   #print(numNodes)
   #print(len(graph_str))
   adj_list = []
   if str_len <= 2:
      for i in range(0, numNodes):
         adj_list.append([(i, None)])
      return adj_list
   for i in range(numNodes):
      adj_list.append([])
   isWeighted = 'N'
   #print(graph_str)
   if len(graph_str) != 0:
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


def bfs_connected_component(graph, start):
   explored = []
   queue = [start]
   while queue:
      node = queue.pop(0)
      if node not in explored:
         explored.append(node)
         neighbours = graph[node]
         for neighbour in neighbours:
            queue.append(neighbour[0])
   return sorted(explored)


def which_walkways(campus_map):
   adj_list = adjacency_list(campus_map)
   return adj_list
    
campus_map = """\
U 3 W
0 1 1
2 1 2
2 0 4
"""

print(sorted(which_walkways(campus_map)))