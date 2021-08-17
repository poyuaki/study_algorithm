import random

list_len = random.randrange(5, 100) # 配列の要素数をランダムに生成

target_list = []

while len(target_list) < list_len:
  target_list.append(random.randrange(1, list_len))

print("要素数 => {}".format(list_len))
print("配列 => {}".format(target_list))

for i in range(list_len - 1):
  for n in range(i + 1, list_len):
    if target_list[i] > target_list[n]:
      temp = target_list[i]
      target_list[i] = target_list[n]
      target_list[n] = temp

print("======= 結果 =======")
print(target_list)
