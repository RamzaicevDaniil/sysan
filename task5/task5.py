import numpy as np
import json

def func(A):
    max_elem = 0
    for sublist in A:
      for n in sublist:
        max_elem = max(int(n), max_elem)

    matrix = np.zeros(shape=(max_elem, max_elem))
    low_set = set()
    for i in range(len(A)):
      current_set = A[i]
      for number in current_set:
        low_set.add(number)
      for number in current_set:
        for k in range(1, max_elem+1):
            # print(number, k)
            if k in low_set:
              matrix[k-1, number-1] = 1
    return matrix

def str_to_list(A):
  A = json.loads(A)
  for i, item in enumerate(A):
    if type(item) == list:
      A[i] = []
      for num in item:
        A[i].append(int(num))
    else:
      A[i] = [int(item)]
  return A

def task(A, B):
  A_list = str_to_list(A)
  B_list = str_to_list(B)
  res_A = func(A_list)
  res_B = func(B_list)
  res = res_A*res_B + res_A.T*res_B.T
  p1, p2 = np.where(res==0)
  pairs = np.concatenate([np.expand_dims(p1[0:int(p1.shape[0]/2)], -1), np.expand_dims(p2[0:int(p2.shape[0]/2)], -1)], axis=-1) + 1
  pairs = pairs.tolist()
  return json.dumps([[str(elem) for elem in pair] for pair in pairs])