def verify(board, x, y, is_circle, winning_length):
  # vertical
  if 1 + countInDirection(board, x, y, is_circle, lambda x, y: x - 1, y) + countInDirection(board, x, y, is_circle, lambda x, y: x + 1, y) >= winning_length:
    return True

  # horizontal
  if 1 + countInDirection(board, x, y, is_circle, lambda x, y: x, y - 1) + countInDirection(board, x, y, is_circle, lambda x, y: x, y + 1) >= winning_length:
    return True

  # top left to bottom right
  if 1 + countInDirection(board, x, y, is_circle, lambda x, y: x - 1, y - 1) + countInDirection(board, x, y, is_circle, lambda x, y: x + 1, y + 1) >= winning_length:
    return True

  # top right to bottom left
  if 1 + countInDirection(board, x, y, is_circle, lambda x, y: x + 1, y - 1) + countInDirection(board, x, y, is_circle, lambda x, y: x - 1, y + 1) >= winning_length:
    return True

  return False

def countInDirection(board, x, y, is_circle, move_func):
  counts = 0
  x, y = move_func(x, y)
  while x >= 0 and x < len(board) and y >= 0 and y < len(board[0]) and board[x][y] == is_circle:
    counts += 1
    x, y = move_func(x, y)
  return counts