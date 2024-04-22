import numpy as np
import torch
import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf

#câu1
list_data = list(range(1,10))

array_1D = np.array(list_data)
print(f"Mảng 1 chiều: {array_1D} có shape = {array_1D.shape} có kiểu dữ liệu của các phần tử = {array_1D.dtype} và có kiểu dữ liệu = {type(array_1D)}")
array_1D_torch = torch.tensor(list_data)
print(f"Mảng 1 chiều: {array_1D_torch } có shape = {array_1D_torch .shape} có kiểu dữ liệu của các phần tử = {array_1D_torch .dtype} và có kiểu dữ liệu = {type(array_1D_torch )}")
array_1D_tf = tf.convert_to_tensor(list_data)
print(f"Mảng 1 chiều: {array_1D_tf } có shape = {array_1D_tf .shape} có kiểu dữ liệu của các phần tử = {array_1D_tf .dtype} và có kiểu dữ liệu = {type(array_1D_tf )}")

#câu2

list_2D = [[1,2,3],
           [4,5,6],
           [7,8,9]
]
array_2D = np.array(list_2D)
print(f"Mảng 2 chiều = {array_2D} có số chiều = {array_2D.shape} có kiểu dữ liệu = {array_2D.dtype} có kiểu dữ liệu mảng = {type(array_2D)}")
array_2D_torch = torch.tensor(list_2D)
print(f"Mảng 2 chiều = {array_2D_torch} có số chiều = {array_2D_torch.shape} có kiểu dữ liệu = {array_2D_torch.dtype} có kiểu dữ liệu mảng = {type(array_2D_torch)} nơi lưu trữ tại {array_2D_torch.device}")
array_2D_tf = tf.convert_to_tensor(list_2D)
print(f"Mảng 2 chiều = {array_2D_tf} có số chiều = {array_2D_tf.shape} có kiểu dữ liệu = {array_2D_tf.dtype} có kiểu dữ liệu mảng = {type(array_2D_tf)} nơi lưu trữ tại {array_2D_tf.device}")