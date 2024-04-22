import numpy as np
import torch
import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf

array_zr = np.zeros((3,4))
print(f"Mảng có kích thước (3,4): {array_zr}")
torch_zr = torch.zeros((3,4))
print(f"Torch có kích thước (3,4): {torch_zr}")
tf_zr = tf.zeros((3,4))
print(f"Tf có kích thước (3,4): {torch_zr}")
print("------------------------------------------")
array_zr = np.ones((3,4))
print(f"Mảng có kích thước (3,4): {array_zr}")
torch_zr = torch.ones((3,4))
print(f"Torch có kích thước (3,4): {torch_zr}")
tf_zr = tf.ones((3,4))
print(f"Tf có kích thước (3,4): {torch_zr}")
print("------------------------------------------")
array_zr = np.full((3,4),5)
print(f"Mảng có kích thước (3,4) và có giá trị là 5: {array_zr}")
torch_zr = torch.full((3,4),5)
print(f"Torch có kích thước (3,4) và có giá trị là 5: {torch_zr}")
tf_zr = tf.fill((3,4),5)
print(f"Tf có kích thước (3,4) và có giá trị là 5: {torch_zr}")