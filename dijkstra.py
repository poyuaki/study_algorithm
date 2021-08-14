#　ダイクストラ法(Dijkstra's algorithm)のプログラム

def get_cost (now_node, next_node):
  """
  始まりのノード(now_node)から、進むノード(next_node)へ進むときのコストを返す。
  見つからない場合は-1を返す。
  """
  if now_node == "a":
    if next_node == "b":
      return 2
    elif next_node == "c":
      return 5
    elif next_node == "d":
      return 4
  elif now_node == "b":
    if next_node == "d":
      return 3
    elif next_node == "e":
      return 6
  elif now_node == "c":
    if next_node == "d":
      return 2
    elif next_node == "f":
      return 6
  elif now_node == "d":
    if next_node == "e":
      return 2
    elif next_node == "f":
      return 4
  return -1


