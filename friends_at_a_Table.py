"""
COSC262 UC 2019

undirected graph

People want to be seated at the same table with people they are directly friends with,
or can become friends with if a friend or a chain of friends can introduce them.

found using breadth-first-search
"""

def adjacency_list(graph_str):
   graph_str = graph_str.split()
   str_len = len(graph_str)
   isDir = graph_str.pop(0)
   numNodes = int(graph_str.pop(0))
   adj_list = []
   if str_len <= 2:
      for i in range(0, numNodes):
         adj_list.append([(i, None)])
      return adj_list
   for i in range(numNodes):
      adj_list.append([])
   isWeighted = 'N'
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


def arrangement(direct_friendship_info):
   adj_list = adjacency_list(direct_friendship_info)
   tables = []
   numNodes = len(adj_list)
   for i in range(0, numNodes):
      new_table = bfs_connected_component(adj_list, i)
      if len(tables) > 0:
         if new_table not in tables:
            tables.append(new_table)
      else:
         tables.append(new_table)
      print(tables)
         
   return tables
    




	
direct_friendship_info = """\
U 7
1 4
2 0
4 6
5 3
"""

print(sorted(sorted(tables) for tables in arrangement(direct_friendship_info)))