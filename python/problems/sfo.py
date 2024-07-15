def findLowMetric(distances, matrix):
  low_metric = None
  low_metric_modes = []

  for mode, distance in distances.items():
    total_metric = distance * matrix[mode]
    if low_metric is None or total_metric < low_metric:
      low_metric = total_metric
      low_metric_modes = [mode]
    elif total_metric == low_metric:
      low_metric_modes.append(mode)

  return low_metric_modes

def findBest(distances, time_matrix, cost_matrix):
  if not distances:
    return None

  low_time_modes = findLowMetric(distances, time_matrix)

  if len(low_time_modes) == 1:
    return low_time_modes[0]

  low_time_distances = {mode: distances[mode] for mode in low_time_modes}
  return findLowMetric(low_time_distances, cost_matrix)[0]

def findDistances(citymap, mode_matrix):
  ret = {}
  x, y = findStart(citymap)
  for mode, sign in mode_matrix.items():
    distance = bfs(citymap, sign, x, y)
    if distance is not None:
      ret[mode] = distance
  return ret

def bfs(citymap, sign, start_x, start_y):
  from collections import deque

  queue = deque()
  queue.append((start_x, start_y, 0))
  visited = {(start_x, start_y)}

  while queue:
    cur_x, cur_y, cur_dist = queue.popleft()
    ret = (tryVisit(cur_x - 1, cur_y, sign, queue, visited, citymap, cur_dist)
      or tryVisit(cur_x + 1, cur_y, sign, queue, visited, citymap, cur_dist)
      or tryVisit(cur_x, cur_y - 1, sign, queue, visited, citymap, cur_dist)
      or tryVisit(cur_x, cur_y + 1, sign, queue, visited, citymap, cur_dist))
    if ret:
      return ret
  return None

def tryVisit(x, y, sign, queue, visited, citymap, cur_dist):
  m = len(citymap)
  n = len(citymap[0])
  if x < 0 or x >= m or y < 0 or y >= n:
    return None

  if (x, y) in visited:
    return None

  if citymap[x][y] == 'D':
    return cur_dist + 1
  elif citymap[x][y] == sign:
    visited.add((x, y))
    queue.append((x, y, cur_dist + 1))

def solve(citymap, mode_matrix, time_matrix, cost_matrix):
  distances = findDistances(citymap, mode_matrix)
  return findBest(distances, time_matrix, cost_matrix)

def findStart(citymap):
  for x in range(len(citymap)):
    for y in range(len(citymap[0])):
      if citymap[x][y] == 'S':
        return x, y

import unittest

class Test(unittest.TestCase):

  def test1(self):
    mode_matrix = {"walk": '1', "bike": '2', "car": '3', "train": '4'}
    time_matrix = {"walk": 3, "bike": 2, "car": 1, "train": 1}
    cost_matrix = {"walk": 0, "bike": 1, "car": 3, "train": 2}

    citymap = [
      ['3', '3', 'S', '2', 'X', 'X'],
      ['3', '1', '1', '2', 'X', '2'],
      ['3', '1', '1', '2', '2', '2'],
      ['3', '1', '1', '1', 'D', '3'],
      ['3', '3', '3', '3', '3', '4'],
      ['4', '4', '4', '4', '4', '4']
    ]

    print(solve(citymap, mode_matrix, time_matrix, cost_matrix))

if __name__ == '__main__':
    unittest.main()











