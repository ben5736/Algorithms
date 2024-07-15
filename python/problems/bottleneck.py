from collections import defaultdict

def topological_sort(graph):
  visited = [0] * len(graph)
  order = []

  for node in graph:
    if not visited[node]:
      dfs(graph, node, visited, order)

  return reversed(order)


def dfs(graph, start, visited, order):
  unprocessed = 0
  processing = 1
  processed = 2

  stack = [start]

  while stack:
    cur = stack[-1]
    if visited[cur] == unprocessed:
      visited[cur] = processing
      neighbors = graph[cur]
      for n in neighbors:
        if visited[n] == unprocessed:
          stack.append(n)
        elif visited[n] == processing:
          raise Exception('cyclic graph')
    elif visited[cur] == processing:
      visited[cur] = processed
      order.append(cur)
      stack.pop()
    elif visited[cur] == processed:
      stack.pop()

def reverse_graph(graph):
  ret = defaultdict(list)

  for node in graph:
    for neighbor in graph[node]:
      ret[neighbor].append(node)

  return ret

def solve(graph):
  bottlenecks = []
  reversed_graph = reverse_graph(graph)
  topo_order = topological_sort(graph)

  node_depth_map = {}
  unique_depths = {}
  for node in topo_order:
    depth = 1
    for neighbor in reversed_graph[node]:
      depth = max(node_depth_map[neighbor] + 1, depth)
    node_depth_map[node] = depth

    if depth not in unique_depths:
      unique_depths[depth] = (node, True)
    else:
      unique_depths[depth] = (node, False)

  ret = set()
  for depth in unique_depths:
    if unique_depths[depth][1]:
      ret.add(unique_depths[depth][0])
  return ret

import unittest

class Test(unittest.TestCase):

  def test1(self):
    graph = {
      0: [2],
      1: [2, 3],
      2: [5],
      3: [4],
      4: [5],
      5: []
    }
    sol = solve(graph)
    self.assertEqual(sol, {4, 5})

  def test2(self):
    graph = {
      0: [],
      1: [0],
      2: [0],
      3: [1],
      4: [2, 3],
      5: [4],
      6: [5],
      7: [4]
    }
    sol = solve(graph)
    self.assertEqual(sol, {0, 1, 4, 5})


if __name__ == '__main__':
    unittest.main()
