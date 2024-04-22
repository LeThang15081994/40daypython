import numpy as np
import torch
import os
import random

os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import tensorflow as tf
seed = 2024
#câu1
#khởi tạo hai mảng ngẫu nhiên bằng numpy
np.random.seed(seed)
array_np_1 = np.random.randint(-10,10,size=(3,4))
array_np_2 = np.random.randint(-10,10,size=(3,4))
array_np_2_trp = np.transpose(array_np_2)
array_multi = array_np_1.dot(array_np_2_trp)
print(f"Matran số 1: {array_np_1}")
print(f"Matran số 2: {array_np_2}")
print(f"Matran nghịch đảo của matran số 2: {array_np_2_trp}")
print(f"Phép nhân hai ma trận: {array_multi}")

#khởi tạo hai mảng ngẫu nhiên bằng torch
seed = 2024
torch.manual_seed(seed)
torch_arrray_1 = torch.randint(-10,10,size=(3,4))
torch_arrray_2 = torch.randint(-10,10,size=(3,4))
print(torch_arrray_1)
print(torch_arrray_2)
print("\nKết quả giống nhau:", torch.equal(torch_arrray_1 , torch_arrray_2))