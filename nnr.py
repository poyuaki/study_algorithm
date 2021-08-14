# 最近傍法(nearest neighbor algorithm:NNR)のプログラム
import random
import copy

def make_cost (node_array):
  """
  自動的にコストを生成
  """
  temp_array = copy.copy(node_array)
  result_array = []
  print("=======ノード間のコスト一覧=======")
  print("----------")
  for n in node_array:
    temp_array.pop(0)
    add_array = []
    for i in temp_array:
      add_array.append(random.randrange(2, 15))
      print("{} - {} => {}".format(n, i, add_array[len(add_array) - 1]))
    result_array.append(add_array)
    print("----------")
  return result_array

def get_cost (now_node, next_node):
  """
  始まりのノード(now_node)から、進むノード(next_node)へ進むときのコストを返す。
  見つからない場合は-1を返す。
  """
  global node_array
  global node_cost_array
  now_index = node_array.index(now_node) # 現在のノードのindexを取得
  temp_array = copy.copy(node_array) # コピー
  temp_array = temp_array[now_index + 1:len(temp_array)] # now_nodeからnext_nodeへのコストを求めるためのスライス
  if node_array.index(next_node) < now_index:
    return -1
  next_index = temp_array.index(next_node)
  return node_cost_array[now_index][next_index] # コスト

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

def get_move_node (now_node, node_array, is_give_cost):
  """
  現在のノードから、次に進めるノードを配列にして返す。第三引数をFalseにするとノード名が、Trueにするとコストが取得できる
  """
  get_node_array = []
  for next_node in node_array: # ノードの数だけ繰り返す
    cost = get_cost_two_way(now_node, next_node)
    if cost != -1: # もしも存在していれば
      if is_give_cost:
        get_node_array.append(cost)
      else:
        get_node_array.append(next_node)
  return get_node_array


def get_initial_node (node_array, initial_position_array):
  """
  初期の現在位置(今まで選択されていない)をランダムに抽出
  """
  fillter_array = node_array
  for x in initial_position_array:
    fillter_array.remove(x)
  if len(fillter_array) == 0: # もしもランダムに選ぶノードがなければ => 全て見終わったら
    return "None"
  return fillter_array[random.randrange(0, len(fillter_array))]


node_array = ["a", "b", "c", "d", "e", "f"]
now_first_node = node_array[random.randrange(0, len(node_array))] # ランダムな初期ノードを設定
initial_position_array = [] # 現在位置として最初に選ばれたノードを格納する配列

node_cost_array = make_cost(node_array)

all_cost = 1000 # 普通ではありえないようなコスト

result_array = []

while True: # 全てのパターンを試す
  came_node_array = [] # 今まで訪れたノード名を格納する配列
  not_came_node_array = copy.copy(node_array) # 訪れていないノード名を格納する配列
  came_node_array.append(now_first_node) # 初期化
  not_came_node_array.remove(now_first_node) # 初期化

  patrol_count = 0 # ループ変数
  now_node = now_first_node # 現在のノード
  total_cost = 0 # 合計コスト

  while True:
    if len(get_move_node(now_node, not_came_node_array, True)) == 0: # もしも全てのノードを巡回し終わったら
      break

    min_cost = min(get_move_node(now_node, not_came_node_array, True)) # 最小コスト
    total_cost += min_cost
    min_index = get_move_node(now_node, not_came_node_array, True).index(min_cost) # 最小コストがある要素のindexを取得
    perfect_node = get_move_node(now_node, not_came_node_array, False)[min_index] # min_indexに対応するノード名を取得
    came_node_array.append(perfect_node) # 訪れたノードとして登録
    not_came_node_array.remove(perfect_node) # 訪れていないノードとしての登録を削除
    now_node = perfect_node # 現在のノードを更新

  if all_cost > total_cost: # もしも今のルートの方がコストが小さければ
    all_cost = total_cost #更新
    result_array = copy.copy(came_node_array) # コピー

  if len(initial_position_array) < len(came_node_array): # もしも全てのノードを回っていなければ
    initial_position_array.append(now_first_node)

  now_first_node = get_initial_node(came_node_array, initial_position_array) # 次の初期位置のノードを取得
  if now_first_node == "None":
    break

print("======= 結果 =======")
print("最短コスト => %d" % all_cost)
print("--最短巡回ルート--")
for result_node in result_array:
  print(result_node, end=", ")
