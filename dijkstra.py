#　ダイクストラ法(Dijkstra's algorithm)のプログラム
import random
import copy

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
  elif now_node == "e":
    if next_node == "f":
      return 4
  return -1

def get_cost_two_way (now_node, next_node):
  """
  始まりのノード(now_node)から、次のノード(next_node)までのコストを双方向に取得する。もしも見つからなれけば-1を返す。
  """
  count = 0 # ループ変数
  is_find = True # 見つかったかどうか
  now_node_temp = now_node # 仮の変数に代入
  next_node_temp = next_node
  cost = 0 # コスト
  while count <= 1:
    cost = get_cost(now_node_temp, next_node_temp) # コストの取得
    if cost == -1: # もしも見つからなければ
      now_node_temp = next_node # 入れ替える
      next_node_temp = now_node
      is_find = False
    else:
      is_find = True
      break
    count += 1
  if is_find:
    return cost
  else:
    return -1

def get_move_node (now_node, node_array):
  """
  現在のノードから、次に進めるノードの情報を連想配列で格納。
  """
  get_node_array = {"cost": [], "name": []}
  for next_node in node_array: # ノードの数だけ繰り返す
    cost = get_cost_two_way(now_node, next_node)
    if cost != -1: # もしも存在していれば
      get_node_array["cost"].append(cost)
      get_node_array["name"].append(next_node)
  return get_node_array

def search_all_root (now_node, came_node_array, came_total_cost, temp_node_array):
  """
  現在のノードから全てのノードへの探索
  """
  global goal_node
  global result_list
  global total_count

  temp_array = copy.copy(temp_node_array)
  came_array = copy.copy(came_node_array)

  temp_array.remove(now_node) # 探索対象ノードを減らす
  came_array.append(now_node) # 到着ノードを追加
  if now_node == goal_node: # ゴールに到着したら
    result_list["costs"].append(came_total_cost) # 最終の合計コスト
    root_str = ""
    for s in came_array:
      root_str += s + " > "
    result_list["nodes"].append(root_str) # そこまでに至る経路を表示
    return
  move_nodes = get_move_node(now_node, temp_array) # 進めるノードのコスト
  index = 0
  for cost in move_nodes["cost"]:
    search_all_root(move_nodes["name"][index], came_array, came_total_cost + cost, temp_array)
    index += 1

node_array = ["a", "b", "c", "d", "e", "f"]
total_node_cost_array = [] # 各ノードの一時的なコストを記憶する配列
result_list = {"costs": [], "nodes": []} # 結果を格納する連想配列

start_node = node_array[random.randrange(0, len(node_array))]
goal_node = start_node
while goal_node == start_node:
  goal_node = node_array[random.randrange(0, len(node_array))] # start_nodeと異なるノードを格納

print("スタートノード : {}".format(start_node))
print("ゴールノード : {}".format(goal_node))

search_all_root(start_node, [], 0, node_array)

result_index = result_list["costs"].index(min(result_list["costs"])) # 最小コストの配列のインデックス

print("======= 出力結果 =======")
print("合計コスト => {}".format(result_list["costs"][result_index]))
print("ルート => {}".format(result_list["nodes"][result_index][:len(result_list["nodes"][result_index]) - 2]))
