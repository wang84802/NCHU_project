import config
import numpy as np

#get knapsack file data
file_empty = 0
with open(config.path_p07_c, mode="r") as file:
    capacity = np.loadtxt(file)
    if capacity.size == 0:
        file_empty = 1

with open(config.path_p07_w, mode="r") as file:
    weights = np.loadtxt(file)
    weights = weights.astype(np.int32)
    if weights.size == 0:
        file_empty = 1
with open(config.path_p07_p, mode="r") as file:
    profits = np.loadtxt(file)
    profits = profits.astype(np.int32)
    if profits.size == 0:
        file_empty = 1
with open(config.path_p07_s, mode="r") as file:
    selects = np.loadtxt(file)
    selects = selects.astype(np.int32)
    if selects.size == 0:
        file_empty = 1

if file_empty == 1:
    print('file is empty')
    exit()

#dynamic programming
items = np.size(weights)
C = np.array([[0 for x in range(int(capacity) + 1)] for x in range(int(items) + 1)])

for i in range(int(items)+1): #0~15
    for k in range(int(capacity)+1): #0~750
            C[i][k] = 0

for i in range(int(items)+1): #0~15
    for k in range(int(capacity)+1): #0~750
        if k==0 or i==0:
            C[i][k] = 0
        elif int(weights[i-1]) <= k: #拿得動item i
            C[i][k] = max(profits[i-1] + C[i-1][k-int(weights[i-1])], C[i-1][k])
        else:
            C[i][k] = C[i-1][k] #拿不動item i

# for i in range(int(items)+1): #0~15
#     for k in range(int(capacity)+1): #0~750
#         print(int(C[i][k]), end='')
#     print('\n')

#check items is select or not
is_selects = np.array([0 for x in range(int(items))])
n = items
res = C[int(items)][int(capacity)]
w = int(capacity)
print("maximum value:" + str(res))

for i in range(n,0,-1):
    if res <=0:
        break
    if res == C[i-1][w]: #item i沒取
        continue
    else:
        is_selects[i-1] = 1
        res = res - profits[i-1]
        w = w - weights[i-1]

if np.array_equal(is_selects, selects):
    print('correct answer:', end='')
    print(selects)
else:
    print('wrong answer')